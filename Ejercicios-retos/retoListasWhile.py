a=[1,2,3,4,5]
b=[2,4,6,8,10]
c=[]
i=0
print("lista 1:", a)
print("lista 2:", b)
z=int(input("\ndesea sumar ambas listas?\n 1.si 2.no\n"))
if z==1:
    while i<len(a):
        x=[a[i]+b[i]]
        c.append(x)
        i+=1
    print("La suma de ambas listas es: ", c)
elif z==2:
    print("Entendido, programa cerrado.")
else:
    print("por favor, ingresa una opcion correcta")