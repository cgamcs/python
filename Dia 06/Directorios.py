import os
from pathlib import Path

# Obtiene la ruta de origen
ruta = os.getcwd()
print(ruta)

# Entra a otros directorios
ruta = os.chdir("C:\\Users\\cesargael.garcia\\Documents\\01-PROYECTOS\\curso-python")
archivo = open("prueba.txt")
print(archivo.read())
archivo.close()

# Crea nuevos directorios
# ruta = os.makedirs("C:\\Users\\cesargael.garcia\\Documents\\01-PROYECTOS\\curso-python\\otra")

# Obtener nombre y directorio
ruta = 'C:\\Users\\cesargael.garcia\\Documents\\01-PROYECTOS\\python\\Dia 06\\prueba.txt'

elemento = os.path.basename(ruta) # prueba.txt
elemento = os.path.dirname(ruta) # C:\Users\cesargael.garcia\Documents\01-PROYECTOS\python\Dia 06
elemento = os.path.split(ruta) # ('C:\\Users\\cesargael.garcia\\Documents\\01-PROYECTOS\\python\\Dia 06', 'prueba.txt')

print(elemento)

# Eliminar carpeta
# os.rmdir("C:\\Users\\cesargael.garcia\\Documents\\01-PROYECTOS\\curso-python\\otra")

# Abrir un archivo con ruta directa
archivo = open("C:\\Users\\cesargael.garcia\\Documents\\01-PROYECTOS\\curso-python\\prueba.txt")
print(archivo.read())
archivo.close()

# Froma alternativa para poder leer el directorio de cualquier sistema operativo
carpeta = Path('C:/Users/cesargael.garcia/Documents/01-PROYECTOS/curso-python')
archivo = carpeta / 'prueba.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())
mi_archivo.close()