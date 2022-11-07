from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from Cross_platform.rest_MVVM.Model.clients import Client
from Cross_platform.rest_MVVM.ModelView.SignUp import SignUp

client = Client()
sign_up = SignUp()


class SignUpClientWindow(Screen):
    c_first_name = ObjectProperty(None)
    c_last_name = ObjectProperty(None)
    c_phone = ObjectProperty(None)
    c_address = ObjectProperty(None)
    c_mail = ObjectProperty(None)
    c_password = ObjectProperty(None)

    def sign_up_client(self):
        c_first_name = self.c_first_name.text
        c_last_name = self.c_last_name.text
        c_phone = self.c_phone.text
        c_address = self.c_address.text
        c_mail = self.c_mail.text
        c_password = self.c_password.text
        sign_up.sign_up_client(c_first_name, c_last_name, c_phone, c_address, c_mail, c_password)


