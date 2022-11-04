import sqlite3 as sql
import os


class DBHelper:
    def __init__(self):
        self.BASE_DIR = r'C:\Users\Admin\PycharmProjects1\Cross_platform\rest_MVVM\Model'
        self.db_name = "restaurantProjectDB.db"
        self.db_path = os.path.join(self.BASE_DIR, self.db_name)
        self.conn = sql.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def login_check_client(self, c_mail, c_password):
        self.cursor.execute(f""" SELECT * FROM Clients WHERE Email = '{c_mail}' AND Password = '{c_password}' """)
        l_c_result = [i for i in self.cursor.fetchall()][0]
        return l_c_result

    def login_check_admin(self, a_phone, a_password):
        self.cursor.execute(f""" SELECT * FROM Admins WHERE Phone = '{a_phone}' AND Password = '{a_password}' """)
        l_a_result = [i for i in self.cursor.fetchall()]
        return l_a_result[0]

    def find_restaurants(self):
        self.cursor.execute(f""" PRAGMA table_info(Restaurants) """)
        rest_result = self.cursor.fetchall()
        return rest_result

    def register_client(self, fullname, c_phone, c_address, c_mail, c_password):
        self.cursor.execute(''' SELECT MAX(IDClient) FROM Clients ''')
        c_id = int(self.cursor.fetchall()[0][0])
        c_id += 1

        self.cursor.execute(f""" INSERT INTO Clients VALUES 
                                                     ({c_id}, '{fullname}', '{c_phone}', '{c_address}',
                                                      '{c_mail}', '{c_password}') """)
        self.conn.commit()
        return c_id

    def register_admin(self, a_fullname, a_rest, a_phone, a_password, a_if_host):
        self.cursor.execute(''' SELECT MAX(IDAdmin) FROM Admins ''')
        a_id = int(self.cursor.fetchall()[0][0])
        a_id += 1

        self.cursor.execute(f""" INSERT INTO Admins VALUES 
                                 ({a_id}, '{a_fullname}', '{a_rest}',
                                  '{a_phone}', '{a_password}', '{a_if_host}') """)
        self.conn.commit()
        return a_id
