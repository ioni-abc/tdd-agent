import unittest


import unittest

import sqlite3

import os

import tempfile

class AgentTest_create_student_table(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_students.db")
        self.processor = StudentDatabaseProcessor(self.db_path)

    def tearDown(self):
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _table_names(self):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
            return [row[0] for row in cursor.fetchall()]
        finally:
            conn.close()

    def _columns(self):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute("PRAGMA table_info(students)")
            return {row[1].lower(): row[2].upper() for row in cursor.fetchall()}
        finally:
            conn.close()

    def test_create_student_table_1(self):
        # The "students" table should exist after calling create_student_table.
        self.processor.create_student_table()
        self.assertIn("students", self._table_names())

    def test_create_student_table_2(self):
        # The table should contain exactly the fields ID, name, age, gender, grade.
        self.processor.create_student_table()
        columns = self._columns()
        self.assertEqual(set(columns.keys()), {"id", "name", "age", "gender", "grade"})

    def test_create_student_table_3(self):
        # ID, age and grade should be of type int; name and gender of type str (text).
        self.processor.create_student_table()
        columns = self._columns()
        for field in ("id", "age", "grade"):
            self.assertIn("INT", columns[field], f"{field} should be an int type")
        for field in ("name", "gender"):
            declared = columns[field]
            self.assertTrue(
                "CHAR" in declared or "TEXT" in declared or "CLOB" in declared,
                f"{field} should be a string type, got {declared}",
            )

    def test_create_student_table_4(self):
        # Calling create_student_table when the table already exists should not
        # raise an error and should not remove existing rows.
        self.processor.create_student_table()
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)",
            ("John", 15, "Male", 9),
        )
        conn.commit()
        conn.close()

        try:
            self.processor.create_student_table()
        except Exception as e:
            self.fail(f"Second call to create_student_table raised {e!r}")

        conn = sqlite3.connect(self.db_path)
        rows = conn.execute("SELECT name FROM students").fetchall()
        conn.close()
        self.assertEqual(rows, [("John",)])

    def test_create_student_table_5(self):
        # create_student_table returns None.
        result = self.processor.create_student_table()
        self.assertIsNone(result)

import unittest

import sqlite3

import os

import tempfile

class AgentTest_insert_student(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_students.db")
        self.processor = StudentDatabaseProcessor(self.db_path)
        self.processor.create_student_table()

    def tearDown(self):
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _all_rows(self):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(
                "SELECT name, age, gender, grade FROM students ORDER BY ID"
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def test_insert_student_1(self):
        # Inserting a student should add a row to the "students" table with the
        # given name, age, gender and grade.
        student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        self.processor.insert_student(student_data)
        self.assertEqual(self._all_rows(), [("John", 15, "Male", 9)])

    def test_insert_student_2(self):
        # Inserting two different students should result in two rows, one for each student.
        self.processor.insert_student({'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9})
        self.processor.insert_student({'name': 'Mary', 'age': 14, 'gender': 'Female', 'grade': 8})
        rows = self._all_rows()
        self.assertEqual(len(rows), 2)
        self.assertEqual({row[0] for row in rows}, {"John", "Mary"})

    def test_insert_student_3(self):
        # insert_student returns None.
        student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        result = self.processor.insert_student(student_data)
        self.assertIsNone(result)

    def test_insert_student_4(self):
        # Each dictionary key should be stored in the matching field of the table.
        student_data = {'name': 'Alice', 'age': 17, 'gender': 'Female', 'grade': 11}
        self.processor.insert_student(student_data)
        rows = self._all_rows()
        self.assertEqual(len(rows), 1)
        name, age, gender, grade = rows[0]
        self.assertEqual(name, "Alice")
        self.assertEqual(age, 17)
        self.assertEqual(gender, "Female")
        self.assertEqual(grade, 11)

    def test_insert_student_5(self):
        # Inserting a new student should not alter the rows already in the table.
        self.processor.insert_student({'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9})
        self.processor.insert_student({'name': 'Mary', 'age': 14, 'gender': 'Female', 'grade': 8})
        rows = self._all_rows()
        self.assertIn(("John", 15, "Male", 9), rows)
        self.assertIn(("Mary", 14, "Female", 8), rows)
        self.assertEqual(len(rows), 2)

import unittest

import sqlite3

import os

import tempfile

class AgentTest_search_student_by_name(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_students.db")
        self.processor = StudentDatabaseProcessor(self.db_path)
        self.processor.create_student_table()

    def tearDown(self):
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _insert_raw(self, name, age, gender, grade):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)",
            (name, age, gender, grade),
        )
        conn.commit()
        conn.close()

    def _all_rows(self):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(
                "SELECT ID, name, age, gender, grade FROM students ORDER BY ID"
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def test_search_student_by_name_1(self):
        # Searching for an existing name returns a list containing the matching row as a tuple.
        self._insert_raw("John", 15, "Male", 9)
        result = self.processor.search_student_by_name("John")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], tuple)
        self.assertEqual(result[0][1:], ("John", 15, "Male", 9))

    def test_search_student_by_name_2(self):
        # Searching for a name shared by several students returns a row for each of them.
        self._insert_raw("John", 15, "Male", 9)
        self._insert_raw("John", 16, "Male", 10)
        result = self.processor.search_student_by_name("John")
        self.assertEqual(len(result), 2)
        self.assertEqual(
            sorted(row[1:] for row in result),
            sorted([("John", 15, "Male", 9), ("John", 16, "Male", 10)]),
        )

    def test_search_student_by_name_3(self):
        # Only rows whose name matches the search criteria are returned.
        self._insert_raw("John", 15, "Male", 9)
        self._insert_raw("Mary", 14, "Female", 8)
        result = self.processor.search_student_by_name("John")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "John")
        self.assertNotIn("Mary", [row[1] for row in result])

    def test_search_student_by_name_4(self):
        # Searching for a name not present in the table returns an empty list.
        self._insert_raw("John", 15, "Male", 9)
        result = self.processor.search_student_by_name("Alice")
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])

    def test_search_student_by_name_5(self):
        # Each returned row holds the ID and the four student fields, and the table is left unchanged.
        self._insert_raw("Mary", 14, "Female", 8)
        rows_before = self._all_rows()
        result = self.processor.search_student_by_name("Mary")
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 5)
        self.assertEqual(result[0], rows_before[0])
        self.assertEqual(self._all_rows(), rows_before)

