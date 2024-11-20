import flet as ft

def main(page: ft.Page):
    page.title = "Clientes"
    page.vertical_alignment = ft.MainAxisAlignment.START

    clientes = [
        {"id": 1, "nombre": "Juan Pérez", "direccion": "Calle 123", "telefono": "123456789"},
        {"id": 2, "nombre": "Ana López", "direccion": "Avenida 456", "telefono": "987654321"},

    ]

    search_input = ft.TextField(label="Buscar por nombre", on_change=lambda e: filtrar_clientes(e.control.value))

    tabla_clientes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Dirección")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[],
    )

    def filtrar_clientes(search_value):
        search_value = search_value.lower()
        tabla_clientes.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(cliente["id"])),
                    ft.DataCell(ft.Text(cliente["nombre"])),
                    ft.DataCell(ft.Text(cliente["direccion"])),
                    ft.DataCell(ft.Text(cliente["telefono"])),
                    ft.DataCell(
                        ft.Row(
                            [
                                ft.ElevatedButton("Editar", on_click=lambda e, id=cliente["id"]: editar_cliente(id)),
                                ft.ElevatedButton("Eliminar", on_click=lambda e, id=cliente["id"]: eliminar_cliente(id)),
                            ]
                        )
                    ),
                ]
            )
            for cliente in clientes
            if search_value in cliente["nombre"].lower()
        ]
        page.update()

    def editar_cliente(cliente_id):
        print(f"Editar cliente: {cliente_id}")

    def eliminar_cliente(cliente_id):
        print(f"Eliminar: {cliente_id}")

    def agregar_cliente(e):
        print("Redirigir a formulario de agregar cliente")

    def regresar(e):
        print("Regresar al inicio de sesión")

    botones = ft.Row(
        [
            ft.ElevatedButton("Agregar", on_click=agregar_cliente),
            ft.ElevatedButton("Regresar", on_click=regresar),
        ],
        alignment=ft.MainAxisAlignment.END,
    )

    filtrar_clientes("")  
    page.add(
        ft.Column(
            [
                ft.Text("Lista de Clientes", size=24, weight="bold"),
                search_input,
                tabla_clientes,
                botones,
            ],
            spacing=20,
            expand=True,
        )
    )

ft.app(target=main)
