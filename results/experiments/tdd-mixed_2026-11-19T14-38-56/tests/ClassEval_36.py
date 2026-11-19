import unittest



class EmailClientTestFetch(unittest.TestCase):
    def test_fetch(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receiver.inbox = [
            {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
             'time': timestamp, 'state': 'unread'}]
        self.assertEqual(receiver.fetch(), {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time':timestamp, 'state': 'read'})

    def test_fetch_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(receiver.fetch(),None)

    def test_fetch_3(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receiver.inbox = [
            {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
             'time': timestamp, 'state': 'read'}]
        self.assertEqual(receiver.fetch(), None)

import unittest

from datetime import datetime

class AgentTest_fetch(unittest.TestCase):
    def test_fetch_1(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receiver.inbox = [
            {'sender': 'old@example.com', 'receiver': 'receiver@example.com', 'content': 'Old', 'size': 5,
             'time': timestamp, 'state': 'read'},
            {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
             'time': timestamp, 'state': 'unread'},
            {'sender': 'other@example.com', 'receiver': 'receiver@example.com', 'content': 'Later', 'size': 7,
             'time': timestamp, 'state': 'unread'}]
        self.assertEqual(receiver.fetch(), {'sender': 'sender@example.com', 'receiver': 'receiver@example.com',
                                            'content': 'Hello', 'size': 10, 'time': timestamp, 'state': 'read'})
        self.assertEqual(receiver.inbox[0]['state'], 'read')
        self.assertEqual(receiver.inbox[1]['state'], 'read')
        self.assertEqual(receiver.inbox[2]['state'], 'unread')

    def test_fetch_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receiver.inbox = [
            {'sender': 'first@example.com', 'receiver': 'receiver@example.com', 'content': 'First', 'size': 4,
             'time': timestamp, 'state': 'unread'},
            {'sender': 'second@example.com', 'receiver': 'receiver@example.com', 'content': 'Second', 'size': 6,
             'time': timestamp, 'state': 'unread'}]
        self.assertEqual(receiver.fetch(), {'sender': 'first@example.com', 'receiver': 'receiver@example.com',
                                            'content': 'First', 'size': 4, 'time': timestamp, 'state': 'read'})
        self.assertEqual(receiver.fetch(), {'sender': 'second@example.com', 'receiver': 'receiver@example.com',
                                            'content': 'Second', 'size': 6, 'time': timestamp, 'state': 'read'})
        self.assertEqual(receiver.fetch(), None)

class EmailClientTestGetOccupiedSize(unittest.TestCase):
    def test_get_occupied_size(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': datetime.now, 'state': 'unread'}]
        self.assertEqual(sender.get_occupied_size(), 10)

    def test_get_occupied_size_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        sender.inbox =[]
        self.assertEqual(sender.get_occupied_size(), 0)

    def test_get_occupied_size_3(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        sender.inbox = [
            {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 20,
             'time': datetime.now, 'state': 'unread'}]
        self.assertEqual(sender.get_occupied_size(), 20)

import unittest

class AgentTest_get_occupied_size(unittest.TestCase):
    def test_get_occupied_size_1(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'First', 'size': 5,
             'time': '2023-07-13 11:36:40', 'state': 'unread'},
            {'sender': 'other@example.com', 'receiver': 'receiver@example.com', 'content': 'Second', 'size': 7,
             'time': '2023-07-13 11:37:00', 'state': 'read'},
            {'sender': 'third@example.com', 'receiver': 'receiver@example.com', 'content': 'Third', 'size': 3,
             'time': '2023-07-13 11:38:20', 'state': 'unread'}]
        self.assertEqual(receiver.get_occupied_size(), 15)

    def test_get_occupied_size_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Small', 'size': 2.5,
             'time': '2023-07-13 11:36:40', 'state': 'unread'},
            {'sender': 'other@example.com', 'receiver': 'receiver@example.com', 'content': 'Tiny', 'size': 1.25,
             'time': '2023-07-13 11:37:00', 'state': 'unread'},
            {'sender': 'third@example.com', 'receiver': 'receiver@example.com', 'content': 'Half', 'size': 0.5,
             'time': '2023-07-13 11:38:20', 'state': 'read'}]
        self.assertEqual(receiver.get_occupied_size(), 4.25)

class EmailClientTestIsFullWithOneMoreEmail(unittest.TestCase):
    def test_is_full_with_one_more_email(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        self.assertFalse(receiver.is_full_with_one_more_email(10))

    def test_is_full_with_one_more_email_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 0)
        self.assertTrue(receiver.is_full_with_one_more_email(10))

    def test_is_full_with_one_more_email_3(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 10)
        self.assertFalse(receiver.is_full_with_one_more_email(10))

import unittest

class AgentTest_is_full_with_one_more_email(unittest.TestCase):
    def test_is_full_with_one_more_email_1(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 20)
        receiver.inbox = [
            {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Existing', 'size': 15,
             'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        self.assertTrue(receiver.is_full_with_one_more_email(10))

    def test_is_full_with_one_more_email_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 20)
        receiver.inbox = [
            {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Existing', 'size': 5,
             'time': '2023-07-13 11:36:40', 'state': 'read'}]
        self.assertFalse(receiver.is_full_with_one_more_email(10))

class EmailClientTestClearInbox(unittest.TestCase):
    def test_clear_inbox(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        receiver.clear_inbox(30)
        self.assertEqual(receiver.inbox, [{'size': 15}])

    def test_clear_inbox_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('', 50)
        receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        self.assertEqual(receiver.clear_inbox(30),None)
        self.assertEqual(receiver.inbox, [{'size': 10},{'size': 20},{'size': 15}])

    def test_clear_inbox_3(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'size': 10}, {'size': 20}, {'size': 15}]
        self.assertEqual(receiver.clear_inbox(50), None)

import unittest

class AgentTest_clear_inbox(unittest.TestCase):
    def test_clear_inbox_1(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'size': 10}, {'size': 20}, {'size': 15}]
        receiver.clear_inbox(40)
        self.assertEqual(receiver.inbox, [])

    def test_clear_inbox_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'size': 10}, {'size': 20}, {'size': 15}]
        self.assertEqual(receiver.clear_inbox(1), None)
        self.assertEqual(receiver.inbox, [{'size': 10}, {'size': 20}, {'size': 15}])

class EmailClientTestSendTo(unittest.TestCase):
    def test_send_to(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertTrue(sender.send_to(receiver, 'Hello', 10))
        self.assertEqual(receiver.inbox[0], {"sender": 'sender@example.com','receiver': 'receiver@example.com','content': 'Hello','size': 10,'time': timestamp,'state': 'unread'})

    def test_send_to_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 0)
        self.assertFalse(sender.send_to(receiver, 'Hello', 10))

    def test_send_to_3(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 50, 'time': '2021-01-01 00:00:00', 'state': 'unread'}]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertFalse(sender.send_to(receiver, 'Hello', 10))
        self.assertEqual(receiver.inbox, [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 50, 'time': '2021-01-01 00:00:00', 'state': 'unread'}])

