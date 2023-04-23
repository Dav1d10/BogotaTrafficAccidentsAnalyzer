﻿"""
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
                                      comparefunction=None)
    
    data_structs["Hora"] = om.newMap(omaptype="RBT", 
                                      comparefunction=None)
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
    entry = om.get(mapa, horaAccidente.date())
    if entry is None:
        hora_entry = nuevaEntrada()
        om.put(mapa, horaAccidente.date(), hora_entry)
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
                    
    


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


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
