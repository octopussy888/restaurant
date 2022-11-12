from Cross_platform.rest_MVVM.Model.clients import Client
from Cross_platform.rest_MVVM.Model.admins import Admin
from Cross_platform.rest_MVVM.Model.db_queries import DBHelper


class SignIn:
    def __init__(self):
        self.db_helper = DBHelper()

    def sign_in_client(self, c_mail, c_password):

        l_c_result = self.db_helper.login_check_client(c_mail, c_password)

        if c_mail == '' or c_password == '':
            print('You did not finish! ')
        elif not l_c_result:
            print("There is no such user. Please, check if you're signed up.")
        elif c_password != l_c_result[5]:
            print("Login or password is wrong. Please, try again!")
        else:
            print("You signed in!")
            # exit()

    def sign_in_admin(self, a_phone, a_password):

        l_a_result = self.db_helper.login_check_admin(a_phone, a_password)

        if a_phone == '' or a_password == '':
            print('You did not finish! ')
        elif not l_a_result:
            print("There is no such admin. Please, check if you're signed up.")
        elif a_password != l_a_result[4]:
            print("Login or password is wrong. Please, try again!")
        else:
            print("You signed in!")
            # exit()
