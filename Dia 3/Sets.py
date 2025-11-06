mi_set = set([1, 2, 3, 4, 5, 6])
otro_set = {1, 2, 3, 4, 5, 6}

print(type(mi_set))
print(type(otro_set))

print(mi_set)

"""
No se pueden anidar listas
ni diccionarios en un set,
pero si se puede agregar tuples,
ya que son inmutables
"""
mi_tuple = (1, 2, (3, 4))
print(mi_tuple)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)

s1.remove(4)
print(s1)

s1.discard(6)
print(s1)

"""
Tambien funciona el metodo pop()
solo que en este caso como los sets no tienen un orden,
la eliminacion sera aleatorio
"""
s1.pop()
print(s1)

s1.clear()
print(s1)