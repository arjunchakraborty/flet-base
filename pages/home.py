import flet as ft
from flet_model import Model

class HomeModel(Model):
    route = 'home'

    # Layout configuration
    vertical_alignment = ft.MainAxisAlignment.CENTER
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
    padding = 20
    spacing = 10

    # UI Components
    appbar = ft.AppBar(
        title=ft.Text("Home"),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST
    )

    controls = [
        ft.Text("Welcome to Home Page", size=24),
        ft.ElevatedButton("Go to login", on_click="navigate_to_login")
    ]

    def navigate_to_login(self, e):
        self.page.go('/login')