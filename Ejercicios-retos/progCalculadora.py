import math 
print("Bienvenido a la calculadora")
z=int(input("Por favor ingresa la operacion que deseas hacer:\n 1.Sumar \n 2.Restar\n 3.Multiplicacion \n 4.division\n 5.Potencia \n 6.Raiz\n"))
if z==1:
    lista=[]
    y=int(input("¿cuantos numeros deseas sumar?: "))
    for x in range(y):
        valor=float(input("Ingrese el numero que quiera sumar:"))
        lista.append(valor)
    mas=sum(lista)
    print("La suma de los numeros es:", mas)
elif z==2:
    y=float(input("ingrese un numero: "))
    x=float(input("¿Cuanto desea restarle?: "))
    resta= y-x
    print("El resultado de su resta es:", resta)
elif z==3:
    y=int(input("¿cuantos numeros deseas multiplicar?: "))
    lista=[]
    for x in range(y):
        valor=float(input("Ingrese el numero que quiera multiplicar:"))
        lista.append(valor)
    mult =math.prod(lista)
    print("La multiplicacion de esos numeros es:", mult)
elif z==4:
    y=float(input("ingrese un numero: "))
    x=float(input("¿entre cuanto desea dividirlo?: "))
    div= y/x
    print("El resultado de su division es: ", div)
elif z==5:
    y=float(input("¿Que numero desea elevar?: "))
    x=float(input("¿A que numero desea elevarlo?: "))
    pot=y**x
    print(f"El numero ", [y], "elevado a la ",[x], " es: ",pot)
elif z==6:
    y=int(input("ingrese un numero: "))
    x=int(input("¿Que raiz desea sacarle al numero? \n 1. Raiz Cuadrada 2. Raiz cubica\n"))
    if x==1:
        cuad= math.sqrt(y)
        print(f"La raiz cuadrada del numero",[y], "es:", cuad)
    elif x==2:
        cub= math.cbrt(y)
        print(f"La raiz cubica del numero",[y], "es:", cub)
    else:
        print("Este programa solo saca raiz cuadrada y cubica, por favor ingresa una opcion valida")
else:
    print("Por favor, ingresa una opcion valida")