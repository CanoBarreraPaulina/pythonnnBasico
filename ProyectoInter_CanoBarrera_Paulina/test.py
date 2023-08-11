from .ProyectoInter_CanoBarrera_Paulina import *

def main():
    x=int(input("¿Qué accion desea realizar? \n1.Agregar Usuario \n2.Consultar Datos \n3.Editar Usuario\n"))
    if x==1:
        z= int(input("¿que tipo de usuario desea agregar? \n1.Administrativo \n2.Estuiante \n3.Profesor\n"))
        if z==1:
            a=input("Nombre completo y sin espacios: ")
            b=int(input("Numero de cuenta (solo numeros, sin espacios): "))
            c=input("Contraseña(sin espacios): ")
            d=float(input("Experiencia laboral(años): "))
            ad=administrativo(a,b,c,d)
            print(ad)
        elif z==2:
            a=input("Nombre completo y sin espacios: ")
            b=int(input("Numero de cuenta (solo numeros, sin espacios): "))
            c=input("Contraseña(sin espacios): ")
            d=int(input("Cantidad de creditos: "))
            e=float(input("Promedio general: "))
            est=estudiante(a,b,c,d,e)
            print(est)
        elif z==3:
            a=input("Nombre completo y sin espacios: ")
            b=int(input("Numero de cuenta (solo numeros, sin espacios): "))
            c=input("Contraseña(sin espacios): ")
            d=int(input("Numero de grupos:"))
            e=float(input("Experiencia laboral(años): "))
            prof=Profesor(a,b,c,d,e)
            print(prof)
        else:
            print("Por favor ingresa una opcion correcta")
    elif x==2:
        z= int(input("¿que tipo de usuario desea consultar? \n1.Administrativo \n2.Estuiante \n3.Profesor\n"))
    else:
        print("por favor ingresa una opcion correcta")
main()