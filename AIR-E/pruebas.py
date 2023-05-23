"""
    --- Esta hoja es para solo pruebas a realizar ---
"""

aprobado = "aprobado"
rechazado = "rechazado"

atc = rechazado
gf = aprobado
ce = rechazado

if atc == aprobado and ce == aprobado and gf == aprobado:
    print("Aprobado")
elif    atc == rechazado and ce == rechazado and gf == rechazado:
    print("Rechazado")
else:
    print("Nada")