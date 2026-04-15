import json
import os

# =============================
#   GESTOR DE TAREAS EN PYTHON
#   Autor: Wily Duvan Villamil Rey
#   LinkedIn: www.linkedin.com/in/wily-rey-administrador-bases-datos
# =============================

DB_FILE = "tareas.json"


def cargar_tareas():
    """Carga las tareas desde el archivo JSON, si existe."""
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON."""
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(tareas, file, indent=4, ensure_ascii=False)


def mostrar_tareas(tareas):
    """Muestra todas las tareas con su estado."""
    if not tareas:
        print("\n📌 No hay tareas registradas.")
        return
    print("\n=== LISTA DE TAREAS ===")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✅ Completada" if tarea["completada"] else "❌ Pendiente"
        print(f"{i}. {tarea['titulo']} - {estado}")


def agregar_tarea(tareas):
    """Agrega una nueva tarea."""
    titulo = input("\nEscribe el título de la nueva tarea: ").strip()
    if titulo:
        tareas.append({"titulo": titulo, "completada": False})
        guardar_tareas(tareas)
        print("✅ Tarea agregada con éxito.")
    else:
        print("⚠️ El título no puede estar vacío.")


def marcar_completada(tareas):
    """Marca una tarea como completada."""
    try:
        num = int(input("\nNúmero de la tarea a completar: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]["completada"] = True
            guardar_tareas(tareas)
            print("🎉 Tarea marcada como completada.")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Debes ingresar un número.")


def eliminar_tarea(tareas):
    """Elimina una tarea de la lista."""
    try:
        num = int(input("\nNúmero de la tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            tarea_eliminada = tareas.pop(num - 1)
            guardar_tareas(tareas)
            print(f"🗑️ Tarea '{tarea_eliminada['titulo']}' eliminada.")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Debes ingresar un número.")


def menu():
    """Menú principal de la aplicación."""
    tareas = cargar_tareas()
    while True:
        print("\n========= GESTOR DE TAREAS =========")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
            marcar_completada(tareas)
        elif opcion == "4":
            mostrar_tareas(tareas)
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("\n👋 ¡Hasta luego! Tus tareas se han guardado.")
            break
        else:
            print("⚠️ Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
