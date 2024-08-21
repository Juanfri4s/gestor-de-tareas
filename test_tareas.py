import pytest
from tareas import agregar_tarea, actualizar_tarea, marcar_completada, eliminar_tarea, listar_tareas, tareas

def setup_function():
    # Limpiar las tareas antes de cada prueba
    tareas.clear()

def test_agregar_tarea():
    agregar_tarea(1, "Compras", "Comprar leche y pan", "Alta")
    assert tareas[1] == {'nombre': "Compras", 'descripcion': "Comprar leche y pan", 'prioridad': "Alta", 'completada': False}
   
    with pytest.raises(ValueError):
        agregar_tarea(1, "Compras duplicadas", "Comprar algo más", "Baja")  # Tarea con ID duplicado

def test_actualizar_tarea():
    agregar_tarea(1, "Compras", "Comprar leche y pan", "Alta")
    actualizar_tarea(1, "Compras actualizadas", "Comprar leche, pan y huevos", "Media")
    assert tareas[1] == {'nombre': "Compras actualizadas", 'descripcion': "Comprar leche, pan y huevos", 'prioridad': "Media", 'completada': False}
   
    with pytest.raises(KeyError):
        actualizar_tarea(2, "Tarea inexistente", "Nada", "Baja")  # Tarea no existe

def test_marcar_completada():
    agregar_tarea(1, "Compras", "Comprar leche y pan", "Alta")
    marcar_completada(1)
    assert tareas[1]['completada'] == True
   
    with pytest.raises(KeyError):
        marcar_completada(2)  # Tarea no existe

def test_eliminar_tarea():
    agregar_tarea(1, "Compras", "Comprar leche y pan", "Alta")
    eliminar_tarea(1)
    assert 1 not in tareas
   
    with pytest.raises(KeyError):
        eliminar_tarea(2)  # Tarea no existe

def test_listar_tareas():
    agregar_tarea(1, "Compras", "Comprar leche y pan", "Alta")
    agregar_tarea(2, "Limpieza", "Limpiar la cocina", "Baja")
    marcar_completada(1)
   
    pendientes = listar_tareas()
    completadas = listar_tareas(completadas=True)
   
    assert len(pendientes) == 1
    assert pendientes[0]['nombre'] == "Limpieza"
   
    assert len(completadas) == 1
    assert completadas[0]['nombre'] == "Compras" 
