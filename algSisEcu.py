import numpy as np

 def solve_3x3_system(A, B):
     try:
         A_inv = np.linalg.inv(A)
         X = np.dot(A_inv, B)

        return X
    except np.linalg.LinAlgError:
        raise Exception("La matriz A no es invertible. El sistema no tiene solución única.")
A = np.array([[2, 1, -1],
                  [3, 4, 2],
                  [1, 2, 3]])

B = np.array([1, 2, 3])

try:
    result = solve_3x3_system(A, B)
    print("Los resultados son:")
    print("x =", result[0])
    print("y =", result[1])
    print("z =", result[2])
except Exception as e:
    print("Error:", e)