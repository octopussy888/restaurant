from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from Cross_platform.rest_MVVM.Model.clients import Client

client = Client()


class HelloWindow(Screen):
    role = ObjectProperty(None)

    def submit_role(self):
        role = self.role.text
        if role == 'Admin' or role == 'User':
            if role == 'User':
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
