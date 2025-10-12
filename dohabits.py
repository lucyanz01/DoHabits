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

    def agregar_tarea(self, nombre_tarea):
        nueva_tarea = Tarea(nombre_tarea)
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, nombre_tarea):
        tareas_cantidad = len(self.tareas)
        self.tareas = [t for t in self.tareas if t.nombre != nombre_tarea]
        if len(self.tareas) == tareas_cantidad:
            print(f"No se encontró la tarea '{nombre_tarea}'")

    def progreso(self):
        if not self.tareas:
            return 0
        tareas_completadas = sum(tarea.completada for tarea in self.tareas)
        return round(tareas_completadas / len(self.tareas) * 100, 2)
    
    def __str__(self):
        return f"{self.nombre} - {self.progreso()}% completado"

class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def desmarcar_completada(self):
        self.completada = False

    def __str__(self):
        estado = "✔" if self.completada else "✘"
        return f"{self.nombre} [{estado}]"
    
def main():
    usuario = Usuario("Lucy")

    usuario.crear_objetivo("Tareas de la noche")

    usuario.objetivos[0].agregar_tarea("Cocinar la cena")
    usuario.objetivos[0].agregar_tarea("Acomodar la cama")

    usuario.objetivos[0].tareas[0].marcar_completada()

    print(usuario.objetivos[0])

    for tarea in usuario.objetivos[0].tareas:
        print(tarea)

if __name__ == "__main__":
    main()