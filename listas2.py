par=[]
imp=[]
numero=int(input("ingrese hasta que numero quiere acomodar:"))
if numero>=1:
    for n in range (1, numero, +1):
        if n % 2==0:
            par.append(n)
        else:
            imp.append(n)
    print("los numeros pares son:", par)
    print("los numeros impares son:",imp)
else:
    print("numero invalido, vuelve a intentarlo")