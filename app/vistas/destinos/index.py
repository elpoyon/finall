import flet as ft

def main(page: ft.Page):
    page.title = "Destinos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    destinos_data = [
        {"id": 1, "nombre": "Hotel Central", "direccion": "Calle 123", "telefono": "123456789"},
        {"id": 2, "nombre": "Playa Azul", "direccion": "Avenida 45", "telefono": "987654321"},
    ]

    def buscar_destinos(e):
        query = search_field.value.lower()
        table_data.controls.clear()
        for destino in destinos_data:
            if query in destino["nombre"].lower():
                table_data.controls.append(crear_fila_destino(destino))
        table_data.update()

    def crear_fila_destino(destino):
        return ft.DataRow(cells=[
            ft.DataCell(ft.Text(destino["id"])),
            ft.DataCell(ft.Text(destino["nombre"])),
            ft.DataCell(ft.Text(destino["direccion"])),
            ft.DataCell(ft.Text(destino["telefono"])),
            ft.DataCell(ft.Row([
                ft.ElevatedButton("Editar", on_click=lambda e: editar_destino(destino["id"])),
                ft.ElevatedButton("Eliminar", on_click=lambda e: eliminar_destino(destino["id"])),
            ]))
        ])

    def editar_destino(destino_id):
        print(f"Editar destino con ID: {destino_id}")

    def eliminar_destino(destino_id):
        print(f"Eliminar destino con ID: {destino_id}")

    search_field = ft.TextField(
        label="Buscar por nombre",
        on_change=buscar_destinos,
    )

    table_data = ft.Column(
        [crear_fila_destino(destino) for destino in destinos_data]
    )
    destinos_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Dirección")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[crear_fila_destino(destino) for destino in destinos_data],
    )

    page.add(
        ft.Column(
            [
                ft.Text("Lista de Destinos", size=24, weight="bold"),
                search_field,
                destinos_table,
                ft.Row([
                    ft.ElevatedButton("Agregar", on_click=lambda e: print("Agregar destino")),
                    ft.ElevatedButton("Regresar", on_click=lambda e: print("Regresar al menú")),
                ], spacing=20),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        )
    )

ft.app(target=main)
