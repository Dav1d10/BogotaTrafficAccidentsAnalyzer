"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
...
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control
    


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, filename):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    accidentes = controller.load_data(control, filename)
    return accidentes
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass


def imprimir_datos(datos):
    size = lt.size(datos)
    if size:
        headers = ["FECHA_OCURRENCIA_ACC", "FECHA_HORA_ACC", "LOCALIDAD", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "LATITUD", "LONGITUD"]
        table = []
        for dato in lt.iterator(datos):
            table.append([dato["FECHA_OCURRENCIA_ACC"],
                          dato["FECHA_HORA_ACC"],
                          dato["LOCALIDAD"],
                          dato["DIRECCION"],
                          dato["GRAVEDAD"],
                          dato["CLASE_ACC"],
                          dato["LATITUD"],
                          dato["LONGITUD"],])         
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=14, maxheadercolwidths=9))  
        print('\n')
    else:
        print("No se encontraron datos")
        

def print_req_1(control, fechaInicial, fechaFinal):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    datos = controller.req_1(control, fechaInicial, fechaFinal)
    size = lt.size(datos)
    print("Hay " + str(size) + " accidentes registrados entre " + fechaInicial + " y " + fechaFinal)
    
    if size:
        headers = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "LOCALIDAD", "FECHA_HORA_ACC", "LATITUD", "LONGITUD"]
        table = []
        for dato in lt.iterator(datos):
            table.append([dato["CODIGO_ACCIDENTE"],
                        dato["DIA_OCURRENCIA_ACC"],
                        dato["DIRECCION"],
                        dato["GRAVEDAD"],
                        dato["CLASE_ACC"],
                        dato["LOCALIDAD"],
                        dato["FECHA_HORA_ACC"],
                        dato["LATITUD"],
                        dato["LONGITUD"]])         
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=14, maxheadercolwidths=9))  
        print('\n')
    else:
        print("No se encontraron datos")
    


def print_req_2(control, horaInicial, horaFinal, mes, año):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    datos = controller.req_2(control, horaInicial, horaFinal, mes, año)
    size = lt.size(datos)
    print("Hay " + str(size) + " accidentes registrados entre " + horaInicial + " y " + horaFinal + " de todos los días del mes de " + mes + " de " + año)
    
    if size:
        headers = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "LOCALIDAD", "FECHA_HORA_ACC", "LATITUD", "LONGITUD"]
        table = []
        for dato in lt.iterator(datos):
            table.append([dato["CODIGO_ACCIDENTE"],
                        dato["DIA_OCURRENCIA_ACC"],
                        dato["DIRECCION"],
                        dato["GRAVEDAD"],
                        dato["CLASE_ACC"],
                        dato["LOCALIDAD"],
                        dato["FECHA_HORA_ACC"],
                        dato["LATITUD"],
                        dato["LONGITUD"]])         
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=14, maxheadercolwidths=9))  
        print('\n')
    else:
        print("No se encontraron datos")
        
    
    


def print_req_3(control, clase, calle):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    lista, finalList = controller.req_3(control, clase, calle)
    size = lt.size(finalList)
    size2 = lt.size(lista)
    print("Hay " + str(size2) + " accidentes de clase " + clase + " registrados en la via " + calle)
    print("Estos son los " + str(size) + " accidentes más recientes: ")
    
    if size:
        headers = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "LOCALIDAD", "FECHA_HORA_ACC", "LATITUD", "LONGITUD"]
        table = []
        for dato in lt.iterator(finalList):
            table.append([dato["CODIGO_ACCIDENTE"],
                        dato["DIA_OCURRENCIA_ACC"],
                        dato["DIRECCION"],
                        dato["GRAVEDAD"],
                        dato["LOCALIDAD"],
                        dato["FECHA_HORA_ACC"],
                        dato["LATITUD"],
                        dato["LONGITUD"]])         
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=14, maxheadercolwidths=9))  
        print('\n')
    else:
        print("No se encontraron datos")
    


