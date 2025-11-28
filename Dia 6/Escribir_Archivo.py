mi_archivo = open("prueba.txt", "a")
'''
a: reescribe el archivo agregando el texto al final del documento
w: reescribe el archivo completamente
r: solo lee el archivo
'''

mi_archivo.write("\nSoy el nuevo texto")
mi_archivo.close()