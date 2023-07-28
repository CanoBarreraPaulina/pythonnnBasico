archivo = open("archivo.txt","w+")
archivo.write(input("escribe lo que quieras agregar al archivo:"))

archivo.seek(0,0)
print("el contenido del archivo es: ", archivo.readline())