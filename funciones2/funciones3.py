def concatenar_nombres(prefijo, nombres):
    nombres_prefijo = [f"{prefijo} {nombre}" for nombre in nombres]
    return nombres_prefijo


prefijo_usuario = input("Ingrese el prefijo (Sr., Joven o Niño): ")
nombres = ["Luis","Pepe","Ramon","juan"]
nombres_prefijo = concatenar_nombres(prefijo_usuario, nombres)

print("Nombres con prefijo:")
for nombre in nombres_prefijo:
    print(nombre)