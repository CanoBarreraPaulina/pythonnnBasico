class vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def arrancar(self):
        return ("El vehiculo arrancó: ")

class coche(vehiculo):
    def __init__(self,color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad=velocidad
    def __str__(self):
        return(f"{super().arrancar()}Es un coche de color {self.color}, tiene {self.ruedas} ruedas y alcanza los {self.velocidad} km/h") 

class Bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo
    def __str__(self):
        return(f"{super().arrancar()}Es una bicicleta de color {self.color}, tiene {self.ruedas} ruedas y es {self.tipo}") 