import unittest

import sqlite3

import os

import tempfile

class AgentTest_delete_student_by_name(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_students.db")
        self.processor = StudentDatabaseProcessor(self.db_path)
        self.processor.create_student_table()

    def tearDown(self):
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _insert_raw(self, name, age, gender, grade):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)",
            (name, age, gender, grade),
        )
        conn.commit()
        conn.close()

    def _all_rows(self):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(
                "SELECT ID, name, age, gender, grade FROM students ORDER BY ID"
            )
            return cursor.fetchall()
        finally:
            conn.close()

    def _table_names(self):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
            return [row[0] for row in cursor.fetchall()]
        finally:
            conn.close()

    def test_delete_student_by_name_1(self):
        # Following the docstring example: a student inserted with insert_student
        # is no longer in the table after delete_student_by_name is called with their name.
        student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        self.processor.insert_student(student_data)
        self.assertEqual(len(self._all_rows()), 1)
        self.processor.delete_student_by_name("John")
        self.assertEqual(self._all_rows(), [])

    def test_delete_student_by_name_2(self):
        # Only the named student is removed; the other student's row is kept unchanged.
        self._insert_raw("John", 15, "Male", 9)
        self._insert_raw("Mary", 14, "Female", 8)
        self.processor.delete_student_by_name("John")
        rows = self._all_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1:], ("Mary", 14, "Female", 8))
        self.assertNotIn("John", [row[1] for row in rows])

    def test_delete_student_by_name_3(self):
        # Deleting a student removes the row from the "students" table,
        # but the table itself still exists.
        self._insert_raw("John", 15, "Male", 9)
        self.processor.delete_student_by_name("John")
        self.assertIn("students", self._table_names())
        self.assertEqual(self._all_rows(), [])

    def test_delete_student_by_name_4(self):
        # delete_student_by_name returns None.
        self._insert_raw("John", 15, "Male", 9)
        result = self.processor.delete_student_by_name("John")
        self.assertIsNone(result)

    def test_delete_student_by_name_5(self):
        # Deleting a name that is not in the table leaves the existing rows unchanged.
        self._insert_raw("John", 15, "Male", 9)
        self._insert_raw("Mary", 14, "Female", 8)
        rows_before = self._all_rows()
        self.processor.delete_student_by_name("Alice")
        self.assertEqual(self._all_rows(), rows_before)