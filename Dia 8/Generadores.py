def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x)
    return lista 

def mi_generador():
    for x in range(1,5):
        yield x

print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g)) # forma de generar
print(next(g)) # forma de generar
print(next(g)) # forma de generar
print(next(g)) # forma de generar
