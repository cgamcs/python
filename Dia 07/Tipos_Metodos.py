class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahorra el pajaro es {self.color}')

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False # con cls podemos entrar a las intancias de la clase
        print(Pajaro.alas)

    '''
    El staticmethod no puede acceder
    a las intancias de la clase
    ni tampoco puede cambiar los atributos
    de la clase
    '''
    @staticmethod
    def mirar():
        print("El pajaro mira")

# piolin = Pajaro("amarillo", "canario")

# piolin.pintar_negro()

# piolin.volar(50)

# piolin.alas = False

# print(piolin.alas)

# Pajaro.poner_huevos(5) # funciona por que es un metodo de clase

Pajaro.mirar()