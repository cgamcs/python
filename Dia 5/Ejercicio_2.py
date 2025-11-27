def devolver_letras(string):
    lista_caracteres = list(set(string))
    lista_caracteres.sort()

    return lista_caracteres

print(devolver_letras("entretenido"))