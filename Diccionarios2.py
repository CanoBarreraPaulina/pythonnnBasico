materias ={}

numero = int(input("¿cuantas materias deseas registrar?: "))
for i in range(numero):
    Key = input("nombre de la materia: ")
    value= input("creditos de la materia: ")
    materias[Key] = value
print(materias)