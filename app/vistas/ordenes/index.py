import flet as ft

def main(page: ft.Page):
    data = [
        {'id': 1, 'fecha': '2024-11-20', 'fletes': 1000, 'conductores': {'nombre': 'Juan'}, 'vehiculos': {'placa': 'ABC123'}, 
         'mercancias': {'nombre': 'Electrónica'}, 'origenes': {'nombre': 'Madrid'}, 'destinos': {'nombre': 'Barcelona'}, 
         'clientes': {'nombre': 'Cliente X'}},
        {'id': 2, 'fecha': '2024-11-19', 'fletes': 1500, 'conductores': {'nombre': 'Pedro'}, 'vehiculos': {'placa': 'DEF456'}, 
         'mercancias': {'nombre': 'Ropa'}, 'origenes': {'nombre': 'Sevilla'}, 'destinos': {'nombre': 'Valencia'}, 
         'clientes': {'nombre': 'Cliente Y'}}
    ]

    search_input = ft.TextField(label="Buscar por nombre", autofocus=True)

    def search_filter(e):
        search_value = search_input.value.lower()
        for row in table_rows:
            row.visible = search_value in row.cells[1].content.lower()
        page.update()

    search_input.on_change = search_filter

    table_rows = []
    for orden in data:
        row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(orden['id']))),
                ft.DataCell(ft.Text(orden['fecha'])),
                ft.DataCell(ft.Text(str(orden['fletes']))),
                ft.DataCell(ft.Text(orden['conductores']['nombre'])),
                ft.DataCell(ft.Text(orden['vehiculos']['placa'])),
                ft.DataCell(ft.Text(orden['mercancias']['nombre'])),
                ft.DataCell(ft.Text(orden['origenes']['nombre'])),
                ft.DataCell(ft.Text(orden['destinos']['nombre'])),
                ft.DataCell(ft.Text(orden['clientes']['nombre'])),
                ft.DataCell(
                    ft.Row([
                        ft.IconButton(ft.icons.EDIT, on_click=lambda e, orden_id=orden['id']: edit_order(orden_id)),
                        ft.IconButton(ft.icons.DELETE, on_click=lambda e, orden_id=orden['id']: delete_order(orden_id)),
                    ])
                ),
            ]
        )
        table_rows.append(row)

    def edit_order(orden_id):
        print(f"Editando la orden {orden_id}")

    def delete_order(orden_id):
        print(f"Eliminando la orden {orden_id}")

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Valor Flete")),
            ft.DataColumn(ft.Text("Conductores")),
            ft.DataColumn(ft.Text("Vehiculos")),
            ft.DataColumn(ft.Text("Mercancia")),
            ft.DataColumn(ft.Text("Origen")),
            ft.DataColumn(ft.Text("Destino")),
            ft.DataColumn(ft.Text("Cliente")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=table_rows,
    )

    add_button = ft.ElevatedButton("Agregar", on_click=lambda e: add_order())
    back_button = ft.ElevatedButton("Regresar", on_click=lambda e: go_back())

    def add_order():
        print("Agregando nueva orden")

    def go_back():
        print("Regresando")

    page.add(
        search_input,
        table,
        add_button,
        back_button,
    )

ft.app(target=main)
