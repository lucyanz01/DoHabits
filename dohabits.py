# Lógica principal de mi app

class Usuario:
    def __init__(self, username):
        self.nombre = username
        self.objetivos = []

    # Funciones del usuario

    def crear_objetivo(self, titulo_objetivo):
        if any(o.titulo == titulo_objetivo for o in self.objetivos):
            print(f"El objetivo {titulo_objetivo} ya existe. Ingresa un nuevo objetivo.")
            return
        nuevo_objetivo = Objetivo(titulo_objetivo)
        self.objetivos.append(nuevo_objetivo)

    def eliminar_objetivo(self, titulo_objetivo):
        self.objetivos = [o for o in self.objetivos if o.titulo != titulo_objetivo]
        

class Objetivo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.tareas = []

    def agregar_tarea(self, descripcion_tarea):
        if any(t.descripcion == descripcion_tarea for t in self.tareas):
            print(f"La tarea {descripcion_tarea} ya existe. Ingresa una nueva tarea.")
            return
        nueva_tarea = Tarea(descripcion_tarea)
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, descripcion_tarea):
        tareas_cantidad = len(self.tareas)
        self.tareas = [t for t in self.tareas if t.descripcion != descripcion_tarea]
        if len(self.tareas) == tareas_cantidad:
            print(f"No se encontró la tarea '{descripcion_tarea}'")

    def progreso(self):
        if not self.tareas:
            return 0
        tareas_completadas = sum(tarea.completada for tarea in self.tareas)
        return round(tareas_completadas / len(self.tareas) * 100, 2)
    
    def __str__(self):
        return f"{self.titulo} - {self.progreso()}% completado"

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def desmarcar_completada(self):
        self.completada = False

    def __str__(self):
        estado = "✔" if self.completada else "✘"
        return f"{self.descripcion} [{estado}]"
    
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