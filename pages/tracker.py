
from .basepage import BasePage
import flet as ft

class TrackerPage(BasePage):
    def __init__(self, route, page):
        self.poop_count = ft.TextField(label="💩 Poop Frequency", keyboard_type=ft.KeyboardType.NUMBER)
        self.poop_consistency = ft.Dropdown(
            label="📊 Consistency (1-7)",
            options=[ft.dropdown.Option(str(i)) for i in range(1, 8)]
        )
        self.med_count = ft.TextField(label="💊 Medication Count", keyboard_type=ft.KeyboardType.NUMBER)
        self.result_display = ft.Text("")

        body = [
            ft.Text("📝 Daily Report", size=20, weight=ft.FontWeight.BOLD),
            self.poop_count,
            self.poop_consistency,
            self.med_count,
            ft.ElevatedButton("Submit", on_click=self.submit_data),
            ft.Divider(),
            self.result_display,
        ]

        super().__init__(route, page, title="Tracker", body_controls=body)

    def submit_data(self, e):
        try:
            poop = int(self.poop_count.value)
            meds = int(self.med_count.value)
            consist = self.poop_consistency.value
            if not consist:
                raise ValueError("Consistency not selected")
            self.result_display.value = (
                f"✅ Poop: {poop} times\n"
                f"📊 Type: {consist}\n"
                f"💊 Meds: {meds} times"
            )
        except:
            self.result_display.value = "⚠️ Please fill all fields correctly."
        self.update()
