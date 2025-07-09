import flet as ft
from flet_model import Model, route
import flet as ft
import openai
import os

from .basepage import BasePage


# Set your OpenAI API key securely
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace this with your key


class HomePage(BasePage):
  
  def __init__(self, route, page):
        body = list([ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Home Page", size=22),
                            ]
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        visible=True,
                    )])
        
        super().__init__(route, page, title="Home", body_controls=body)