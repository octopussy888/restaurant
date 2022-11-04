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
import os
import sqlite3 as sql

BASE_DIR = r'C:\Users\Admin\PycharmProjects1\Cross_platform\rest_MVVM\Model'
db_name = "restaurantProjectDB.db"
db_path = os.path.join(BASE_DIR, db_name)
conn = sql.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

Window.size = (500, 700)

client = Client()
admin = Admin()


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
        if c_first_name == '' or c_last_name == '' or c_phone == '' \
                or c_address == '' or c_mail == '' or c_password == '':
            print('You did not finish! ')
        else:
            client.fullname = f'{c_first_name} {c_last_name}'
            client.c_phone = c_phone
            client.c_address = c_address
            client.c_mail = c_mail
            client.c_password = c_password
            client.register_client()
            print('Successfully signed up!')
            exit()

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
        if a_first_name == '' or a_last_name == '' or a_phone == '' \
                or a_rest == '' or a_password == '':
            print('You did not finish! ')
        else:
            admin.a_fullname = f'{a_first_name} {a_last_name}'
            admin.a_phone = a_phone
            admin.a_rest = a_rest
            admin.a_password = a_password
            if a_rest == 'Host':
                admin.a_if_host = 1
                admin.a_rest = None
            admin.register_admin()
            print('Successfully signed up!')
            exit()


class SignInClientWindow(Screen):
    c_mail = ObjectProperty(None)
    c_password = ObjectProperty(None)

    def sign_in_client(self):
        c_mail = self.c_mail.text
        c_password = self.c_password.text

        cursor.execute(f""" SELECT * FROM Clients WHERE Email = '{c_mail}' AND Password = '{c_password}' """)
        result = [i for i in cursor.fetchall()][0]

        if c_mail == '' or c_password == '':
            print('You did not finish! ')
        elif c_mail != result[4] or c_password != result[5]:
            print("Login or password is wrong or you are not signed up:(")
        else:
            print("You signed in!")
            exit()


class SignInAdminWindow(Screen):
    a_phone = ObjectProperty(None)
    a_password = ObjectProperty(None)

    def sign_in_admin(self):
        a_phone = self.a_phone.text
        a_password = self.a_password.text

        cursor.execute(f""" SELECT * FROM Admins WHERE Email = '{a_phone}' AND Password = '{a_password}' """)
        result = [i for i in cursor.fetchall()][0]

        if a_phone == '' or a_password == '':
            print('You did not finish! ')
        elif a_phone != result[3] or a_password != result[4]:
            print("Login or password is wrong or you are not signed up:(")
        else:
            print("You signed in!")
            exit()


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
