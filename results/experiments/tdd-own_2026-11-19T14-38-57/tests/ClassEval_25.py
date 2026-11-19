import unittest


import json

import os

import tempfile

import unittest

class AgentTest_load_cookies(unittest.TestCase):

    def setUp(self):
        self._tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp_dir.cleanup)

    def _write_cookies_file(self, name, data):
        path = os.path.join(self._tmp_dir.name, name)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        return path

    def test_load_cookies_1(self):
        path = self._write_cookies_file('cookies.json',
                                        {'key1': 'value1', 'key2': 'value2'})
        cookies_util = CookiesUtil(path)
        self.assertEqual(cookies_util.load_cookies(),
                         {'key1': 'value1', 'key2': 'value2'})

    def test_load_cookies_2(self):
        path = self._write_cookies_file('cookies.json',
                                        {'key1': 'value1', 'key2': 'value2'})
        cookies_util = CookiesUtil(path)
        cookies_util.load_cookies()
        self.assertEqual(cookies_util.cookies,
                         {'key1': 'value1', 'key2': 'value2'})

    def test_load_cookies_3(self):
        path = self._write_cookies_file('cookies.json',
                                        {'session': 'abc123'})
        cookies_util = CookiesUtil(path)
        result = cookies_util.load_cookies()
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'session': 'abc123'})

    def test_load_cookies_4(self):
        path = self._write_cookies_file('empty_cookies.json', {})
        cookies_util = CookiesUtil(path)
        self.assertEqual(cookies_util.load_cookies(), {})

    def test_load_cookies_5(self):
        path = self._write_cookies_file('cookies.json', {'key1': 'old'})
        cookies_util = CookiesUtil(path)
        self.assertEqual(cookies_util.load_cookies(), {'key1': 'old'})

        self._write_cookies_file('cookies.json', {'key1': 'new', 'key3': 'value3'})
        self.assertEqual(cookies_util.load_cookies(),
                         {'key1': 'new', 'key3': 'value3'})

import json

import os

import tempfile

import unittest

class AgentTest__save_cookies(unittest.TestCase):

    def setUp(self):
        self._tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp_dir.cleanup)

    def _path(self, name):
        return os.path.join(self._tmp_dir.name, name)

    def test__save_cookies_1(self):
        cookies_util = CookiesUtil(self._path('cookies.json'))
        cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        self.assertTrue(cookies_util._save_cookies())

    def test__save_cookies_2(self):
        path = self._path('cookies.json')
        cookies_util = CookiesUtil(path)
        cookies_util.cookies = {'key1': 'value1', 'key2': 'value2'}
        cookies_util._save_cookies()
        with open(path, 'r', encoding='utf-8') as f:
            self.assertEqual(json.load(f),
                             {'key1': 'value1', 'key2': 'value2'})

    def test__save_cookies_3(self):
        path = self._path('cookies.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({'old': 'data'}, f)
        cookies_util = CookiesUtil(path)
        cookies_util.cookies = {'key1': 'new'}
        self.assertTrue(cookies_util._save_cookies())
        with open(path, 'r', encoding='utf-8') as f:
            self.assertEqual(json.load(f), {'key1': 'new'})

    def test__save_cookies_4(self):
        path = self._path(os.path.join('missing_dir', 'cookies.json'))
        cookies_util = CookiesUtil(path)
        cookies_util.cookies = {'key1': 'value1'}
        self.assertFalse(cookies_util._save_cookies())

    def test__save_cookies_5(self):
        path = self._path('cookies.json')
        cookies_util = CookiesUtil(path)
        cookies_util.cookies = {}
        self.assertTrue(cookies_util._save_cookies())
        self.assertEqual(CookiesUtil(path).load_cookies(), {})

import json

import os

import tempfile

import unittest

class AgentTest_get_cookies(unittest.TestCase):

    def setUp(self):
        self._tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp_dir.cleanup)

    def _path(self, name):
        return os.path.join(self._tmp_dir.name, name)

    def test_get_cookies_1(self):
        cookies_util = CookiesUtil(self._path('cookies.json'))
        cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
        self.assertEqual(cookies_util.cookies,
                         {'key1': 'value1', 'key2': 'value2'})

    def test_get_cookies_2(self):
        path = self._path('cookies.json')
        cookies_util = CookiesUtil(path)
        cookies_util.get_cookies({'cookies': {'key1': 'value1', 'key2': 'value2'}})
        with open(path, 'r', encoding='utf-8') as f:
            self.assertEqual(json.load(f),
                             {'key1': 'value1', 'key2': 'value2'})

    def test_get_cookies_3(self):
        path = self._path('cookies.json')
        cookies_util = CookiesUtil(path)
        cookies_util.get_cookies({'cookies': {'key1': 'old'}})
        cookies_util.get_cookies({'cookies': {'key1': 'new', 'key3': 'value3'}})
        self.assertEqual(cookies_util.cookies,
                         {'key1': 'new', 'key3': 'value3'})
        self.assertEqual(CookiesUtil(path).load_cookies(),
                         {'key1': 'new', 'key3': 'value3'})

    def test_get_cookies_4(self):
        path = self._path('cookies.json')
        cookies_util = CookiesUtil(path)
        cookies_util.get_cookies({'cookies': {}})
        self.assertEqual(cookies_util.cookies, {})
        with open(path, 'r', encoding='utf-8') as f:
            self.assertEqual(json.load(f), {})

    def test_get_cookies_5(self):
        path = self._path('cookies.json')
        cookies_util = CookiesUtil(path)
        cookies_util.get_cookies({'cookies': {'session': 'abc123'}})
        self.assertIsInstance(cookies_util.cookies, dict)
        self.assertEqual(CookiesUtil(path).load_cookies(), {'session': 'abc123'})