# class Client represents a client's account. It has None values by default, but it also has a register method,
# which allows client to sign up and change the default setting,
# so that when they make an order they don`t need to input their contacts each time.
# It can be only one unique account for each telephone number AND e-mail.
class Client:
    def __init__(self):
        self.c_id = 0000000000
        self.c_name = None
        self.c_phone = None
        self.c_address = None
        self.c_mail = None
        self.delivery_arrived = False

    def register_client(self):
        # registration form
        pass

