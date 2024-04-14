from datetime import datetime
import os


print(datetime.now())
print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

#Result
# 2024-04-13 13:55:58.126011
# 13-04-2024 13:55:58

archivo ="D:/busqueda.xlsx"
nombre,extension=os.path.splitext(archivo)
print(nombre,extension)
#Result  
#D:/busqueda

#if
# if(1==1):
#     print("es igual")
# else:
#     print("No es igual")

#Eliminar el .
numero = "13.900"
numero_sin_punto = numero.replace(".", "")
print(numero_sin_punto)