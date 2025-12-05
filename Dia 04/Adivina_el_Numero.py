from random import *

print('INICIO DEL JUEGO\n')
nombre = input('¿Cuál es tu nombre? ')
print(f'{nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número')

numero_aleatorio = randint(1,100)

print('\nEMPIEZAN LOS 8 INTENTOS DE ADIVINAR')
for intento in range(0,8):
    respuesta = int(input(f'Intento {intento+1}: '))

    if respuesta > 100 or respuesta < 100:
        print('Solo se permiten numeros menores a 100 y mayores que 0')
    elif intento + 1 == 8 and respuesta != numero_aleatorio:
        print('\n¡GAME OVER!')
    elif respuesta > numero_aleatorio:
        print('Escogiste un numero más alto del que pense')
    elif respuesta < numero_aleatorio:
        print('Escogiste un numero más bajo del que pense')
    elif respuesta == numero_aleatorio:
        print('\n!Felicitaciones haz acertado al numero correcto!')
        break