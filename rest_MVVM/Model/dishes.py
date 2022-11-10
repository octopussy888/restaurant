from menus import Menu
import numpy as np

class Dishes:
    def __init__(self):
        self.menu = Menu()
        self.id_rest = self.menu.id_rest
        self.gen_name = self.menu.chosen_gen_name
        self.dishes = np.array([[]]).reshape(-1, 5)     # template: name, ingredient, weight, price, time to cook
        self.chosen_items = np.array([[]]).reshape(-1, 5)

    def display_info_about_dish(self):
        pass

