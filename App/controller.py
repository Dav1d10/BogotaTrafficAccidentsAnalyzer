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
 """

import config as cf
import model
import time
import csv
import tracemalloc
import datetime
...
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = model.new_data_structs()
    return control
    

# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    dianfile = cf.data_dir + "Challenge-3/siniestros/datos_siniestralidad-" + filename
    input_file = csv.DictReader(open(dianfile, encoding='utf-8'), delimiter=",")
    for accidente in input_file:
        model.añadir_accidente(control, accidente)
    return control


def primerosTres(control):
    datos = model.primerosTres(control)
    return datos

def ultimosTres(control):
    datos = model.ultimosTres(control)
    return datos
    

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, fechaInicial, fechaFinal):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    fechaInicial = datetime.datetime.strptime(fechaInicial, "%Y/%m/%d")
    fechaFinal = datetime.datetime.strptime(fechaFinal, "%Y/%m/%d")
    accidente = model.req_1(control, fechaInicial.date(), fechaFinal.date())
    return accidente
    

def req_2(control, horaInicial, horaFinal, mes, año):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    mes = mes.upper()
    mes = mes.replace(" ", "")
    año = año.replace(" ", "")
    horaInicial = datetime.datetime.strptime(horaInicial, "%H:%M:%S")
    horaFinal = datetime.datetime.strptime(horaFinal, "%H:%M:%S")
    accidente = model.req_2(control, horaInicial.time(), horaFinal.time(), mes, año)
    return accidente
    


def req_3(control, clase, calle):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    clase = clase.upper()
    calle = calle.replace(" ", "")
    calle = calle.upper()
    return model.req_3(control, clase, calle)
    
    


def req_4(control, fechaInicial, fechaFinal, gravedad):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    gravedad = gravedad.upper()
    fechaInicial = datetime.datetime.strptime(fechaInicial, "%Y-%m-%d %H:%M:%S")
    fechaFinal = datetime.datetime.strptime(fechaFinal, "%Y-%m-%d %H:%M:%S")
    subList, finalList = model.req_4(control, fechaInicial.date(), fechaFinal.date(), gravedad)
    return subList, finalList
    


def req_5(control, localidad, mes, año):
    localidad = localidad.upper()
    localidad = localidad.replace(" ", "")
    mes = mes.upper()
    mes = mes.replace(" ", "")
    año = año.replace(" ", "")
    return model.req_5(control, localidad, mes, año)
    

def req_6(control, mes, año, latitud, longitud, radio, num_acc):
    """
    Retorna el resultado del requerimiento 6
    """
    mes = mes.upper()
    mes = mes.replace(" ", "")
    año = año.replace(" ", "")
    return model.req_6(control, mes, año, latitud, longitud, radio, num_acc)


def req_7(control, mes, año):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    return model.req_7(control, mes, año)
    


def req_8(control, fechaInicial, fechaFinal, clase):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    fechaInicial = datetime.datetime.strptime(fechaInicial, "%d/%m/%Y")
    fechaFinal = datetime.datetime.strptime(fechaFinal, "%d/%m/%Y")
    return model.req_8(control, fechaInicial.date(), fechaFinal.date(), clase)
    
    


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
