import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Clientes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    search_field = ft.TextField(label="Buscar por nombre", autofocus=True)
    
    # Placeholder data for clientes
    clientes = [
        {"id": 1, "nombre": "Juan Perez", "direccion": "Calle 123", "telefono": "123-4567890"},
        {"id": 2, "nombre": "Ana Gomez", "direccion": "Avenida 456", "telefono": "987-6543210"},
        {"id": 3, "nombre": "Carlos Ruiz", "direccion": "Calle 789", "telefono": "456-1239870"},
    ]

    def buscar_cliente(e):
        search_value = search_field.value.lower()
        filtered_clientes = [
            cliente for cliente in clientes if search_value in cliente["nombre"].lower()
        ]
        table.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(cliente["id"])),
                    ft.DataCell(ft.Text(cliente["nombre"])),
                    ft.DataCell(ft.Text(cliente["direccion"])),
                    ft.DataCell(ft.Text(cliente["telefono"])),
                ]
            )
            for cliente in filtered_clientes
        ]
        page.update()

    search_field.on_change = buscar_cliente

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Dirección")),
            ft.DataColumn(ft.Text("Teléfono")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(cliente["id"])),
                    ft.DataCell(ft.Text(cliente["nombre"])),
                    ft.DataCell(ft.Text(cliente["direccion"])),
                    ft.DataCell(ft.Text(cliente["telefono"])),
                ]
            )
            for cliente in clientes
        ],
    )

    page.add(
        ft.Column(
            [
                ft.Text("Lista de Clientes", size=24, weight="bold"),
                search_field,
                table,
                ft.Row(
                    [
                        ft.ElevatedButton("Agregar", on_click=lambda e: print("Agregar cliente")),
                        ft.ElevatedButton("Regresar", on_click=lambda e: print("Regresar")),
                    ],
                    spacing=20,
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
