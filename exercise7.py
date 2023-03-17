# 7.	Dadas dos listas enlazadas simples ya creadas (PTR1 y PTR2) ordenadas ascendentemente,
# hacer un algoritmo que cree una tercera lista PTR3 ordenada descendentemente con los
# elementos comunes de las dos listas.

ptr1 = [8, 2, 4, 7, 8]
ptr2 = [8, 1, 2, 3, 4, 5, 6, 7]
ptr3 = []

for i in ptr1:
    for j in ptr2:
        if i == j and i not in ptr3:
            ptr3.append(i)

ptr3.sort(reverse=True)

print(ptr3)
