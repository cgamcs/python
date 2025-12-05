def chequear_3_cifras(numero):
    return numero in range(100, 1000)

resultado = chequear_3_cifras(689)
print(resultado)

def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass

resultado = chequear_3_cifras([12, 559, 42, 4012])
print(resultado)

def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado = chequear_3_cifras([12, 559, 42, 401])
print(resultado)