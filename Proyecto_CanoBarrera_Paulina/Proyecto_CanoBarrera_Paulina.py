def  main():
    archivo=open("Proyecto_CanoBarrera_Paulina/Gastos.txt", "a+")
    archivo1=open("Proyecto_CanoBarrera_Paulina/Ingresos.txt", "a+")
    if i==1:
        archivo2=open("Proyecto_CanoBarrera_Paulina/GastosDes.txt", "a")
        Gasto=input("Ingrese la cantidad del gasto:\n")
        archivo.write(Gasto)
        archivo.write(",")
        archivo.close()
        Des=input("Por favor ingrese una descripcion del gasto:\n")
        archivo2.write(Des)
        archivo2.write(",")
        archivo2.close()
        print("Gasto Guardado")
        return main
    elif i==2:
        archivo2=open("Proyecto_CanoBarrera_Paulina/IngresosDes.txt", "a")
        ingreso=input("Ingrese la cantidad del Ingreso:\n")
        archivo1.write(ingreso)
        archivo1.write(",")
        archivo1.close()
        Des=input("Por favor ingrese una descripcion del ingreso:\n")
        archivo2.write(Des)
        archivo2.write(",")
        archivo2.close()
        print("Ingreso Guardado")
        return main
    elif i==3:
        datos1=[]
        datos2=[]
        archivo=open("Proyecto_CanoBarrera_Paulina/Gastos.txt", "r")
        archivo1=open("Proyecto_CanoBarrera_Paulina/Ingresos.txt", "r")
        leer=archivo.readlines()
        archivo.close()
        for lista in leer:
            datos1.append(lista.split(','))
            print(datos1)

        leeer=archivo1.readlines()
        archivo1.close()
        for lista in leeer:
            datos2.append(lista.split(','))
            print(datos2)
           
i=int(input('''BIENVENIDO A TU CALCULADORA DE GASTOS
por favor, ingresa la opcion que desees ejecutar:
1.Registrar Gasto         2.Registrar Ingreso
3.Consulta de Saldo       4.Historial de Transacciones\n'''))
main()    