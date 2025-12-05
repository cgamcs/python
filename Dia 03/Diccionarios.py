diccionario = {
    "nombre": "César",
    "edad": 21,
    "peso": 62
}
consulta = diccionario['nombre']
print(consulta)

dic = {
    'c1': 55,
    'c2': [10, 20, 30],
    'c3': {
        's1': 100,
        's2': 200
    }
}

print(dic['c2'][2])
print(dic['c3']['s2'])

dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper())

dic = {1: 'a', 2: 'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())