nombre = input('¿Cuál es tu nombre? ')
ventas = input('¿Cuánto vendiste? ')

ventas = float(ventas)

comision = ventas * 0.13

print(f'{nombre} tu comision es de {comision} segun tus ventas de {ventas}')