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
    print(clave+" : ", valor)

conjunto = {1, 2, 3, 4, 5}
for elemento in conjunto:
    print(elemento)

cadena = "Hola"
for caracter in cadena:
    print(caracter)