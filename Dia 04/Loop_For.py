lista = ['a', 'b', 'c', 'd', 'e']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

lista = ['Pedro', 'Laura', 'Maria', 'Luis', 'Julia']
for nombre in lista:
    if nombre.lower().startswith('l'):
        print(nombre)


numeros = [1, 2, 3, 4, 5, 6]
mi_valor = 0

for numero in numeros:
    mi_valor += numero

print(mi_valor)

for a,b in [[1,2], [3,4], [5,6], [7,8]]:
    print(a)
    print(b)

for objeto in [[1,2], [3,4], [5,6], [7,8]]:
    print(objeto)
    for numero in objeto:
        print(numero)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)