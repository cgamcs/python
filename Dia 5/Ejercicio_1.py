def devolver_distintos(*args):
    total = 0
    recuento = 0
    lista_enteros = []

    for arg in args:
        lista_enteros.append(arg)
        recuento += 1
        total += arg

    if recuento > 4:
        print("Solo se deben de agregar 3 enteros")
        return

    lista_enteros.sort()

    if total > 15:
        print(lista_enteros[2])
    elif total >= 10 and total <= 15:
        print(lista_enteros[1])
    elif total < 10:
        print(lista_enteros[0])

devolver_distintos(4, 3, 2)