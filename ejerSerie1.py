import pandas as pd

diccionario = {}
for i in range(1, 11):
    clave = input(f"Ingrese la clave {i}: ")
    valor = input(f"Ingrese el valor {i}: ")
    diccionario[clave] = valor


lista = []
for i in range(1, 11):
    dato = input(f"Ingrese el dato {i} de la lista: ")
    lista.append(dato)

serie_diccionario = pd.Series(diccionario)
serie_lista = pd.Series(lista)

print("Serie a partir del diccionario:")
print(serie_diccionario)

print("\nSerie a partir de la lista:")
print(serie_lista)

print("\nTipo de dato de la serie del diccionario:", type(serie_diccionario))
print("Tipo de dato de la lista:", type(serie_lista))