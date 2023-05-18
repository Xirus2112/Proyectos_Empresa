import chardet
from tqdm import tqdm


def determinar_codificacion(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo:
        datos = archivo.read()
        total_bytes = len(datos)

        with tqdm(total=total_bytes, unit='B', unit_scale=True, desc='Analizando archivo') as pbar:
            resultado = chardet.detect(datos)
            codificacion = resultado['encoding']
            pbar.update(total_bytes)

    return codificacion


ruta_archivo = r'C:/TareasProgramadas/DescDatos/Biblia/biblia.csv'
codificacion = determinar_codificacion(ruta_archivo)
print("La codificación del archivo CSV es:", codificacion)

# Codificacion de la biblia es Windows-1252