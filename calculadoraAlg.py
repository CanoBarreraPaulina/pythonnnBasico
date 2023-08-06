import numpy as np

def producto_escalar(vector1, vector2):
    return np.dot(vector1, vector2)

def modulo_vector(vector):
    return np.linalg.norm(vector)

def producto_matrices(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

def inversa_matriz(matriz):
    try:
        return np.linalg.inv(matriz)
    except np.linalg.LinAlgError:
        raise Exception("La matriz no es invertible.")

def trazo_matriz(matriz):
    return np.trace(matriz)

def determinante_matriz(matriz):
    return np.linalg.det(matriz)

def mostrar_menu():
    print("=== CALCULADORA ===")
    print("1. Producto escalar de 2 vectores")
    print("2. Módulo de un vector")
    print("3. Producto de dos matrices")
    print("4. Inversa de una matriz")
    print("5. Trazo de una matriz")
    print("6. Determinante de una matriz cuadrada")
    print("7. Salir")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-7): ")

    if opcion == "1":
        v1 = np.array(input("Ingrese el primer vector separado por espacios: ").split(), dtype=float)
        v2 = np.array(input("Ingrese el segundo vector separado por espacios: ").split(), dtype=float)
        resultado = producto_escalar(v1, v2)
        print("El producto escalar de los vectores es:", resultado)

    elif opcion == "2":
        v = np.array(input("Ingrese el vector separado por espacios: ").split(), dtype=float)
        resultado = modulo_vector(v)
        print("El módulo del vector es:", resultado)

    elif opcion == "3":
        m1 = np.array(eval(input("Ingrese la primera matriz como lista de listas: ")))
        m2 = np.array(eval(input("Ingrese la segunda matriz como lista de listas: ")))
        resultado = producto_matrices(m1, m2)
        print("El producto de las matrices es:")
        print(resultado)

    elif opcion == "4":
        m = np.array(eval(input("Ingrese la matriz como lista de listas: ")))
        try:
            resultado = inversa_matriz(m)
            print("La matriz inversa es:")
            print(resultado)
        except Exception as e:
            print("Error:", e)
    elif opcion == "5":
        m = np.array(eval(input("Ingrese la matriz como lista de listas: ")))
        resultado = trazo_matriz(m)
        print("El trazo de la matriz es:", resultado)

    elif opcion == "6":
        m = np.array(eval(input("Ingrese la matriz cuadrada como lista de listas: ")))
        resultado = determinante_matriz(m)
        print("El determinante de la matriz es:", resultado)

    elif opcion == "7":
        print("Programa cerrado")
        break

    else:
        print("opción no válida. Intenta de nuevo")