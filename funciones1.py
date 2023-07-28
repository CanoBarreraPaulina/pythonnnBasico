def operacion(estatura, peso):
    return peso / estatura**2
estatura = float(input("Introduzca su estatura(m):" ))
peso = float(input("Introduzca su peso (Kg):" ))
imc=operacion(estatura,peso)
print("Su IMC es:{}".format(imc))