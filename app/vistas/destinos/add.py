import flet as ft

def main(page: ft.Page):
    page.title = "Agregar Destinos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def agregar_destino(e):
        print(f"Nombre: {nombre_field.value}")
        print(f"Dirección: {direccion_field.value}")
        print(f"Teléfono: {telefono_field.value}")
        print("Destino agregado.")

    nombre_field = ft.TextField(label="Nombre", required=True)
    direccion_field = ft.TextField(label="Dirección", required=True)
    telefono_field = ft.TextField(label="Teléfono", required=True)

    page.add(
        ft.Column(
            [
                ft.Text("Agregar Destinos", size=24, weight="bold"),
                nombre_field,
                direccion_field,
                telefono_field,
                ft.ElevatedButton("Agregar Destinos", on_click=agregar_destino),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
