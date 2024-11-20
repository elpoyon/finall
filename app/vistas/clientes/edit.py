import flet as ft

def main(page: ft.Page):
    page.title = "Editar Cliente"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def actualizar_cliente(e):
        nombre = nombre_field.value
        direccion = direccion_field.value
        telefono = telefono_field.value
        print(f"Actualizando cliente: Nombre={nombre}, Dirección={direccion}, Teléfono={telefono}")

    nombre_field = ft.TextField(label="Nombre", value="Juan Pérez", required=True)
    direccion_field = ft.TextField(label="Dirección", value="Calle 123", required=True)
    telefono_field = ft.TextField(label="Teléfono", value="123456789", required=True)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Editar Clientes", size=24, weight="bold"),
                    nombre_field,
                    direccion_field,
                    telefono_field,
                    ft.ElevatedButton("Actualizar", on_click=actualizar_cliente),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=400,
            padding=20,
            bgcolor="#f0f0f0",
            border_radius=10,
        )
    )

ft.app(target=main)
