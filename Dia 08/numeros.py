def generador_perfumeria():
    numero = 0

    while True:
        numero += 1
        yield f'P-{numero}'

def generador_farmacia():
    numero = 0

    while True:
        numero += 1
        yield f'F-{numero}'

def generador_cosmetica():
    numero = 0

    while True:
        numero += 1
        yield f'C-{numero}'

def decorador_generador(funcion):
    generador = funcion()
    def imprimir_ticket():
        print('Su turno es:')
        print(next(generador))
        print('Aguarde y sera atendido\n')

    return imprimir_ticket