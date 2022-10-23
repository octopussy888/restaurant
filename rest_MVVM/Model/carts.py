from dishes import Dishes


class Cart:
    def __init__(self):
        self.dishes = Dishes()
        self.id_rest = self.dishes.id_rest
        self.id_cart = 0
        self.chosen_items = self.dishes.chosen_items

    def _del_item(self):
        pass
