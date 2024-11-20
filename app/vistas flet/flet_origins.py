import flet as ft
import requests

BASE_URL = "http://127.0.0.1:5000/OrigenesAsync"

def main(page: ft.Page):
    page.title = "Gestión de Orígenes"
    page.padding = 20

    name_input = ft.TextField(label="Nombre", width=300)
    address_input = ft.TextField(label="Dirección", width=300)
    phone_input = ft.TextField(label="Teléfono", width=300)
    message_label = ft.Text(value="", color="green")

    origins_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Dirección")),
            ft.DataColumn(ft.Text("Teléfono")),
        ],
        rows=[]
    )

    def load_data():
        try:
            response = requests.get(f"{BASE_URL}/index")
            response.raise_for_status()
            data = response.json()
            origins_table.rows.clear()
            for origin in data:
                origins_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(origin["id"]))),
                            ft.DataCell(ft.Text(origin["nombre"])),
                            ft.DataCell(ft.Text(origin["direccion"])),
                            ft.DataCell(ft.Text(origin["telefono"])),
                        ]
                    )
                )
            page.update()
        except Exception as e:
            message_label.value = f"Error al cargar datos: {e}"
            message_label.color = "red"
            page.update()

    def add_origin(e):
        try:
            payload = {
                "nombre": name_input.value,
                "direccion": address_input.value,
                "telefono": phone_input.value
            }
            response = requests.post(f"{BASE_URL}/add", json=payload)
            response.raise_for_status()
            message_label.value = "¡Origen agregado exitosamente!"
            message_label.color = "green"
            name_input.value = ""
            address_input.value = ""
            phone_input.value = ""
            load_data()
        except Exception as e:
            message_label.value = f"Error al agregar origen: {e}"
            message_label.color = "red"
        page.update()

    def update_origin(e):
        try:
            if not origins_table.selected_rows:
                message_label.value = "Selecciona un origen para actualizar."
                message_label.color = "red"

                page.update()
                return

            selected_id = origins_table.selected_rows[0].cells[0].content.value
            payload = {
                "nombre": name_input.value,
                "direccion": address_input.value,
                "telefono": phone_input.value
            }
            response = requests.put(f"{BASE_URL}/update/{selected_id}", json=payload)
            response.raise_for_status()
            message_label.value = "¡Origen actualizado exitosamente!"
            message_label.color = "green"
            load_data()
        except Exception as e:
            message_label.value = f"Error al actualizar origen: {e}"
            message_label.color = "red"
        page.update()

    def delete_origin(e):
        try:
            if not origins_table.selected_rows:
                message_label.value = "Selecciona un origen para eliminar."
                message_label.color = "red"
                page.update()
                return

            selected_id = origins_table.selected_rows[0].cells[0].content.value
            response = requests.delete(f"{BASE_URL}/delete/{selected_id}")
            response.raise_for_status()
            message_label.value = "¡Origen eliminado exitosamente!"
            message_label.color = "green"
            load_data()
        except Exception as e:
            message_label.value = f"Error al eliminar origen: {e}"
            message_label.color = "red"
        page.update()

    add_button = ft.ElevatedButton("Agregar", on_click=add_origin)
    update_button = ft.ElevatedButton("Actualizar", on_click=update_origin)
    delete_button = ft.ElevatedButton("Eliminar", on_click=delete_origin)

    page.add(
        ft.Row([name_input, address_input, phone_input]),
        ft.Row([add_button, update_button, delete_button]),
        origins_table,
        message_label,
    )

    load_data()

ft.app(target=main)
