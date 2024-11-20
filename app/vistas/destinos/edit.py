import flet as ft

def main(page: ft.Page):
    page.title = "Editar Destinos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def actualizar_destino(e):
        print(f"Nombre: {nombre_field.value}")
        print(f"Dirección: {direccion_field.value}")
        print(f"Teléfono: {telefono_field.value}")
        print("Destino actualizado.")

    nombre_field = ft.TextField(label="Nombre", value="Nombre actual del destino", required=True)
    direccion_field = ft.TextField(label="Dirección", value="Dirección actual del destino", required=True)
    telefono_field = ft.TextField(label="Teléfono", value="Teléfono actual del destino", required=True)

    page.add(
        ft.Column(
            [
                ft.Text("Editar Destinos", size=24, weight="bold"),
                nombre_field,
                direccion_field,
                telefono_field,
                ft.ElevatedButton("Actualizar Destinos", on_click=actualizar_destino),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
