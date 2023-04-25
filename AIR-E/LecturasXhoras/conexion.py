import cx_Oracle
from datetime import datetime
import logging

def conLect():
    # Consulta proveniente de un archivo externo
    file = open('D:\Desarrollos\sql\consultaCsmo.txt', 'r')
    # guarda en variable la consulta del archivo externo
    query = file.read()
    rowarray_list = []
    logging.warning('conexión base de datos!')  # will print a message to the console
    """
    year = str(datetime.today().year)
    month = str(datetime.today().month)
    date = year + '' + month
    logging.info('consulta de base de datos!')  # will print a message to the console
    """
    dsn_tns = cx_Oracle.makedsn('10.20.10.58', '1521', service_name='')
    conn = cx_Oracle.connect(user=r'', password='', dsn=dsn_tns)
    querystring = query
    c = conn.cursor()
    c.execute(querystring)
    for row in c:
        rowarray_list.append(row)
    return rowarray_list
    # Cierra la conexio a la base
    conn.close()
