from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy. uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from clients import Client
import os
import sqlite3 as sql
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_name = "restaurantProjectDB.db"
db_path = os.path.join(BASE_DIR, db_name)
conn = sql.connect(db_name, check_same_thread=False)
cursor = conn.cursor()

Window.size = (500, 700)

client = Client()

class HelloWindow(Screen):
    role = ObjectProperty(None)

    def submit_role(self):
        role = self.role.text
        if role == 'Admin' or role == 'User':
            client.role = self.role.text
        else:
            print('Please, choose your role first!')


class SignUpWindow(Screen):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    phone = ObjectProperty(None)
    address = ObjectProperty(None)
    mail = ObjectProperty(None)
    password = ObjectProperty(None)

    def sign_up(self):
        first_name = self.first_name.text
        last_name = self.last_name.text
        phone = self.phone.text
        address = self.address.text
        mail = self.mail.text
        password = self.password.text
        if first_name == '' or last_name == '' or phone == '' \
                or address == '' or mail == '' or password == '':
            print('You did not finish! ')
        else:
            client.c_id += 1
            client.fullname = f'{first_name} {last_name}'
            client.c_phone = phone
            client.c_address = address
            client.c_mail = mail
            client.c_password = password
            cursor.execute(f""" INSERT INTO Clients VALUES 
                                             ({client.c_id}, '{client.fullname}', '{client.c_phone}', '{client.c_address}',
                                              '{client.c_mail}', '{client.c_password}', '{client.role}') """)
            conn.commit()
            print(f"Hello, {client.c_name}!")
            print(f'Hello, {first_name}!\n'
                  f'Thanks for signing up :)')
            exit()


class SignInWindow(Screen):
    mail = ObjectProperty(None)
    password = ObjectProperty(None)

    def sign_in(self):
        mail = self.mail.text
        password = self.password.text

        cursor.execute(f""" SELECT * FROM Clients WHERE Email = '{mail}' AND Password = '{password}' """)
        result = [i for i in cursor.fetchall()][0]

        if mail == '' or password == '':
            print('You did not finish! ')
        elif mail != result[4] or password != result[5]:
            print("Login or password is wrong or you are not signed up:(")
        else:
            print("You signed in!")
            exit()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('Signing.kv')


class SigningApp(App):
    def build(self):
        self.icon = 'icon.png'
        return kv


if __name__ == '__main__':
    sign_app = SigningApp()
    sign_app.run()