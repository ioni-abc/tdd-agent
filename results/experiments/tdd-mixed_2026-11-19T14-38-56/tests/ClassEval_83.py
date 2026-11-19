import unittest




class StudentDatabaseProcessorTestInsertStudent(unittest.TestCase):
    def setUp(self):
        self.processor = StudentDatabaseProcessor("test_database.db")
        self.processor.create_student_table()

    def tearDown(self):
        conn = sqlite3.connect("test_database.db")
        conn.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        conn.close()

    def test_insert_student_1(self):
        student_data = {
            'name': 'Alice',
            'age': 20,
            'gender': 'female',
            'grade': 90
        }
        self.processor.insert_student(student_data)

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", ('Alice',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Alice')

    def test_insert_student_2(self):
        student_data = {
            'name': 'aaa',
            'age': 20,
            'gender': 'female',
            'grade': 90
        }
        self.processor.insert_student(student_data)

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", ('aaa',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'aaa')

    def test_insert_student_3(self):
        student_data = {
            'name': 'bbb',
            'age': 20,
            'gender': 'female',
            'grade': 90
        }
        self.processor.insert_student(student_data)

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", ('bbb',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'bbb')

import sqlite3

import unittest

class AgentTest_create_student_table(unittest.TestCase):
    def setUp(self):
        self.processor = StudentDatabaseProcessor("test_database.db")

    def tearDown(self):
        conn = sqlite3.connect("test_database.db")
        conn.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        conn.close()

    def test_create_student_table_1(self):
        self.processor.create_student_table()

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(students)")
        columns = {row[1]: row[2].upper() for row in cursor.fetchall()}
        conn.close()

        self.assertEqual(set(columns.keys()), {'ID', 'name', 'age', 'gender', 'grade'})
        self.assertIn('INT', columns['ID'])
        self.assertIn('TEXT', columns['name'])
        self.assertIn('INT', columns['age'])
        self.assertIn('TEXT', columns['gender'])
        self.assertIn('INT', columns['grade'])

    def test_create_student_table_2(self):
        self.processor.create_student_table()

        conn = sqlite3.connect("test_database.db")
        conn.execute(
            "INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)",
            ('Carol', 16, 'female', 88)
        )
        conn.commit()
        conn.close()

        self.processor.create_student_table()

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM students")
        rows = cursor.fetchall()
        conn.close()

        self.assertEqual(rows, [('Carol',)])

class StudentDatabaseProcessorTestSearchStudentByName(unittest.TestCase):
    def setUp(self):
        self.processor = StudentDatabaseProcessor("test_database.db")
        self.processor.create_student_table()

    def tearDown(self):
        conn = sqlite3.connect("test_database.db")
        conn.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        conn.close()

    def test_search_student_by_name_1(self):
        student_data = {
            'name': 'Bob',
            'age': 19,
            'gender': 'male',
            'grade': 85
        }
        self.processor.insert_student(student_data)

        result = self.processor.search_student_by_name('Bob')

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Bob')

    def test_search_student_by_name_2(self):
        student_data = {
            'name': 'aaa',
            'age': 19,
            'gender': 'male',
            'grade': 85
        }
        self.processor.insert_student(student_data)

        result = self.processor.search_student_by_name('aaa')

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'aaa')

    def test_search_student_by_name_3(self):
        student_data = {
            'name': 'bbb',
            'age': 19,
            'gender': 'male',
            'grade': 85
        }
        self.processor.insert_student(student_data)

        result = self.processor.search_student_by_name('bbb')

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'bbb')

import sqlite3

import unittest

class AgentTest_insert_student(unittest.TestCase):
    def setUp(self):
        self.processor = StudentDatabaseProcessor("test_database.db")
        self.processor.create_student_table()

    def tearDown(self):
        conn = sqlite3.connect("test_database.db")
        conn.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        conn.close()

    def test_insert_student_1(self):
        student_data = {
            'name': 'Dave',
            'age': 15,
            'gender': 'Male',
            'grade': 9
        }
        self.processor.insert_student(student_data)

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, age, gender, grade FROM students WHERE name=?", ('Dave',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('Dave', 15, 'Male', 9))

    def test_insert_student_2(self):
        first_student = {
            'name': 'Eve',
            'age': 16,
            'gender': 'Female',
            'grade': 10
        }
        second_student = {
            'name': 'Frank',
            'age': 17,
            'gender': 'Male',
            'grade': 11
        }
        self.processor.insert_student(first_student)
        self.processor.insert_student(second_student)

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        count = cursor.fetchone()[0]
        cursor.execute("SELECT name FROM students ORDER BY name")
        names = [row[0] for row in cursor.fetchall()]
        conn.close()

        self.assertEqual(count, 2)
        self.assertEqual(names, ['Eve', 'Frank'])

