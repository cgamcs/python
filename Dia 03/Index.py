texto = "Esta es una prueba de index"

resultado = texto[0]
print(resultado)

resultado = texto.index("a")
print(resultado)

resultado = texto.index("a", 5)
print(resultado)

resultado = texto.index("a", 5, 12) # si el ultimo parametro fuera 10 habria un error
print(resultado)

resultado = texto.index("index")
print(resultado)

resultado = texto.rindex("a")
print(resultado)
