from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from Cross_platform.rest_MVVM.Model.admins import Admin
from Cross_platform.rest_MVVM.ModelView.SignIn import SignIn

admin = Admin()
sign_in = SignIn()


class SignInAdminWindow(Screen):
    a_phone = ObjectProperty(None)
    a_password = ObjectProperty(None)

    def sign_in_admin(self):
        a_phone = self.a_phone.text
        a_password = self.a_password.text

        sign_in.sign_in_admin(a_phone, a_password)