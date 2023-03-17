# 5.	Hacer un algoritmo que recorra una lista y regrese dos listas L1 y L2.
# L1 debe contener los elementos de la lista inicial (sin repetir) y L2
# debe contener las veces que se repite ese número.

lista = [1, 2, 3, 2, 1, 4, 5, 5, 1]
L1 = []
L2 = []

for num in lista:
    if num not in L1:
        L1.append(num)
        L2.append(1)
    else:
        index = L1.index(num)
        L2[index] = L2[index] + 1

print("Elementos iniciales de la lista sin repetir: ", L1)
print("Número de veces que se repide cada número: ", L2)