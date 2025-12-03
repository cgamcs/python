from datetime import datetime, date, time

'''
mi_hora = datetime.time(15, 40, 21)
print(mi_hora)

mi_dia = datetime.date(2025, 12, 2)
print(mi_dia)
'''

mi_fecha = datetime(2025, 12, 2, 15, 44, 22)
print(mi_fecha)

mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento
print(vida)

hoy = date.today()

print(hoy)

hoy = datetime.now().minute

print(hoy)