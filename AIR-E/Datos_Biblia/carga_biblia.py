import pandas as pd
import unicodedata

# Carga el archivo CSV con la codificación adecuada
df = pd.read_csv('//10.20.11.226/Compartida/Talend Job/bibliaCopia.csv', encoding='ANSI', nrows=1000 )

# Elimina los espacios en la primera línea del archivo
df.columns = df.columns.str.strip()

# Crea un diccionario de encabezados antiguos y nuevos
new_headers = {}
for old_header in df.columns:
    # Elimina las tildes de los encabezados antiguos
    new_header = unicodedata.normalize('NFKD', old_header).encode('ASCII', 'ignore').decode('utf-8')
    # Reemplaza los caracteres especiales por letras comunes
    new_header = new_header.replace('ñ', 'n').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace(' ','_')

    new_headers[old_header] = new_header

# Renombra las columnas del dataframe
df = df.rename(columns=new_headers)

df.to_csv("encabezadosCam.csv", index=False)
# Muestra el dataframe con los nuevos encabezados
print("Se realizo la ejecución...")

