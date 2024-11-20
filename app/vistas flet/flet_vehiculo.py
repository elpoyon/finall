import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000/VehiculoAsync"

def main(page: ft.Page):
    page.title = "Gestión de Vehículos"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def listar_vehiculos():
        response = requests.get(f"{API_BASE_URL}/index")
        if response.status_code == 200:
            vehiculos = response.json()
            listar_vehiculos.controls = [
                ft.Text(f"Marca: {v['marca']}, Placa: {v['placa']}") for v in vehiculos
            ]
            page.update()
        
    def agregar_vehiculo(e):
        marca = campo_marca.value
        placa = campo_placa.value
        response = requests.post(f"{API_BASE_URL}/add", json={'marca': marca, 'placa': placa})
        if response.status_code == 201:
            listar_vehiculos()
        else:
            print("Error al agregar vehículo")
        
    def eliminar_vehiculo(e):
        vehiculo_id = int(campo_id.value)
        response = requests.delete(f"{API_BASE_URL}/delete/{vehiculo_id}")
        if response.status_code == 200:
            listar_vehiculos()
        else:
            print("Error al eliminar vehículo")
        
    titulo = ft.Text("Gestión de vehículos", size=25, weight="bold")
    campo_marca = ft.TextField(label="Marca", width=200)
    campo_placa = ft.TextField(label="Placa", width=200)
    campo_id = ft.TextField(label="ID para eliminar", width=200)

    boton_agregar = ft.ElevatedButton("Agregar vehículo", on_click=agregar_vehiculo)
    boton_eliminar = ft.ElevatedButton("Eliminar vehículo", on_click=eliminar_vehiculo)    
    
    listar_vehiculos = ft.Column()

    page.add(
        titulo,
        campo_marca,
        campo_placa,
        campo_id,
        boton_agregar,
        boton_eliminar,
        listar_vehiculos
    )

ft.app(target=main)
