# Lógica principal de mi app

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.objetivos = []

    # Funciones del usuario

    def crear_objetivo(self, nombre_objetivo):
        nuevo_obj = Objetivo(nombre_objetivo)
        self.objetivos.append(nuevo_obj)

    def eliminar_objetivo(self, nombre_objetivo):
        self.objetivos = [o for o in self.objetivos if o.nombre != nombre_objetivo]

class Objetivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def progreso(self):
        if not self.tareas:
            return 0
        tareas_completadas = sum(tarea.completadas for tarea in self.tareas)
        return round((tareas_completadas / len(self.tareas) * 100, 2))