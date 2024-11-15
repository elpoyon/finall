import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000/conductoresAync"

def main(page: ft.Page):
    page.title = "Gestion de Conductores"
    page.horizontal_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def listar_conductores():
        response = requests.get(f"{API_BASE_URL}/index")
        if response.status_code == 200:
            conductores = response.json()
            listar_conductores.controls = [
                ft.Text(f"Nombre:{c['nombre']}, Direción: {c['direccion']}, Teléfono: {c['telefono']}") for c in conductores
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
    
    titulo = ft.Text("Gestion de Conductores",size=25, weight="bold")
    
    campo_nombre = ft.TextField(label="Nombre", width=200)
    campo_direccion = ft.TextField("Dirección", width=200)
    campo_telefono = ft.TextField(label="Telefono",width=200)
    campo_id = ft.TextField(label="ID para eliminar",width=200)
    
    boton_agregar = ft.ElevatedButton("Agregar Conductor", on_click=agregar_conductor)
    boton_eliminar = ft.ElevatedButton("Eliminar Conductor",on_click=eliminar_conductor)
    
    listar_conductores = ft.Column()
    listar_conductores()
    
    page.add(
        titulo,
        campo_nombre,
        campo_direccion,
        campo_telefono,
        campo_id,
        boton_agregar,
        boton_eliminar,
        listar_conductores
        
    )
    
ft.app(target=main)
            
    