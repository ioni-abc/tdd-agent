import unittest


import unittest

class AgentTest_is_start_with(unittest.TestCase):

    def setUp(self):
        self.filter = AccessGatewayFilter()

    def test_is_start_with_1(self):
        self.assertTrue(self.filter.is_start_with('/api/data'))

    def test_is_start_with_2(self):
        self.assertTrue(self.filter.is_start_with('/login'))

    def test_is_start_with_3(self):
        self.assertFalse(self.filter.is_start_with('/home'))

    def test_is_start_with_4(self):
        self.assertFalse(self.filter.is_start_with('/static/api/data'))

    def test_is_start_with_5(self):
        self.assertFalse(self.filter.is_start_with('/logout'))

import unittest

import datetime

class AgentTest_get_jwt_user(unittest.TestCase):

    def setUp(self):
        self.filter = AccessGatewayFilter()

    def test_get_jwt_user_1(self):
        request = {'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1' + str(datetime.date.today())}}}
        self.assertEqual(self.filter.get_jwt_user(request), {'user': {'name': 'user1'}})

    def test_get_jwt_user_2(self):
        request = {'headers': {'Authorization': {'user': {'name': 'user2'}, 'jwt': 'user2' + str(datetime.date.today())}}}
        self.assertEqual(self.filter.get_jwt_user(request), {'user': {'name': 'user2'}})

    def test_get_jwt_user_3(self):
        request = {'path': '/api/data', 'method': 'GET'}
        self.assertIsNone(self.filter.get_jwt_user(request))

    def test_get_jwt_user_4(self):
        request = {'headers': {'Authorization': {'user': {'name': 'user1'}}}}
        self.assertIsNone(self.filter.get_jwt_user(request))

    def test_get_jwt_user_5(self):
        request = {'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1' + str(datetime.date.today())}}}
        result = self.filter.get_jwt_user(request)
        self.assertIsInstance(result, dict)
        self.assertIn('user', result)

import unittest

class AgentTest_set_current_user_info_and_log(unittest.TestCase):

    def setUp(self):
        self.filter = AccessGatewayFilter()

    def test_set_current_user_info_and_log_1(self):
        user = {'name': 'user1', 'address': '127.0.0.1'}
        self.assertIsNone(self.filter.set_current_user_info_and_log(user))

    def test_set_current_user_info_and_log_2(self):
        user = {'name': 'user1', 'address': '127.0.0.1'}
        try:
            self.filter.set_current_user_info_and_log(user)
        except Exception as exc:
            self.fail(f"set_current_user_info_and_log raised {exc!r} unexpectedly")

    def test_set_current_user_info_and_log_3(self):
        user = {'name': 'user1', 'address': '127.0.0.1'}
        with self.assertLogs(level='INFO') as cm:
            self.filter.set_current_user_info_and_log(user)
        self.assertGreaterEqual(len(cm.records), 1)

    def test_set_current_user_info_and_log_4(self):
        user = {'name': 'user1', 'address': '127.0.0.1'}
        with self.assertLogs(level='INFO') as cm:
            self.filter.set_current_user_info_and_log(user)
        self.assertTrue(any('user1' in message for message in cm.output))

    def test_set_current_user_info_and_log_5(self):
        user = {'name': 'user2', 'address': '192.168.0.1'}
        with self.assertLogs(level='INFO') as cm:
            result = self.filter.set_current_user_info_and_log(user)
        self.assertIsNone(result)
        self.assertTrue(any('user2' in message for message in cm.output))

import unittest

import datetime

class AgentTest_filter(unittest.TestCase):

    def setUp(self):
        self.filter = AccessGatewayFilter()

    def test_filter_1(self):
        self.assertTrue(self.filter.filter({'path': '/login', 'method': 'POST'}))

    def test_filter_2(self):
        result = self.filter.filter({'path': '/login', 'method': 'POST'})
        self.assertIsInstance(result, bool)

    def test_filter_3(self):
        request = {'path': '/api/data', 'method': 'GET'}
        result = self.filter.filter(request)
        self.assertIsInstance(result, bool)

    def test_filter_4(self):
        request = {
            'path': '/api/data',
            'method': 'GET',
            'headers': {'Authorization': {'user': {'name': 'user1'}, 'jwt': 'user1' + str(datetime.date.today())}}
        }
        self.assertTrue(self.filter.filter(request))

    def test_filter_5(self):
        request = {'path': '/api/data', 'method': 'GET'}
        self.assertFalse(self.filter.filter(request))