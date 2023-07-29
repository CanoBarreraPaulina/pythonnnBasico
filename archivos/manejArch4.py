def leer_archivo():
    if i=="ejercicio4.txt":
        archivo=open("archivos/ejercicio4.txt","r")
        leer=archivo.read()
        archivo.close()
        x=int(input("¿desea ver el contenido guardado?\n 1.si 2.no\n"))
        if x==1:
            print("El contenido guardado es: ", leer)
        if x==2:
            print("contenido guardado, archivo cerrado")
    else: 
        print("por favor, ingresa un nombre valido.")
i=input("ingresa el nombre del archivo a leer (ejercicio4.txt): ")
leer_archivo()