texto = input('Ingresa un texto a analizar: ')
print('Ingresa 3 letras de tu agrado')
primer_letra = input('Ingresa la primer letra: ')
segunda_letra = input('Ingresa la segunda letra: ')
tercer_letra = input('Ingresa la tercer letra: ')

texto_procesado = texto.lower()
primer_letra.lower()
segunda_letra.lower()
tercer_letra.lower()

total_primer_letra = texto_procesado.count(primer_letra)
total_segunda_letra = texto_procesado.count(segunda_letra)
total_tercer_letra = texto_procesado.count(tercer_letra)

print(f'\nLa letra "{primer_letra}" se repite {total_primer_letra} veces')
print(f'La letra "{segunda_letra}" se repite {total_segunda_letra} veces')
print(f'La letra "{tercer_letra}" se repite {total_tercer_letra} veces')

texto_a_lista = texto.split()
longitud_de_texto = len(texto_a_lista)

print(f'\nEn el texto hay un total de {longitud_de_texto} palabras')

print(f'\nLa primer letra del texto es {texto[0]} y la ultima letra del texto es {texto[-1]}')

texto_a_lista.reverse()
texto_inverso = " ".join(texto_a_lista)
print(f'\nEste es el texto en orden inverso:\n{texto_inverso}\n')

resultado = 'Python' in texto

dic = {True: 'La palabra Python si aparece en el texto', False: 'La palabra Python no aparece en el texto'}
print(dic[resultado])