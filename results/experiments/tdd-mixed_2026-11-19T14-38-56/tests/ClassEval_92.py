import unittest
import os
from tempfile import gettempdir




class UserLoginDBTestInsertUser(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(gettempdir(), 'test_db.db')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )
                """
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
        self.db = UserLoginDB(self.db_path)

    def tearDown(self):
        self.db.connection.close()
        os.unlink(self.db_path)

    def test_insert_user_1(self):
        self.db.insert_user('user1', 'pass1')
        user = self.db.search_user_by_username('user1')
        self.assertIsNotNone(user)
        self.assertEqual(user[0], 'user1')
        self.assertEqual(user[1], 'pass1')

    def test_insert_user_2(self):
        self.db.insert_user('user2', 'pass2')
        user = self.db.search_user_by_username('user2')
        self.assertIsNotNone(user)
        self.assertEqual(user[0], 'user2')
        self.assertEqual(user[1], 'pass2')

    def test_insert_user_3(self):
        self.db.insert_user('user3', 'pass3')
        user = self.db.search_user_by_username('user3')
        self.assertIsNotNone(user)
        self.assertEqual(user[0], 'user3')
        self.assertEqual(user[1], 'pass3')

import unittest

import os

import sqlite3

from tempfile import gettempdir

class AgentTest_insert_user(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(gettempdir(), 'test_insert_user_db.db')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )
                """
        cursor.execute(create_table_query)
        conn.commit()
        conn.close()
        self.db = UserLoginDB(self.db_path)

    def tearDown(self):
        self.db.connection.close()
        os.unlink(self.db_path)

    def test_insert_user_1(self):
        result = self.db.insert_user('user1', 'pass1')
        self.assertIsNone(result)

    def test_insert_user_2(self):
        self.db.insert_user('alice', 'a1')
        self.db.insert_user('bob', 'b2')
        self.db.cursor.execute("SELECT username, password FROM users ORDER BY username")
        rows = self.db.cursor.fetchall()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows, [('alice', 'a1'), ('bob', 'b2')])

class UserLoginDBTestSearchUserByUsername(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(gettempdir(), 'test_db.db')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )
                """
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
        self.db = UserLoginDB(self.db_path)

    def tearDown(self):
        self.db.connection.close()
        os.unlink(self.db_path)

    def test_search_user_by_username_1(self):
        self.db.insert_user('user1', 'pass1')
        user = self.db.search_user_by_username('user1')
        self.assertIsNotNone(user)
        self.assertEqual(user[0], 'user1')
        self.assertEqual(user[1], 'pass1')

    def test_search_user_by_username_2(self):
        self.db.insert_user('user2', 'pass2')
        user = self.db.search_user_by_username('user2')
        self.assertIsNotNone(user)
        self.assertEqual(user[0], 'user2')
        self.assertEqual(user[1], 'pass2')

    def test_search_user_by_username_3(self):
        self.db.insert_user('user3', 'pass3')
        user = self.db.search_user_by_username('user3')
        self.assertIsNotNone(user)
        self.assertEqual(user[0], 'user3')
        self.assertEqual(user[1], 'pass3')

import unittest

import os

import sqlite3

from tempfile import gettempdir

class AgentTest_search_user_by_username(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(gettempdir(), 'test_search_user_by_username_db.db')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )
                """
        cursor.execute(create_table_query)
        conn.commit()
        conn.close()
        self.db = UserLoginDB(self.db_path)

    def tearDown(self):
        self.db.connection.close()
        os.unlink(self.db_path)

    def test_search_user_by_username_1(self):
        self.db.insert_user('user1', 'pass1')
        result = self.db.search_user_by_username('nobody')
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])

    def test_search_user_by_username_2(self):
        self.db.insert_user('user1', 'pass1')
        self.db.insert_user('user2', 'pass2')
        result = self.db.search_user_by_username('user2')
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], tuple)
        self.assertEqual(result[0], ('user2', 'pass2'))

