# Manejo de datos

datosObtenidos = """x\np.666"""
print(datosObtenidos)
# listas de listas
b=datosObtenidos.split("\n")
print(b)

b=datosObtenidos.split(".")
print(b[0])

a = [x.split(" ") for x in b]

print(a)

b="-2,86"
a =eval("-2.86%".replace("%","")) 
print(type(a))
print(a)
print(eval(b))


