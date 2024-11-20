import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000/conductoresAync"

def main(page: ft.Page):
    page.title = "Gestion de Conductores"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT

    lista_conductores_column = ft.Column()  # Cambié el nombre de la columna para evitar conflictos

    def listar_conductores():
        response = requests.get(f"{API_BASE_URL}/index")
        if response.status_code == 200:
            conductores = response.json()
            lista_conductores_column.controls = [
                ft.Text(f"Nombre: {c['nombre']}, Dirección: {c['direccion']}, Teléfono: {c['telefono']}") for c in conductores
            ]
            page.update()

    def agregar_conductor(e):
        nombre = campo_nombre.value
        direccion = campo_direccion.value
        telefono = campo_telefono.value
        response = requests.post(f"{API_BASE_URL}/add", json={'Username': nombre, 'direccion': direccion, 'celphone': telefono})
        if response.status_code == 201:
            listar_conductores()
        else:
            print("Error al agregar conductor")

    def eliminar_conductor(e):
        conductor_id = int(campo_id.value)
        response = requests.delete(f"{API_BASE_URL}/delete/{conductor_id}")
        if response.status_code == 200:
            listar_conductores()
        else:
            print("Error al eliminar conductor")

    titulo = ft.Text("Gestion de Conductores", size=25, weight="bold")

    campo_nombre = ft.TextField(label="Nombre", width=200)
    campo_direccion = ft.TextField(label="Dirección", width=200)
    campo_telefono = ft.TextField(label="Teléfono", width=200)
    campo_id = ft.TextField(label="ID para eliminar", width=200)

    boton_agregar = ft.ElevatedButton("Agregar Conductor", on_click=agregar_conductor)
    boton_eliminar = ft.ElevatedButton("Eliminar Conductor", on_click=eliminar_conductor)

    # Carga inicial de la lista de conductores
    listar_conductores()

    page.add(
        titulo,
        campo_nombre,
        campo_direccion,
        campo_telefono,
        campo_id,
        boton_agregar,
        boton_eliminar,
        lista_conductores_column  # Referencia actualizada
    )

ft.app(target=main)
