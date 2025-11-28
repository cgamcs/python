from pathlib import Path, PureWindowsPath

archivo = Path('C:/Users/cesargael.garcia/Documents/01-PROYECTOS/python/Dia 6/prueba.txt')

ruta_windows = PureWindowsPath(archivo)

print(ruta_windows)