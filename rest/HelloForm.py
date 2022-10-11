from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from SignUpForm import SignUpApp

from kivy.core.window import Window

Window.size = (500, 400)

class HelloGrid(Widget):
    role = ObjectProperty(None)

    def sign_up(self):
        role = self.role.text
        if role == 'Admin' or role == 'User':
            sign_up_app = SignUpApp()
            hello_app.stop()
            sign_up_app.run()
            exit()
        else:
            print('Please, choose your role first!')


class HelloApp(App):
    def build(self):
        self.icon = 'icon.png'
        return HelloGrid()


if __name__ == "__main__":
    hello_app = HelloApp()
    hello_app.run()
