import os
import re
import math
import time
import shutil
from datetime import date
from pathlib import Path

shutil.unpack_archive('Proyecto+Dia+9.zip', 'Esxtraccion_Instrucciones', 'zip')

dir = 'C:\\Users\\cesargael.garcia\\Documents\\01-PROYECTOS\\python\\Dia 9\\Esxtraccion_Instrucciones\\Mi_Gran_Directorio'

lista = []

def busqueda_no_serie(ruta):
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            abrir_archivo = open(Path(carpeta, arch), 'r')
            patron = r'N\w{3}-\d{5}'
            busqueda = re.search(patron, abrir_archivo.read())
            if busqueda:
                lista.append({'archivo': arch, 'nro. serie': busqueda.group()})

inicio = time.time()
busqueda_no_serie(dir)
final = time.time()
tiempo = final - inicio

print(f'Fecha de busqueda: {date.today()}')

print('-'*30)
print('ARCHIVO \t\t NRO. SERIE')
print('-'*30)

for encontrado in lista:
    print(f'{encontrado['archivo']} \t {encontrado['nro. serie']}')

print('-'*30)
print(f'Números encontrados: {len(lista)}')
print(f'Duración de la búsqueda: {math.ceil(tiempo)} segundos')