archivo = open("archivos/originalMJ.txt","r")
archivo2 = open("archivocopia.txt","w+")
Linea=archivo.readlines()
archivo2.write(str(Linea))
archivo2.readlines()
archivo2.seek(0,0)
print("el contenido de la copia es:"+ str (archivo2.readlines()))
