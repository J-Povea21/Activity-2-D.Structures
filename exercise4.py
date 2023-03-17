# 4.	Hacer un algoritmo que realice las siguientes operaciones a medida que recorre una lista:
# a.	Si la información del nodo es negativa insertar un nuevo nodo antes de este con información igual a -1000
# b.	Si la información del nodo es positiva insertar un nuevo nodo después de este con información igual a 1000
# c.	Si la información del nodo es cero eliminarlo.

# No se permite recorrer la lista más de una vez.

lista = [3, -4, 0, 5, -6, 0, 7]
nueva_lista = []

for i in range(len(lista)):
    if lista[i] < 0:
        nueva_lista.append(-1000)
        nueva_lista.append(lista[i])
    elif lista[i] > 0:
        nueva_lista.append(lista[i])
        nueva_lista.append(1000)

nueva_lista = [x for x in nueva_lista if x != 0]

print(nueva_lista)
