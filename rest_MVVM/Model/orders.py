import datetime as dt
from clients import Client
from carts import Cart
from restaurants import Restaurant


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

    def delete_order(self):
        pass

    def pay_order(self):
        if not self.o_paid:
            pass
        if self.o_paid:
            self.rest.got_order = True
