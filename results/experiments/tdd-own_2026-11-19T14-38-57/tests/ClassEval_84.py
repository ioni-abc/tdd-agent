import unittest


import unittest

import json

import os

import shutil

import tempfile

class AgentTest_read_file_as_json(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _make_file(self, name, content):
        path = os.path.join(self.temp_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path

    def test_read_file_as_json_1(self):
        path = self._make_file('test.json', '{\n    "name": "test",\n    "age": 12\n}')
        processor = TextFileProcessor(path)
        self.assertEqual(processor.read_file_as_json(), {'name': 'test', 'age': 12})

    def test_read_file_as_json_2(self):
        path = self._make_file('test.json', '{"name": "test", "age": 12}')
        processor = TextFileProcessor(path)
        self.assertIsInstance(processor.read_file_as_json(), dict)

    def test_read_file_as_json_3(self):
        path = self._make_file('number.txt', '42')
        processor = TextFileProcessor(path)
        result = processor.read_file_as_json()
        self.assertEqual(result, 42)
        self.assertIsInstance(result, int)

    def test_read_file_as_json_4(self):
        path = self._make_file('string.txt', '"Hello world"')
        processor = TextFileProcessor(path)
        result = processor.read_file_as_json()
        self.assertEqual(result, 'Hello world')
        self.assertIsInstance(result, str)

    def test_read_file_as_json_5(self):
        path = self._make_file('invalid.json', 'Hello world!')
        processor = TextFileProcessor(path)
        with self.assertRaises(ValueError):
            processor.read_file_as_json()

import unittest

import os

import shutil

import tempfile

class AgentTest_read_file(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _make_file(self, name, content):
        path = os.path.join(self.temp_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path

    def test_read_file_1(self):
        content = '{\n    "name": "test",\n    "age": 12\n}'
        path = self._make_file('test.json', content)
        processor = TextFileProcessor(path)
        self.assertEqual(processor.read_file(), content)

    def test_read_file_2(self):
        path = self._make_file('test.json', '{\n    "name": "test",\n    "age": 12\n}')
        processor = TextFileProcessor(path)
        self.assertIsInstance(processor.read_file(), str)

    def test_read_file_3(self):
        path = self._make_file('hello.txt', 'Hello world!')
        processor = TextFileProcessor(path)
        self.assertEqual(processor.read_file(), 'Hello world!')

    def test_read_file_4(self):
        path = self._make_file('empty.txt', '')
        processor = TextFileProcessor(path)
        self.assertEqual(processor.read_file(), '')

    def test_read_file_5(self):
        path = self._make_file('number.txt', '42')
        processor = TextFileProcessor(path)
        result = processor.read_file()
        self.assertEqual(result, '42')
        self.assertIsInstance(result, str)

import unittest

import os

import shutil

import tempfile

class AgentTest_write_file(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _make_file(self, name, content):
        path = os.path.join(self.temp_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path

    def _read_raw(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def test_write_file_1(self):
        path = os.path.join(self.temp_dir, 'hello.txt')
        processor = TextFileProcessor(path)
        processor.write_file('Hello world!')
        self.assertTrue(os.path.exists(path))
        self.assertEqual(self._read_raw(path), 'Hello world!')

    def test_write_file_2(self):
        path = self._make_file('existing.txt', 'old content that is much longer than the new one')
        processor = TextFileProcessor(path)
        processor.write_file('new')
        self.assertEqual(self._read_raw(path), 'new')

    def test_write_file_3(self):
        path = os.path.join(self.temp_dir, 'roundtrip.txt')
        processor = TextFileProcessor(path)
        processor.write_file('Hello world!')
        self.assertEqual(processor.read_file(), 'Hello world!')

    def test_write_file_4(self):
        path = os.path.join(self.temp_dir, 'test.json')
        content = '{\n    "name": "test",\n    "age": 12\n}'
        processor = TextFileProcessor(path)
        processor.write_file(content)
        self.assertEqual(self._read_raw(path), content)
        self.assertEqual(processor.read_file(), content)

    def test_write_file_5(self):
        path = self._make_file('overwrite_empty.txt', 'some existing text')
        processor = TextFileProcessor(path)
        processor.write_file('')
        self.assertEqual(self._read_raw(path), '')

import unittest

import os

import shutil

import tempfile

class AgentTest_process_file(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _make_file(self, name, content):
        path = os.path.join(self.temp_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path

    def _read_raw(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def test_process_file_1(self):
        path = self._make_file('test.json', '{\n    "name": "test",\n    "age": 12\n}')
        processor = TextFileProcessor(path)
        self.assertEqual(processor.process_file(), 'nametestage')

    def test_process_file_2(self):
        path = self._make_file('test.json', '{\n    "name": "test",\n    "age": 12\n}')
        processor = TextFileProcessor(path)
        processor.process_file()
        self.assertEqual(self._read_raw(path), 'nametestage')
        self.assertEqual(processor.read_file(), 'nametestage')

    def test_process_file_3(self):
        path = self._make_file('letters.txt', 'Hello')
        processor = TextFileProcessor(path)
        self.assertEqual(processor.process_file(), 'Hello')
        self.assertEqual(self._read_raw(path), 'Hello')

    def test_process_file_4(self):
        path = self._make_file('mixed.txt', 'Hello, World! 123\n')
        processor = TextFileProcessor(path)
        self.assertEqual(processor.process_file(), 'HelloWorld')
        self.assertEqual(self._read_raw(path), 'HelloWorld')

    def test_process_file_5(self):
        path = self._make_file('empty.txt', '')
        processor = TextFileProcessor(path)
        self.assertEqual(processor.process_file(), '')
        self.assertEqual(self._read_raw(path), '')