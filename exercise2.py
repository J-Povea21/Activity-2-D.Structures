# 2.	Hacer un algoritmo que escriba el número total de elementos diferentes
# en una lista enlazada ya creada. ¿Cuáles son?

lista = [3, 5, 2, 3, 1, 5, 2, 5, 4, 3]
diferentes = []
cant_dif = 0

for i in lista:
    if lista.count(i) == 1:
        diferentes.append(i)
        cant_dif += 1

print("Hay ", cant_dif, " de números diferentes y son: ", diferentes)
