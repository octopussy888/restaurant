from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from SignInForm import SignInApp

from kivy.core.window import Window

class SignUpGrid(Widget):
    Window.size = (500, 700)
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    phone = ObjectProperty(None)
    mail = ObjectProperty(None)
    password = ObjectProperty(None)

    def press(self):
        first_name = self.first_name.text
        last_name = self.last_name.text
        phone = self.phone.text
        mail = self.mail.text
        password = self.password.text
        if first_name == '' or last_name == '' or phone == '' \
                or mail == '' or password == '':
            print('You did not finish! ')
        else:
            print(f'Hello, {first_name}!\n'
                  f'Thanks for signing up :)')
            exit()

    def sign_in(self):
        sign_in_app = SignInApp()
        sign_up_app.stop()
        sign_in_app.run()
        exit()


class SignUpApp(App):
    def build(self):
        self.icon = 'icon.png'
        return SignUpGrid()


if __name__ == "__main__":
    sign_up_app = SignUpApp()
    sign_up_app.run()
