archivo = open("archivos/archivo.txt","w+")

archivo.write(input("escribe lo que quieras agregar al archivo:")+"\n")

archivo.seek(0,0)
print(archivo.readline())
archivo.close()
print("¿el archivo fue cerrado?"+ str(archivo.closed))
