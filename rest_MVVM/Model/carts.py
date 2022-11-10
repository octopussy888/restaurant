from menus import Menu


class Cart:
    def __init__(self):
        self.menu = Menu()
        self.id_rest = self.menu.id_rest
        self.id_cart = 0
        self.chosen_items = []

    def _del_item(self):
        pass