class StudentDatabaseProcessorTestDeleteStudentByName(unittest.TestCase):
    def setUp(self):
        self.processor = StudentDatabaseProcessor("test_database.db")
        self.processor.create_student_table()

    def tearDown(self):
        conn = sqlite3.connect("test_database.db")
        conn.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        conn.close()

    def test_delete_student_by_name_1(self):
        student_data = {
            'name': 'Charlie',
            'age': 18,
            'gender': 'male',
            'grade': 95
        }
        self.processor.insert_student(student_data)

        self.processor.delete_student_by_name('Charlie')

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", ('Charlie',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 0)

    def test_delete_student_by_name_2(self):
        student_data = {
            'name': 'aaa',
            'age': 18,
            'gender': 'male',
            'grade': 95
        }
        self.processor.insert_student(student_data)

        self.processor.delete_student_by_name('aaa')

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", ('aaa',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 0)

    def test_delete_student_by_name_3(self):
        student_data = {
            'name': 'bbb',
            'age': 18,
            'gender': 'male',
            'grade': 95
        }
        self.processor.insert_student(student_data)

        self.processor.delete_student_by_name('bbb')

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", ('bbb',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 0)

import sqlite3

import unittest

class AgentTest_search_student_by_name(unittest.TestCase):
    def setUp(self):
        self.processor = StudentDatabaseProcessor("test_database.db")
        self.processor.create_student_table()

    def tearDown(self):
        conn = sqlite3.connect("test_database.db")
        conn.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        conn.close()

    def test_search_student_by_name_1(self):
        student_data = {
            'name': 'Ivy',
            'age': 17,
            'gender': 'female',
            'grade': 92
        }
        self.processor.insert_student(student_data)

        result = self.processor.search_student_by_name('Nobody')

        self.assertEqual(result, [])

    def test_search_student_by_name_2(self):
        first_student = {
            'name': 'Grace',
            'age': 20,
            'gender': 'female',
            'grade': 80
        }
        second_student = {
            'name': 'Grace',
            'age': 21,
            'gender': 'female',
            'grade': 75
        }
        other_student = {
            'name': 'Henry',
            'age': 19,
            'gender': 'male',
            'grade': 88
        }
        self.processor.insert_student(first_student)
        self.processor.insert_student(second_student)
        self.processor.insert_student(other_student)

        result = self.processor.search_student_by_name('Grace')

        self.assertEqual(len(result), 2)
        for row in result:
            self.assertIsInstance(row, tuple)
            self.assertEqual(row[1], 'Grace')
        self.assertEqual(sorted(row[2] for row in result), [20, 21])

class StudentDatabaseProcessorTest(unittest.TestCase):
    def setUp(self):
        self.processor = StudentDatabaseProcessor("test_database.db")
        self.processor.create_student_table()

    def tearDown(self):
        conn = sqlite3.connect("test_database.db")
        conn.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        conn.close()

    def test_StudentDatabaseProcessor(self):
        student_data = {
            'name': 'Alice',
            'age': 20,
            'gender': 'female',
            'grade': 90
        }
        self.processor.insert_student(student_data)

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", ('Alice',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Alice')

        student_data = {
            'name': 'Bob',
            'age': 19,
            'gender': 'male',
            'grade': 85
        }
        self.processor.insert_student(student_data)

        result = self.processor.search_student_by_name('Bob')

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Bob')

        student_data = {
            'name': 'Charlie',
            'age': 18,
            'gender': 'male',
            'grade': 95
        }
        self.processor.insert_student(student_data)

        self.processor.delete_student_by_name('Charlie')

        conn = sqlite3.connect("test_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", ('Charlie',))
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 0)