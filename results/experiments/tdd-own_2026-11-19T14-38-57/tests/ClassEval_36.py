import unittest


import unittest

from datetime import datetime

class AgentTest_fetch(unittest.TestCase):

    def test_fetch_1(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        result = receiver.fetch()
        self.assertEqual(result, {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'read'})

    def test_fetch_2(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        receiver.fetch()
        self.assertEqual(receiver.inbox[0]['state'], 'read')

    def test_fetch_3(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'Old', 'size': 5, 'time': '2023-07-13 10:00:00', 'state': 'read'},
            {'sender': 'b@example.com', 'receiver': 'receiver@example.com', 'content': 'First', 'size': 10, 'time': '2023-07-13 11:00:00', 'state': 'unread'},
            {'sender': 'c@example.com', 'receiver': 'receiver@example.com', 'content': 'Second', 'size': 12, 'time': '2023-07-13 12:00:00', 'state': 'unread'},
        ]
        result = receiver.fetch()
        self.assertEqual(result['content'], 'First')
        self.assertEqual(receiver.inbox[1]['state'], 'read')
        self.assertEqual(receiver.inbox[2]['state'], 'unread')

    def test_fetch_4(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 10, 'time': '2023-07-13 11:00:00', 'state': 'unread'},
            {'sender': 'b@example.com', 'receiver': 'receiver@example.com', 'content': 'B', 'size': 10, 'time': '2023-07-13 12:00:00', 'state': 'unread'},
        ]
        first = receiver.fetch()
        second = receiver.fetch()
        self.assertEqual(first['content'], 'A')
        self.assertEqual(second['content'], 'B')

    def test_fetch_5(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        result = receiver.fetch()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['sender'], 'sender@example.com')
        self.assertEqual(result['receiver'], 'receiver@example.com')
        self.assertEqual(result['content'], 'Hello')
        self.assertEqual(result['size'], 10)
        self.assertEqual(result['time'], '2023-07-13 11:36:40')

import unittest

import unittest

from datetime import datetime

class AgentTest_get_occupied_size(unittest.TestCase):

    def test_get_occupied_size_1(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': datetime.now, 'state': 'unread'}]
        self.assertEqual(sender.get_occupied_size(), 10)

    def test_get_occupied_size_2(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = []
        self.assertEqual(receiver.get_occupied_size(), 0)

    def test_get_occupied_size_3(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 10, 'time': '2023-07-13 10:00:00', 'state': 'unread'},
            {'sender': 'b@example.com', 'receiver': 'receiver@example.com', 'content': 'B', 'size': 20, 'time': '2023-07-13 11:00:00', 'state': 'read'},
            {'sender': 'c@example.com', 'receiver': 'receiver@example.com', 'content': 'C', 'size': 15, 'time': '2023-07-13 12:00:00', 'state': 'unread'},
        ]
        self.assertEqual(receiver.get_occupied_size(), 45)

    def test_get_occupied_size_4(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 2.5, 'time': '2023-07-13 10:00:00', 'state': 'unread'},
            {'sender': 'b@example.com', 'receiver': 'receiver@example.com', 'content': 'B', 'size': 3.5, 'time': '2023-07-13 11:00:00', 'state': 'unread'},
        ]
        self.assertEqual(receiver.get_occupied_size(), 6.0)

    def test_get_occupied_size_5(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 10, 'time': '2023-07-13 10:00:00', 'state': 'read'},
            {'sender': 'b@example.com', 'receiver': 'receiver@example.com', 'content': 'B', 'size': 10, 'time': '2023-07-13 11:00:00', 'state': 'read'},
        ]
        result = receiver.get_occupied_size()
        self.assertIsInstance(result, (int, float))
        self.assertEqual(result, 20)

import unittest

from datetime import datetime

