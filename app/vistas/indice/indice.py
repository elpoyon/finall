import flet as ft

def main(page: ft.Page):
    page.title = "Bejarano´s Transport"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Image(src="static/logo.png", width=100, height=100),
                        ft.Text("Bejarano´s Transport", size=24, weight="bold"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Inicio", on_click=lambda _: page.add(ft.Text("Inicio"))),
                        ft.ElevatedButton("Servicios", on_click=lambda _: page.add(ft.Text("Servicios"))),
                        ft.ElevatedButton("Nosotros", on_click=lambda _: page.add(ft.Text("Nosotros"))),
                        ft.ElevatedButton("Flota", on_click=lambda _: page.add(ft.Text("Flota"))),
                        ft.Dropdown(
                            label="Gestión",
                            options=[
                                ft.DropdownOption("Conductores"),
                                ft.DropdownOption("Vehículos"),
                                ft.DropdownOption("Tipos de Mercancías"),
                                ft.DropdownOption("Mercancías"),
                                ft.DropdownOption("Orígenes"),
                                ft.DropdownOption("Destinos"),
                                ft.DropdownOption("Clientes"),
                                ft.DropdownOption("Órdenes"),
                            ],
                        ),
                        ft.ElevatedButton("Login", on_click=lambda _: page.add(ft.Text("Login"))),
                        ft.ElevatedButton("Logout", on_click=lambda _: page.add(ft.Text("Logout"))),
                    ],
                    spacing=10,
                ),
                ft.Header(
                    title="Inicio",
                    description="Tu carga en las mejores manos. Entrega segura y confiable en todo el país.",
                ),
                ft.Section(
                    title="Servicios",
                    content=ft.Column(
                        [
                            ft.Box(
                                title="Nivel Nacional",
                                description="Servicio de transporte de mercancías a nivel nacional, cualquier tipo de mercancía no viva.",
                            ),
                            ft.Box(
                                title="Nivel Urbano",
                                description="Servicio de transporte de mercancías a nivel municipal o intermunicipal, cualquier tipo de mercancía no viva.",
                            ),
                        ]
                    ),
                ),
                ft.Section(
                    title="Nosotros",
                    content=ft.Text(
                        "Somos una empresa de transporte comprometida con la excelencia y la satisfacción de nuestros clientes. Nuestro equipo especializado ofrece soluciones eficaces para cumplir con la expectativa de cada cliente."
                    ),
                ),
                ft.Section(
                    title="Flota",
                    content=ft.Text("Nuestra flota es moderna, segura y eficiente, lista para atender cualquier necesidad de transporte."),
                ),
                ft.Section(
                    title="Misión",
                    content=ft.Text(
                        "Ofrecer soluciones de transporte confiables, seguras y eficientes de acuerdo a la necesidad de nuestros clientes. Nuestro compromiso es prestar un servicio integral y amable, en conjunto con un equipo dispuesto a brindar soluciones a la medida."
                    ),
                ),
                ft.Section(
                    title="Visión",
                    content=ft.Text(
                        "Transformar la industria del transporte de mercancías a través de soluciones innovadoras y a la medida de cada cliente. También ser la empresa líder de transporte de mercancías a nivel nacional, cumpliendo con las expectativas de nuestros clientes."
                    ),
                ),
                ft.Footer(
                    content="©2024 Samuel Bejarano. Todos los derechos reservados. Ninguna parte de este contenido, ya sea texto, imagen o cualquier otro material, puede ser reproducida, distribuida, transmitida o almacenada de ninguna forma ni por ningún medio, sin el permiso previo por escrito del autor."
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    )

ft.app(target=main)
