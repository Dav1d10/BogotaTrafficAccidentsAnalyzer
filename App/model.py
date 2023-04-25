"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from math import radians, cos, sin, asin, sqrt
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    data_structs = {"Accidente": None, "Fecha": None}

    data_structs["Accidente"] = lt.newList("ARRAY_LIST")

    data_structs["Fecha"] = om.newMap(omaptype="RBT", 
                                      comparefunction=compararFechas)
    
    data_structs["Hora"] = om.newMap(omaptype="RBT", 
                                      comparefunction=compararFechas)
    
    data_structs["Clase del accidente"] = mp.newMap(6, maptype="CHAINING",
                                                    loadfactor=0.5,
                                                    cmpfunction=None)
    return data_structs


# Funciones para agregar informacion al modelo


def añadir_accidente(data_structs, accidente):
    lt.addLast(data_structs["Accidente"], accidente)
    actualizarFecha(data_structs["Fecha"], accidente)
    actualizarHora(data_structs["Hora"], accidente)
    return data_structs


def actualizarFecha(mapa, accidente):
    fecha = accidente["FECHA_OCURRENCIA_ACC"]
    fechaAccidente = datetime.datetime.strptime(fecha, "%Y/%m/%d")
    entry = om.get(mapa, fechaAccidente.date())
    if entry is None:
        fecha_entry = nuevaEntrada()
        om.put(mapa, fechaAccidente.date(), fecha_entry)
    else:
        fecha_entry = me.getValue(entry)
    añadirFecha(fecha_entry, accidente)
    return mapa


def actualizarHora(mapa, accidente):
    hora = accidente["HORA_OCURRENCIA_ACC"]
    horaAccidente = datetime.datetime.strptime(hora, "%H:%M:%S")
    entry = om.get(mapa, horaAccidente.time())
    if entry is None:
        hora_entry = nuevaEntrada()
        om.put(mapa, horaAccidente.time(), hora_entry)
    else:
        hora_entry = me.getValue(entry)
    añadirFecha(hora_entry, accidente)
    return mapa


def nuevaEntrada():
    entry = {"lstaccidentes": None}
    entry["lstaccidentes"] = lt.newList("ARRAY_LIST")
    return entry


def añadirFecha(fecha_entry, accidente):
    lst = fecha_entry["lstaccidentes"]
    lt.addLast(lst, accidente)
    return fecha_entry


def añadir_impuesto_por_ca(data_structs, accidente):
    clases = data_structs["Clase del accidente"]
    if accidente["CLASE_ACC"] != "":
        llave = accidente["CLASE_ACC"]
    llave_existe = mp.contains(clases, llave)
    if llave_existe:
        clase = me.getValue(mp.get(clases, llave))
    else:
        clase = nuevaClase(llave)
        mp.put(clases, llave, clase)
    calles = clase["data"]
    if accidente["DIRECCION"] != "":
        llave2 = arreglarcalle(accidente["DIRECCION"])
    llave2_existe = mp.contains(calles, llave2)
    if llave2_existe:
        calle = me.getValue(mp.get(calles, llave2))
    else:
        calle = nuevaCalle(llave2)
        mp.put(calles, llave2, calle)
    lt.addLast(calle["data"], accidente)
    

def arreglarcalle(calle):
    calle = calle.replace(" ", "")
    num_str = calle.find("-")
    calle = calle[0:num_str]
    return calle


def nuevaCalle(calle1):
    calle = {"calle": "", "data": None}
    calle["calle"] = calle1
    calle["data"] = lt.newList("ARRAY_LIST", cmpreq1)
    return calle


def nuevaClase(clase1):
    clase = {"clase": "", "data": None}
    clase["clase"] = clase1
    clase["data"] = mp.newMap(30, maptype="CHAINING", loadfactor=0.5,cmpfunction=None)
    return clase




# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def primerosTres(data):
    datos = lt.subList(data, 1, 3)
    return datos

def ultimosTres(data):
    datos = lt.subList(data, lt.size(data) -2, 3)
    return datos

