from random import choice

lista_palabras = ['ahorcado', 'helicoptero', 'ambulancia', 'avion', 'puente']

print('""""""""""""""""""')
print("Juego del Ahorcado")
print('""""""""""""""""""')

def escoger_palabra(lista):
    palabra_escogida = choice(lista)

    return palabra_escogida

def mostrar_guiones(palabra_escogida):
    len_palabra = len(list(palabra_escogida))

    print(len_palabra * '_')

def intentos_letra(palabra_escogida):
    vidas = 6
    lista_palabra = list(palabra_escogida)
    palabra_guiones = list(len(lista_palabra) * "_")
    resultado = ""

    while vidas > 0 and len(lista_palabra) > 0:
        intento = input('\nIntroduce una letra: ')

        if intento not in lista_palabra:
            vidas -= 1

        contador = 0
        for letra in lista_palabra:
            contador += 1

            if letra == intento:
                palabra_guiones[contador - 1] = intento
                lista_palabra[contador - 1] = '_'
                resultado = "".join(palabra_guiones)
                print(resultado)

        if palabra_escogida == resultado:
            print("Felicidades Ganaste!")
            break

    if vidas == 0: print("Game Over")


palabra = escoger_palabra(lista_palabras)
mostrar_guiones(palabra)
intentos_letra(palabra)