import flet as ft

class BasePage(ft.View):

    def __init__(self, route, page, title, body_controls: list):
        super().__init__(route)
        # Layout configuration
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = 20
        self.spacing = 10
        self.page = page
        self.appbar = ft.AppBar(title=ft.Text(title))
        self.controls = [ft.Column(body_controls, expand=True)]
        self.bottom = self._bottom_navigation()

    def _bottom_navigation(self):
        return ft.BottomAppBar(
            ft.Row(
                [
                    ft.IconButton(ft.icons.HOME, tooltip="Home", on_click=lambda _: self.page.go("/")),
                    ft.IconButton(ft.icons.FAVORITE, tooltip="Tracker", on_click=lambda _: self.page.go("/tracker")),
                    ft.IconButton(ft.icons.INSIGHTS, tooltip="Report", on_click=lambda _: self.page.go("/report")),
                    ft.IconButton(ft.icons.SETTINGS, tooltip="Settings", on_click=lambda _: self.page.go("/settings")),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            )
        )
