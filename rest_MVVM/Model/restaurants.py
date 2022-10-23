from orders import Order
from deliveries import Delivery


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
        if self.got_order:
            self.deliv.got_order = True
        else:
            self.deliv.got_order = False


