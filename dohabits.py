# Lógica principal de mi app

class Usuario:
    def __init__(self, nombre, ):
        self.nombre = nombre
        self.objetivos = []

    # Funciones del usuario

    def crear_objetivo(self, nombre_objetivo):
        nuevo_obj = Objetivo(nombre_objetivo)
        self.objetivos.append(nuevo_obj)

    def eliminar_objetivo(self, nombre_objetivo):
        self.objetivos = [o for o in self.objetivos if o.nombre != nombre_objetivo]

