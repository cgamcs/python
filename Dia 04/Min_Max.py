menor = min(32, 52, 65, 23, 49, 93)
mayor = max(32, 52, 65, 23, 49, 93)

print(menor, mayor)

lista = [32, 52, 65, 23, 49, 93]
print(min(lista))

"""
La bsuqueda del caracter
de menor valor se hace de la A-Z
empezando por mayusculas 
"""
palabra = 'Python'

print(min(palabra)) # resultado: P
print(min(palabra.lower())) # resultado: h

dic = {'C1': 45, 'C2': 11}

print(min(dic))

print(min(dic.values()))
print(min(dic.keys()))