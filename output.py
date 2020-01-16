from service import Service

service = Service()

service.display_faculties()

service.display_students_by_average_mark()

service.display_groups_by_faculty(input('Enter the faculty name: '))

del service
