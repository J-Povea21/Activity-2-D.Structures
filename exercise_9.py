import collections
L1 = [2, 3, 2, 4]
L2 = [4, 2, 2, 3]

print(L1, L2)
if collections.Counter(L1) == collections.Counter(L2):
    print("The lists are equal")
else:
    print("The list are not equal")