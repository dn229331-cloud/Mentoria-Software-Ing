class tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
    def mostrar_info(self):
        return f"tarea: {self.descripcion} | prioridad: {self.prioridad}"
lista_tareas = []
tarea1 = tarea("Estudiar POO", "Alta")
tarea2 = tarea("Configurar git", "Media")

lista_tareas.append(tarea1)
lista_tareas.append(tarea2)

print("Lista de tareas:")
for t in lista_tareas:
    print(t.mostrar_info())
    