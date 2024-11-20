import flet as ft

def main(page: ft.Page):
    page.title = "Agregar Mercancías"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    datos_tmercancia = [
        {"id": 1, "nombre": "Tipo A"},
        {"id": 2, "nombre": "Tipo B"},
        {"id": 3, "nombre": "Tipo C"},
    ]

    campo_nombre = ft.TextField(label="Nombre", autofocus=True)
    
    dropdown_tmercancia = ft.Dropdown(
        label="Tipo de Mercancías",
        options=[ft.dropdown.Option(t["nombre"], value=t["id"]) for t in datos_tmercancia]
    )

    def agregar_mercancia(e):
        datos_nuevos = {
            "nombre": campo_nombre.value,
            "tmercancia_id": dropdown_tmercancia.value,
        }
        page.add(ft.Text(f"Mercancía agregada: {datos_nuevos}"))
        page.update()

    boton_enviar = ft.ElevatedButton(
        text="Agregar Mercancías",
        on_click=agregar_mercancia
    )

    page.add(
        ft.Column(
            [
                ft.Text("Agregar Mercancías", size=24, weight="bold"),
                campo_nombre,
                dropdown_tmercancia,
                boton_enviar
            ]
        )
    )

ft.app(target=main)
