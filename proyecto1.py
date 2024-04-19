from datetime import datetime
import os
import re


# print(datetime.now())
# print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# Result
# 2024-04-13 13:55:58.126011
# 13-04-2024 13:55:58

# archivo ="D:/busqueda.xlsx"
# nombre,extension=os.path.splitext(archivo)
# print(nombre,extension)
# Result
# D:/busqueda

# if
# if(1==1):
#     print("es igual")
# else:
#     print("No es igual")

# Eliminar el .
# numero = "13.900"
# numero_sin_punto = numero.replace(".", "")
# print(numero_sin_punto)

# expresion regular Filtrar xml
xml = """<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><FahrenheitToCelsiusResponse xmlns="https://www.w3schools.com/xml/"><FahrenheitToCelsiusResult>37.7777777777778</FahrenheitToCelsiusResult></FahrenheitToCelsiusResponse></soap:Body></soap:Envelope>"""
# Cuando tiene salto de linea
# re.search("<FahrenheitToCelsiusResult>(.+?)</FahrenheitToCelsiusResult>","""{res}""").group(1)

result = re.search(
    "<FahrenheitToCelsiusResult>(.+?)</FahrenheitToCelsiusResult>", xml
).group(1)
print(result)


import subprocess

# Iniciar un proceso para ejecutar el comando 'ls' y capturar la salida
proceso = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)

# Capturar la salida del proceso
salida, errores = proceso.communicate()

# Imprimir la salida del comando
print(salida.decode())

# Manejo de datos

# datosObtenidos = """x.p"""

# listas de listas
# b=datosObtenidos.split("\n")

# print(b)
# a = [x.split(" ") for x in b]

# print(a)

nExcel="PRICE LIST 24RTMX-ELEN006.xls"

pricelist="PRICE LIST" in nExcel

print(pricelist)

palabra = None

#if None
if palabra is not None:
    print(palabra)
    print("No Es None","xxxxxxxxxxxxxxxx")
else:
    print(palabra)
    print("Es None",">>>>>>>>>>>>>>>>")

#for

#for i in range(0,100):
 #   print (i)

lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

diccionario = {"a": 1, "b": 2, "c": 3}
for clave in diccionario:
    print(clave, diccionario[clave])

diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():
    print(clave, valor)

conjunto = {1, 2, 3, 4, 5}
for elemento in conjunto:
    print(elemento)

cadena = "Hola"
for caracter in cadena:
    print(caracter)