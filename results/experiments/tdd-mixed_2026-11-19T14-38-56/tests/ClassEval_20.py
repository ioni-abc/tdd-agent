import unittest



class ChatTestAddUser(unittest.TestCase):
    def test_add_user(self):
        chat = Chat()
        self.assertEqual(chat.add_user('John'), True)
        self.assertEqual(chat.users, {'John': []})

    def test_add_user_2(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertEqual(chat.add_user('John'), False)
        self.assertEqual(chat.users, {'John': []})

    def test_add_user_3(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertEqual(chat.add_user('Mary'), True)
        self.assertEqual(chat.users, {'John': [], 'Mary': []})

import unittest

class AgentTest_add_user(unittest.TestCase):
    def test_add_user_1(self):
        chat = Chat()
        self.assertEqual(chat.add_user('John'), True)
        self.assertEqual(chat.add_user('Mary'), True)
        self.assertEqual(chat.add_user('Tom'), True)
        self.assertEqual(chat.users, {'John': [], 'Mary': [], 'Tom': []})

    def test_add_user_2(self):
        chat = Chat()
        self.assertEqual(chat.add_user('John'), True)
        self.assertEqual(chat.add_user('John'), False)
        self.assertEqual(chat.users, {'John': []})

class ChatTestRemoveUser(unittest.TestCase):
    def test_remove_user(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertEqual(chat.remove_user('John'), True)
        self.assertEqual(chat.users, {})

    def test_remove_user_2(self):
        chat = Chat()
        self.assertEqual(chat.remove_user('John'), False)
        self.assertEqual(chat.users, {})

    def test_remove_user_3(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertEqual(chat.remove_user('John'), True)
        self.assertEqual(chat.users, {'Mary': []})

import unittest

class AgentTest_remove_user(unittest.TestCase):
    def test_remove_user_1(self):
        chat = Chat()
        chat.users = {'John': []}
        self.assertEqual(chat.remove_user('John'), True)
        self.assertEqual(chat.remove_user('John'), False)
        self.assertEqual(chat.users, {})

    def test_remove_user_2(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertEqual(chat.remove_user('Tom'), False)
        self.assertEqual(chat.users, {'John': [], 'Mary': []})

class ChatTestSendMessage(unittest.TestCase):
    def test_send_message(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(chat.send_message('John', 'Mary', 'Hello'), True)
        self.assertEqual(chat.users, {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}], 'Mary': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]})

    def test_send_message_2(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertEqual(chat.send_message('John', 'Tom', 'Hello'), False)
        self.assertEqual(chat.users, {'John': [], 'Mary': []})

    def test_send_message_3(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertEqual(chat.send_message('Amy', 'Mary', 'Hello'), False)
        self.assertEqual(chat.users, {'John': [], 'Mary': []})

import unittest

class AgentTest_send_message(unittest.TestCase):
    def test_send_message_1(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertEqual(chat.send_message('Amy', 'Tom', 'Hello'), False)
        self.assertEqual(chat.users, {'John': [], 'Mary': []})

    def test_send_message_2(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertEqual(chat.send_message('John', 'Mary', 'Hello'), True)
        self.assertEqual(chat.send_message('Mary', 'John', 'Hi'), True)
        expected = [('John', 'Mary', 'Hello'), ('Mary', 'John', 'Hi')]
        self.assertEqual(
            [(m['sender'], m['receiver'], m['message']) for m in chat.users['John']],
            expected
        )
        self.assertEqual(
            [(m['sender'], m['receiver'], m['message']) for m in chat.users['Mary']],
            expected
        )

class ChatTestGetMessages(unittest.TestCase):
    def test_get_messages(self):
        chat = Chat()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]}
        self.assertEqual(chat.get_messages('John'), [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}])

    def test_get_messages_2(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertEqual(chat.get_messages('John'), [])

    def test_get_messages_3(self):
        chat = Chat()
        chat.users = {'John': [], 'Mary': []}
        self.assertEqual(chat.get_messages('Amy'), [])

import unittest

from datetime import datetime

class AgentTest_get_messages(unittest.TestCase):
    def test_get_messages_1(self):
        chat = Chat()
        first = {'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}
        second = {'sender': 'Mary', 'receiver': 'John', 'message': 'Hi', 'timestamp': '2023-01-01 00:01:00'}
        third = {'sender': 'John', 'receiver': 'Mary', 'message': 'How are you?', 'timestamp': '2023-01-01 00:02:00'}
        chat.users = {'John': [first, second, third], 'Mary': []}
        self.assertEqual(chat.get_messages('John'), [first, second, third])

    def test_get_messages_2(self):
        chat = Chat()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        chat.users = {'John': [{'sender': 'Mary', 'receiver': 'John', 'message': 'Hi', 'timestamp': timestamp}]}
        messages = chat.get_messages('John')
        self.assertIsInstance(messages, list)
        self.assertEqual(len(messages), 1)
        self.assertIsInstance(messages[0], dict)
        self.assertEqual(set(messages[0].keys()), {'sender', 'receiver', 'message', 'timestamp'})
        self.assertEqual(messages[0]['sender'], 'Mary')
        self.assertEqual(messages[0]['receiver'], 'John')
        self.assertEqual(messages[0]['message'], 'Hi')
        self.assertEqual(messages[0]['timestamp'], timestamp)