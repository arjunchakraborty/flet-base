import flet as ft
from flet_model import Model, Router


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
        ft.ElevatedButton("Go to Profile", on_click="navigate_to_profile")
    ]

    def navigate_to_profile(self, e):
        self.page.go('/home/profile')


class ProfileModel(Model):
    route = 'profile'

    # Layout configuration
    vertical_alignment = ft.MainAxisAlignment.CENTER
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
    padding = 20
    spacing = 10

    # UI Components
    appbar = ft.AppBar(
        title=ft.Text("Profile"),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST
    )

    controls = [
        ft.Text("Welcome to Profile Page", size=24),
    ]


def main(page: ft.Page):
    page.title = "Flet Model Demo"
    Router(
        {'home': HomeModel(page)},
        {'profile': ProfileModel(page)},
    )
    page.go(page.route)


ft.app(target=main)