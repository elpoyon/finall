import flet as ft

def main(page: ft.Page):
    page.title = "Editar Cliente"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    cliente = {"id": 1, "nombre": "Juan Perez", "direccion": "Calle 123", "telefono": "123-4567890"}

    nombre_field = ft.TextField(label="Nombre", value=cliente["nombre"], autofocus=True)
    direccion_field = ft.TextField(label="Dirección", value=cliente["direccion"])
    telefono_field = ft.TextField(label="Teléfono", value=cliente["telefono"])

    def actualizar_cliente(e):
        cliente["nombre"] = nombre_field.value
        cliente["direccion"] = direccion_field.value
        cliente["telefono"] = telefono_field.value
        print(f"Cliente actualizado: {cliente}")

    page.add(
        ft.Column(
            [
                ft.Text("Editar Cliente", size=24, weight="bold"),
                nombre_field,
                direccion_field,
                telefono_field,
                ft.ElevatedButton("Actualizar", on_click=actualizar_cliente),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
