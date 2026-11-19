import unittest




class SQLQueryBuilderTestSelect(unittest.TestCase):
    def test_select_1(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', ["id", "name"], {'age': 30}),
            "SELECT id, name FROM users WHERE age='30'"
        )

    def test_select_2(self):
        self.assertEqual(
            SQLQueryBuilder.select('students', ["id", "name"], {'age': 18}),
            "SELECT id, name FROM students WHERE age='18'"
        )

    def test_select_3(self):
        self.assertEqual(
            SQLQueryBuilder.select('items', ["id", "name"], {'price': 1.0}),
            "SELECT id, name FROM items WHERE price='1.0'"
        )

    def test_select_4(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', ["id"], {'age': 30}),
            "SELECT id FROM users WHERE age='30'"
        )

    def test_select_5(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', ["name"], {'age': 30}),
            "SELECT name FROM users WHERE age='30'"
        )

import unittest

class AgentTest_select(unittest.TestCase):
    def test_select_1(self):
        self.assertEqual(
            SQLQueryBuilder.select('table1'),
            "SELECT * FROM table1"
        )

    def test_select_2(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', ["id", "name"]),
            "SELECT id, name FROM users"
        )

class SQLQueryBuilderTestInsert(unittest.TestCase):
    def test_insert_1(self):
        self.assertEqual(
            SQLQueryBuilder.insert('users', {'name': 'Tom', 'age': 30}),
            "INSERT INTO users (name, age) VALUES ('Tom', '30')"
        )

    def test_insert_2(self):
        self.assertEqual(
            SQLQueryBuilder.insert('students', {'name': 'Tom', 'age': 18}),
            "INSERT INTO students (name, age) VALUES ('Tom', '18')"
        )

    def test_insert_3(self):
        self.assertEqual(
            SQLQueryBuilder.insert('items', {'name': 'apple', 'price': 1.0}),
            "INSERT INTO items (name, price) VALUES ('apple', '1.0')"
        )

class AgentTest_insert(unittest.TestCase):
    def test_insert_1(self):
        self.assertEqual(
            SQLQueryBuilder.insert('users', {'name': 'Tom'}),
            "INSERT INTO users (name) VALUES ('Tom')"
        )

    def test_insert_2(self):
        self.assertEqual(
            SQLQueryBuilder.insert('users', {'name': 'Tom', 'age': 30, 'city': 'Paris'}),
            "INSERT INTO users (name, age, city) VALUES ('Tom', '30', 'Paris')"
        )

class SQLQueryBuilderTestDetele(unittest.TestCase):
    def test_delete_1(self):
        self.assertEqual(
            SQLQueryBuilder.delete('users', {'name': 'Tom'}),
            "DELETE FROM users WHERE name='Tom'"
        )

    def test_delete_2(self):
        self.assertEqual(
            SQLQueryBuilder.delete('students', {'name': 'Tom'}),
            "DELETE FROM students WHERE name='Tom'"
        )

    def test_delete_3(self):
        self.assertEqual(
            SQLQueryBuilder.delete('items', {'name': 'apple'}),
            "DELETE FROM items WHERE name='apple'"
        )

    def test_delete_4(self):
        self.assertEqual(
            SQLQueryBuilder.delete('items', {'name': 'aaa'}),
            "DELETE FROM items WHERE name='aaa'"
        )

import unittest

class AgentTest_delete(unittest.TestCase):
    def test_delete_1(self):
        self.assertEqual(
            SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14}),
            "DELETE FROM table1 WHERE name='Test' AND age='14'"
        )

    def test_delete_2(self):
        self.assertEqual(
            SQLQueryBuilder.delete('users', {'city': 'Paris', 'age': 30, 'name': 'Tom'}),
            "DELETE FROM users WHERE city='Paris' AND age='30' AND name='Tom'"
        )

class SQLQueryBuilderTestUpdate(unittest.TestCase):
    def test_update_1(self):
        self.assertEqual(
            SQLQueryBuilder.update('users', {'age': 35}, {'name': 'Tom'}),
            "UPDATE users SET age='35' WHERE name='Tom'"
        )

    def test_update_2(self):
        self.assertEqual(
            SQLQueryBuilder.update('students', {'age': 18}, {'name': 'Tom'}),
            "UPDATE students SET age='18' WHERE name='Tom'"
        )

    def test_update_3(self):
        self.assertEqual(
            SQLQueryBuilder.update('items', {'price': 1.0}, {'name': 'apple'}),
            "UPDATE items SET price='1.0' WHERE name='apple'"
        )

    def test_update_4(self):
        self.assertEqual(
            SQLQueryBuilder.update('items', {'price': 1.0}, {'name': 'aaa'}),
            "UPDATE items SET price='1.0' WHERE name='aaa'"
        )

class AgentTest_update(unittest.TestCase):
    def test_update_1(self):
        self.assertEqual(
            SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where={'name': 'Test'}),
            "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        )

    def test_update_2(self):
        self.assertEqual(
            SQLQueryBuilder.update('users', {'city': 'Paris', 'age': 30}, {'name': 'Tom', 'age': 18}),
            "UPDATE users SET city='Paris', age='30' WHERE name='Tom' AND age='18'"
        )