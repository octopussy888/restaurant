from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

from kivy.core.window import Window



class SignInGrid(Widget):
    Window.size = (300, 300)
    mail = ObjectProperty(None)
    password = ObjectProperty(None)

    def press(self):
        mail = self.mail.text
        password = self.password.text
        if mail == '' or password == '':
            print('You did not finish! ')
        else:
            print("You signed in!")
            exit()


class SignInApp(App):
    def build(self):
        self.icon = 'icon.png'
        return SignInGrid()


if __name__ == "__main__":
    sign_in_app = SignInApp()
    sign_in_app.run()
