monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1

respuesta = 's'

while respuesta == 's':
    respuesta = input('Quieres seguie (s/n) ')
else:
    print('Fin')

while respuesta == 's':
    pass

print('Paso')