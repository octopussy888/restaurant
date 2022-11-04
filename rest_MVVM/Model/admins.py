# class Admin represents a admin's account. It has None values by default, but it also has a required register method,
# which allows admin to sign up and change the default setting,
# so that they can operate clients' orders.
# It can be only one unique account for each telephone number.

from Cross_platform.rest_MVVM.Model.db_queries import DBHelper

class Admin:
    def __init__(self):
        self.a_id = 0000000000
        self.a_name = None
        self.a_sname = None
        self.a_fullname = None
        self.a_rest = None
        self.a_phone = None
        self.a_password = ''
        self.a_if_host = 0

        self.db_helper = DBHelper()

    def register_admin(self):
        self.a_id = self.db_helper.register_admin(self.a_fullname, self.a_rest, self.a_phone,
                                                  self.a_password, self.a_if_host)
        print(f'Hello, {self.a_fullname}!\n'
              f'Thanks for signing up :)')