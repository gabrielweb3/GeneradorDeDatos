# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:37:17 2020

@author: d935892
"""

#LIBRERIAS
import pandas as pd
import numpy as np
import os
 
#vector con nombres de archivos
strings_archivos = []
#dataframe almacenamiento temporal de archivos
data_aux = pd.DataFrame()
#dataframe para concatenar archivos
datos = pd.DataFrame()

# se listan los archivos de una carpeta
# almacenando el nombre de cada archivo en el vector strings_archivos
def devolverArchivos(carpeta):
    global strings_archivos
    for archivo in os.listdir(carpeta):
        strings_archivos.append(os.path.join(carpeta,archivo))
        if os.path.isdir(os.path.join(carpeta,archivo)):
            devolverArchivos(os.path.join(carpeta,archivo))
                                 
# de la ruta de archivo almacenada, se toma unicamente
# el nombre del archivo y se reescribe el mismo string para almacenarlo
def convertir_nombres_archivos():
    global strings_archivos
    for file in range(0,len(strings_archivos)):
        strings_archivos[file] = strings_archivos[file][109:134]
    strings_archivos.pop(0)
    return strings_archivos

# se elimina información de los archivos es necesario que aparezca en 
# el dataframe final
def eliminar_info_no_utilizada():
    global data_aux
    indx = 144
    for fila in range(0,237):
        data_aux = data_aux.drop([indx])
        indx+=1
    return data_aux
        
# se levanta en un dataframe auxiliar los datos de cada archivo y se los
# concatena con el resto de los datos en el dataframe principal
# se aplican las funciones eliminar_info y eliminar_filas para filtrar
# los datos y dejar la que se necesita
def concatenacion_de_datos():            
    global data_aux
    global datos
    global strings_archivos
    for file_name in strings_archivos:
        print(file_name)
        data_aux = pd.read_csv(file_name)
        eliminar_info_no_utilizada()
        datos = pd.concat([datos,data_aux], ignore_index=True)
    eliminar_filas_sobra()
    return datos
    
# se busca un string específico que siempre se encuentra en la primera
# posición de la fila y en caso de encontrarlo se eliminar la fila
def eliminar_filas_sobra():
    global datos
    for fila in range(0,len(datos['Date/time'])):
        if datos['Date/time'][fila] == 'unit=°C':
            datos = datos.drop([fila])
    return datos
  
# se llaman las funciones en el orden que se debe ejecutar
# devolverArchivos("C:/Users/d935892/Desktop/Generador Datos Mensuales")
devolverArchivos("//ntpal/grupos2/Eolica/2. INGENIERÍA/04.- Sistemas informáticos/Desarrollos Python/Generador Datos Mensuales")
convertir_nombres_archivos()
concatenacion_de_datos()

# t = "//ntpal/grupos2/Eolica/2. INGENIERÍA/04.- Sistemas informáticos/Desarrollos Python/Generador Datos Mensuales"

# borrar_indx = np.arange(start=144, stop=len(datos['Date/time']), step=145)