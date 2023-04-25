'''Versión 2'''
import time
import subprocess
import datetime

count = 0

while True:
    now = datetime.datetime.now()
    start_time = datetime.datetime(now.year, now.month, now.day, 7, 0, 0)
    end_time = datetime.datetime(now.year, now.month, now.day, 19, 0, 0)

    if start_time <= now <= end_time:
        count += 1
        subprocess.run("D:/tareasProgramadas_tos/AjusteFacturacion/ejecAjusteFact.bat", shell=True)
        print(f"Ejecución número {count} a las {now}")
    else:
        print(f"Esperando para ejecutar... hora actual: {now}")
    time.sleep(1800) # Esperar 30 minutos (1800 segundos)