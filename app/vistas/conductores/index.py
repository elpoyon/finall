import flet as ft

def main(page: ft.Page):
    page.title = "Conductores"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

 
    conductores_data = [
        {"id": 1, "nombre": "Juan Pérez", "direccion": "Calle 123", "telefono": "123456789"},
        {"id": 2, "nombre": "María Gómez", "direccion": "Avenida 45", "telefono": "987654321"},
    ]

    def buscar_conductores(e):
        query = search_field.value.lower()
        table_data.controls.clear()
        for conductor in conductores_data:
            if query in conductor["nombre"].lower():
                table_data.controls.append(crear_fila_conductor(conductor))
        table_data.update()

    def crear_fila_conductor(conductor):
        return ft.DataRow(cells=[
            ft.DataCell(ft.Text(conductor["id"])),
            ft.DataCell(ft.Text(conductor["nombre"])),
            ft.DataCell(ft.Text(conductor["direccion"])),
            ft.DataCell(ft.Text(conductor["telefono"])),
            ft.DataCell(ft.Row([
                ft.ElevatedButton("Editar", on_click=lambda e: editar_conductor(conductor["id"])),
                ft.ElevatedButton("Eliminar", on_click=lambda e: eliminar_conductor(conductor["id"])),
            ]))
        ])

    def editar_conductor(conductor_id):
        print(f"Editar conductor con ID: {conductor_id}")

    def eliminar_conductor(conductor_id):
        print(f"Eliminar conductor con ID: {conductor_id}")

    search_field = ft.TextField(
        label="Buscar por nombre",
        on_change=buscar_conductores,
    )

    table_data = ft.Column(
        [crear_fila_conductor(conductor) for conductor in conductores_data]
    )
    conductores_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Dirección")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[crear_fila_conductor(conductor) for conductor in conductores_data],
    )

    page.add(
        ft.Column(
            [
                ft.Text("Lista de Conductores", size=24, weight="bold"),
                search_field,
                conductores_table,
                ft.Row([
                    ft.ElevatedButton("Agregar", on_click=lambda e: print("Agregar conductor")),
                    ft.ElevatedButton("Regresar", on_click=lambda e: print("Regresar al menú")),
                ], spacing=20),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        )
    )

ft.app(target=main)
