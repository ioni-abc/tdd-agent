import unittest
import sqlite3




class DatabaseProcessorTestCreateTable(unittest.TestCase):
    def setUp(self):
        self.database_name = "test.db"
        self.processor = DatabaseProcessor(self.database_name)

    def tearDown(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()
        conn.close()

    def test_create_table_1(self):
        table_name = "test_table"
        self.processor.create_table(table_name, 'name', 'age')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], table_name)

    def test_create_table_2(self):
        table_name = "test_table2"
        self.processor.create_table(table_name, 'name', 'age')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], table_name)

    def test_create_table_3(self):
        table_name = "test_table3"
        self.processor.create_table(table_name, 'name', 'age')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], table_name)

import unittest

import sqlite3

class AgentTest_create_table(unittest.TestCase):
    def setUp(self):
        self.database_name = "test.db"
        self.processor = DatabaseProcessor(self.database_name)

    def tearDown(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS schema_table")
        cursor.execute("DROP TABLE IF EXISTS existing_table")
        conn.commit()
        conn.close()

    def test_create_table_1(self):
        table_name = "schema_table"
        self.processor.create_table(table_name, 'name', 'age')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        conn.close()

        # PRAGMA table_info rows: (cid, name, type, notnull, dflt_value, pk)
        column_info = {col[1]: {'type': col[2].upper(), 'pk': col[5]} for col in columns}

        self.assertEqual(len(columns), 3)
        self.assertEqual(set(column_info.keys()), {'id', 'name', 'age'})

        self.assertEqual(column_info['id']['type'], 'INTEGER')
        self.assertEqual(column_info['id']['pk'], 1)

        self.assertEqual(column_info['name']['type'], 'TEXT')
        self.assertEqual(column_info['name']['pk'], 0)

        self.assertEqual(column_info['age']['type'], 'INTEGER')
        self.assertEqual(column_info['age']['pk'], 0)

    def test_create_table_2(self):
        table_name = "existing_table"

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(
            f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        )
        cursor.execute(
            f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", ('John', 25)
        )
        conn.commit()
        conn.close()

        # Creating a table that already exists should not raise or remove its data.
        self.processor.create_table(table_name, 'name', 'age')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name, age FROM {table_name}")
        rows = cursor.fetchall()
        conn.close()

        self.assertEqual(rows, [('John', 25)])

class DatabaseProcessorTestInsertIntoDatabase(unittest.TestCase):
    def setUp(self):
        self.database_name = "test.db"
        self.processor = DatabaseProcessor(self.database_name)

    def tearDown(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()
        conn.close()

    def test_insert_into_database_1(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), len(data))
        self.assertEqual(result[0][2], 25)

    def test_insert_into_database_2(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 15},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), len(data))
        self.assertEqual(result[0][2], 15)

    def test_insert_into_database_3(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 16},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), len(data))
        self.assertEqual(result[0][2], 16)

import unittest

import sqlite3

class AgentTest_insert_into_database(unittest.TestCase):
    def setUp(self):
        self.database_name = "test.db"
        self.processor = DatabaseProcessor(self.database_name)

    def tearDown(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()
        conn.close()

    def test_insert_into_database_1(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, name, age FROM {table_name} ORDER BY id")
        result = cursor.fetchall()
        conn.close()

        # id is an INTEGER PRIMARY KEY assigned automatically; each row keeps its own name and age.
        self.assertEqual(result, [(1, 'John', 25), (2, 'Alice', 30)])

    def test_insert_into_database_2(self):
        table_name = "test_table"
        first_batch = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        second_batch = [
            {'name': 'Bob', 'age': 40}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, first_batch)
        self.processor.insert_into_database(table_name, second_batch)

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name, age FROM {table_name} ORDER BY id")
        result = cursor.fetchall()
        conn.close()

        # Subsequent inserts append to the existing rows rather than replacing them.
        self.assertEqual(result, [('John', 25), ('Alice', 30), ('Bob', 40)])

class DatabaseProcessorTestSearchDatabase(unittest.TestCase):
    def setUp(self):
        self.database_name = "test.db"
        self.processor = DatabaseProcessor(self.database_name)

    def tearDown(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()
        conn.close()

    def test_search_database_1(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        result = self.processor.search_database(table_name, 'John')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'John')

    def test_search_database_2(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        result = self.processor.search_database(table_name, 'Alice')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Alice')

    def test_search_database_3(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        result = self.processor.search_database(table_name, 'Bob')
        self.assertIsNone(result)

import unittest

import sqlite3

class AgentTest_search_database(unittest.TestCase):
    def setUp(self):
        self.database_name = "test.db"
        self.processor = DatabaseProcessor(self.database_name)

    def tearDown(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()
        conn.close()

    def test_search_database_1(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30},
            {'name': 'John', 'age': 40}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        result = self.processor.search_database(table_name, 'John')

        # All rows whose name matches should be returned, not just the first one.
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(isinstance(row, tuple) for row in result))
        self.assertTrue(all(row[1] == 'John' for row in result))
        self.assertEqual(sorted(row[2] for row in result), [25, 40])

    def test_search_database_2(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        result = self.processor.search_database(table_name, 'John')

        # Each row is returned as a tuple of (id, name, age), matching the docstring example.
        self.assertIsInstance(result, list)
        self.assertEqual(result, [(1, 'John', 25)])

class DatabaseProcessorTestDeteleFromDatabase(unittest.TestCase):
    def setUp(self):
        self.database_name = "test.db"
        self.processor = DatabaseProcessor(self.database_name)

    def tearDown(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()
        conn.close()

    def test_delete_from_database_1(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        self.processor.delete_from_database(table_name, 'John')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Alice')

    def test_delete_from_database_2(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        self.processor.delete_from_database(table_name, 'Alice')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'John')

    def test_delete_from_database_3(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        self.processor.delete_from_database(table_name, 'John')
        self.processor.delete_from_database(table_name, 'Alice')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
        conn.close()

        self.assertEqual(len(result), 0)

import unittest

import sqlite3

class AgentTest_delete_from_database(unittest.TestCase):
    def setUp(self):
        self.database_name = "test.db"
        self.processor = DatabaseProcessor(self.database_name)

    def tearDown(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test_table")
        conn.commit()
        conn.close()

    def test_delete_from_database_1(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30},
            {'name': 'John', 'age': 40}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        self.processor.delete_from_database(table_name, 'John')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name, age FROM {table_name} ORDER BY id")
        result = cursor.fetchall()
        conn.close()

        # Every row with a matching name is deleted, not just the first one.
        self.assertEqual(result, [('Alice', 30)])

    def test_delete_from_database_2(self):
        table_name = "test_table"
        data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ]
        self.processor.create_table(table_name, 'name', 'age')
        self.processor.insert_into_database(table_name, data)

        self.processor.delete_from_database(table_name, 'Bob')

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT name, age FROM {table_name} ORDER BY id")
        result = cursor.fetchall()
        conn.close()

        # Deleting a name that matches no rows leaves the existing rows untouched.
        self.assertEqual(result, [('John', 25), ('Alice', 30)])