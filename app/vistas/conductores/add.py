import flet as ft

def main(page: ft.Page):
    page.title = "Agregar Conductores"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def agregar_conductor(e):
        nombre = nombre_field.value
        direccion = direccion_field.value
        telefono = telefono_field.value
        print(f"Agregando conductor: Nombre={nombre}, Dirección={direccion}, Teléfono={telefono}")

    nombre_field = ft.TextField(label="Nombre", required=True)
    direccion_field = ft.TextField(label="Dirección", required=True)
    telefono_field = ft.TextField(label="Teléfono", required=True)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Agregar Conductores", size=24, weight="bold"),
                    nombre_field,
                    direccion_field,
                    telefono_field,
                    ft.ElevatedButton("Agregar Conductores", on_click=agregar_conductor),
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
