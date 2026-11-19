import unittest


import unittest

class AgentTest_select(unittest.TestCase):

    def test_select_1(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.select(['field1', 'field2'], 'filed3 = value1'),
            'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
        )

    def test_select_2(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.select(['field1', 'field2']),
            'SELECT field1, field2 FROM table1;'
        )

    def test_select_3(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.select(['field1'], 'field1 = value1'),
            'SELECT field1 FROM table1 WHERE field1 = value1;'
        )

    def test_select_4(self):
        sql = SQLGenerator('users')
        self.assertEqual(
            sql.select(['name', 'age', 'city'], 'age > 18'),
            'SELECT name, age, city FROM users WHERE age > 18;'
        )

    def test_select_5(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.select(None, 'age < 30'),
            'SELECT * FROM table1 WHERE age < 30;'
        )

import unittest

class AgentTest_insert(unittest.TestCase):

    def test_insert_1(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.insert({'key1': 'value1', 'key2': 'value2'}),
            "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
        )

    def test_insert_2(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.insert({'key1': 'value1'}),
            "INSERT INTO table1 (key1) VALUES ('value1');"
        )

    def test_insert_3(self):
        sql = SQLGenerator('users')
        self.assertEqual(
            sql.insert({'name': 'Alice', 'city': 'Paris', 'country': 'France'}),
            "INSERT INTO users (name, city, country) VALUES ('Alice', 'Paris', 'France');"
        )

    def test_insert_4(self):
        sql = SQLGenerator('table1')
        result = sql.insert({'key1': 'value1', 'key2': 'value2'})
        self.assertIsInstance(result, str)

    def test_insert_5(self):
        sql = SQLGenerator('orders')
        self.assertEqual(
            sql.insert({'item': 'book', 'status': 'shipped'}),
            "INSERT INTO orders (item, status) VALUES ('book', 'shipped');"
        )

class AgentTest_update(unittest.TestCase):

    def test_update_1(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1"),
            "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        )

    def test_update_2(self):
        sql = SQLGenerator('users')
        self.assertEqual(
            sql.update({'name': 'Alice'}, "id = 5"),
            "UPDATE users SET name = 'Alice' WHERE id = 5;"
        )

    def test_update_3(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.update({'city': 'Paris', 'country': 'France', 'age': 'thirty'}, "age > 18"),
            "UPDATE table1 SET city = 'Paris', country = 'France', age = 'thirty' WHERE age > 18;"
        )

    def test_update_4(self):
        sql = SQLGenerator('table1')
        result = sql.update({'field1': 'new_value1'}, "field2 = value2")
        self.assertIsInstance(result, str)

    def test_update_5(self):
        sql = SQLGenerator('orders')
        self.assertEqual(
            sql.update({'status': 'shipped'}, "item = 'book'"),
            "UPDATE orders SET status = 'shipped' WHERE item = 'book';"
        )

import unittest

class AgentTest_delete(unittest.TestCase):

    def test_delete_1(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.delete("field1 = value1"),
            'DELETE FROM table1 WHERE field1 = value1;'
        )

    def test_delete_2(self):
        sql = SQLGenerator('users')
        self.assertEqual(
            sql.delete("age > 18"),
            'DELETE FROM users WHERE age > 18;'
        )

    def test_delete_3(self):
        sql = SQLGenerator('orders')
        self.assertEqual(
            sql.delete("item = 'book'"),
            "DELETE FROM orders WHERE item = 'book';"
        )

    def test_delete_4(self):
        sql = SQLGenerator('table1')
        result = sql.delete("field2 = value2")
        self.assertIsInstance(result, str)

    def test_delete_5(self):
        sql = SQLGenerator('customers')
        self.assertEqual(
            sql.delete("id = 5"),
            'DELETE FROM customers WHERE id = 5;'
        )

import unittest

class AgentTest_select_female_under_age(unittest.TestCase):

    def test_select_female_under_age_1(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.select_female_under_age(30),
            "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        )

    def test_select_female_under_age_2(self):
        sql = SQLGenerator('users')
        self.assertEqual(
            sql.select_female_under_age(25),
            "SELECT * FROM users WHERE age < 25 AND gender = 'female';"
        )

    def test_select_female_under_age_3(self):
        sql = SQLGenerator('orders')
        self.assertEqual(
            sql.select_female_under_age(18),
            "SELECT * FROM orders WHERE age < 18 AND gender = 'female';"
        )

    def test_select_female_under_age_4(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(30)
        self.assertIsInstance(result, str)

    def test_select_female_under_age_5(self):
        sql = SQLGenerator('customers')
        self.assertEqual(
            sql.select_female_under_age(65),
            "SELECT * FROM customers WHERE age < 65 AND gender = 'female';"
        )

import unittest

class AgentTest_select_by_age_range(unittest.TestCase):

    def test_select_by_age_range_1(self):
        sql = SQLGenerator('table1')
        self.assertEqual(
            sql.select_by_age_range(20, 30),
            'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
        )

    def test_select_by_age_range_2(self):
        sql = SQLGenerator('users')
        self.assertEqual(
            sql.select_by_age_range(18, 65),
            'SELECT * FROM users WHERE age BETWEEN 18 AND 65;'
        )

    def test_select_by_age_range_3(self):
        sql = SQLGenerator('orders')
        self.assertEqual(
            sql.select_by_age_range(0, 10),
            'SELECT * FROM orders WHERE age BETWEEN 0 AND 10;'
        )

    def test_select_by_age_range_4(self):
        sql = SQLGenerator('table1')
        result = sql.select_by_age_range(20, 30)
        self.assertIsInstance(result, str)

    def test_select_by_age_range_5(self):
        sql = SQLGenerator('customers')
        self.assertEqual(
            sql.select_by_age_range(25, 25),
            'SELECT * FROM customers WHERE age BETWEEN 25 AND 25;'
        )