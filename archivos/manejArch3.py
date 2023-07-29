archivo=open("archivos/ejercicio3.txt","a")

def text():
    if i==1:
        texto=input("por favor ingrese el texto que desea agregar:\n")
        archivo.write(texto)
        archivo.close()
    elif i==2:
        archiv=open("archivos/ejercicio3.txt", "r")
        ver=archiv.read()
        print("el texto guardado es:\n", ver)
        archiv.close()
        
i=int(input("ingrese la opcion deseada\n 1.agregar texto 2.Ver texto guardado\n"))
text()
