def suma():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))

    print(n1+n2)
    print("Gracias por sumar" + n1)

'''
try:
    # Código que queremos probar
    suma()
except TypeError:
    # Código a ejecutar si hay un error"
    print("¡Estas concatenando tipos de datos ditintos!")
except ValueError:
    # Código a ejecutar si hay un error"
    print("¡Estas ingresando un tipo de dato diferente al entero!")
else:
    # Código a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    # Código que se va a ejecutar de todos modos
    print("Todo termino")
'''


def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Gracias")

pedir_numero()