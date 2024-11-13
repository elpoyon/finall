import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK  # Puedes adaptar el tema según tus preferencias
    
    # Función para manejar el envío del formulario
    def handle_login(e):
        username = username_field.value
        password = password_field.value
        # Aquí podrías agregar lógica de autenticación o navegar a otra vista

    # Elementos del formulario
    title_text = ft.Text("Iniciar Sesión", size=30, weight="bold", color="white")
    
    username_field = ft.TextField(
        label="Email",
        icon=ft.icons.EMAIL,
        border_color="blue",
        filled=True,
        width=250
    )
    
    password_field = ft.TextField(
        label="Contraseña",
        icon=ft.icons.LOCK,
        password=True,
        border_color="blue",
        filled=True,
        width=250
    )
    
    remember_me_checkbox = ft.Checkbox(label="Recordar", value=False)
    forgot_password_text = ft.TextButton("Olvidar la Contraseña", on_click=lambda e: print("Recuperar contraseña"))
    
    login_button = ft.ElevatedButton("Ingresar", on_click=handle_login)
    
    register_text = ft.Text("No tengo cuenta", color="white")
    register_button = ft.TextButton("Crear cuenta", on_click=lambda e: page.go("/add"))

    # Estructura del formulario
    form = ft.Column(
        [
            title_text,
            username_field,
            password_field,
            ft.Row(
                [remember_me_checkbox, forgot_password_text],
                alignment="spaceBetween"
            ),
            login_button,
            ft.Row(
                [register_text, register_button],
                alignment="center"
            )
        ],
        alignment="center",
        spacing=10
    )
    
    # Contenedor principal
    page.add(
        ft.Container(
            content=form,
            width=350,
            padding=20,
            border_radius=10,
            bgcolor="#333333"
        )
    )

ft.app(target=main)
    