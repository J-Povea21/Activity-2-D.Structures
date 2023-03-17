lista1 = [2,3,4,8,9,5,7]
lista2 = [7,4,9,10,34]

for i in lista1:
    for j in lista2:
        if i==j:
            lista1.remove(i)

print(lista1)