import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import sys
import warnings

warnings.simplefilter("ignore")

# Ruta de los archivos
ruta_archivos = r'C:\Desarrollos\Reclamos\input'

# Obtener la lista de archivos en la ruta especificada
archivos = os.listdir(ruta_archivos)

# Crear un DataFrame vacío para almacenar los datos consolidados
df_consolidado = pd.DataFrame(
    columns=['Nic', 'Ciclo', 'ItinerarioEnvio', 'DepartamentoEnvio', 'FECHA DE IMPRESIÓN', 'HORA RECIBIDA',
             'ESTADO', 'FECHA DE ENTREGA DE LA FACTURA', 'TIPO', 'CLASIFICACIÓN'])

# Variable para contar el número total de registros
total_registros = 0

# Inicializar la ventana de mensajes
root = tk.Tk()
root.withdraw()

# Iterar sobre los archivos
for archivo in archivos:
    if archivo.endswith('.xlsx'):
        ruta_archivo = os.path.join(ruta_archivos, archivo)

        try:
            # Leer el archivo Excel
            xls = pd.ExcelFile(ruta_archivo)
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer el archivo {archivo}: {str(e)}")
            sys.exit(1)  # Abortar el proceso en caso de error

        # Iterar sobre las hojas del archivo
        for hoja in ['LECTA', 'PYG']:
            if hoja in xls.sheet_names:
                try:
                    # Leer la hoja y seleccionar las columnas requeridas
                    df = pd.read_excel(xls, hoja, usecols=['Nic', 'Ciclo', 'ItinerarioEnvio', 'DepartamentoEnvio',
                                                           'FECHA DE IMPRESIÓN', 'HORA RECIBIDA', 'ESTADO',
                                                           'FECHA DE ENTREGA DE LA FACTURA', 'TIPO', 'CLASIFICACIÓN'])

                    # Agregar los datos al DataFrame consolidado
                    df_consolidado = pd.concat([df_consolidado, df])

                    # Actualizar el número total de registros
                    total_registros += len(df)
                except Exception as e:
                    messagebox.showerror("Error", f"Error al leer la hoja {hoja} del archivo {archivo}: {str(e)}, Por favor abra el archivo e identifique lo encerrado dentro de los [ ]")
                    sys.exit(1)  # Abortar el proceso en caso de error

    # Calcular el porcentaje de avance
    #porcentaje_avance = (total_registros / len(archivos)) * 100
    #print(f"Porcentaje de avance: {porcentaje_avance:.2f}%")

# Guardar el DataFrame consolidado en un archivo CSV
ruta_salida = r'C:\Desarrollos\Reclamos\output\consolidadoReparto_indi.csv'
df_consolidado.to_csv(ruta_salida, index=False)

print("Consolidación finalizada. Archivo CSV guardado en:", ruta_salida)

# Mostrar un mensaje de éxito al finalizar
messagebox.showinfo("Finalizado", f"La consolidación ha finalizado. El archivo CSV ha sido guardado en la ruta: {ruta_salida}")