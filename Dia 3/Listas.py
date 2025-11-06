mi_lista = ["a", "b", "c"]

print(mi_lista)
print(mi_lista[:2])
print(mi_lista[0])

mi_lista2 = ["d", "e", "f"]

print(mi_lista + mi_lista2)

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista3[0] = "alfa"
print(mi_lista3)

mi_lista3.append("g")
print(mi_lista3)

mi_lista3.pop() # elimina el ultimo elemento de la lista
nueva_lista = mi_lista3.pop() # devuelve el ultimo elemento de la lista
print(nueva_lista)

mi_lista4 = ["b", "g", "e", "f", "a", "d", "c"]
mi_lista4.sort() # este metodo no devuelve una nueva lista
mi_lista4.reverse() # este metodod no devuelve nada
print(mi_lista4)