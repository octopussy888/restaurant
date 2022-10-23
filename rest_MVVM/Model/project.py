import datetime as dt
import numpy as np


# class restaurant only exists to show restaurant's contacts,
# cuisine and showing interactive menu after clicking on its name in app, where you can choose what to order.
# This class's instances are kept in db. it is the main content of app
class Restaurant:
    def __init__(self):
        self.order = Order()
        self.deliv = Delivery()
        self.id_rest = 0000000000
        self.r_name = ''
        self.r_contacts = {'Address': '', 'Phone': ''}
        self.r_cuisine = []
        self.chosen_items = ''
        self.got_order = False

    def check_got_order(self):
        pass


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


class Cart(Restaurant):
    def __init__(self):
        super().__init__()
        self.dishes = Dishes()
        self.id_rest = self.dishes.id_rest
        self.id_cart = 0
        self.chosen_items = self.dishes.chosen_items

    def _del_item(self):
        pass


# class order is used to make an order. it gives a blank to fill clients name, phone, mail and address
# (if not filled by signing up)
class Order:
    def __init__(self):
        self.cart = Cart()
        self.client = Client()
        self.rest = Restaurant()
        self.c_name = self.client.c_name
        self.c_phone = self.client.c_phone
        self.c_address = self.client.c_address
        self.c_mail = self.client.c_mail
        self.o_order = self.cart.chosen_items
        self.rest = self.cart.id_rest
        self.o_datetime_ordered = dt.datetime.now()
        self.o_datetime_end = dt.datetime.now() + dt.timedelta(hours=1)
        self.o_paid = False

    def finish_order(self):
        pass

    def pay_order(self):
        pass


class Delivery:
    def __init__(self):
        self.rest = Restaurant()
        self.order = Order()
        self.client = Client()
        self.got_order = self.rest.check_got_order()
        self.time_ready = None
        self.time = None
        self.start_order = False
        self._end_order = False
        self.start_deliv = False
        self.order_arrived = self.client.delivery_arrived

    def get_time_start(self):
        pass

    def _check_start_order(self):
        pass

    def _check_end_order(self):
        pass

    def _check_delivery_arrived(self):
        pass

    def _del_order(self):
        pass


class Menu:
    def __init__(self):
        self.rest = Restaurant()
        self.dishes = Dishes()
        self.id_rest = self.rest.id_rest
        self.gen_names = []
        self.chosen_gen_name = ''

    def _get_gen_names(self):
        pass

    def _check_gen_name(self):
        pass

    def search_menu(self):
        self.dishes.display_dishes()


class Dishes:
    def __init__(self):
        self.menu = Menu()
        self.id_rest = self.menu.id_rest
        self.gen_name = self.menu.chosen_gen_name
        self.dishes = np.array([[]]).reshape(-1, 5)     # template: name, ingredient, weight, price, time to cook
        self.chosen_items = np.array([[]]).reshape(-1, 5)

    def display_dishes(self):
        pass

    def check_chosen_items(self):
        pass

