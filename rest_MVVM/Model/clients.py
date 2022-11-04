# class Client represents a client's account. It has None values by default, but it also has a register method,
# which allows client to sign up and change the default setting,
# so that when they make an order they don`t need to input their contacts each time.
# It can be only one unique account for each telephone number AND e-mail.

from Cross_platform.rest_MVVM.Model.db_queries import DBHelper


class Client:
    def __init__(self):
        self.c_id = 0000000000
        self.c_name = None
        self.c_sname = None
        self.fullname = None
        self.c_phone = None
        self.c_address = None
        self.c_mail = None
        self.c_password = ''
        self.delivery_arrived = False

        self.db_helper = DBHelper()

    def register_client(self):
        self.c_id = self.db_helper.register_client(self.fullname, self.c_phone, self.c_address,
                                                   self.c_mail, self.c_password)
        print(f'Hello, {self.fullname}!\n')

