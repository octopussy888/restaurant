# class Client represents a client's account. It has None values by default, but it also has a register method,
# which allows client to sign up and change the default setting,
# so that when they make an order they don`t need to input their contacts each time.
# It can be only one unique account for each telephone number AND e-mail.
import os
import sqlite3 as sql


class Client:
    def __init__(self):
        self.c_id = 0000000000
        self.c_name = None
        self.c_sname = None
        self.fullname = None
        self.c_phone = None
        self.c_address = None
        self.c_mail = None
        self.c_password = ''
        self.delivery_arrived = False

        self.BASE_DIR = r'C:\Users\Admin\PycharmProjects1\Cross_platform\rest_MVVM\Model'
        self.db_name = "restaurantProjectDB.db"
        self.db_path = os.path.join(self.BASE_DIR, self.db_name)
        self.conn = sql.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def register_client(self):
        self.cursor.execute(''' SELECT MAX(IDClient) FROM Clients ''')
        self.c_id = int(self.cursor.fetchall()[0][0])
        self.c_id += 1

        self.cursor.execute(f""" INSERT INTO Clients VALUES 
                                                     ({self.c_id}, '{self.fullname}', '{self.c_phone}', '{self.c_address}',
                                                      '{self.c_mail}', '{self.c_password}') """)
        self.conn.commit()
        print(f'Hello, {self.fullname}!\n'
              f'Thanks for signing up :)')

