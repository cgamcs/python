lista = ['a', 'b', 'c', 'd', 'e']
indice = 0

for letra in lista:
    indice += 1
    print(f'{indice} - {letra}')

print('\n')
# Usando enumerate
lista = ['a', 'b', 'c', 'd', 'e']
for indice, letra in enumerate(lista):
    print(indice, letra)