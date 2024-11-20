import flet as ft

def main(page: ft.Page):
    page.title = "Editar Mercancías"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    datos_mercancia = {"id": 1, "nombre": "Mercancía A", "tmercancia_id": 2}
    datos_tmercancia = [
        {"id": 1, "nombre": "Tipo A"},
        {"id": 2, "nombre": "Tipo B"},
        {"id": 3, "nombre": "Tipo C"},
    ]

    campo_nombre = ft.TextField(label="Nombre", value=datos_mercancia["nombre"])
    
    dropdown_tmercancia = ft.Dropdown(
        label="Tipo de Mercancías",
        options=[ft.dropdown.Option(t["nombre"], value=t["id"]) for t in datos_tmercancia],
        value=datos_mercancia["tmercancia_id"]
    )

    def actualizar_mercancia(e):
        datos_actualizados = {
            "nombre": campo_nombre.value,
            "tmercancia_id": dropdown_tmercancia.value,
        }
        page.add(ft.Text(f"Mercancía actualizada: {datos_actualizados}"))
        page.update()

    boton_enviar = ft.ElevatedButton(
        text="Actualizar Mercancías",
        on_click=actualizar_mercancia
    )

    page.add(
        ft.Column(
            [
                ft.Text("Editar Mercancías", size=24, weight="bold"),
                campo_nombre,
                dropdown_tmercancia,
                boton_enviar
            ]
        )
    )

ft.app(target=main)
