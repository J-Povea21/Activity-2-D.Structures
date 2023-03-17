lista = [2,3,4,5,9,87,-32,45]
print("Estos son los valors que tiene la lista: ",lista)
numero = int(input("Cual quieres eliminar? "))
for i in lista:
    if i==numero:
        lista.remove(i)

print(lista)

