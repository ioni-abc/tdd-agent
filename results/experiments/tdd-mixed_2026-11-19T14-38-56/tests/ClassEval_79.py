import unittest



class SQLGeneratorTestSelect(unittest.TestCase):
    def test_select_1(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1'], "field2 = value1")
        self.assertEqual(result, "SELECT field1 FROM table1 WHERE field2 = value1;")

    def test_select_2(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1', 'field2'], "field3 = value1")
        self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1;")

    def test_select_3(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1, field2'], "field3 = value1")
        self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1;")

    def test_select_4(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1, field2'], "field3 = value1, field4 = value2")
        self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1, field4 = value2;")

import unittest

class AgentTest_select(unittest.TestCase):
    def test_select_1(self):
        sql = SQLGenerator('table1')
        result = sql.select(None, "field1 = value1")
        self.assertEqual(result, "SELECT * FROM table1 WHERE field1 = value1;")

    def test_select_2(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1', 'field2'])
        self.assertEqual(result, "SELECT field1, field2 FROM table1;")

class SQLGeneratorTestInsert(unittest.TestCase):
    def test_insert(self):
        sql = SQLGenerator('table1')
        result = sql.insert({'field1': 'value1', 'field2': 'value2'})
        self.assertEqual(result, "INSERT INTO table1 (field1, field2) VALUES ('value1', 'value2');")

    def test_insert_2(self):
        sql = SQLGenerator('table1')
        result = sql.insert({'field1': 'value1', 'field2': 'value2', 'field3': 'value3'})
        self.assertEqual(result, "INSERT INTO table1 (field1, field2, field3) VALUES ('value1', 'value2', 'value3');")

    def test_insert_3(self):
        sql = SQLGenerator('table1')
        result = sql.insert({'field1': 'value1', 'field2': 'value2', 'field3': 'value3', 'field4': 'value4'})
        self.assertEqual(result,
                         "INSERT INTO table1 (field1, field2, field3, field4) VALUES ('value1', 'value2', 'value3', 'value4');")

class AgentTest_insert(unittest.TestCase):
    def test_insert_1(self):
        sql = SQLGenerator('table1')
        result = sql.insert({'key1': 'value1'})
        self.assertEqual(result, "INSERT INTO table1 (key1) VALUES ('value1');")

    def test_insert_2(self):
        sql = SQLGenerator('users')
        result = sql.insert({'key1': 'value1', 'key2': 'value2'})
        self.assertEqual(result, "INSERT INTO users (key1, key2) VALUES ('value1', 'value2');")

class SQLGeneratorTestUpdate(unittest.TestCase):
    def test_update(self):
        sql = SQLGenerator('table1')
        result = sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
        self.assertEqual(result,
                         "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;")

    def test_update_2(self):
        sql = SQLGenerator('table1')
        result = sql.update({'field1': 'new_value1', 'field2': 'new_value2', 'field3': 'new_value3'},
                            "field4 = value1")
        self.assertEqual(result,
                         "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2', field3 = 'new_value3' WHERE field4 = value1;")

    def test_update_3(self):
        sql = SQLGenerator('table1')
        result = sql.update({'field1': 'new_value1', 'field2': 'new_value2', 'field3': 'new_value3',
                             'field4': 'new_value4'}, "field5 = value1")
        self.assertEqual(result,
                         "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2', field3 = 'new_value3', field4 = 'new_value4' WHERE field5 = value1;")

import unittest

class AgentTest_update(unittest.TestCase):
    def test_update_1(self):
        sql = SQLGenerator('table1')
        result = sql.update({'field1': 'new_value1'}, "field2 = value1")
        self.assertEqual(result, "UPDATE table1 SET field1 = 'new_value1' WHERE field2 = value1;")

    def test_update_2(self):
        sql = SQLGenerator('users')
        result = sql.update({'name': 'Bob'}, "id = 5 AND age > 20")
        self.assertEqual(result, "UPDATE users SET name = 'Bob' WHERE id = 5 AND age > 20;")

class SQLGeneratorTestDelete(unittest.TestCase):
    def test_delete(self):
        sql = SQLGenerator('table1')
        result = sql.delete("field1 = value1")
        self.assertEqual(result, "DELETE FROM table1 WHERE field1 = value1;")

    def test_delete_2(self):
        sql = SQLGenerator('table1')
        result = sql.delete("field1 = value1 AND field2 = value2")
        self.assertEqual(result, "DELETE FROM table1 WHERE field1 = value1 AND field2 = value2;")

    def test_delete_3(self):
        sql = SQLGenerator('table1')
        result = sql.delete("field1 = value1 AND field2 = value2 AND field3 = value3")
        self.assertEqual(result, "DELETE FROM table1 WHERE field1 = value1 AND field2 = value2 AND field3 = value3;")

import unittest

class AgentTest_delete(unittest.TestCase):
    def test_delete_1(self):
        sql = SQLGenerator('users')
        result = sql.delete("id = 5")
        self.assertEqual(result, "DELETE FROM users WHERE id = 5;")

    def test_delete_2(self):
        sql = SQLGenerator('table1')
        result = sql.delete("age > 20 OR name = 'Bob'")
        self.assertEqual(result, "DELETE FROM table1 WHERE age > 20 OR name = 'Bob';")

class SQLGeneratorTestSelectFemaleUnderAge(unittest.TestCase):
    def test_select_female_under_age(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(30)
        self.assertEqual(result, "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';")

    def test_select_female_under_age_2(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(40)
        self.assertEqual(result,"SELECT * FROM table1 WHERE age < 40 AND gender = 'female';")

    def test_select_female_under_age_3(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(20)
        self.assertEqual(result,"SELECT * FROM table1 WHERE age < 20 AND gender = 'female';")

import unittest

class AgentTest_select_female_under_age(unittest.TestCase):
    def test_select_female_under_age_1(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(25)
        self.assertEqual(result, "SELECT * FROM table1 WHERE age < 25 AND gender = 'female';")

    def test_select_female_under_age_2(self):
        sql = SQLGenerator('users')
        result = sql.select_female_under_age(65)
        self.assertEqual(result, "SELECT * FROM users WHERE age < 65 AND gender = 'female';")

class SQLGeneratorTestSelectByAgeRange(unittest.TestCase):
    def test_select_by_age_range(self):
        sql = SQLGenerator('table1')
        result = sql.select_by_age_range(20, 30)
        self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;")

    def test_select_by_age_range_2(self):
        sql = SQLGenerator('table1')
        result = sql.select_by_age_range(10, 20)
        self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 10 AND 20;")

    def test_select_by_age_range_3(self):
        sql = SQLGenerator('table1')
        result = sql.select_by_age_range(30, 40)
        self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 30 AND 40;")

import unittest

class AgentTest_select_by_age_range(unittest.TestCase):
    def test_select_by_age_range_1(self):
        sql = SQLGenerator('users')
        result = sql.select_by_age_range(18, 65)
        self.assertEqual(result, "SELECT * FROM users WHERE age BETWEEN 18 AND 65;")

    def test_select_by_age_range_2(self):
        sql = SQLGenerator('table1')
        result = sql.select_by_age_range(25, 25)
        self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 25 AND 25;")