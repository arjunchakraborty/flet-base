import flet as ft
from flet_model import Model, Router
from pages import basepage
from pages import home
from pages import tracker


def main(page: ft.Page):
    def route_change(e):
        page.views.clear()
        route = page.route

        if route == "/":
            page.views.append(home.HomePage(route, page))
        elif route == "/tracker":
            page.views.append(tracker.TrackerPage(route, page))
        elif route == "/report":
            page.views.append(basepage.BasePage(route, page, "Report", [ft.Text("📊 Report Coming Soon...")]))
        elif route == "/settings":
            page.views.append(basepage.BasePage(route, page, "Settings", [ft.Text("⚙️ Settings Coming Soon...")]))
        else:
            page.views.append(home.HomePage("/", page))

        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")

ft.app(target=main)
