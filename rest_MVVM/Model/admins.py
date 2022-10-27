# class Admin represents a admin's account. It has None values by default, but it also has a required register method,
# which allows admin to sign up and change the default setting,
# so that they can operate clients' orders.
# It can be only one unique account for each telephone number.
import os
import sqlite3 as sql


class Admin:
    def __init__(self):
        self.a_id = 0000000000
        self.a_name = None
        self.a_sname = None
        self.a_fullname = None
        self.a_rest = None
        self.a_phone = None
        self.a_password = ''
        self.a_if_host = 0

        self.BASE_DIR = r'C:\Users\Admin\PycharmProjects1\Cross_platform\rest_MVVM\Model'
        self.db_name = "restaurantProjectDB.db"
        self.db_path = os.path.join(self.BASE_DIR, self.db_name)
        self.conn = sql.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def register_admin(self):
        self.cursor.execute(''' SELECT MAX(IDAdmin) FROM Admins ''')
        if self.cursor.fetchall()[0][0] is not None:
            self.a_id = int(self.cursor.fetchall()[0][0])
        else:
            self.a_id += 1

        self.cursor.execute(f""" INSERT INTO Admins VALUES 
                                 ({self.a_id}, '{self.a_fullname}', '{self.a_rest}',
                                  '{self.a_phone}', '{self.a_password}', '{self.a_if_host}') """)
        self.conn.commit()
        print(f'Hello, {self.a_fullname}!\n'
              f'Thanks for signing up :)')