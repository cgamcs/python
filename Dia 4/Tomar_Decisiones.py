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