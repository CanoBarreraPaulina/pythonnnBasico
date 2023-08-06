import numpy as np

def calcular_matrizIn(matriz):
    try:
        matrizIn = np.linalg.inv(matriz)
        return matrizIn
    except np.linalg.LinAlgError:
        return None

def main():
    print("Ingrese elementos de la matriz (3x3) separados por espacios:")


    matriz_entrada = []
    for i in range(3):
        fila = input(f"Fila {i + 1}: ").split()
        fila = [float(num) for num in fila]
        matriz_entrada.append(fila)
    matriz_c = np.array(matriz_entrada)

    if matriz_c.shape != (3, 3):
        print("La matriz no es cuadrada (3x3).")
        return

    matrizIn = calcular_matrizIn(matriz_c)
    if matrizIn is None:
        print("La matriz no tiene inversa.")
    else:
        print("La matriz inversa es:")
        print(matrizIn)

main()