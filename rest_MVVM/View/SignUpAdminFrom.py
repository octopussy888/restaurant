from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from Cross_platform.rest_MVVM.Model.admins import Admin
from Cross_platform.rest_MVVM.ModelView.SignUp import SignUp

admin = Admin()
sign_up = SignUp()


class SignUpAdminWindow(Screen):
    a_first_name = ObjectProperty(None)
    a_last_name = ObjectProperty(None)
    a_phone = ObjectProperty(None)
    a_rest = ObjectProperty(None)
    a_password = ObjectProperty(None)

    def sign_up_admin(self):
        a_first_name = self.a_first_name.text
        a_last_name = self.a_last_name.text
        a_phone = self.a_phone.text
        a_rest = self.a_rest.text
        a_password = self.a_password.text
        sign_up.sign_up_admin(a_first_name, a_last_name, a_phone, a_rest, a_password)