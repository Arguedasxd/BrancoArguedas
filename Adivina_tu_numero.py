from random import *

class Juego:
    def __init__(self, niveles):
        self.niveles = niveles
        self.min_valor = 0
        self.max_valor = 0
    
    def max_min_segunNivel(self):
        if self.niveles == 1:
            self.min_valor == 0
            self.max_valor == 9
        elif self.niveles == 2:
            self.min_valor == 10
            self.max_valor == 99
        else:
            self.min_valor = 100
            self.max_valor = 999

    def generar_numero_aleatorio(self):
        self.numero_aleatorio = randint(self.min_valor,self.max_valor)
        print("Número secreto creado.")
        return self.numero_aleatorio

    def proceso(self):
        op = True
        intento=0
        while(op):
            intento += 1
            prueba = int(input("Digite un valor: "))
            if prueba == self.numero_aleatorio:
                op = False
                break
            elif prueba < self.numero_aleatorio:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
            
        print(f"****FELICITACIONES, HALLASTE EL NÚMERO SECRETO AL INTENTO {intento}")
    
def menu():
    print("Bienvenido al juego ADIVINA EL NÚMERO")
    print("Según las siguientes opciones: ")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    Opc = int(input("¿Qué nivel desea jugar?\n"))
    return Opc

probando = Juego(menu())
probando.max_min_segunNivel()
probando.generar_numero_aleatorio()
probando.proceso()
