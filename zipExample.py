a = [1, 2,3,4]
b = ["Uno", "Dos","Tres"]
c = zip(a, b)
print(c)

print(type(c))
print(list(c))

for num,word in c:
    print(num,word)

# [(1, 'Uno'), (2, 'Dos')]