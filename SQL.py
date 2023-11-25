"""
Задача 1

С помощью библиотеки sqlite3 создайте базу данных и подключитесь к ней.
Создайте в ней таблицы:


Students
Поля: (id, name, surname, age, city)


Courses
Поля: (id, name, time_start, time_end)

Student_courses
Поля: (student_id, course_id)
course_id - id курса, который проходит студет (Foreign key)
student_id - id студента, который проходит курс (Foreign key)

Задача 2

Добавьте в таблицы объекты:
Courses:
(1, 'python', 21.07.21, 21.08.21)
(2, 'java', 13.07.21, 16.08.21)


Students:
(1, 'Max', 'Brooks', 24, 'Spb')
(2, 'John', 'Stones', 15, 'Spb')
(3, 'Andy', 'Wings', 45, 'Manhester')
(4, 'Kate', 'Brooks', 34, 'Spb')
Student_courses:
(1, 1)
(2, 1)
(3, 1)
(4, 2)

Напишите запросы, чтобы получить:
1. Всех студентов старше 30 лет.
2. Всех студентов, которые проходят курс по python.
3. Всех студентов, которые проходят курс по python и из Spb.

Задача 3

Реализуйте код задачи 1 и 2 в виде класса.
Добавьте тестирование функционала
Сохраните все в git

!!! При запуске проверяйте, если база уже создана и заполнена, то не следует ее заполнять второй раз.

Создайте функцию внутри класса которая позволяет быстро выполнять произвольны запрос без дублирования кода SQL
"""

import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Students (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    surname TEXT NOT NULL,
                                    age INTEGER NOT NULL,
                                    city TEXT NOT NULL);
                                '''

    sqlite_create_table_query1 = '''CREATE TABLE IF NOT EXISTS Courses (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    time_start TEXT NOT NULL,
                                    time_end TEXT NOT NULL);
                                '''
    sqlite_create_table_query2 = '''CREATE TABLE IF NOT EXISTS Student_courses (
                                    student_id INTEGER NOT NULL,
                                    course_id INTEGER NOT NULL,
                                    FOREIGN KEY (student_id) REFERENCES Students (id),
                                    FOREIGN KEY (course_id) REFERENCES Courses (id),
                                    UNIQUE (student_id, course_id));
                                '''
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    cursor.execute(sqlite_create_table_query1)
    cursor.execute(sqlite_create_table_query2)

    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

print('\n')

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')

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

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")

    cursor.executemany('INSERT or REPLACE INTO Courses VALUES(?, ?, ?, ?)', data_Courses)
    cursor.executemany('INSERT or REPLACE INTO Students VALUES(?, ?, ?, ?, ?)', data_Students)
    cursor.executemany('INSERT or IGNORE INTO Student_courses VALUES(?, ?)', data_Student_courses)
    sqlite_connection.commit()
    print("Данные внесены")

    print('\n')


    for string in cursor.execute(f'''
                                    SELECT Students.name, Students.surname
                                    FROM Students
                                    WHERE Students.age > 30
                                ''').fetchall():
        print(string[0], string[1])

    print('\n')
    string = []
    for string in cursor.execute('''
                                    SELECT Students.name, Students.surname
                                    FROM Student_courses
                                    JOIN Students ON Student_courses.student_id = Students.id
                                    JOIN Courses ON Student_courses.course_id = Courses.id
                                    WHERE Courses.name = "python"
                                ''').fetchall():
        print(string[0], string[1])
    print('\n')
    string = []
    for string in cursor.execute('''
                                    SELECT Students.name, Students.surname
                                    FROM Student_courses
                                    JOIN Students ON Student_courses.student_id = Students.id
                                    JOIN Courses ON Student_courses.course_id = Courses.id
                                    WHERE Courses.name = "python" AND Students.city = "Spb"
                                ''').fetchall():
        print(string[0], string[1])

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")