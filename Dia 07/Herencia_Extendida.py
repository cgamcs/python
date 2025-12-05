class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, cantidad_metros):
        print(f"El pajaro vuela {cantidad_metros} metros")

# piolin = Pajaro(2, 'rojo', 30)

# piolin.hablar()

# piolin.volar(100)

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("JA JA")

    def hablar(self):
        print("Que tal?")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar() # Hereda la funcion hablar de padre
                  # porque fue el primero en definirse
                  # en la clase Hijo(Padre, Madre)

mi_nieto.reir()