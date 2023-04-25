'''
### factNovedadFronteras
import os
import pandas as pd

# Ruta donde se encuentran los archivos de Excel
ruta = "//10.20.11.226/Compartida/BASEc/novedadesFronteras/PubFC_Fronteras"

# Lista para almacenar los datos de cada archivo
datos = []

# Recorremos los archivos en la ruta
for archivo in os.listdir(ruta):
    if archivo.startswith("PubFC2023"):
        # Leemos el archivo y almacenamos los datos en la lista
        df = pd.read_excel(os.path.join(ruta, archivo))
        datos.append(df)

# Unimos los datos de todos los archivos
datos_unidos = pd.concat(datos)

# Filtrando la columna Operador de Red
datos_filtrados = datos_unidos[datos_unidos["Operador de Red"] == "AIR- E S.A.S. E.S.P. - DISTRIBUIDOR"]

# Guardamos los datos en un archivo nuevo
datos_filtrados.to_excel("ProcesoReg2023.xlsx", index=False)

print("Finaliza. . .")'''

import os
import pandas as pd
import schedule
import time

def unificar_y_filtrar_archivos():
    # Ruta donde se encuentran los archivos de Excel
    ruta = "ruta/a/tus/archivos"

    # Lista para almacenar los datos de cada archivo
    datos = []

    # Recorremos los archivos en la ruta
    for archivo in os.listdir(ruta):
        if archivo.startswith("PubFC2023"):
            # Leemos el archivo y almacenamos los datos en la lista
            df = pd.read_excel(os.path.join(ruta, archivo))
            datos.append(df)

    # Unimos los datos de todos los archivos
    datos_unidos = pd.concat(datos)

    # Filtramos los registros de la columna "Operador de Red"
    datos_filtrados = datos_unidos[datos_unidos["Operador de Red"] == "AIR- E S.A.S. E.S.P. - DISTRIBUIDOR"]

    # Guardamos los datos filtrados en un archivo nuevo
    datos_filtrados.to_excel("archivo_filtrado.xlsx", index=False)
    print("Archivos unificados y filtrados con éxito.")

# Programamos la tarea para que se ejecute todos los días a las 00:00
schedule.every().day.at("00:00").do(unificar_y_filtrar_archivos)

# Ejecutamos la tarea indefinidamente
while True:
    schedule.run_pending()
    time.sleep(1)
