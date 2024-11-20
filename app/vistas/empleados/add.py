import flet as ft

def main(page: ft.Page):
    page.title = "Agregar Empleados"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def agregar_empleado(e):
        empleado = {
            "nombre": nombre_field.value,
            "direccion": direccion_field.value,
            "telefono": telefono_field.value,
        }
        print(f"Empleado agregado: {empleado}")

    nombre_field = ft.TextField(label="Nombre", autofocus=True)
    direccion_field = ft.TextField(label="Dirección")
    telefono_field = ft.TextField(label="Teléfono")

    page.add(
        ft.Column(
            [
                ft.Text("Agregar Empleados", size=24, weight="bold"),
                nombre_field,
                direccion_field,
                telefono_field,
                ft.ElevatedButton("Agregar", on_click=agregar_empleado),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
