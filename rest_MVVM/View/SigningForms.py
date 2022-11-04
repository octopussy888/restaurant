from kivy.config import Config

Config.set("graphics", "resizable", 0)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window


from Cross_platform.rest_MVVM.Model.clients import Client
from Cross_platform.rest_MVVM.Model.admins import Admin
from Cross_platform.rest_MVVM.ModelView.SignIn import SignIn
from Cross_platform.rest_MVVM.ModelView.SignUp import SignUp


Window.size = (500, 700)

client = Client()
admin = Admin()
sign_in = SignIn()
sign_up = SignUp()


class HelloWindow(Screen):
    role = ObjectProperty(None)

    def submit_role(self):
        role = self.role.text
        if role == 'Admin' or role == 'User':
            client.role = self.role.text
            print(f'Role "{role}" was chosen!')
            self.ids.but_s_in.disabled = False
            self.ids.but_s_up.disabled = False
        else:
            print('Please, choose your role first!')

    def s_up(self):
        role = self.role.text
        if role == 'Admin':
            self.manager.current = 'SignUpAdmin'
        elif role == 'User':
            self.manager.current = 'SignUpClient'

    def s_in(self):
        role = self.role.text
        if role == 'Admin':
            self.manager.current = 'SignInAdmin'
        elif role == 'User':
            self.manager.current = 'SignInClient'


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


class SignInClientWindow(Screen):
    c_mail = ObjectProperty(None)
    c_password = ObjectProperty(None)

    def sign_in_client(self):
        c_mail = self.c_mail.text
        c_password = self.c_password.text

        sign_in.sign_in_client(c_mail, c_password)


class SignInAdminWindow(Screen):
    a_phone = ObjectProperty(None)
    a_password = ObjectProperty(None)

    def sign_in_admin(self):
        a_phone = self.a_phone.text
        a_password = self.a_password.text

        sign_in.sign_in_admin(a_phone, a_password)


class WindowManager(ScreenManager):
    pass


class SigningApp(App):
    def build(self):
        kv = Builder.load_file(r'C:\Users\Admin\PycharmProjects1\Cross_platform\rest_MVVM\View\Signing.kv')
        self.icon = r'C:\Users\Admin\PycharmProjects1\Cross_platform\rest_MVVM\View\icon.png'
        return kv


if __name__ == '__main__':
    sign_app = SigningApp()
    sign_app.run()
