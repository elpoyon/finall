import flet as ft

def main(page: ft.Page):
    data1 = [{'id': 1, 'nombre': 'Juan'}, {'id': 2, 'nombre': 'Pedro'}]
    data5 = [{'id': 1, 'placa': 'ABC123'}, {'id': 2, 'placa': 'DEF456'}]
    data3 = [{'id': 1, 'nombre': 'Electrónica'}, {'id': 2, 'nombre': 'Ropa'}]
    data6 = [{'id': 1, 'nombre': 'Madrid'}, {'id': 2, 'nombre': 'Sevilla'}]
    data2 = [{'id': 1, 'nombre': 'Barcelona'}, {'id': 2, 'nombre': 'Valencia'}]

    fecha_input = ft.TextField(label="Fecha", required=True)
    fletes_input = ft.TextField(label="Valor Flete", required=True)

    conductores_dropdown = ft.Dropdown(
        label="Conductores",
        options=[ft.dropdown.Option(conductor['nombre'], value=conductor['id']) for conductor in data1]
    )

    vehiculos_dropdown = ft.Dropdown(
        label="Vehículos",
        options=[ft.dropdown.Option(vehiculo['placa'], value=vehiculo['id']) for vehiculo in data5]
    )

    mercancias_dropdown = ft.Dropdown(
        label="Mercancía",
        options=[ft.dropdown.Option(mercancia['nombre'], value=mercancia['id']) for mercancia in data3]
    )

    origenes_dropdown = ft.Dropdown(
        label="Origen",
        options=[ft.dropdown.Option(origen['nombre'], value=origen['id']) for origen in data6]
    )

    destinos_dropdown = ft.Dropdown(
        label="Destino",
        options=[ft.dropdown.Option(destino['nombre'], value=destino['id']) for destino in data2]
    )

    clientes_dropdown = ft.Dropdown(
        label="Cliente",
        options=[ft.dropdown.Option(cliente['nombre'], value=cliente['id']) for cliente in data1]
    )

    def add_order(e):
        # Aquí puedes manejar la adición de la nueva orden
        print("Orden agregada")

    add_button = ft.ElevatedButton("Agregar Ordenes", on_click=add_order)

    page.add(
        ft.Column([
            fecha_input,
            fletes_input,
            conductores_dropdown,
            vehiculos_dropdown,
            mercancias_dropdown,
            origenes_dropdown,
            destinos_dropdown,
            clientes_dropdown,
            add_button
        ])
    )

ft.app(target=main)
