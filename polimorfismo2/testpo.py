from peliculas import *

def main():
    z= int(input("¿que pelicula quiere agregar? \n 1.terror 2.accion\n"))
    if z==1:
        x=input("ingrese el nombre de la pelicula: ")
        y=input("ingrese la duracion de su pelicula (min.): ")
        f=input("Del 1 al 10 ¿Qué tanto miedo le dio?: ")
        
        pelit=terror(x,y,f)
        print(pelit)
    elif z==2:
        x=input("ingrese el nombre de la pelicula: ")
        y=input("ingrese la duracion de su pelicula (min.): ")
        f=input("Del 1 al 10 ¿Qué tan entretenida fue?: ")
        pelia=accion(x,y,f)
        print(pelia)
    else:
        print("por favor, ingresa una opcion correcta")
main()