import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('sql/test.sqlite')
        self.cursor = self.connection.cursor()

    def get_faculties(self):
        self.cursor.execute("SELECT * FROM faculties")
        return self.cursor.fetchall()

    def get_students_by_average_mark(self):
        self.cursor.execute('''SELECT last_name || ' ' || first_name || ': ' || average_mark 
                            FROM students WHERE average_mark > (
                            SELECT AVG(average_mark) FROM students
                            ORDER BY average_mark
                            )''')
        return self.cursor.fetchall()

    def get_groups_by_faculty(self, faculty):
        self.cursor.execute('''SELECT groups.title, specialities.title FROM groups 
                            LEFT OUTER JOIN specialities
                            ON groups.speciality = specialities.number
                            WHERE specialities.faculty = "{}" 
                            ORDER BY speciality
                            '''.format(faculty))
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
