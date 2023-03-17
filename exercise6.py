# 6.	Dada una lista enlazada simple ya creada, hacer un algoritmo que vaya formando dos listas
# (PTR1 y PTR2) con los mismos nodos de la lista inicial de tal forma que en la lista PTR1
# vayan quedando todos los elementos positivos, y en la lista PTR2 todos los elementos
# negativos. Si hay nodos que tengan como información el 0 se eliminan.

ptr1 = [37, 23, -32, 34, -56, 45, 78, -21, -13, 23, 56, -34, 34, 20, 89, 32, 0]
ptr2 = []
ptr3 = []
for value in ptr1:
    if value < 0:
        ptr2.append(value)
    elif value > 0:
        ptr3.append(value)
    else:
        pass

print("Lista con valores negativos: ", ptr2)
print("----------------------------------------------------------------------------")
print("Lista con valores positivos: ", ptr3)
