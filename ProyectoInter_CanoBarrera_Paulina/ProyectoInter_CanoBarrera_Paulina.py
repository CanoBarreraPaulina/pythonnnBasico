class Comunidad:
    def __init__(self, nombre, cuenta, contra):
        self.nombre = nombre
        self.cuenta = cuenta
        self.contra = contra
    def guardar(self):
        return ("El usuario a sido guardado")

class administrativo(Comunidad):
    def __init__(self, nombre, cuenta, contra, experiencia):
        super().__init__(nombre, cuenta, contra)
        self.experiencia = experiencia
    def __str__(self):
        return(f"{super().guardar()} \nCargo: Administrativo. \nNombre: {self.nombre}. \nCuenta: {self.cuenta}. \nContraseña: {self.contra}. \nExperiencia laboral: {self.experiencia}")

class estudiante(Comunidad):
    def __init__(self, nombre, cuenta, contra, creditos, promedio):
        super().__init__(nombre, cuenta, contra)
        self.creditos = creditos
        self.promedio = promedio
    def __str__(self):
        return(f"{super().guardar()} \nCargo: Estudiante. \nNombre: {self.nombre}. \nCuenta: {self.cuenta}. \nContraseña: {self.contra}. \nCantidad de creditos: {self.creditos}. \nPromedio general: {self.promedio}")

class Profesor(Comunidad):
    def __init__(self, nombre, cuenta, contra, grupos, experiencia):
        super().__init__(nombre, cuenta, contra)
        self.grupos = grupos
        self.experiencia = experiencia
    def __str__(self):
        return(f"{super().guardar()} \nCargo: Profesor. \nNombre: {self.nombre}. \nCuenta: {self.cuenta}. \nContraseña: {self.contra}. \nNumero de Grupos: {self.grupos}. \nExperiencia laboral: {self.experiencia}")

