from numeros import *

cosmetica_decorado = decorador_generador(generador_cosmetica)
farmacia_decorado = decorador_generador(generador_farmacia)
perfumeria_decorado = decorador_generador(generador_perfumeria)

def preguntar_departamento():
    print('----------------')
    print('[P] - Perfumeria')
    print('[F] - Farmacia')
    print('[C] - Cosmetica')
    respuesta = input('Qué departamento desea ingresar? ').upper()

    menu(respuesta)

def menu(opcion):
    match opcion:
        case 'P':
            print('\nEstas en Perfumeria')
            perfumeria_decorado()
        case 'F':
            print('\nEstas en Farmacia')
            farmacia_decorado()
        case 'C':
            print('\nEstas en Cosmetica')
            cosmetica_decorado()

def iniciar():
    while True:
        preguntar_departamento()

iniciar()