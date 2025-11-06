from random import *

aleatorio = randint(1, 10)
print(aleatorio)

aleatorio = round(uniform(1, 5), 2)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['azul', 'verde', 'amarillo', 'verde']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5, 51, 5))
shuffle(numeros)
print(numeros)