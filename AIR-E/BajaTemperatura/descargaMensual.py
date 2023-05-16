import requests
import csv

# Llave
api_key = "9293df161ee2c0da596868e2f5a54b7e"

# URL base de la API
base_url = "http://api.openweathermap.org/data/2.5/weather"

# parámetros de consulta comunes
params = {
    "q": "Barranquilla",
    "appid": api_key,
    "units": "metric"
}

# Creo el archivo en modo escritura
with open("datos_climaticos.csv", mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Cabecera
    writer.writerow(["Fecha", "Temperatura", "Sensacion_Termica"])

    # Extraigo Abril
    for dia in range(1, 31):
        params["dt"] = f"2023-04-{dia}"
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            fecha = f"2023-04-{dia}"
            temperatura = data['main']['temp']
            sensacion_termica = data['main']['feels_like']
            writer.writerow([fecha, temperatura, sensacion_termica])

    # Extraer datos de temperatura y sensación térmica para mayo
    for dia in range(1, 32):
        params["dt"] = f"2023-05-{dia}"
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            fecha = f"2023-05-{dia}"
            temperatura = data['main']['temp']
            sensacion_termica = data['main']['feels_like']
            writer.writerow([fecha, temperatura, sensacion_termica])

print("Los datos climáticos se han guardado en el archivo datos_climaticos.csv.")
