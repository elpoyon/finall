import flet as ft

def main(page: ft.Page):
    page.title = "Agregar Usuario"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def submit_form(e):
        username = username_field.value
        password = password_field.value
        print(f"Username: {username}, Password: {password}")

    username_field = ft.TextField(label="Username", name="username")
    password_field = ft.TextField(label="Password", name="password", password=True)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Agregar Usuario", size=20, weight="bold"),
                    username_field,
                    password_field,
                    ft.ElevatedButton("Agregar Usuario", on_click=submit_form),
                ]
            ),
            padding=20,
            bgcolor="#f0f0f0",
            border_radius=10,
        )
    )

ft.app(target=main)
