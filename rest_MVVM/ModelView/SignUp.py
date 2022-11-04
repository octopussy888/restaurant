from Cross_platform.rest_MVVM.Model.clients import Client
from Cross_platform.rest_MVVM.Model.admins import Admin


class SignUp:
    def __init__(self):
        self.client = Client()
        self.admin = Admin()

    def sign_up_client(self, c_first_name, c_last_name, c_phone, c_address, c_mail, c_password):
        if c_first_name == '' or c_last_name == '' or c_phone == '' \
                or c_address == '' or c_mail == '' or c_password == '':
            print('You did not finish! ')
        else:
            self.client.fullname = f'{c_first_name} {c_last_name}'
            self.client.c_phone = c_phone
            self.client.c_address = c_address
            self.client.c_mail = c_mail
            self.client.c_password = c_password
            self.client.register_client()
            print('Successfully signed up!')
            exit()

    def sign_up_admin(self, a_first_name, a_last_name, a_phone, a_rest, a_password):
        if a_first_name == '' or a_last_name == '' or a_phone == '' \
                or a_rest == '' or a_password == '':
            print('You did not finish! ')
        else:
            self.admin.a_fullname = f'{a_first_name} {a_last_name}'
            self.admin.a_phone = a_phone
            self.admin.a_rest = a_rest
            self.admin.a_password = a_password
            if a_rest == 'Host':
                self.admin.a_if_host = 1
                self.admin.a_rest = None
            self.admin.register_admin()
            print('Successfully signed up!')
            exit()
