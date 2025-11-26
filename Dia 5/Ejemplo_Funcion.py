precios_cafe = [('Capuccino', 1.5), ('Expresso', 1.7), ('Moka', 1.2)]

def cafe_mas_caro(lista_precios):
    cafe_nombre = ''
    precio_caro = 0

    for cafe, precio in lista_precios:
        if precio > precio_caro:
            precio_caro = precio
            cafe_nombre = cafe
        else:
            pass

    return (cafe_nombre, precio_caro)

cafe, precio = cafe_mas_caro(precios_cafe)

print(f'El cafe más caro es {cafe} cuyo precio es ${precio}')
