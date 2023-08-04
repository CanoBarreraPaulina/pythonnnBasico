import numpy as np

arreglo = np.random.randint(0, 100, 10)
arreglo1 = arreglo.copy()
arreglo1[arreglo1 % 2 != 0] = -1
print("Arreglo original:", arreglo)
print("Arreglo con impares reemplazados con -1:", arreglo1)