def primerosCinco(data):
    datos = lt.subList(data, 1, 5)
    return datos

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, fechaInicial, fechaFinal):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    finalList = lt.newList("ARRAY_LIST")
    mapa = data_structs["Fecha"]
    rango = om.values(mapa, fechaInicial, fechaFinal)
    for fechas in lt.iterator(rango):
        for i in lt.iterator(fechas["lstaccidentes"]):
            lt.addLast(finalList, i)
    merg.sort(finalList, cmpreq1)
    return finalList
    


def req_2(data_structs, horaInicial, horaFinal, mes, año):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    finalList = lt.newList("ARRAY_LIST")
    mapa = data_structs["Hora"]
    rango = om.values(mapa, horaInicial, horaFinal)
    for horas in lt.iterator(rango):
        for i in lt.iterator(horas["lstaccidentes"]):
            if str(i["MES_OCURRENCIA_ACC"]) == mes:
                if str(i["ANO_OCURRENCIA_ACC"]) == año:
                    respuesta = i
                    lt.addLast(finalList, respuesta)
    return finalList
                    
    


def req_3(data_structs, clase, calle):
    mapa = data_structs["Clase del accidente"]
    hash = me.getValue(mp.get(mapa, clase))
    lista = me.getValue(mp.get(hash["data"], calle))
    lista = lista["data"]
    lista = merg.sort(lista, cmpreq1)
    size = lt.size(lista)
    if size > 3:
        finalList = primerosTres(lista)
    else:
        finalList
    return size, finalList
    


def req_4(data_structs, fechaInicial, fechaFinal, gravedad):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    finalList = lt.newList("ARRAY_LIST")
    mapa = data_structs["Fecha"]
    rango = om.values(mapa, fechaInicial, fechaFinal)
    for fechas in lt.iterator(rango):
        for i in lt.iterator(fechas["lstaccidentes"]):
            if str(i["GRAVEDAD"]) == gravedad:
                respuesta = i
                lt.addLast(finalList, respuesta)
    merg.sort(finalList, cmpreq1)
    size =lt.size(finalList)
    if size > 5:
        subList = primerosCinco(finalList)
    else:
        subList = finalList
    return subList, finalList
    


def req_5(data_structs, localidad, mes, año):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    localidad = localidad.upper()
    localidad = localidad.replace(" ", "")
    mes = mes.upper()
    mes = mes.replace(" ", "")
    año = año.replace(" ", "")
    finalList = lt.newList("ARRAY_LIST")
    lista = data_structs["Accidente"]
    for fechas in lt.iterator(lista):
        if str(fechas["LOCALIDAD"]) == localidad:
            if str(fechas["MES_OCURRENCIA_ACC"]) == mes:
                if str(fechas["ANO_OCURRENCIA_ACC"]) == año:
                    respuesta = fechas
                    lt.addLast(finalList, respuesta)
    merg.sort(finalList, cmpreq1)
    size = lt.size(finalList)
    if size > 10:
        subList = lt.subList(finalList, size - 9, 10)
    else:
        subList = finalList
    return finalList, subList
                    
        


def req_6(data_structs, mes, año, latitud1, longitud1, radio, num_acc):
    mapa = data_structs["Fecha"]
    min_año = datetime.datetime(2015,1,1)
    max_año = datetime.datetime(2022,12,31)
    rango = om.values(mapa, min_año.date(), max_año.date())
    finalList = lt.newList("ARRAY_LIST")
    for fechas in lt.iterator(rango):
        for i in lt.iterator(fechas["lstaccidentes"]):
            if str(i["ANO_OCURRENCIA_ACC"]) == año and str(i["MES_OCURRENCIA_ACC"]) == mes:
                latitud = float(i["LATITUD"])
                longitud = float(i["LONGITUD"])
                distancia = haversine(longitud, latitud, longitud1, latitud1)
                if distancia <= radio:
                    i["DISTANCIA"] = distancia
                    lt.addLast(finalList, i)
    size = lt.size(finalList)
    finalList = merg.sort(finalList, compararDistancia)
    if size > num_acc:
        finalList = lt.subList(finalList, 1, num_acc)
    else:
        finalList = finalList
    return finalList
                
    
    
