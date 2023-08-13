import csv

class Comunidad:
    def __init__(self, nombre, cuenta, contra):
        self.nombre = nombre
        self.cuenta = cuenta
        self.contra = contra
    def guardar(self):
        print("Usuario Guardado.")

class Administrativo(Comunidad):
    def __init__(self, nombre, cuenta, contra, experiencia):
        super().__init__(nombre, cuenta, contra)
        self.experiencia = experiencia
    def __str__(self):
        return(f"{super().guardar()} Cargo: Administrativo. Nombre: {self.nombre}. Cuenta: {self.cuenta}. Contraseña: {self.contra}. Experiencia laboral: {self.experiencia} años\n")

class Estudiante(Comunidad):
    def __init__(self, nombre, cuenta, contra, creditos, promedio):
        super().__init__(nombre, cuenta, contra)
        self.creditos = creditos
        self.promedio = promedio
    def __str__(self):
        return(f"{super().guardar()} Cargo: Estudiante. Nombre: {self.nombre}. Cuenta: {self.cuenta}. Contraseña: {self.contra}. Cantidad de creditos: {self.creditos}. Promedio general: {self.promedio}\n")

class Profesor(Comunidad):
    def __init__(self, nombre, cuenta, contra, grupos, experiencia):
        super().__init__(nombre, cuenta, contra)
        self.grupos = grupos
        self.experiencia = experiencia
    def __str__(self):
        return(f"{super().guardar()} Cargo: Profesor. Nombre: {self.nombre}. Cuenta: {self.cuenta}. Contraseña: {self.contra}. Numero de Grupos: {self.grupos}. Experiencia laboral: {self.experiencia} años\n")

def Registrar():
    try:
        z= int(input("¿que tipo de usuario desea agregar? \n1.Administrativo \n2.Estudiante \n3.Profesor\n"))
        a=input("Nombre completo: ")
        b=int(input("Numero de cuenta (solo numeros, sin espacios): "))
        c=input("Contraseña: ")
    except Exception as e:
        print(f"Ocurrio un error {e}. Por favor verifica que los datos sean correctos")
        Registrar()

    arch=open("ProyectoInter_CanoBarrera_Paulina/datos.txt","+a")
    arch1=open("ProyectoInter_CanoBarrera_Paulina/cuentas.txt","+a")
    if z==1:
        try:
            d=float(input("Experiencia laboral(años): ")) 
        except Exception as e:
            print(f"Ocurrio un error {e}. Por favor verifica que los datos sean correctos")
            Registrar()
        usu=Administrativo(a,b,c,d)
        print(usu)
    if z==2:
        try:
            d=int(input("Cantidad de creditos: "))
            e=float(input("Promedio general: "))
        except Exception as e:
            print(f"Ocurrio un error {e}. Por favor verifica que los datos sean correctos")
            Registrar()
        usu=Estudiante(a,b,c,d,e)
        print(usu)
    if z==3:
        try:
            d=int(input("Numero de grupos: "))
            e=float(input("Experiencia laboral(años): "))
        except Exception as e:
            print(f"Ocurrio un error {e}. Por favor verifica que los datos sean correctos")
            Registrar()
        usu=Profesor(a,b,c,d,e)
        print(usu)
    arch.write(str(usu))
    arch.close()
    a = a.replace( " " , "" )
    arch1.write(a+" ")
    arch1.close()
def Consulta():
    arch=open("ProyectoInter_CanoBarrera_Paulina/datos.txt","r")
    arch1=open("ProyectoInter_CanoBarrera_Paulina/cuentas.txt","r")
    print("Estos son los Usuarios guardados en el sistema, por favor ingresa el numero de indice del usuario que desees consultar")
    line = csv.reader(arch1, delimiter=' ')
    cuentas=list(line)[0]
    for i, cuenta in enumerate(cuentas):
        print(i,cuenta)
    y=int(input())
    Dato = [linea.strip() for linea in arch]
    print(Dato[y])
def Editar():
    arch=open("ProyectoInter_CanoBarrera_Paulina/datos.txt","r+")
    arch1=open("ProyectoInter_CanoBarrera_Paulina/cuentas.txt","r")
    z=int(input("¿que tipo de usuario desea editar?\n1.Administrativo \n2.Estudiante \n3.Profesor\n"))
    print("Estos son los Usuarios guardados en el sistema, por favor ingresa el numero de indice del usuario que desees editar")
    line = csv.reader(arch1, delimiter=' ')
    cuentas=list(line)[0]
    for i, cuenta in enumerate(cuentas):
        print(i,cuenta)
    y=int(input())
    try:
        z= int(input("¿que tipo de usuario desea agregar? \n1.Administrativo \n2.Estudiante \n3.Profesor\n"))
        a=input("Nombre completo: ")
        b=int(input("Numero de cuenta (solo numeros, sin espacios): "))
        c=input("Contraseña: ")
    except Exception as e:
        print(f"Ocurrio un error {e}. Por favor verifica que los datos sean correctos")
        Editar()
    if z==1:
        try:
           d=float(input("Experiencia laboral(años): "))  
        except Exception as e:
            print(f"Ocurrio un error {e}. Por favor verifica que los datos sean correctos")
            Editar()
        usu=Administrativo(a,b,c,d)
    if z==2:
        try:
            d=int(input("Cantidad de creditos: "))
            e=float(input("Promedio general: "))
        except Exception as e:
            print(f"Ocurrio un error {e}. Por favor verifica que los datos sean correctos")
            Editar()
        usu=Estudiante(a,b,c,d,e)
    if z==3:
        try:
            d=int(input("Numero de grupos: "))
            e=float(input("Experiencia laboral(años): "))
        except Exception as e:
            print(f"Ocurrio un error {e}. Por favor verifica que los datos sean correctos")
        usu=Profesor(a,b,c,d,e)
    else:
        print ("ingrese una opcion correcta")
    cuentas[y]=a.replace( " " , "" )
    arch1.close()
    Dato = arch.readlines()
    arch=open("ProyectoInter_CanoBarrera_Paulina/datos.txt","w")
    arch1=open("ProyectoInter_CanoBarrera_Paulina/cuentas.txt","w")
    arch1.write(" ".join(cuentas))
    Dato[y]=str(usu)
    for i in Dato:
        arch.write(str(i))

x=0
while x!=4:
    def main():
        x=int(input("¿Qué accion desea realizar? \n1.Agregar Usuario \n2.Consultar Datos \n3.Editar Usuario \n4.Salir\n"))
        if x==1:
            Registrar()
        elif x==2:
            Consulta()
        elif x==3:
            Editar()
        elif x==4:
            print ("Programa cerrado")
        else:
            print("por favor ingresa una opcion correcta")
    main()