import datetime as dt
import sqlite3 as sql
import os
# from restaurants import Restaurant
from clients import Client


class DBHelper:
    def __init__(self):
        self.client = Client()
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db_name = "restaurantProjectDB.db"
        self.db_path = os.path.join(self.BASE_DIR, self.db_name)
        self.conn = sql.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.table_names = []
        self.col_names = []

    def run(self):
        self._find_table_names()

    def _find_table_names(self):
        self.cursor.execute(""" SELECT name FROM sqlite_master WHERE type='table' """)
        for i in self.cursor.fetchall():
            self.table_names.append(i[0])
        self.choose_restaurant()

    def choose_restaurant(self):
        self.col_names = []
        self.cursor.execute(f""" PRAGMA table_info(Restaurants) """)
        result = self.cursor.fetchall()
        for t in range(len(result)):
            self.col_names.append(result[t][1])
        print(self.col_names)

    def register_client(self):
        self.client.register_client()
        # write clients' data to a db


if __name__ == '__main__':
    db_helper = DBHelper()
    db_helper.run()

