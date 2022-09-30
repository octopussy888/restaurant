import datetime as dt


# class restaurant only exists to show restaurant's contacts,
# cuisine and showing interactive menu after clicking on its name in app, where you can choose what to order.
# This class's instances are kept in db. it is the main content of app
class Restaurant:
    def __init__(self, r_name, r_contacts, r_cuisine, menu, chosen_items):
        self.r_name = r_name
        self.r_contacts = r_contacts  # dict with two keys: address and phone
        self.r_cuisine = r_cuisine  # list of cuisines
        self.menu = menu  # dict where keys are general topics, values are names of dishes
        self.chosen_items = chosen_items

    def choose_items(self):
        pass


rest_name = input()
rest_contacts = [{}]
rest_cuisine = []
rest_menu = {}
rest_ch_items = []
rest = Restaurant(rest_name, rest_contacts, rest_cuisine, rest_menu, rest_ch_items)


# class Client represents a client's account. It has None values by default, but it also has a register method,
# which allows client to sign up and change the default setting,
# so that when they make an order they don`t need to input their contacts each time.
# It can be only one unique account for each telephone number AND e-mail.
class Client:
    def __init__(self, c_name, c_phone, c_address, c_mail):
        self.c_name = c_name
        self.c_phone = c_phone
        self.c_address = c_address
        self.c_mail = c_mail

    def _register_client(self):
        pass


new_client = Client(None, None, None, None)


class Cart(Restaurant):
    def __init__(self, chosen_items):
        super().__init__(chosen_items)
        self.chosen_items = rest.choose_items()

    def _del_item(self):
        pass


cart = Cart(None)


# class order is used to make an order. it gives a blank to fill clients name, phone, mail and address
# (if not filled by signing up)
class Order(Client, Cart):
    def __init__(self, o_order, c_name, c_phone, c_address, c_mail, o_time, o_date):
        super(Client).__init__(c_name, c_phone, c_address, c_mail)
        self.c_name = new_client.c_name
        self.c_phone = new_client.c_phone
        self.c_address = new_client.c_address
        self.c_mail = new_client.c_mail
        self.o_order = o_order
        self.o_time = o_time
        self.o_date = o_date

    def make_order(self):
        pass


o_order = cart.chosen_items
o_time = dt.datetime.now().time() + dt.timedelta(hours=1)
o_date = dt.datetime.now().date()
new_order = Order(o_order, new_client.c_name, new_client.c_phone,
                  new_client.c_address, new_client.c_mail, o_time, o_date)


class Delivery(Order):
    def __init__(self, o_order, c_name, c_phone, c_address, c_mail, time, date):
        super().__init__(o_order, c_name, c_phone, c_address, c_mail, time, date)


deliv = Delivery(new_order.o_order, new_client.c_name, new_client.c_phone,
                  new_client.c_address, new_client.c_mail, new_order.o_time, new_order.o_date)