class AgentTest_is_full_with_one_more_email(unittest.TestCase):

    def test_is_full_with_one_more_email_1(self):
        receiver = EmailClient('receiver@example.com', 50)
        self.assertIs(receiver.is_full_with_one_more_email(10), False)

    def test_is_full_with_one_more_email_2(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 45, 'time': '2023-07-13 10:00:00', 'state': 'unread'},
        ]
        self.assertIs(receiver.is_full_with_one_more_email(10), True)

    def test_is_full_with_one_more_email_3(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 40, 'time': '2023-07-13 10:00:00', 'state': 'read'},
        ]
        self.assertIs(receiver.is_full_with_one_more_email(10), True)

    def test_is_full_with_one_more_email_4(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 10, 'time': '2023-07-13 10:00:00', 'state': 'unread'},
            {'sender': 'b@example.com', 'receiver': 'receiver@example.com', 'content': 'B', 'size': 10, 'time': '2023-07-13 11:00:00', 'state': 'read'},
        ]
        self.assertIs(receiver.is_full_with_one_more_email(25), False)

    def test_is_full_with_one_more_email_5(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 2.5, 'time': '2023-07-13 10:00:00', 'state': 'unread'},
            {'sender': 'b@example.com', 'receiver': 'receiver@example.com', 'content': 'B', 'size': 3.5, 'time': '2023-07-13 11:00:00', 'state': 'unread'},
        ]
        self.assertIs(receiver.is_full_with_one_more_email(43.5), False)
        self.assertIs(receiver.is_full_with_one_more_email(44.5), True)

import unittest

class AgentTest_clear_inbox(unittest.TestCase):

    def test_clear_inbox_1(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'size': 10}, {'size': 20}, {'size': 15}]
        receiver.clear_inbox(30)
        self.assertEqual(receiver.inbox, [{'size': 15}])

    def test_clear_inbox_2(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 10, 'time': '2023-07-13 10:00:00', 'state': 'read'},
            {'sender': 'b@example.com', 'receiver': 'receiver@example.com', 'content': 'B', 'size': 10, 'time': '2023-07-13 11:00:00', 'state': 'unread'},
        ]
        original = list(receiver.inbox)
        receiver.clear_inbox(30)
        self.assertEqual(receiver.inbox, original)

    def test_clear_inbox_3(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'size': 10}, {'size': 20}, {'size': 15}]
        result = receiver.clear_inbox(30)
        self.assertIsNone(result)

    def test_clear_inbox_4(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'content': 'A', 'size': 10},
            {'content': 'B', 'size': 10},
            {'content': 'C', 'size': 10},
            {'content': 'D', 'size': 10},
        ]
        receiver.clear_inbox(35)
        self.assertEqual(len(receiver.inbox), 1)
        self.assertEqual(receiver.inbox[0]['content'], 'D')

    def test_clear_inbox_5(self):
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'size': 10}, {'size': 20}]
        receiver.clear_inbox(50)
        self.assertEqual(receiver.inbox, [])

import unittest

from datetime import datetime

class AgentTest_send_to(unittest.TestCase):

    def test_send_to_1(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        result = sender.send_to(receiver, 'Hello', 10)
        self.assertIs(result, True)
        self.assertEqual(len(receiver.inbox), 1)

    def test_send_to_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        sender.send_to(receiver, 'Hello', 10)
        email = receiver.inbox[0]
        self.assertEqual(email['sender'], 'sender@example.com')
        self.assertEqual(email['receiver'], 'receiver@example.com')
        self.assertEqual(email['content'], 'Hello')
        self.assertEqual(email['size'], 10)
        self.assertEqual(email['state'], 'unread')
        self.assertIsInstance(email['time'], str)
        datetime.strptime(email['time'], '%Y-%m-%d %H:%M:%S')

    def test_send_to_3(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 45, 'time': '2023-07-13 10:00:00', 'state': 'unread'},
        ]
        result = sender.send_to(receiver, 'Hello', 10)
        self.assertIs(result, False)
        self.assertEqual(len(receiver.inbox), 1)
        self.assertEqual(receiver.inbox[0]['content'], 'A')

    def test_send_to_4(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        sender.send_to(receiver, 'First', 5)
        sender.send_to(receiver, 'Second', 7)
        self.assertEqual(len(receiver.inbox), 2)
        self.assertEqual(receiver.inbox[0]['content'], 'First')
        self.assertEqual(receiver.inbox[1]['content'], 'Second')

    def test_send_to_5(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'a@example.com', 'receiver': 'receiver@example.com', 'content': 'A', 'size': 30, 'time': '2023-07-13 10:00:00', 'state': 'read'},
        ]
        result = sender.send_to(receiver, 'Fits', 15)
        self.assertIs(result, True)
        self.assertEqual(len(receiver.inbox), 2)
        self.assertEqual(receiver.inbox[1]['content'], 'Fits')
        self.assertEqual(receiver.inbox[1]['size'], 15)