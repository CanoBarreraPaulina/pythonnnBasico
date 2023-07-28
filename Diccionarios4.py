Divisas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("¿Que divisa quiere buscar?: ")
if divisa.title() in Divisas:
    print(Divisas[divisa.title()])
else:
    print("La divisa no está en el diccionario.")