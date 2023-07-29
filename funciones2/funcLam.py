suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a, b: a / b

def operaciones():
    a=num1
    b=num2
    resultado_suma = suma(num1, num2)
    resultado_resta = resta(num1, num2)
    resultado_multiplicacion = multiplicacion(num1, num2)
    resultado_division = division(num1, num2)

    print("Resultado suma: ", resultado_suma)
    print("Resultado resta: ", resultado_resta)
    print("Resultado multiplicación: ", resultado_multiplicacion)
    print("Resultado división: ", resultado_division)
num1=float(input("Por favor, ingresa un numero:"))
num2=float(input("Por favor, ingresa otro numero:"))
operaciones()