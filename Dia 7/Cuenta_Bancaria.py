from random import randrange

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido} \nBalance de cuenta {self.numero_cuenta}: ${self.balance}'

    def imprimir(self):
        print(f'Su balance actual es ${self.balance}')

    def depositar(self, valor):
        self.balance += valor

    def retirar(self, valor):
        if valor > self.balance:
            print('Fondos insuficientes')
        else:
            self.balance -= valor

def crear_cliente():
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    cuenta = randrange(10000, 99999)

    return Cliente(nombre, apellido, cuenta)

def inicio():
    cliente = crear_cliente()

    while True:
        print("\n[1] - Mi información")
        print("[2] - Depositar")
        print("[3] - Retirar")
        print("[4] - Salir")

        opcion = int(input('\n¿Qué desea hacer?: '))

        match opcion:
            case 1:
                print(cliente)

            case 2:
                cantidad = int(input('\nIngrese la cantidad que desea depositar: '))
                cliente.depositar(cantidad)
                cliente.imprimir()

            case 3:
                cantidad = int(input('\nIngrese la cantidad que desea retirar: '))
                cliente.retirar(cantidad)
                cliente.imprimir()

            case 4:
                print('\nSaliendo')
                return

inicio()