def print_req_4(control, fechaInicial, fechaFinal, gravedad):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    subList, finalList = controller.req_4(control, fechaInicial, fechaFinal, gravedad)
    size = lt.size(subList)
    size2 = lt.size(finalList)
    print("Hay " + str(size2) + " accidentes de gravedad " + gravedad + " registrados entre " + fechaInicial + " y " + fechaFinal)
    print("Estos son los " + str(size) + " accidentes más recientes: ")
    
    if size:
        headers = ["CODIGO_ACCIDENTE", "DIA_OCURRENCIA_ACC", "DIRECCION", "GRAVEDAD", "CLASE_ACC", "LOCALIDAD", "FECHA_HORA_ACC", "LATITUD", "LONGITUD"]
        table = []
        for dato in lt.iterator(subList):
            table.append([dato["CODIGO_ACCIDENTE"],
                        dato["DIA_OCURRENCIA_ACC"],
                        dato["DIRECCION"],
                        dato["GRAVEDAD"],
                        dato["CLASE_ACC"],
                        dato["LOCALIDAD"],
                        dato["FECHA_HORA_ACC"],
                        dato["LATITUD"],
                        dato["LONGITUD"]])         
        print(tabulate(table, headers, tablefmt="grid", maxcolwidths=14, maxheadercolwidths=9))  
        print('\n')
    else:
        print("No se encontraron datos")
    


def print_req_5(control, localidad, mes, año):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    datos = controller.req_5(control, localidad, mes, año)
    return datos 
    
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                control = new_controller()
                print("Seleccione el porcentaje de datos que desea utilizar: ")
                print("1: 0.5% ")
                print("2: 5% ")
                print("3: 10% ")
                print("4: 20% ")
                print("5: 30% ")
                print("6: 50% ")
                print("7: 80% ")
                print("8: 100% ")
                respuesta = int(input())
                if respuesta == 1:
                    filename = "small.csv"
                elif respuesta == 2:
                    filename = "5pct.csv"
                elif respuesta == 3:
                    filename = "10pct.csv"
                elif respuesta == 4:
                    filename = "20pct.csv"
                elif respuesta == 5:
                    filename = "30pct.csv"
                elif respuesta == 6:
                    filename = "50pct.csv"
                elif respuesta == 7:
                    filename = "80pct.csv"
                elif respuesta == 8:
                    filename = "large.csv"  
                print("--------------------------------------------------------------------") 
                print("Cargando información de los archivos ....\n")
                data = load_data(control, filename)
                #print(data)
                primeros_tres = controller.primerosTres(data["Accidente"])
                ultimos_tres = controller.ultimosTres(data["Accidente"])
                print("Los primeros tres registros de accidentes cargados fueron: ")
                imprimir_datos(primeros_tres)
                print("Los últimos tres registros de accidentes cargados fueron: ")
                imprimir_datos(ultimos_tres)
            elif int(inputs) == 2:
                fechaInicial = str(input("Ingrese la fecha inicial: "))
                fechaFinal = str(input("Ingrese la fecha final: "))
                print(print_req_1(control, fechaInicial, fechaFinal))

            elif int(inputs) == 3:
                horaInicial = str(input("Ingrese la hora inicial: "))
                horaFinal = str(input("Ingrese la hora final: "))
                mes = str(input("Ingrese el mes del accidente: "))
                año = str(input("Ingrese el año del accidente: "))
                print(print_req_2(control, horaInicial, horaFinal, mes, año))

            elif int(inputs) == 4:
                clase = str(input("Ingrese la clase del accidente: "))
                calle = str(input("Ingrese la calle del accidente: "))
                print(print_req_3(control, clase, calle))

            elif int(inputs) == 5:
                fechaInicial = str(input("Ingrese la fecha inicial: "))
                fechaFinal = str(input("Ingrese la fecha final: "))
                gravedad = str(input("Ingrese la gravedad del accidente: "))
                print(print_req_4(control, fechaInicial, fechaFinal, gravedad))

            elif int(inputs) == 6:
                localidad = str(input("Ingrese la localidad del accidente: "))
                mes = str(input("Ingrese el mes del accidente: "))
                año = str(input("Ingrese el año del accidente: "))
                print(print_req_5(control, localidad, mes, año))

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
