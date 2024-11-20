import flet as ft

def main(page: ft.Page):
    page.title = "Agregar Clientes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def submit_form(e):
        nombre = nombre_field.value
        direccion = direccion_field.value
        telefono = telefono_field.value
        print(f"Nombre: {nombre}, Dirección: {direccion}, Teléfono: {telefono}")

    nombre_field = ft.TextField(label="Nombre", name="nombre", required=True)
    direccion_field = ft.TextField(label="Dirección", name="direccion", required=True)
    telefono_field = ft.TextField(label="Teléfono", name="telefono", required=True)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Agregar Clientes", size=24, weight="bold"),
                    nombre_field,
                    direccion_field,
                    telefono_field,
                    ft.ElevatedButton(
                        "Agregar Clientes",
                        on_click=submit_form,
                        style=ft.ButtonStyle(
                            padding=ft.EdgeInsets.symmetric(vertical=10, horizontal=20)
                        ),
                    ),
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=400,
            padding=20,
            bgcolor="#f0f0f0",
            border_radius=10,
            alignment=ft.alignment.center,
        )
    )

ft.app(target=main)
