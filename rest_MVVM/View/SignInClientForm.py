from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from Cross_platform.rest_MVVM.Model.clients import Client
from Cross_platform.rest_MVVM.ModelView.SignIn import SignIn

client = Client()
sign_in = SignIn()


class SignInClientWindow(Screen):
    c_mail = ObjectProperty(None)
    c_password = ObjectProperty(None)

    def sign_in_client(self):
        c_mail = self.c_mail.text
        c_password = self.c_password.text

        sign_in.sign_in_client(c_mail, c_password)

