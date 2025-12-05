import os
import shutil

archivo = open('curso.txt', 'w')
archivo.write('Curso en python')
archivo.close()

# mueve un archivo a la carpeta que designes
# shutil.move('curso.txt', "C:\\Users\\cesargael.garcia\\Desktop")

# os.unlink elimina un archivo desde una ruta
# os.rmdir - elimina una carpeta vacia desde una ruta

# precaucion con este metodo porque
# borra todo sin dejarlo en la papelera
# shutil.rmtree elimina todo lo que se encuentra en una ruta

# Alternativas
# puedes usar send2trash con pip install send2trash

# send2trash.send2trash('curso.txt')

# metodo para recorrer todos los directorios, carpetas y subcarpetas
ruta = 'C:\\Users\\cesargael.garcia\\Desktop\\carpeta_padre'
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print('Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
