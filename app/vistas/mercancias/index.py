import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Mercancías"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Simulación de datos
    mercancias_data = [
        {"id": 1, "nombre": "Mercancía A", "direccion": "Dirección A", "telefono": "123456789"},
        {"id": 2, "nombre": "Mercancía B", "direccion": "Dirección B", "telefono": "987654321"},
        {"id": 3, "nombre": "Mercancía C", "direccion": "Dirección C", "telefono": "555555555"},
    ]

    search_input = ft.TextField(label="Buscar por nombre", on_change=lambda e: filter_mercancias(e.control.value))
    table_rows = []
    
    def filter_mercancias(query):
        filtered_data = [
            mercancia for mercancia in mercancias_data if query.lower() in mercancia["nombre"].lower()
        ]
        update_table(filtered_data)

    def update_table(data):
        global table_rows
        table_rows = []
        for mercancia in data:
            table_rows.append(
                ft.Row(
                    [
                        ft.Text(str(mercancia["id"])),
                        ft.Text(mercancia["nombre"]),
                        ft.Text(mercancia["direccion"]),
                        ft.Text(mercancia["telefono"]),
                        ft.Row(
                            [
                                ft.ElevatedButton("Editar", on_click=lambda _: page.add(ft.Text("Editar Mercancía"))),
                                ft.ElevatedButton("Eliminar", on_click=lambda _: page.add(ft.Text("Eliminar Mercancía"))),
                            ]
                        ),
                    ]
                )
            )
        page.update()

    update_table(mercancias_data)

    page.add(
        ft.Column(
            [
                ft.Text("Lista de Mercancías", size=24, weight="bold"),
                search_input,
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("ID")),
                        ft.DataColumn(ft.Text("Nombre")),
                        ft.DataColumn(ft.Text("Dirección")),
                        ft.DataColumn(ft.Text("Teléfono")),
                        ft.DataColumn(ft.Text("Acciones")),
                    ],
                    rows=table_rows,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Agregar", on_click=lambda _: page.add(ft.Text("Agregar Mercancía"))),
                        ft.ElevatedButton("Regresar", on_click=lambda _: page.add(ft.Text("Regresar a login"))),
                    ]
                ),
            ]
        )
    )

ft.app(target=main)
