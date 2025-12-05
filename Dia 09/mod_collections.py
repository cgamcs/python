from collections import Counter, defaultdict, namedtuple, deque

numeros = [8,4,5,5,5,6,6,6,8,8,8,4,4,2,2,2,1,1,1,]
frase = 'al pan pan y al vino vino'
palabra = 'mississipi'

print(Counter(numeros))
print(Counter(frase.split()))
print(Counter(palabra))

serie = Counter(numeros)
print(serie.most_common())


'''
mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_dic['cuatro'])

En este caso obtendriamos un error, para evitar que marque un error
podemos usar defaultdict
'''

mi_dic = defaultdict(lambda: 'No hay datos')
mi_dic['uno'] = 'verde'
mi_dic['dos'] = 'azul'
mi_dic['tres'] = 'rojo'
print(mi_dic['cuatro'])


'''
Con namedtuple podemos agregar nombre a los valores
de una tupla evitando la necesidad de saber el indice
en el que se encuentra cierto valor
'''
mi_tupla = (500, 18, 65)
print(mi_tupla[1])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.80, 79)

print(ariel.nombre)