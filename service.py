from repository import Database


class Service:
    def __init__(self):
        self.database = Database()

    def display_faculties(self):
        faculties = self.database.get_faculties()
        print(faculties)

    def display_students_by_average_mark(self):
        students = self.database.get_students_by_average_mark()
        print(students)

    def display_groups_by_faculty(self, faculty):
        students = self.database.get_groups_by_faculty(faculty)
        print(students)

    def __del__(self):
        del self.database
