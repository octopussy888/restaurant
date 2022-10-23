from restaurants import Restaurant
from dishes import Dishes


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

