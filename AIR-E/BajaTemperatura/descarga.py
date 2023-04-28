import requests
import csv
from datetime import datetime, timedelta
import calendar

# Inserta aquí tu API Key
api_key = "9293df161ee2c0da596868e2f5a54b7e"

# Definir la fecha de inicio del mes actual
start_date = datetime.now().date().replace(day=1)

# Definir la fecha de finalización como el último día del mes actual
_, last_day_of_month = calendar.monthrange(start_date.year, start_date.month)
end_date = start_date.replace(day=last_day_of_month)

# URL de la API para obtener los datos de temperatura de Barranquilla
url = f"http://api.openweathermap.org/data/2.5/forecast?q=Barranquilla,CO&appid={api_key}&units=metric"

# Realizar la solicitud GET a la API y obtener los datos en formato JSON
response = requests.get(url).json()

# Filtrar los datos para obtener solo las temperaturas diarias del mes actual
daily_temperatures = {}
for forecast in response["list"]:
    # Obtener la fecha y hora de la previsión
    forecast_date = datetime.fromtimestamp(forecast["dt"])

    # Si la fecha de la previsión está dentro del rango especificado
    if start_date <= forecast_date.date() <= end_date:
        # Obtener la fecha y temperatura diarias y agregarla al diccionario de temperaturas
        daily_date = forecast_date.date()
        daily_temperature = forecast["main"]["temp"]
        if daily_date not in daily_temperatures:
            daily_temperatures[daily_date] = daily_temperature

# Crear un archivo CSV y escribir los datos de temperatura
with open("C:/TalendDesc/temperaturas_barranquilla.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Fecha", "Temperatura"])
    for date, temperature in daily_temperatures.items():
        writer.writerow([date, temperature])
