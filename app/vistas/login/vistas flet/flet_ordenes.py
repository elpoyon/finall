import flet as ft
import requests

BASE_URL = "http://127.0.0.1:5000/OrdenesAsync"

def main(page: ft.Page):
    page.title = "Gestión de Órdenes"
    page.padding = 20

    date_input = ft.TextField(label="Fecha", hint_text="YYYY-MM-DD", width=200)
    fletes_input = ft.TextField(label="Fletes", width=200)
    cliente_id_input = ft.TextField(label="ID Cliente", width=200)
    vehiculo_id_input = ft.TextField(label="ID Vehículo", width=200)
    conductor_id_input = ft.TextField(label="ID Conductor", width=200)
    mercancia_id_input = ft.TextField(label="ID Mercancía", width=200)
    origen_id_input = ft.TextField(label="ID Origen", width=200)
    destino_id_input = ft.TextField(label="ID Destino", width=200)
    message_label = ft.Text(value="", color="green")

    orders_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Fletes")),
            ft.DataColumn(ft.Text("Cliente ID")),
            ft.DataColumn(ft.Text("Vehículo ID")),
            ft.DataColumn(ft.Text("Conductor ID")),
            ft.DataColumn(ft.Text("Mercancía ID")),
            ft.DataColumn(ft.Text("Origen ID")),
            ft.DataColumn(ft.Text("Destino ID")),
        ],
        rows=[]
    )

    def load_data():
        try:
            response = requests.get(f"{BASE_URL}/index")
            response.raise_for_status()
            data = response.json()
            orders_table.rows.clear()
            for order in data:
                orders_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(order["id"]))),
                            ft.DataCell(ft.Text(order["fecha"])),
                            ft.DataCell(ft.Text(str(order["fletes"]))),
                            ft.DataCell(ft.Text(str(order["cliente_id"]))),
                            ft.DataCell(ft.Text(str(order["vehiculo_id"]))),
                            ft.DataCell(ft.Text(str(order["conductor_id"]))),
                            ft.DataCell(ft.Text(str(order["mercancia_id"]))),
                            ft.DataCell(ft.Text(str(order["origen_id"]))),
                            ft.DataCell(ft.Text(str(order["destino_id"]))),
                        ]
                    )
                )
            page.update()
        except Exception as e:
            message_label.value = f"Error al cargar datos: {e}"
            message_label.color = "red"
            page.update()

    def add_order(e):
        try:
            payload = {
                "fecha": date_input.value,
                "fletes": fletes_input.value,
                "cliente_id": cliente_id_input.value,
                "vehiculo_id": vehiculo_id_input.value,
                "conductor_id": conductor_id_input.value,
                "mercancia_id": mercancia_id_input.value,
                "origen_id": origen_id_input.value,
                "destino_id": destino_id_input.value,
            }
            response = requests.post(f"{BASE_URL}/add", json=payload)
            response.raise_for_status()
            message_label.value = "¡Orden creada exitosamente!"
            message_label.color = "green"
            date_input.value = ""
            fletes_input.value = ""
            cliente_id_input.value = ""
            vehiculo_id_input.value = ""
            conductor_id_input.value = ""
            mercancia_id_input.value = ""
            origen_id_input.value = ""
            destino_id_input.value = ""
            load_data()
        except Exception as e:
            message_label.value = f"Error al crear la orden: {e}"
            message_label.color = "red"
        page.update()

    def update_order(e):
        try:
            if not orders_table.selected_rows:
                message_label.value = "Selecciona una orden para actualizar."
                message_label.color = "red"
                page.update()
                return

            selected_id = orders_table.selected_rows[0].cells[0].content.value
            payload = {
                "fecha": date_input.value,
                "fletes": fletes_input.value,
                "cliente_id": cliente_id_input.value,
                "vehiculo_id": vehiculo_id_input.value,
                "conductor_id": conductor_id_input.value,
                "mercancia_id": mercancia_id_input.value,
                "origen_id": origen_id_input.value,
                "destino_id": destino_id_input.value,
            }
            response = requests.put(f"{BASE_URL}/update/{selected_id}", json=payload)
            response.raise_for_status()
            message_label.value = "¡Orden actualizada exitosamente!"
            message_label.color = "green"
            load_data()
        except Exception as e:
            message_label.value = f"Error al actualizar la orden: {e}"
            message_label.color = "red"
        page.update()

    def delete_order(e):
        try:
            if not orders_table.selected_rows:
                message_label.value = "Selecciona una orden para eliminar."
                message_label.color = "red"
                page.update()
                return

            selected_id = orders_table.selected_rows[0].cells[0].content.value
            response = requests.delete(f"{BASE_URL}/delete/{selected_id}")
            response.raise_for_status()
            message_label.value = "¡Orden eliminada exitosamente!"
            message_label.color = "green"
            load_data()
        except Exception as e:
            message_label.value = f"Error al eliminar la orden: {e}"
            message_label.color = "red"
        page.update()

    add_button = ft.ElevatedButton("Agregar", on_click=add_order)
    update_button = ft.ElevatedButton("Actualizar", on_click=update_order)
    delete_button = ft.ElevatedButton("Eliminar", on_click=delete_order)

    page.add(
        ft.Row([date_input, fletes_input, cliente_id_input]),
        ft.Row([vehiculo_id_input, conductor_id_input, mercancia_id_input]),
        ft.Row([origen_id_input, destino_id_input]),
        ft.Row([add_button, update_button, delete_button]),
        orders_table,
        message_label,
    )

    load_data()

ft.app(target=main)
