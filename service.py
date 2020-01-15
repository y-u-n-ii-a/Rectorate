from repository import Database


class Service:
    def __init__(self):
        self.database = Database()

    def __del__(self):
        del self.database
