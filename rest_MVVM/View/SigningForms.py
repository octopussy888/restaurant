from kivy.config import Config

Config.set("graphics", "resizable", 0)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

Window.size = (500, 700)

from Cross_platform.rest_MVVM.View.HelloWindowForm import HelloWindow
from Cross_platform.rest_MVVM.View.SignInAdminForm import SignInAdminWindow
from Cross_platform.rest_MVVM.View.SignUpAdminForm import SignUpAdminWindow
from Cross_platform.rest_MVVM.View.SignInClientForm import SignInClientWindow
from Cross_platform.rest_MVVM.View.SignUpClientForm import SignUpClientWindow
from Cross_platform.rest_MVVM.View.MainScreenForm import MainWindow


class WindowManager(ScreenManager):
    pass


class SigningApp(App):
    def build(self):
        kv = Builder.load_file(r'C:\Users\Admin\PycharmProjects1\Cross_platform\rest_MVVM\View\Signing.kv')
        self.icon = r'C:\Users\Admin\PycharmProjects1\Cross_platform\rest_MVVM\View\pics\icon.png'
        return kv


if __name__ == '__main__':
    sign_app = SigningApp()
    sign_app.run()
