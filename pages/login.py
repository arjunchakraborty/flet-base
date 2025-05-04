import flet as ft
from flet_model import Model
from utils import build_request, async_build_request

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
                        ft.Row(
                            controls=[
                            ft.OutlinedButton(text="Login", on_click="request_login"),
                            ft.OutlinedButton(text="Sign Up", on_click="sign_up"),
                            ]
                        )
                        
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
            """
            Send request and handle response here
            use utils.build_request or utils.async_build_request to send your requests
            
            data = {"username": self.username_field.value, "password": self.password_field.value}
            login_resp = build_request(self.page, YOUR_FULL_LOGIN_URL, data, authenticated=False)
            token = json.loads(login_resp.text)
            
            #save the token to client storage (refresh and access tokens) 
            for k in token:
                self.page.client_storage.set(k, token[k])
            """
            self.page.go('/home')

    def sign_up(self, e):
        self.page.go('/signup')