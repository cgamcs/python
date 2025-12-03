import re

texto = 'Si necesitas ayuda llama al 685-598-9977 las 24 horas al servicio de ayuda online'

palabra = 'ayuda' in texto
print(palabra)

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda.start())
print(busqueda.end())
busqueda = re.findall(patron, texto)
print(busqueda)

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
busqueda = re.search(patron, texto)
print(busqueda.group())

patron = re.compile(r'\d{3}-\d{3}-\d{4}')
busqueda = re.search(patron, texto)
print(busqueda.group())

clave = input('Clave: ')
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)
print(chequear.group())

texto = "No atendemos los lunes por la tarde"

buscar = re.search(r'lunes|martes', texto)
print(buscar.group())

buscar = re.search(r'....demos', texto)
print(buscar.group())

buscar = re.search(r'^\D', texto) # revisa que no haya un no digito al inicio del texto
print(buscar.group())

buscar = re.search(r'\D$', texto) # revisa que no haya un no digitio al final del texto
print(buscar.group())

buscar = re.findall(r'[^\s]+', texto) # en este caso lo que esta dentro de los corchetes se excluye
print(buscar)