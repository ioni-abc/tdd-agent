import unittest


import unittest

import os

import shutil

import sqlite3

import tempfile

import pandas as pd

class AgentTest_create_table(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _table_info(self, table_name):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(f"PRAGMA table_info({table_name})")
            return cursor.fetchall()
        finally:
            conn.close()

    def _table_exists(self, table_name):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table_name,)
            )
            return cursor.fetchone() is not None
        finally:
            conn.close()

    def test_create_table_1(self):
        # create_table should create a new table in the database.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        self.assertTrue(self._table_exists('user'))

    def test_create_table_2(self):
        # The table should contain id, key1 and key2 as its column names.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        columns = [row[1] for row in self._table_info('user')]
        self.assertEqual(columns, ['id', 'name', 'age'])

    def test_create_table_3(self):
        # id should be INTEGER, key1 should be TEXT and key2 should be INTEGER.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        types = {row[1]: row[2].upper() for row in self._table_info('user')}
        self.assertEqual(types['id'], 'INTEGER')
        self.assertEqual(types['name'], 'TEXT')
        self.assertEqual(types['age'], 'INTEGER')

    def test_create_table_4(self):
        # id should be the PRIMARY KEY of the table.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        pk_columns = [row[1] for row in self._table_info('user') if row[5] > 0]
        self.assertEqual(pk_columns, ['id'])

    def test_create_table_5(self):
        # Creating a table that already exists should not raise an error
        # and the table should still exist afterwards.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.create_table('user', 'name', 'age')
        self.assertTrue(self._table_exists('user'))
        columns = [row[1] for row in self._table_info('user')]
        self.assertEqual(columns, ['id', 'name', 'age'])

import unittest

import os

import shutil

import sqlite3

import tempfile

import pandas as pd

class AgentTest_insert_into_database(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _fetch_rows(self, table_name):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(f"SELECT * FROM {table_name} ORDER BY id")
            return cursor.fetchall()
        finally:
            conn.close()

    def test_insert_into_database_1(self):
        # Inserting a list of two dictionaries should add two rows to the table.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
        rows = self._fetch_rows('user')
        self.assertEqual(len(rows), 2)

    def test_insert_into_database_2(self):
        # Each dictionary should be stored as a row with its values in the
        # matching columns (name as TEXT, age as INTEGER).
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
        rows = self._fetch_rows('user')
        self.assertEqual([(row[1], row[2]) for row in rows],
                         [('John', 25), ('Alice', 30)])

    def test_insert_into_database_3(self):
        # The id column should be assigned automatically as a distinct INTEGER
        # primary key for each inserted row.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
        ids = [row[0] for row in self._fetch_rows('user')]
        self.assertEqual(len(ids), 2)
        self.assertTrue(all(isinstance(i, int) for i in ids))
        self.assertEqual(len(set(ids)), 2)

    def test_insert_into_database_4(self):
        # Inserting data into a table that already has rows should append the
        # new rows and keep the existing ones.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25}
        ])
        db.insert_into_database('user', [
            {'name': 'Alice', 'age': 30}
        ])
        rows = self._fetch_rows('user')
        self.assertEqual([(row[1], row[2]) for row in rows],
                         [('John', 25), ('Alice', 30)])

    def test_insert_into_database_5(self):
        # Values should be mapped to columns by dictionary key, not by the
        # order in which the keys appear in each dictionary.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'age': 41, 'name': 'Bob'}
        ])
        rows = self._fetch_rows('user')
        self.assertEqual(len(rows), 1)
        self.assertEqual((rows[0][1], rows[0][2]), ('Bob', 41))

import os

import shutil

import tempfile

import unittest

class AgentTest_search_database(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_search_database_1(self):
        # Searching for a name that exists should return a list containing the
        # matching row as a tuple, e.g. [(1, 'John', 25)].
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25}
        ])
        result = db.search_database('user', 'John')
        self.assertEqual(result, [(1, 'John', 25)])

    def test_search_database_2(self):
        # When several rows share the searched name, all of them should be
        # returned, and rows with other names should be excluded.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30},
            {'name': 'John', 'age': 40}
        ])
        result = db.search_database('user', 'John')
        self.assertEqual(len(result), 2)
        self.assertEqual(sorted(result), [(1, 'John', 25), (3, 'John', 40)])

    def test_search_database_3(self):
        # When no row matches the given name, the method should return None.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
        result = db.search_database('user', 'Bob')
        self.assertIsNone(result)

    def test_search_database_4(self):
        # The return value should be a list whose elements are tuples
        # representing the matching rows.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'Alice', 'age': 30}
        ])
        result = db.search_database('user', 'Alice')
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(row, tuple) for row in result))

    def test_search_database_5(self):
        # Searching an empty table (no rows at all) should return None,
        # because there are no rows with a matching name.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        result = db.search_database('user', 'John')
        self.assertIsNone(result)

import unittest

import os

import shutil

import sqlite3

import tempfile

class AgentTest_delete_from_database(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _fetch_names(self, table_name):
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute(f"SELECT name FROM {table_name} ORDER BY id")
            return [row[0] for row in cursor.fetchall()]
        finally:
            conn.close()

    def test_delete_from_database_1(self):
        # Deleting a name should remove the row with that name and keep the other rows.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
        db.delete_from_database('user', 'John')
        self.assertEqual(self._fetch_names('user'), ['Alice'])

    def test_delete_from_database_2(self):
        # All rows sharing the given name should be deleted, while rows with other names remain.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30},
            {'name': 'John', 'age': 40}
        ])
        db.delete_from_database('user', 'John')
        self.assertEqual(self._fetch_names('user'), ['Alice'])

    def test_delete_from_database_3(self):
        # Deleting a name that matches no row should leave the table unchanged.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
        db.delete_from_database('user', 'Bob')
        self.assertEqual(self._fetch_names('user'), ['John', 'Alice'])

    def test_delete_from_database_4(self):
        # Deleting from one table should not remove rows from another table.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.create_table('member', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25}
        ])
        db.insert_into_database('member', [
            {'name': 'John', 'age': 25}
        ])
        db.delete_from_database('user', 'John')
        self.assertEqual(self._fetch_names('user'), [])
        self.assertEqual(self._fetch_names('member'), ['John'])

    def test_delete_from_database_5(self):
        # After deleting a name, searching for that name should return None.
        db = DatabaseProcessor(self.db_path)
        db.create_table('user', 'name', 'age')
        db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
        db.delete_from_database('user', 'John')
        self.assertIsNone(db.search_database('user', 'John'))