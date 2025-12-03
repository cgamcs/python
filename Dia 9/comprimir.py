import zipfile
import shutil

#mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

#mi_zip.write('mi_texto_A.txt')
#mi_zip.write('mi_texto_B.txt')

#mi_zip.close()

#zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
#zip_abierto.extractall()
#zip_abierto.close()

carpeta_org = 'C:\\Users\\cesargael.garcia\\Desktop\\carpeta_padre'

archivo_destino = 'Todo_Comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_org)

shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion_Terminada', 'zip')