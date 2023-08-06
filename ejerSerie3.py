import pandas as pd

num=int(input("¿Cuantos estudiantes son?:"))
diccionario = {}
for i in range(0, num):
    clave = input(f"Ingrese el nombre del estudiante {i+1}: ")
    valor = float(input(f"Ingrese la calificacion del estudiante {i+1}: "))
    diccionario[clave] = valor
print(diccionario)

serieD = pd.Series(diccionario)
print("La nota minima es: ",serieD.min())
print("La nota maxima es: ", serieD.max())
print("La media es: ", serieD.mean())
print("La desviacion tipica es: ", serieD.std())