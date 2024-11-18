import flet as ft
import requests

BASE_URL = "http://127.0.0.1:5000/TMercanciasAsync"

def main(page: ft.Page):
    page.title= "Gestión de MErcancías"
    page.padding = 20
    
    name_input = ft.TextField(label="Nombre de la mercancía", width=300)
    message_label = ft.Text(value="", color="green")
    tmercancias_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
        ],
        rows=[]
    )
    
    def load_data():
        try:
            response = requests.get(f"{BASE_URL}/index")
            response.raise_for_status()
            data = response.json()
            tmercancias_table.rows.clear()
            for item in data:
                tmercancias_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(item["id"]))),
                            ft.DataCell(ft.Text(item["nombre"])),
                        ]
                    )
                )
            page.update()
            
        except Exception as e:
            message_label.value = f"Error al cargar datos: {e}"
            message_label.color = "red"
            page.update()
            
    def add_tmercancia(e):
            
        try:
            payload = {"nombre": name_input.value}
            resposnse = requests.post(f"{BASE_URL}/add",json=payload)
            resposnse.raise_for_status()
            message_label.value = "¡Mercancia agregada exitosamente!"
            message_label.color = "green"
            name_input.value = ""
            load_data()
            
        except Exception as e:
            message_label.value = f"Error al agregar mercancias"
            message_label.color = "red"
        page.update()
        
    def delete_tmercancia(e):
        """Elimina una mercancia seleccionada"""
        try:
            if not tmercancias_table.selected_rows:
                message_label.value = "selecciona una mercancia para eliminar"
                message_label.color = "red"
                page.update()
                return
            selected_id = tmercancias_table.slected_rows[0].cells[0].content.value
            response = requests.delete(f"{BASE_URL}/delete/{selected_id}")
            response.raise_for_status()
            message_label.value = "¡Mercancia eliminada exitosamente!"
            message_label.color= "green"
            load_data()
        except Exception as e:    
            message_label.value = f"Error al eliminar mercancía: {e}"
            message_label.color = "red"
        page.update()
        
    
    add_button = ft.ElevatedButton(text="Agregar",on_click=add_tmercancia)
    delete_button = ft.ElevatedButton(text="Eliminar",on_click=delete_tmercancia)
    page.add(
        ft.Row([name_input, add_button]),
        ft.Row([delete_button]),
        tmercancias_table,
        message_label
    )
    
ft.app(target=main) 