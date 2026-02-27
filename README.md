# 🐍 Python Task Engine: Automatización & Persistencia de Datos

> **CLI Data Management Tool:** Aplicación de interfaz de línea de comandos (CLI) diseñada para la gestión de flujos de trabajo, utilizando un motor de persistencia basado en **JSON** con manejo de estados lógicos.

---

### 🏆 Logros de Ingeniería en este Proyecto

* **Data Persistence Engine:** Implementación de un sistema de lectura/escritura en archivos **JSON**, aplicando técnicas de serialización y deserialización de datos.
  
* **Manejo de Excepciones:** Estructura robusta mediante bloques `try-except` para prevenir la corrupción de datos durante operaciones de I/O (entrada/salida) en el sistema de archivos.
  
* **Arquitectura Modular:** Separación de la lógica de negocio (CRUD) de la capa de presentación (CLI), facilitando el mantenimiento y escalabilidad del código.

---
## ⚙️ Herramientas utilizadas
| Lenguaje | Persistencia | Entorno | Control de Versiones |
| :---: | :---: | :---: | :---: |
| **Python 3.10+** | **JSON (NoSQL)** | **VS Code** | **Git / GitHub** |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="50" height="50"/> | <img src="https://assets.streamlinehq.com/image/private/w_34,h_34,ar_1/f_auto/v1/icons/development/json-v4ofnse1dqj8zl0otiifzw.png/json-2vox5uwk85x39kfwdwhtju.png" alt="JSON" width="50" height="50"/> | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" alt="VS Code" width="50" height="50"/> | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" alt="GitHub" width="50" height="50"/> |

---

## 🚀 Funcionalidades

- 📌 Ver todas las tareas registradas.  
- ➕ Agregar nuevas tareas.  
- ✅ Marcar tareas como completadas.  
- 🗑️ Eliminar tareas de la lista.  
- 💾 Persistencia de datos en archivo `tareas.json`.  

---
## 💻 Código Python
```python
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
```

## 📷 Vista previa

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1WHKgzsVDNzIcTWmNezrQXA0tvh3o28ZN" alt="Vista previa del Gestor de Tareas" width="900"/>
</p>

