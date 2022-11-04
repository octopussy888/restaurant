import datetime as dt

# from restaurants import Restaurant
from clients import Client
from admins import Admin

from Cross_platform.rest_MVVM.View.SigningForms import SigningApp
from Cross_platform.rest_MVVM.Model.db_queries import DBHelper


class Project:
    def __init__(self):
        self.client = Client()
        self.admin = Admin()
        self.db_helper = DBHelper()
        self.table_names = []
        self.col_names = []

    def run(self):
        self.register()

    def choose_restaurant(self):
        self.col_names = []
        rest_result = self.db_helper.find_restaurants()
        for t in range(len(rest_result)):
            self.col_names.append(rest_result[t][1])

    def register(self):
        sign_app = SigningApp()
        sign_app.run()


if __name__ == '__main__':
    project = Project()
    project.run()

