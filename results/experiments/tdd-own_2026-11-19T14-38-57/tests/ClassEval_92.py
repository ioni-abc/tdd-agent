import unittest


import unittest

import sqlite3

class AgentTest_insert_user(unittest.TestCase):

    def setUp(self):
        self.db = UserLoginDB(":memory:")
        self.db.create_table()

    def tearDown(self):
        self.db.connection.close()

    def test_insert_user_1(self):
        # insert_user is documented to return None
        result = self.db.insert_user('user1', 'pass1')
        self.assertIsNone(result)

    def test_insert_user_2(self):
        # After inserting, the user should be found in the "users" table
        self.db.insert_user('user1', 'pass1')
        rows = self.db.search_user_by_username('user1')
        self.assertEqual(len(rows), 1)

    def test_insert_user_3(self):
        # The stored row should contain the inserted username and password
        self.db.insert_user('user1', 'pass1')
        rows = self.db.search_user_by_username('user1')
        self.assertIn('user1', rows[0])
        self.assertIn('pass1', rows[0])

    def test_insert_user_4(self):
        # A user inserted with a password can log in with that password
        self.db.insert_user('user1', 'pass1')
        self.assertTrue(self.db.validate_user_login('user1', 'pass1'))

    def test_insert_user_5(self):
        # Multiple users can be inserted; each keeps its own password
        self.db.insert_user('user1', 'pass1')
        self.db.insert_user('user2', 'pass2')
        self.assertTrue(self.db.validate_user_login('user1', 'pass1'))
        self.assertTrue(self.db.validate_user_login('user2', 'pass2'))
        self.assertFalse(self.db.validate_user_login('user2', 'pass1'))

import unittest

import sqlite3

class AgentTest_search_user_by_username(unittest.TestCase):

    def setUp(self):
        self.db = UserLoginDB(":memory:")
        self.db.create_table()

    def tearDown(self):
        self.db.connection.close()

    def test_search_user_by_username_1(self):
        # The result is documented to be a list
        result = self.db.search_user_by_username('user1')
        self.assertIsInstance(result, list)

    def test_search_user_by_username_2(self):
        # Searching for an inserted username returns exactly one matching row
        self.db.insert_user('user1', 'pass1')
        result = self.db.search_user_by_username('user1')
        self.assertEqual(len(result), 1)

    def test_search_user_by_username_3(self):
        # Each row is a tuple containing the stored username and password
        self.db.insert_user('user1', 'pass1')
        result = self.db.search_user_by_username('user1')
        self.assertIsInstance(result[0], tuple)
        self.assertIn('user1', result[0])
        self.assertIn('pass1', result[0])

    def test_search_user_by_username_4(self):
        # Searching for a username that was never inserted returns no rows
        self.db.insert_user('user1', 'pass1')
        result = self.db.search_user_by_username('unknown_user')
        self.assertEqual(len(result), 0)

    def test_search_user_by_username_5(self):
        # Only rows matching the username are returned when several users exist
        self.db.insert_user('user1', 'pass1')
        self.db.insert_user('user2', 'pass2')
        result = self.db.search_user_by_username('user1')
        self.assertEqual(len(result), 1)
        self.assertIn('user1', result[0])
        self.assertNotIn('user2', result[0])

import unittest

import sqlite3

class AgentTest_delete_user_by_username(unittest.TestCase):

    def setUp(self):
        self.db = UserLoginDB(":memory:")
        self.db.create_table()

    def tearDown(self):
        self.db.connection.close()

    def test_delete_user_by_username_1(self):
        # delete_user_by_username is documented to return None
        self.db.insert_user('user1', 'pass1')
        result = self.db.delete_user_by_username('user1')
        self.assertIsNone(result)

    def test_delete_user_by_username_2(self):
        # After deleting, the user should no longer be found in the "users" table
        self.db.insert_user('user1', 'pass1')
        self.db.delete_user_by_username('user1')
        rows = self.db.search_user_by_username('user1')
        self.assertEqual(len(rows), 0)

    def test_delete_user_by_username_3(self):
        # Deleting one user leaves the other users in the table untouched
        self.db.insert_user('user1', 'pass1')
        self.db.insert_user('user2', 'pass2')
        self.db.delete_user_by_username('user1')
        self.assertEqual(len(self.db.search_user_by_username('user1')), 0)
        self.assertEqual(len(self.db.search_user_by_username('user2')), 1)
        self.assertTrue(self.db.validate_user_login('user2', 'pass2'))

    def test_delete_user_by_username_4(self):
        # A deleted user can no longer log in, even with the correct password
        self.db.insert_user('user1', 'pass1')
        self.assertTrue(self.db.validate_user_login('user1', 'pass1'))
        self.db.delete_user_by_username('user1')
        self.assertFalse(self.db.validate_user_login('user1', 'pass1'))

    def test_delete_user_by_username_5(self):
        # After deletion, the username can be inserted again with a new password,
        # and only the new password is accepted
        self.db.insert_user('user1', 'pass1')
        self.db.delete_user_by_username('user1')
        self.db.insert_user('user1', 'newpass')
        self.assertTrue(self.db.validate_user_login('user1', 'newpass'))
        self.assertFalse(self.db.validate_user_login('user1', 'pass1'))

import unittest

class AgentTest_validate_user_login(unittest.TestCase):

    def setUp(self):
        self.db = UserLoginDB(":memory:")
        self.db.create_table()

    def tearDown(self):
        self.db.connection.close()

    def test_validate_user_login_1(self):
        # A user with the correct password can log in; the result is a bool True
        self.db.insert_user('user1', 'pass1')
        result = self.db.validate_user_login('user1', 'pass1')
        self.assertIs(result, True)

    def test_validate_user_login_2(self):
        # An existing user with a wrong password cannot log in; the result is a bool False
        self.db.insert_user('user1', 'pass1')
        result = self.db.validate_user_login('user1', 'wrongpass')
        self.assertIs(result, False)

    def test_validate_user_login_3(self):
        # A username that is not in the database cannot log in, even with a password
        self.db.insert_user('user1', 'pass1')
        result = self.db.validate_user_login('unknown_user', 'pass1')
        self.assertIs(result, False)

    def test_validate_user_login_4(self):
        # When the database has no users, no login can succeed
        result = self.db.validate_user_login('user1', 'pass1')
        self.assertIs(result, False)

    def test_validate_user_login_5(self):
        # A password belonging to another user is rejected, while each user's
        # own password is still accepted
        self.db.insert_user('user1', 'pass1')
        self.db.insert_user('user2', 'pass2')
        self.assertIs(self.db.validate_user_login('user1', 'pass2'), False)
        self.assertIs(self.db.validate_user_login('user1', 'pass1'), True)
        self.assertIs(self.db.validate_user_login('user2', 'pass2'), True)