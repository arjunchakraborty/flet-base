import flet as ft
from flet_model import Model

class LoginModel(Model):
    route = 'login'

    # Layout configuration
    vertical_alignment = ft.MainAxisAlignment.CENTER
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
    padding = 20
    spacing = 10

    # UI Components

    username_field = ft.TextField(
        label="Username",
    )
    password_field = ft.TextField(
            label="Password", password=True, can_reveal_password=True
    )

    #required_cred_dlg = 

    controls = [
        ft.Text("Login", size=24),
        ft.Column(
                    controls=[
                        username_field,
                        password_field,
                        ft.OutlinedButton(text="Login", on_click="request_login")
                    ]
                ),
    ]

    def request_login(self, e):
        
        if self.username_field.value == "" or self.password_field.value == "":
            #empty fields show error
            self.controls += ft.AlertDialog(
                            title=ft.Text("Username and Password required!", size=18),
                            open=True,
                        ),

            self.update()
        else:
            #send request and handle response here
            print("sending login request ...")
            print("username : ", self.username_field.value)
            print("password : ", self.password_field.value)
            self.page.go('/home')