def haversine(longitud1, latitud1, longitud2, latitud2):
    longitud1 = radians(longitud1)
    longitud2 = radians(longitud2)
    latitud1 = radians(latitud1)
    latitud2 = radians(latitud2)
    dlon = longitud2 - longitud1
    dlat = latitud2 - latitud1
    a = sin(dlat/2)**2 + cos(latitud1) * cos(latitud2) * sin((dlon/2)**2)
    c = 2 * sin(sqrt(sin((dlat/2)**2) + cos(latitud1) * cos(latitud2) * sin((dlon/2)**2))) 
    r = 6371
    return c * r


def req_7(data_structs, mes, año):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    finalList = lt.newList("ARRAY_LIST")
    mapa = data_structs["Fecha"]
    min_año = datetime.datetime(2015,1,1)
    max_año = datetime.datetime(2022,12,31)
    rango = om.values(mapa, min_año.date(), max_año.date())
    for fechas in lt.iterator(rango):
        for i in lt.iterator(fechas["lstaccidentes"]):
            if str(i["MES_OCURRENCIA_ACC"]) == mes and str(i["ANO_OCURRENCIA_ACC"]) == año:
                respuesta = i
                lt.addLast(finalList, respuesta)
    merg.sort(finalList, cmpreq7)
    subList = lt.newList("ARRAY_LIST")
    fecha = lt.getElement(finalList, 1)
    
    fecha1 = datetime.datetime.strptime(fecha["FECHA_OCURRENCIA_ACC"], "%Y/%m/%d").date()
    fechaNumero = datetime.timedelta(days = 1)
   
    for i in lt.iterator(finalList):
        if datetime.datetime.strptime(i["FECHA_OCURRENCIA_ACC"], "%Y/%m/%d") == datetime.datetime.strptime(i["FECHA_OCURRENCIA_ACC"], "%Y/%m/%d"):
            if i["DIA_OCURRENCIA_ACC"] == i["DIA_OCURRENCIA_ACC"]:
                respuesta = i
                lt.addLast(subList, i)
    
    return subList
    


def req_8(data_structs, fechaInicial, fechaFinal, clase):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    finalList = lt.newList("ARRAY_LIST")
    mapa = data_structs["Fecha"]
    rango = om.values(mapa, fechaInicial, fechaFinal)
    total_accidentes = 0
    for fechas in lt.iterator(rango):
        for i in lt.iterator(fechas["lstaccidentes"]):
            if str(i["CLASE_ACC"]) == clase:
                respuesta = i
                lt.addLast(finalList, respuesta)
                size = lt.size(finalList)
    total_accidentes += size
    return total_accidentes
            
    

# Funciones utilizadas para comparar elementos dentro de una lista

def compararFechas(fecha1, fecha2):
    """
    Compara dos fechas
    """
    if (fecha1 == fecha2):
        return 0
    elif (fecha1 > fecha2):
        return 1
    else:
        return -1
    
    
def cmpreq1(fecha1, fecha2):
    if datetime.datetime.strptime(fecha1["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00") == datetime.datetime.strptime(fecha2["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00"):
        return 0
    elif datetime.datetime.strptime(fecha1["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00") > datetime.datetime.strptime(fecha2["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00"):
        return 1
    else:
        return 0
    
    
def compararDistancia(distancia1, distancia2):
    if distancia1["DISTANCIA"] < distancia2["DISTANCIA"]:
        return 1
    else:
        return 0
    
    
def cmpreq7(fecha1, fecha2):
    if datetime.datetime.strptime(fecha1["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00") == datetime.datetime.strptime(fecha2["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00"):
        return 0
    elif datetime.datetime.strptime(fecha1["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00") < datetime.datetime.strptime(fecha2["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00"):
        return 1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
