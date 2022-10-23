import datetime as dt
from orders import Order
from restaurants import Restaurant
from clients import Client


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
        time_cook = []
        for i in self.order.o_order:
            time_cook.append(i[4])
        self.time_ready = max(int(time_cook))
        self.time = self.order.o_datetime_end - \
                    dt.timedelta(minutes=self.time_ready) - \
                    dt.timedelta(minutes=35)

    def _check_start_order(self):
        if self.got_order and dt.datetime.now() == self.time:
            self.start_order = True
            print(f"Approximate time ready: {self.time_ready}")

    def _check_end_order(self):
        if self.start_order and dt.datetime.now() == self.time+\
                dt.timedelta(minutes=self.time_ready):
            self.end_order = True
            self.start_deliv = True

    def _check_delivery_arrived(self):
        if self.order_arrived:
            self._del_order()

    def _del_order(self):
        pass
