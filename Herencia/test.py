from vehiculo import *

def main():
    z= int(input("¿que quieres agregar? \n 1.Coche 2.Bicicleta\n"))
    if z==1:
        x=input("ingresa el color de tu coche: ")
        y=input("ingresa la velocidad de tu coche (km/h): ")
        coche1=coche(x,4,y)
        print(coche1)
    elif z==2:
        x=input("ingresa el color de tu bicicleta: ")
        y=input("ingresa el tipo de bici: ")
        bici1=Bicicleta(x,2,y)
        print(bici1)
    else:
        print("por favor, ingresa una opcion correcta")
main()