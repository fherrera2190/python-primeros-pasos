# [
#     fila
#     for fila in {lista}
#     if "PAGO" in fila[1]
#     and not any(excepcion in fila[1] for excepcion in {excepciones})
# ]

# to="35267568@fi.unju.edu.ar"
# cc= "fernando.herrera@gmail.com, nemesis@gmail.com"
# bcc= "fernando.herrera@rockebot.com, jill@gmail.com"
# to3=""
# print(to3 or True)
# to=to.split(",")
# to2=to2.split(",")
# to3=to3.split(",")




# print(to)
# print(to+to2)


# to3=[]

# if not to3:
#     print("hola")

# if to3:
#     print("vacio")
#     print(to3)
#     print(len([]))

# print( ["AAA"]+[])
def split_emails(emails):
    return emails.split(",") if emails else []

to=""
cc= ""
bcc= ""


result = split_emails(to) + split_emails(cc) + split_emails(bcc)

print(result)