class UserLoginDBTestDeleteUserByUsername(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(gettempdir(), 'test_db.db')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )
                """
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
        self.db = UserLoginDB(self.db_path)

    def tearDown(self):
        self.db.connection.close()
        os.unlink(self.db_path)

    def test_delete_user_by_username_1(self):
        self.db.insert_user('user1', 'pass1')
        self.db.delete_user_by_username('user1')
        user = self.db.search_user_by_username('user1')
        self.assertIsNone(user)

    def test_delete_user_by_username_2(self):
        self.db.insert_user('user2', 'pass2')
        self.db.delete_user_by_username('user2')
        user = self.db.search_user_by_username('user2')
        self.assertIsNone(user)

    def test_delete_user_by_username_3(self):
        self.db.insert_user('user3', 'pass3')
        self.db.delete_user_by_username('user3')
        user = self.db.search_user_by_username('user3')
        self.assertIsNone(user)

import unittest

import os

import sqlite3

from tempfile import gettempdir

class AgentTest_delete_user_by_username(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(gettempdir(), 'test_delete_user_by_username_db.db')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )
                """
        cursor.execute(create_table_query)
        conn.commit()
        conn.close()
        self.db = UserLoginDB(self.db_path)

    def tearDown(self):
        self.db.connection.close()
        os.unlink(self.db_path)

    def test_delete_user_by_username_1(self):
        self.db.insert_user('user1', 'pass1')
        self.db.insert_user('user2', 'pass2')
        self.db.delete_user_by_username('user1')
        self.db.cursor.execute("SELECT username, password FROM users ORDER BY username")
        rows = self.db.cursor.fetchall()
        self.assertEqual(rows, [('user2', 'pass2')])

    def test_delete_user_by_username_2(self):
        self.db.insert_user('user1', 'pass1')
        result = self.db.delete_user_by_username('ghost')
        self.assertIsNone(result)
        self.db.cursor.execute("SELECT username, password FROM users")
        rows = self.db.cursor.fetchall()
        self.assertEqual(rows, [('user1', 'pass1')])

class UserLoginDBTestValidateUserLogin(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(gettempdir(), 'test_db.db')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )
                """
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
        self.db = UserLoginDB(self.db_path)

    def tearDown(self):
        self.db.connection.close()
        os.unlink(self.db_path)

    def test_validate_user_login_1(self):
        self.db.insert_user('user1', 'pass1')
        valid = self.db.validate_user_login('user1', 'pass1')
        self.assertTrue(valid)

    def test_validate_user_login_2(self):
        self.db.insert_user('user1', 'pass1')
        invalid = self.db.validate_user_login('user1', 'wrongpass')
        self.assertFalse(invalid)

    def test_validate_user_login_3(self):
        valid = self.db.validate_user_login('nonexistentuser', 'somepass')
        self.assertFalse(valid)

import unittest

import os

import sqlite3

from tempfile import gettempdir

class AgentTest_validate_user_login(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(gettempdir(), 'test_validate_user_login_db.db')
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT,
                    password TEXT
                )
                """
        cursor.execute(create_table_query)
        conn.commit()
        conn.close()
        self.db = UserLoginDB(self.db_path)

    def tearDown(self):
        self.db.connection.close()
        os.unlink(self.db_path)

    def test_validate_user_login_1(self):
        self.db.insert_user('user1', 'pass1')
        result = self.db.validate_user_login('user1', 'pass1')
        self.assertIsInstance(result, bool)
        self.assertIs(result, True)

    def test_validate_user_login_2(self):
        self.db.insert_user('alice', 'a1')
        self.db.insert_user('bob', 'b2')
        self.assertIs(self.db.validate_user_login('alice', 'b2'), False)
        self.assertIs(self.db.validate_user_login('bob', 'a1'), False)
        self.assertIs(self.db.validate_user_login('alice', 'a1'), True)
        self.assertIs(self.db.validate_user_login('bob', 'b2'), True)