import os
import shutil

# Definir la ruta de la carpeta de descarga y la ruta de la carpeta de destino
descargas_dir = os.path.expanduser('D:/Users/carlos.alvarado/Downloads')
documentos_dir = os.path.expanduser('D:/Users/carlos.alvarado/OneDrive - Air-e SAS ESP/MovimientosDownload/Nuevo/')

# Obtener la lista de extensiones de archivo únicas en la carpeta de descarga
extensiones = set(os.path.splitext(filename)[1][1:].lower() for filename in os.listdir(descargas_dir))

# Mover los archivos a la carpeta de destino correspondiente según su extensión
for extension in extensiones:
    # Construir la ruta completa de origen
    origen_dir = descargas_dir
    # Construir la ruta completa de destino
    destino_dir = os.path.join(documentos_dir, extension)
    # Crear la carpeta de destino si no existe
    os.makedirs(destino_dir, exist_ok=True)
    # Copiar los archivos con la extensión correspondiente a la carpeta de destino
    for filename in os.listdir(origen_dir):
        if filename.lower().endswith(f".{extension}"):
            # Construir la ruta completa de origen y destino
            origen = os.path.join(origen_dir, filename)
            destino = os.path.join(destino_dir, filename)
            # Verificar el espacio disponible en disco antes de copiar el archivo
            espacio_libre = shutil.disk_usage(destino_dir).free
            tamaño_archivo = os.path.getsize(origen)
            if espacio_libre >= tamaño_archivo:
                # Copiar el archivo a la carpeta de destino
                shutil.copy2(origen, destino)
                # Eliminar el archivo original si se copió correctamente
                os.remove(origen)
            else:
                print(f"No hay suficiente espacio en disco para copiar el archivo '{origen}'.")
