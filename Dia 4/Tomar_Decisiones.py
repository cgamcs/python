if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')

mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('No se que animal tienes')


edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('Reprobado')
else:
    print('Eres adulto')

serie = 'N-02'

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Google')
    case 'N-03':
        print('Vivo')
    case _:
        print('No existe ese producto')

cliente = {
    'nombre': 'Federico',
    'edad': 43,
    'ocupacion': 'instructor'
}

pelicula = {
    'titulo': 'Matrix',
    'ficha_tecnica': {
        'protagonista': 'Keanu Reeves',
        'director': 'Lana y Lilly Wachowski'
    }
}

elementos = [cliente, pelicula, 'libro']

print('\n')
for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
            print('Es un pelicula')
            print(titulo, protagonista, director)
        case _:
            print('No se que es esto')