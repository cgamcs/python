def detectar_consecutivos(*args):
    contador = 0

    for arg in args:
        if arg == 0:
            contador += 1

        if contador == 2:
            return True

    return False


print(detectar_consecutivos(5,6,1,0,0,9,3,5))