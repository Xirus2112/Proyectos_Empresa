import requests
import csv
from datetime import date
import schedule
import time

# Obtener tu API key de OpenWeatherMap
api_key = "9293df161ee2c0da596868e2f5a54b7e"

# Definir la URL base de la API
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Definir los parámetros de consulta comunes
params = {
    "q": "Barranquilla",
    "appid": api_key,
    "units": "metric"
}

# Función para extraer y guardar los datos climáticos
def extraer_datos_climaticos():
    # Obtener la fecha actual
    fecha_actual = date.today()

    # Abrir el archivo CSV en modo anexar
    with open("//10.20.11.226/Compartida/BASEc/historicoClimatico/historico_climatico.csv", mode="a", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Si el archivo está vacío, escribir la cabecera
        if csv_file.tell() == 0:
            writer.writerow(["Fecha", "Temperatura", "Sensacion_Termica"])

        params["dt"] = fecha_actual.strftime("%Y-%m-%d")
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            fecha = fecha_actual.strftime("%Y-%m-%d")
            temperatura = data['main']['temp']
            sensacion_termica = data['main']['feels_like']
            writer.writerow([fecha, temperatura, sensacion_termica])

    print(f"Datos climáticos actualizados para el {fecha_actual}.")

# Programar la ejecución diaria de la función
schedule.every().day.at("08:00").do(extraer_datos_climaticos)

# Solo un valor agregado para que este a la escucha y cada 60 segundos se ejecute
while True:
    schedule.run_pending()
    time.sleep(60)  # Esperar 60 segundos antes de verificar nuevamente

