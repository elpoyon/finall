import flet as ft

def main(page: ft.Page):
    ordenes = {
        'id': 1,
        'fecha': '2024-11-20',
        'fletes': 1000,
        'conductores': {'id': 1, 'nombre': 'Juan'},
        'vehiculos': {'id': 1, 'placa': 'ABC123'},
        'mercancias': {'id': 1, 'nombre': 'Electrónica'},
        'origenes': {'id': 1, 'nombre': 'Madrid'},
        'destinos': {'id': 1, 'nombre': 'Barcelona'},
        'clientes': {'id': 1, 'nombre': 'Cliente X'}
    }
    data1 = [{'id': 1, 'nombre': 'Juan'}, {'id': 2, 'nombre': 'Pedro'}]
    datas = [{'id': 1, 'placa': 'ABC123'}, {'id': 2, 'placa': 'DEF456'}]
    data3 = [{'id': 1, 'nombre': 'Electrónica'}, {'id': 2, 'nombre': 'Ropa'}]
    data6 = [{'id': 1, 'nombre': 'Madrid'}, {'id': 2, 'nombre': 'Sevilla'}]
    data2 = [{'id': 1, 'nombre': 'Barcelona'}, {'id': 2, 'nombre': 'Valencia'}]

    fecha_input = ft.TextField(label="Fecha", value=ordenes['fecha'], required=True)
    fletes_input = ft.TextField(label="Valor Flete", value=str(ordenes['fletes']), required=True)

    conductores_dropdown = ft.Dropdown(
        label="Conductores",
        options=[ft.dropdown.Option(conductor['nombre'], value=conductor['id']) for conductor in data1],
        value=ordenes['conductores']['id']
    )

    vehiculos_dropdown = ft.Dropdown(
        label="Vehículos",
        options=[ft.dropdown.Option(vehiculo['placa'], value=vehiculo['id']) for vehiculo in datas],
        value=ordenes['vehiculos']['id']
    )

    mercancias_dropdown = ft.Dropdown(
        label="Mercancía",
        options=[ft.dropdown.Option(mercancia['nombre'], value=mercancia['id']) for mercancia in data3],
        value=ordenes['mercancias']['id']
    )

    origenes_dropdown = ft.Dropdown(
        label="Origen",
        options=[ft.dropdown.Option(origen['nombre'], value=origen['id']) for origen in data6],
        value=ordenes['origenes']['id']
    )

    destinos_dropdown = ft.Dropdown(
        label="Destino",
        options=[ft.dropdown.Option(destino['nombre'], value=destino['id']) for destino in data2],
        value=ordenes['destinos']['id']
    )

    clientes_dropdown = ft.Dropdown(
        label="Cliente",
        options=[ft.dropdown.Option(cliente['nombre'], value=cliente['id']) for cliente in data1],
        value=ordenes['clientes']['id']
    )

    def update_order(e):
        # Aquí puedes manejar la actualización de la orden
        print(f"Orden actualizada: {ordenes['id']}")

    update_button = ft.ElevatedButton("Actualizar Ordenes", on_click=update_order)

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
            update_button
        ])
    )

ft.app(target=main)
