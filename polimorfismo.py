class figura:
    def area(self):
       pass
    def __str__(self):
        pass
class rectangulo(figura):
    def __init__(self,alto,ancho):
        self.alto=alto
        self.ancho=ancho
    def area(self):
        return f"el area de su rectangulo es: {self.alto*self.ancho}"
class cuadrado(figura):
    def __init__(self,lado):
        self.lado=lado
    def area(self):
        return f"el area de su cuadrado es: {self.lado*self.lado}"
class triangulo(figura):
    def __init__(self,alto,base):
        self.alto=alto
        self.base=base
    def area(self):
        return f"el area de su triangulo es: {(self.alto*self.base)/2}"

rectangulo1=rectangulo(12,6)
cuadrado1=cuadrado(15)
triangulo1=triangulo(11,5)
lista=[cuadrado1,rectangulo1,triangulo1]
for figura in lista:
    print(f"{figura.area()}")