import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    def login_action(e):
        username = username_field.value
        password = password_field.value
        if username and password:
            print(f"Iniciar sesión con Usuario: {username}, Contraseña: {password}")
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, completa todos los campos."),
            )
            page.snack_bar.open = True
            page.update()

    username_field = ft.TextField(
        label="Email",
        hint_text="Ingresa tu correo",
        prefix_icon=ft.icons.EMAIL,
        width=300
    )
    password_field = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa tu contraseña",
        prefix_icon=ft.icons.LOCK,
        password=True,
        width=300
    )

    recordar_checkbox = ft.Checkbox(label="Recordar")

    login_button = ft.ElevatedButton(
        text="Ingresar",
        on_click=login_action,
        width=300
    )

    registrar_link = ft.TextButton(
        text="Crear cuenta",
        on_click=lambda e: print("Redirigir a crear cuenta"),
    )

    olvidar_contrasena_link = ft.TextButton(
        text="Olvidar la Contraseña",
        on_click=lambda e: print("Redirigir a olvidar contraseña"),
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Iniciar Sesión", size=24, weight=ft.FontWeight.BOLD),
                username_field,
                password_field,
                ft.Row(
                    controls=[
                        recordar_checkbox,
                        olvidar_contrasena_link,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                login_button,
                ft.Row(
                    controls=[
                        ft.Text("No tengo cuenta"),
                        registrar_link,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
