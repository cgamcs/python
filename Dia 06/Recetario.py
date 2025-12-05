import os
from pathlib import Path

base = Path(Path.home(), "Recetas")
categorias = []

print("BIENVENIDO A TU RECETARIO")

print("=========================")

print("Esta es la ruta de acceso al recetario -", base)

contador = 0
for txt in Path(base).glob("**/*.txt"):
    contador += 1
print(f"El recetario tiene un total de {contador} recetas")

print("=========================")

def elegir_categoria():
    print("\nCategorias disponibles:")

    for carpeta in base.iterdir():
        if carpeta.is_dir():
            categorias.append(os.path.basename(carpeta))
            print(os.path.basename(carpeta))

    categoria = input("\nElige una categoría: ")

    return categoria

def limpiar_categorias():
    categorias = []

def leer_receta():
    # system('cls')
    categoria = elegir_categoria()

    if categoria in categorias:
        for txt in Path(base, categoria).glob("*.txt"):
            print(os.path.basename(txt))

        texto = input("\n¿Qué receta deseas leer?: ")

        abrir_texto = Path(base, categoria, texto)

        leer_texto = open(abrir_texto)
        print(leer_texto.read())
        leer_texto.close()

        input("\nPresiona ENTER para continuar... ")
        elegir_menu()

    limpiar_categorias()

def crear_receta():
    categoria = elegir_categoria()

    if categoria in categorias:
        nombre_receta = input("\nEscribe el nombre de la receta (agrega el .txt): ")
        ruta = Path(base, categoria, nombre_receta)

        receta = input("\nEscribe la receta: ")
        ruta.write_text(receta)


        input("\nPresiona ENTER para continuar... ")
        elegir_menu()

    limpiar_categorias()

def crear_carpeta():
    os.chdir(base)
    nombre_categoria = input("\nEscribe el nombre de la nueva categoria: ")
    os.makedirs(nombre_categoria)
    print("Nueva categoria creada!!")

    input("\nPresiona ENTER para continuar... ")
    elegir_menu()

def eliminar_archivo():
    categoria = elegir_categoria()
    if categoria in categorias:
        nombre_receta = input("\nEscribe el nombre de la receta (agrega el .txt): ")
        ruta = Path(base, categoria, nombre_receta)

        os.remove(ruta)
        print("Archivo eliminado!!")

        input("\nPresiona ENTER para continuar... ")
        elegir_menu()

    limpiar_categorias()

def eliminar_categoria():
    nombre_categoria = input("\nEscribe el nombre de la categoria: ")
    ruta = Path(base, nombre_categoria)

    os.rmdir(ruta)
    print("Archivo eliminado!!")

    input("\nPresiona ENTER para continuar... ")
    elegir_menu()

def elegir_menu():
    print('\n[1] - leer receta')
    print('[2] - crear receta')
    print('[3] - crear categoría')
    print('[4] - eliminar receta')
    print('[5] - eliminar categoría')
    print('[6] - eliminar programa')

    opcion = int(input("\nElige una opcion: "))

    menu(opcion)

def menu(opcion):
    match opcion:
        case 1:
            leer_receta()
        case 2:
            crear_receta()
        case 3:
            crear_carpeta()
        case 4:
            eliminar_archivo()
        case 5:
            eliminar_categoria()
        case 6:
            print("Programa terminado.")
            return

elegir_menu()