import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('sql/test.sqlite')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
