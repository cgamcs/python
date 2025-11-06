nombre = ['Ana', 'Hugo', 'Maria']
edades = [21, 32, 27, 44] # zip toma la longitud de la lista mas corta
ciudades = ['Buenos Aires','CDMX', 'Lima']

combinados = list(zip(nombre, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

