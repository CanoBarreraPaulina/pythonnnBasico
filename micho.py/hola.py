archivo=open("micho.py/Numeros", "a+")
archivo1=open("micho.py/Datos", "a+")

saldo=0
def registrar_gasto():
    monto = input("Ingrese el monto del gasto: ")
    motivo = input("Ingrese el motivo del gasto: ")
    if monto.isdigit() and motivo.isalpha():
        archivo.write("Gasto:"+monto)
        archivo.write(" ")
        #archivo.close()               
        archivo1.write(" "+motivo)
        #archivo1.close()
        saldo= saldo-monto
        print(saldo)
        return saldo
        print("Gasto registrado")
        
    else:
        print("\nIngrese datos correctos.")

def registrar_ingreso():
    monto = input("Ingrese el monto del Ingreso: ")
    motivo = input("Ingrese el motivo del ingreso: ")
    if monto.isdigit() and motivo.isalpha():
        archivo.write("Ingreso:"+monto)
        archivo.write(" ")
        #archivo.close()               
        archivo1.write(" "+motivo)
        #archivo1.close()
        print("Ingreso registrado")
        global saldo
        saldo= saldo+monto
        print(saldo)

def consultar_saldo():
    global saldo
    print("Su saldo actual es:", saldo)

def ver_historial():
    archivo=open("micho.py/Numeros", "r")
    archivo1=open("micho.py/Datos", "r")
    salida = []
    salida2 = []
    a = (linea.split() for linea in archivo)
    b = (linea.split() for linea in archivo1)
    for i, j in zip(a, b):
        print(i, j)
def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Registrar un gasto")
    print("2. Registrar un ingreso")
    print("3. Consultar el saldo actual")
    print("4. Ver el historial de transacciones")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            registrar_gasto()
        elif opcion == '2':
            registrar_ingreso()
        elif opcion == '3':
            consultar_saldo()
        elif opcion == '4':
            ver_historial()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
archivo=open("micho.py/Numeros", "a+")
archivo1=open("micho.py/Datos", "a+")

Gastos=[]
Ingresos=[]
def registrar_gasto():
    global Gastos 
    monto = input("Ingrese el monto del gasto: ")
    motivo = input("Ingrese el motivo del gasto: ")
    if monto.isdigit() and motivo.isalpha():
        archivo.write("Gasto:"+monto)
        archivo.write(" ")
        #archivo.close()               
        archivo1.write(" "+motivo)
        #archivo1.close()
        print("Gasto registrado")
        Gastos.append(monto)
    else:
        print("\nIngrese datos correctos.")

def registrar_ingreso():
    Ingresos=[]
    monto = input("Ingrese el monto del Ingreso: ")
    motivo = input("Ingrese el motivo del ingreso: ")
    if monto.isdigit() and motivo.isalpha():
        archivo.write("Ingreso:"+monto)
        archivo.write(" ")
        #archivo.close()               
        archivo1.write(" "+motivo)
        #archivo1.close()
        print("Ingreso registrado")
        Ingresos.append(monto)
        print(Ingresos)

def consultar_saldo():
    global saldo
    print("Su saldo actual es:", saldo)

def ver_historial():
    archivo=open("micho.py/Numeros", "r")
    archivo1=open("micho.py/Datos", "r")
    salida = []
    salida2 = []
    a = (linea.split() for linea in archivo)
    b = (linea.split() for linea in archivo1)
    for i, j in zip(a, b):
        print(i, j)
def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Registrar un gasto")
    print("2. Registrar un ingreso")
    print("3. Consultar el saldo actual")
    print("4. Ver el historial de transacciones")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            registrar_gasto()
        elif opcion == '2':
            registrar_ingreso()
        elif opcion == '3':
            consultar_saldo()
        elif opcion == '4':
            ver_historial()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()




def salir():
    guardar_transacciones()
    print("BAI BAI")

if __name__ == "__main__":
    cargar_transacciones()
    main()