import unittest


import unittest

class AgentTest_add_user(unittest.TestCase):

    def test_add_user_1(self):
        chat = Chat()
        self.assertTrue(chat.add_user('John'))

    def test_add_user_2(self):
        chat = Chat()
        chat.add_user('John')
        self.assertIn('John', chat.users)
        self.assertEqual(chat.users['John'], [])

    def test_add_user_3(self):
        chat = Chat()
        self.assertTrue(chat.add_user('John'))
        self.assertFalse(chat.add_user('John'))

    def test_add_user_4(self):
        chat = Chat()
        self.assertTrue(chat.add_user('John'))
        self.assertTrue(chat.add_user('Mary'))
        self.assertIn('John', chat.users)
        self.assertIn('Mary', chat.users)
        self.assertEqual(chat.users['John'], [])
        self.assertEqual(chat.users['Mary'], [])

    def test_add_user_5(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertFalse(chat.add_user('John'))
        self.assertTrue(chat.add_user('Mary'))
        self.assertIn('Mary', chat.users)

class AgentTest_remove_user(unittest.TestCase):

    def test_remove_user_1(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertTrue(chat.remove_user('John'))

    def test_remove_user_2(self):
        chat = Chat()
        self.assertFalse(chat.remove_user('John'))

    def test_remove_user_3(self):
        chat = Chat()
        chat.users = {'John': []}
        chat.remove_user('John')
        self.assertNotIn('John', chat.users)

    def test_remove_user_4(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertTrue(chat.remove_user('John'))
        self.assertFalse(chat.remove_user('John'))

    def test_remove_user_5(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertTrue(chat.remove_user('John'))
        self.assertNotIn('John', chat.users)
        self.assertIn('Mary', chat.users)

import unittest

class AgentTest_send_message(unittest.TestCase):

    def test_send_message_1(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertTrue(chat.send_message('John', 'Mary', 'Hello'))

    def test_send_message_2(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertFalse(chat.send_message('John', 'Tom', 'Hello'))

    def test_send_message_3(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertFalse(chat.send_message('Tom', 'John', 'Hello'))

    def test_send_message_4(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertFalse(chat.send_message('Tom', 'Mary', 'Hello'))

    def test_send_message_5(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertTrue(chat.send_message('John', 'John', 'Hello'))

import unittest

class AgentTest_get_messages(unittest.TestCase):

    def test_get_messages_1(self):
        chat = Chat()
        chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        self.assertEqual(
            chat.get_messages('John'),
            [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]
        )

    def test_get_messages_2(self):
        chat = Chat()
        chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        self.assertEqual(chat.get_messages('Mary'), [])

    def test_get_messages_3(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertEqual(chat.get_messages('John'), [])

    def test_get_messages_4(self):
        chat = Chat()
        first = {'sender': 'John', 'receiver': 'Mary', 'message': 'Hi', 'timestamp': '2023-01-01 10:00:00'}
        second = {'sender': 'Mary', 'receiver': 'John', 'message': 'Hey', 'timestamp': '2023-01-01 10:05:00'}
        chat.users = {'John': [first, second], 'Mary': []}
        messages = chat.get_messages('John')
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0], first)
        self.assertEqual(messages[1], second)
        for message in messages:
            self.assertEqual(set(message.keys()), {'sender', 'receiver', 'message', 'timestamp'})

    def test_get_messages_5(self):
        chat = Chat()
        john_msg = {'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}
        mary_msg = {'sender': 'Mary', 'receiver': 'Tom', 'message': 'Bye', 'timestamp': '2023-01-02 00:00:00'}
        chat.users = {'John': [john_msg], 'Mary': [mary_msg], 'Tom': []}
        self.assertEqual(chat.get_messages('Mary'), [mary_msg])
        self.assertEqual(chat.get_messages('John'), [john_msg])
        self.assertEqual(chat.get_messages('Tom'), [])