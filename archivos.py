#archivo = open("archivo.txt","x")
archivo=open("archivo.txt", "r+")

archivo.write(input("escribe lo que quieras agregar al archivo:")+"\n")

archivo.seek(0,0)
print(archivo.readline())