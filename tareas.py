tareas = {}

def agregar_tarea(id_tarea, nombre, descripcion, prioridad):
    if id_tarea in tareas:
        raise ValueError(f"La tarea con ID '{id_tarea}' ya existe.")
    tareas[id_tarea] = {'nombre': nombre, 'descripcion': descripcion, 'prioridad': prioridad, 'completada': False}

def actualizar_tarea(id_tarea, nuevo_nombre, nueva_descripcion, nueva_prioridad):
    if id_tarea not in tareas:
        raise KeyError(f"La tarea con ID '{id_tarea}' no existe.")
    tareas[id_tarea]['nombre'] = nuevo_nombre
    tareas[id_tarea]['descripcion'] = nueva_descripcion
    tareas[id_tarea]['prioridad'] = nueva_prioridad

def marcar_completada(id_tarea):
    if id_tarea not in tareas:
        raise KeyError(f"La tarea con ID '{id_tarea}' no existe.")
    tareas[id_tarea]['completada'] = True

def eliminar_tarea(id_tarea):
    if id_tarea not in tareas:
        raise KeyError(f"La tarea con ID '{id_tarea}' no existe.")
    del tareas[id_tarea]

def listar_tareas(completadas=False):
    return [tarea for tarea in tareas.values() if tarea['completada'] == completadas]