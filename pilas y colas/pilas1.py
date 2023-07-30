lista = []
def main():
    print("[1] agregar elemento")
    print("[2] eliminar elemento")
    print("[3]] imprimir pila")
    print("[1] Salir")
    option = input("Elija una opcion: ")
    if str(option)=="1":
            n = input("Introduzca el numero que desea agregar:")
            lista.append(n)
            print(" Elemento agregado ")
            main()
    elif str(option)=="2":
            if len(lista) == 0:
                print(" No hay elementos para eliminar ")
                main()
            else:
               print("El numero: ",lista.pop()," fue eliminado")
               main()     
    elif str(option)=="3":
            for i in reversed(range(len(lista))):
               print("Pila: ",lista[i])
            main()
    elif str(option)=="4":
            exit()
    else:
            print("\nOpcion incorrecta.\n")
            main()
main()
