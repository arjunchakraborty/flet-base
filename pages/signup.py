import flet as ft
from flet_model import Model

class SignUpModel(Model):
    route = 'signup'

    # Layout configuration
    vertical_alignment = ft.MainAxisAlignment.CENTER
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
    padding = 20
    spacing = 10

    # UI Components
    appbar = ft.AppBar(
        title=ft.Text("Sign Up"),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST
    )

    controls = [
        ft.Text("Sign Up Page", size=24),
    ]