import unittest

from datetime import datetime

class AgentTest_send_to(unittest.TestCase):
    def test_send_to_1(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        receiver.inbox = [
            {'sender': 'old@example.com', 'receiver': 'receiver@example.com', 'content': 'Existing', 'size': 40,
             'time': '2021-01-01 00:00:00', 'state': 'read'}]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertTrue(sender.send_to(receiver, 'Exact', 10))
        self.assertEqual(len(receiver.inbox), 2)
        self.assertEqual(receiver.inbox[1], {'sender': 'sender@example.com', 'receiver': 'receiver@example.com',
                                             'content': 'Exact', 'size': 10, 'time': timestamp, 'state': 'unread'})

    def test_send_to_2(self):
        sender = EmailClient('sender@example.com', 100)
        receiver = EmailClient('receiver@example.com', 50)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertTrue(sender.send_to(receiver, 'First', 10))
        self.assertTrue(sender.send_to(receiver, 'Second', 20))
        self.assertEqual(len(receiver.inbox), 2)
        self.assertEqual(receiver.inbox[0], {'sender': 'sender@example.com', 'receiver': 'receiver@example.com',
                                             'content': 'First', 'size': 10, 'time': timestamp, 'state': 'unread'})
        self.assertEqual(receiver.inbox[1], {'sender': 'sender@example.com', 'receiver': 'receiver@example.com',
                                             'content': 'Second', 'size': 20, 'time': timestamp, 'state': 'unread'})