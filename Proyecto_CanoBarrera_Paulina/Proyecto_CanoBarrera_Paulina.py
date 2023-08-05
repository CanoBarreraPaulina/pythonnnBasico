import csv
continuar=True
while continuar:
    i=int(input('''\n*BIENVENIDO A TU CALCULADORA DE GASTOS*
por favor, ingresa la opcion que desees ejecutar:
1.Registrar Gasto         2.Registrar Ingreso
3.Consulta de Saldo       4.Historial de Transacciones
                   5.Salir\n'''))
    archivo=open("Proyecto_CanoBarrera_Paulina/Gastos.txt", "a+")
    archivo1=open("Proyecto_CanoBarrera_Paulina/Ingresos.txt", "a+")
    if i==1:
        archivo2=open("Proyecto_CanoBarrera_Paulina/GastosDes.txt", "a")
        Gasto=input("Ingrese la cantidad del gasto (Solo numeros):\n")
        Des=input("Por favor ingrese una descripcion del gasto: solo letras, sin espacios(ejemplogasto):\n")
        if Gasto.isdigit() and Des.isalpha():
            archivo.write(" "+ Gasto)
            archivo.close()               
            archivo2.write(" "+ Des)
            archivo2.close()
            print("Gasto Guardado")
        else:
            print("Por favor verifique que los datos ingresados sean correctos. Ingrese de nuevo")
            i==0
    elif i==2:
        archivo2=open("Proyecto_CanoBarrera_Paulina/IngresosDes.txt", "a")
        ingreso=input("Ingrese la cantidad del Ingreso:\n")
        Des=input("Por favor ingrese una descripcion del ingreso, sin espacios. (ejemplo_ingreso):\n")
        if ingreso.isdigit() and Des.isalpha():
            archivo1.write(" "+ ingreso)
            archivo1.close()               
            archivo2.write(" "+ Des)
            archivo2.close()
            print("Ingreso Guardado")
        else:
            print("Por favor verifique que los datos ingresados sean correctos. Ingrese de nuevo")
            i==0
    elif i==3:
        dat=[]
        dat2=[]
        archivo=open("Proyecto_CanoBarrera_Paulina/Gastos.txt", "r")
        archivo1=open("Proyecto_CanoBarrera_Paulina/Ingresos.txt", "r")
        line = csv.reader(archivo, delimiter=' ')
        datos1=list(line)[0]
        for espacio in datos1:
            if espacio != "":
                dat.append(espacio)
        datos1=list(map(int, dat))
        lista=sum(datos1)
        archivo.close()
        lines = csv.reader(archivo1, delimiter=' ')
        datos2=list(lines)[0]
        for espacio in datos2:
            if espacio != "":
                dat2.append(espacio)
        datos2=list(map(int, dat2))
        lista1=sum(datos2)
        archivo1.close()
        saldo=lista1-lista
        if saldo<=0:
            sald=0
        else:
            sald=saldo
        print("Tus ingresos son: ",lista1)
        print("Tus gastos son: ", lista)           
        print("tu saldo es: ", sald)
    elif i==4:
        archivo=open("Proyecto_CanoBarrera_Paulina/Gastos.txt", "r")
        archivo1=open("Proyecto_CanoBarrera_Paulina/Ingresos.txt", "r")
        archivo2=open("Proyecto_CanoBarrera_Paulina/GastosDes.txt", "r")
        archivo3=open("Proyecto_CanoBarrera_Paulina/IngresosDes.txt", "r")
        line = csv.reader(archivo, delimiter=' ')
        datos1=list(line)[0]
        lines = csv.reader(archivo2, delimiter=' ')
        datos2=list(lines)[0]
        print("historial de gastos:")
        for indice, valor_a in enumerate(datos1):
            print(f"{valor_a} {datos2[indice]}")
        linee=csv.reader(archivo1, delimiter=' ')
        datos3=list(linee)[0]
        liness = csv.reader(archivo3, delimiter=' ')
        datos4=list(liness)[0]
        print("\n")
        print("historial de Ingresos:")
        for indice, valor_x in enumerate(datos3):
            print(f"{valor_x} {datos4[indice]}")
    elif i==5:
        print("Programa cerrado")
        continuar= False
    else:
        print("Por favor, ingresa una opcion correcta")