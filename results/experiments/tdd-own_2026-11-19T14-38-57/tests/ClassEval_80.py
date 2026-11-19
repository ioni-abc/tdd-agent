import unittest


import unittest

class AgentTest_select(unittest.TestCase):

    def test_select_1(self):
        # Docstring example: specific columns with a single WHERE condition
        result = SQLQueryBuilder.select('table1', columns=["col1", "col2"], where={"age": 15})
        self.assertEqual(result, "SELECT col1, col2 FROM table1 WHERE age='15'")

    def test_select_2(self):
        # Default columns is '*' and default where is None (no WHERE clause)
        result = SQLQueryBuilder.select('table1')
        self.assertEqual(result, "SELECT * FROM table1")

    def test_select_3(self):
        # Column list without a where condition
        result = SQLQueryBuilder.select('table1', columns=["col1", "col2"])
        self.assertEqual(result, "SELECT col1, col2 FROM table1")

    def test_select_4(self):
        # String value in the where dict is quoted in the same way as the delete example
        result = SQLQueryBuilder.select('table1', columns=["name"], where={"name": "Test"})
        self.assertEqual(result, "SELECT name FROM table1 WHERE name='Test'")

    def test_select_5(self):
        # Multiple where conditions are joined with AND, as shown in the delete example
        result = SQLQueryBuilder.select('table1', where={"name": "Test", "age": 14})
        self.assertEqual(result, "SELECT * FROM table1 WHERE name='Test' AND age='14'")

import unittest

class AgentTest_insert(unittest.TestCase):

    def test_insert_1(self):
        # Docstring example: two columns, string and integer values
        result = SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        self.assertEqual(result, "INSERT INTO table1 (name, age) VALUES ('Test', '14')")

    def test_insert_2(self):
        # Single column insert
        result = SQLQueryBuilder.insert('table1', {'name': 'Test'})
        self.assertEqual(result, "INSERT INTO table1 (name) VALUES ('Test')")

    def test_insert_3(self):
        # Column order follows the order of the keys in the data dict
        result = SQLQueryBuilder.insert('table1', {'age': 14, 'name': 'Test'})
        self.assertEqual(result, "INSERT INTO table1 (age, name) VALUES ('14', 'Test')")

    def test_insert_4(self):
        # Numeric values are quoted in the same way as strings
        result = SQLQueryBuilder.insert('table1', {'age': 15})
        self.assertEqual(result, "INSERT INTO table1 (age) VALUES ('15')")

    def test_insert_5(self):
        # Different table name with several columns
        result = SQLQueryBuilder.insert('users', {'id': 1, 'name': 'Alice', 'city': 'Paris'})
        self.assertEqual(result, "INSERT INTO users (id, name, city) VALUES ('1', 'Alice', 'Paris')")

import unittest

class AgentTest_delete(unittest.TestCase):

    def test_delete_1(self):
        # Docstring example: two conditions, string and integer values
        result = SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        self.assertEqual(result, "DELETE FROM table1 WHERE name='Test' AND age='14'")

    def test_delete_2(self):
        # Single condition
        result = SQLQueryBuilder.delete('table1', {'name': 'Test'})
        self.assertEqual(result, "DELETE FROM table1 WHERE name='Test'")

    def test_delete_3(self):
        # Numeric values are quoted in the same way as strings
        result = SQLQueryBuilder.delete('table1', {'age': 15})
        self.assertEqual(result, "DELETE FROM table1 WHERE age='15'")

    def test_delete_4(self):
        # Conditions are joined with AND in the order of the keys in the dict
        result = SQLQueryBuilder.delete('table1', {'age': 14, 'name': 'Test'})
        self.assertEqual(result, "DELETE FROM table1 WHERE age='14' AND name='Test'")

    def test_delete_5(self):
        # Different table name with several conditions
        result = SQLQueryBuilder.delete('users', {'id': 1, 'name': 'Alice', 'city': 'Paris'})
        self.assertEqual(result, "DELETE FROM users WHERE id='1' AND name='Alice' AND city='Paris'")

import unittest

class AgentTest_update(unittest.TestCase):

    def test_update_1(self):
        # Docstring example: two SET columns, string and integer values, one WHERE condition
        result = SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where={'name': 'Test'})
        self.assertEqual(result, "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'")

    def test_update_2(self):
        # Single SET column with a single WHERE condition
        result = SQLQueryBuilder.update('table1', {'name': 'Test'}, where={'age': 14})
        self.assertEqual(result, "UPDATE table1 SET name='Test' WHERE age='14'")

    def test_update_3(self):
        # Numeric value in the SET part is quoted in the same way as strings
        result = SQLQueryBuilder.update('table1', {'age': 15}, where={'name': 'Test'})
        self.assertEqual(result, "UPDATE table1 SET age='15' WHERE name='Test'")

    def test_update_4(self):
        # Multiple WHERE conditions are joined with AND, as in the delete example
        result = SQLQueryBuilder.update('table1', {'name': 'Test2'}, where={'name': 'Test', 'age': 14})
        self.assertEqual(result, "UPDATE table1 SET name='Test2' WHERE name='Test' AND age='14'")

    def test_update_5(self):
        # Different table name, several SET columns in dict key order, numeric WHERE value
        result = SQLQueryBuilder.update('users', {'city': 'Paris', 'id': 1, 'name': 'Alice'}, where={'id': 2})
        self.assertEqual(result, "UPDATE users SET city='Paris', id='1', name='Alice' WHERE id='2'")