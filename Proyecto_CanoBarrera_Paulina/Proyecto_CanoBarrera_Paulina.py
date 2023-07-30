def  main():
    archivo=open("Proyecto_CanoBarrera_Paulina/Gastos.txt", "a+")
    archivo1=open("Proyecto_CanoBarrera_Paulina/Ingresos.txt", "a+")
    if i==1:
        archivo2=open("Proyecto_CanoBarrera_Paulina/GastosDes.txt", "a")
        Gasto=input("Ingrese la cantidad del gasto:\n")
        archivo.write(Gasto)
        archivo.write("\n")
        archivo.close()
        Des=input("Por favor ingrese una descripcion del gasto:\n")
        archivo2.write(Des)
        archivo2.write("\n")
        archivo2.close()
        print("Gasto Guardado")
        return main
    if i==2:
        archivo2=open("Proyecto_CanoBarrera_Paulina/IngresosDes.txt", "a")
        ingreso=input("Ingrese la cantidad del Ingreso:\n")
        archivo1.write(ingreso)
        archivo1.write("\n")
        archivo1.close()
        Des=input("Por favor ingrese una descripcion del ingreso:\n")
        archivo2.write(Des)
        archivo2.write("\n")
        archivo2.close()
        print("Ingreso Guardado")
        return main
    if i==3:
        
i=int(input('''BIENVENIDO A TU CALCULADORA DE GASTOS
por favor, ingresa la opcion que desees ejecutar:
1.Registrar Gasto         2.Registrar Ingreso
3.Consulta de Saldo       4.Historial de Transaccione\n'''))
main()    