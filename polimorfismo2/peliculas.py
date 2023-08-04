class peliculas:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
    def peli(self):
        return "La pelicula"
class terror(peliculas):
    def __init__(self, nombre, duracion, miedo):
        super().__init__(nombre, duracion)
        self.miedo=miedo
    def __str__(self):
        return(f"{super().peli()} {self.nombre}, dura {self.duracion} min y en una escala del 1-10 la pelicula da un {self.miedo} de miedo")

class accion(peliculas):
    def __init__(self, nombre, duracion, entr):
        super().__init__(nombre, duracion)
        self.entr=entr
    def __str__(self):
        return(f"{super().peli()} {self.nombre}, dura {self.duracion} min y en una escala del 1-10 la pelicula es entretenida un {self.entr}")