mi_tuple = (1, 2, 3, (8, 9, 10), 4, 5, 6, 7)
# mi_tuple[2] = 4 esto no funiona porque los tuples son inmutables

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

mi_tuple = (1, 2, 3)

"""
Esto se puede hacer con listas
y diccionarios, la unica condicion
es que se tenga la misma canitdad
de elementos y variables
"""
x, y, z = mi_tuple
print(x, y, z)