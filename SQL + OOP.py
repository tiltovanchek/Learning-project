import sqlite3

class DB():

    def __init__(self):
        self.connect = sqlite3.connect('sqlite_python.db')
        self.cursor = self.connect.cursor()
        print("База данных подключена к SQLite \n")

    def close(self):
        self.connect.close()

    def execute(self, new_data):
        self.cursor.execute(new_data)

    def commit(self):
        self.connect.commit()

    def insert_in_students(self, many_new_data):
        self.cursor.executemany('INSERT or REPLACE INTO Students VALUES(?, ?, ?, ?, ?)', many_new_data)
        self.commit()
        print('Данные добавлены в табицу Students \n')

    def insert_in_courses(self, many_new_data):
        self.cursor.executemany('INSERT or REPLACE INTO Courses VALUES(?, ?, ?, ?)', many_new_data)
        self.commit()
        print('Данные добавлены в таблицу Courses \n')

    def insert_in_student_courses(self, many_new_data):
        self.cursor.executemany('INSERT or IGNORE INTO Student_courses VALUES(?, ?)', many_new_data)
        self.commit()
        print('Данные добавлены в таблицу Student_courses\n')

    def create_table_students(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                surname TEXT NOT NULL,
                                age INTEGER NOT NULL,
                                city TEXT NOT NULL);
                            ''')
        self.commit()
        print("Таблица Students создана \n")

    def create_table_courses(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                time_start TEXT NOT NULL,
                                time_end TEXT NOT NULL);
                            ''')
        self.commit()
        print("Таблица Courses создана \n")

    def create_table_student_courses(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses (
                               student_id INTEGER NOT NULL,
                               course_id INTEGER NOT NULL,
                               FOREIGN KEY (student_id) REFERENCES Students (id),
                               FOREIGN KEY (course_id) REFERENCES Courses (id),
                               UNIQUE (student_id, course_id));
                            ''')
        self.commit()
        print("Таблица Student_courses создана \n")

    def select_by_age(self, age):
        print(f'Все студенты старше {age}:')
        for string in self.cursor.execute(f'''
                                              SELECT Students.name, Students.surname
                                              FROM Students
                                              WHERE Students.age > {str(age)}
                                           ''').fetchall():
            print(string[0], string[1])

    def select_by_course(self, course):
        print(f'Все студенты, которые проходят курс по "{course}":')
        for string in self.cursor.execute(f'''
                                              SELECT Students.name, Students.surname
                                              FROM Student_courses
                                              JOIN Students ON Student_courses.student_id = Students.id
                                              JOIN Courses ON Student_courses.course_id = Courses.id
                                              WHERE Courses.name = "{course}"
                                           ''').fetchall():
            print(string[0], string[1])

    def select_by_course_and_city(self, course, city):
        print(f'Все студенты, которые проходят курс по "{course}" и живут в "{city}":')
        for string in self.cursor.execute(f'''
                                              SELECT Students.name, Students.surname
                                              FROM Student_courses
                                              JOIN Students ON Student_courses.student_id = Students.id
                                              JOIN Courses ON Student_courses.course_id = Courses.id
                                              WHERE Courses.name = "{course}" AND Students.city = "{city}"
                                           ''').fetchall():
            print(string[0], string[1])

try:
    database = DB()
    database.create_table_students()
    database.create_table_courses()
    database.create_table_student_courses()

    data_Courses = [(1, 'python', '21-07-21', '21-08-21'),
                   (2, 'java', '13-07-21', '16-08-21')]
    data_Students = [(1, 'Max', 'Brooks', 24, 'Spb'),
                     (2, 'John', 'Stones', 15, 'Spb'),
                     (3, 'Andy', 'Wings', 45, 'Manchester'),
                     (4, 'Kate', 'Brooks', 34, 'Spb')]
    data_Student_courses = [(1, 1),
                            (2, 1),
                            (3, 1),
                            (4, 2)]

    database.insert_in_students(data_Students)
    database.insert_in_courses(data_Courses)
    database.insert_in_student_courses(data_Student_courses)

    database.select_by_age(40)
    database.select_by_course('java')
    database.select_by_course_and_city('python', 'Spb')

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (database.connect):
        database.connect.close()
        print("Соединение с SQLite закрыто")
