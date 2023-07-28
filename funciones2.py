diccionario={}
def rellenarDic(*llave):
    for i in llave:
        entrada=input(f"Ingresa la llave de {i}\n")
        diccionario[i]=entrada
rellenarDic("Dia", "Mes","Año")
print(diccionario)