import pandas as pd

# Cargamos el libro de Excel con las dos hojas
excel_file = pd.ExcelFile('C:/Desarrollos/Reclamos/input/ATL SUR.xlsx')

# Leemos la primera hoja y la guardamos en un DataFrame
hoja1 = pd.read_excel(excel_file, 'LECTA')

# Leemos la segunda hoja y la guardamos en otro DataFrame
hoja2 = pd.read_excel(excel_file, 'PYG')

# Unimos las dos hojas en un solo DataFrame
resultado = pd.concat([hoja1, hoja2])

# Guardamos el resultado en un nuevo archivo de Excel
resultado.to_excel('nombre_del_nuevo_archivo.xlsx', index=False)
print("prueba")