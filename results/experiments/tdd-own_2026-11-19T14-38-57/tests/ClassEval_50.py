import unittest


import json

import os

import shutil

import tempfile

import unittest

class AgentTest_read_json(unittest.TestCase):

    def setUp(self):
        self.processor = JSONProcessor()
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir, True)

    def _path(self, name):
        return os.path.join(self.temp_dir, name)

    def test_read_json_1(self):
        file_path = self._path('test.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({'name': 'test', 'age': 14}, f)

        result = self.processor.read_json(file_path)

        self.assertEqual(result, {'name': 'test', 'age': 14})

    def test_read_json_2(self):
        file_path = self._path('does_not_exist.json')
        self.assertFalse(os.path.exists(file_path))

        result = self.processor.read_json(file_path)

        self.assertEqual(result, 0)

    def test_read_json_3(self):
        file_path = self._path('malformed.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('{"name": "test", "age": 14')

        result = self.processor.read_json(file_path)

        self.assertEqual(result, -1)

    def test_read_json_4(self):
        file_path = self._path('empty_object.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)

        result = self.processor.read_json(file_path)

        self.assertEqual(result, {})

    def test_read_json_5(self):
        file_path = self._path('nested.json')
        data = {
            'user': {'name': 'alice', 'tags': ['a', 'b']},
            'active': True,
            'score': 3.5,
        }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

        result = self.processor.read_json(file_path)

        self.assertEqual(result, data)

import json

import os

import shutil

import tempfile

import unittest

class AgentTest_write_json(unittest.TestCase):

    def setUp(self):
        self.processor = JSONProcessor()
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir, True)

    def _path(self, name):
        return os.path.join(self.temp_dir, name)

    def test_write_json_1(self):
        file_path = self._path('test.json')
        data = {'key1': 'value1', 'key2': 'value2'}

        result = self.processor.write_json(data, file_path)

        self.assertEqual(result, 1)
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r', encoding='utf-8') as f:
            self.assertEqual(json.load(f), data)

    def test_write_json_2(self):
        file_path = self._path('roundtrip.json')
        data = {'key1': 'value1', 'key2': 'value2'}

        result = self.processor.write_json(data, file_path)

        self.assertEqual(result, 1)
        self.assertEqual(self.processor.read_json(file_path), {'key1': 'value1', 'key2': 'value2'})

    def test_write_json_3(self):
        file_path = self._path('nested.json')
        data = {
            'user': {'name': 'alice', 'tags': ['a', 'b']},
            'active': True,
            'score': 3.5,
            'nothing': None,
        }

        result = self.processor.write_json(data, file_path)

        self.assertEqual(result, 1)
        with open(file_path, 'r', encoding='utf-8') as f:
            self.assertEqual(json.load(f), data)

    def test_write_json_4(self):
        file_path = self._path('empty.json')

        result = self.processor.write_json({}, file_path)

        self.assertEqual(result, 1)
        self.assertEqual(self.processor.read_json(file_path), {})

    def test_write_json_5(self):
        file_path = self._path('not_serializable.json')
        data = {'key1': {1, 2, 3}}

        result = self.processor.write_json(data, file_path)

        self.assertEqual(result, -1)

import json

import os

import shutil

import tempfile

import unittest

class AgentTest_process_json(unittest.TestCase):

    def setUp(self):
        self.processor = JSONProcessor()
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir, True)

    def _path(self, name):
        return os.path.join(self.temp_dir, name)

    def _write_raw(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def _read_raw(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def test_process_json_1(self):
        file_path = self._path('test.json')
        self._write_raw(file_path, {'key1': 'value1', 'key2': 'value2'})

        result = self.processor.process_json(file_path, 'key1')

        self.assertEqual(result, 1)
        self.assertEqual(self._read_raw(file_path), {'key2': 'value2'})

    def test_process_json_2(self):
        file_path = self._path('does_not_exist.json')
        self.assertFalse(os.path.exists(file_path))

        result = self.processor.process_json(file_path, 'key1')

        self.assertEqual(result, 0)
        self.assertFalse(os.path.exists(file_path))

    def test_process_json_3(self):
        file_path = self._path('missing_key.json')
        original = {'key1': 'value1', 'key2': 'value2'}
        self._write_raw(file_path, original)

        result = self.processor.process_json(file_path, 'no_such_key')

        self.assertEqual(result, 0)
        self.assertEqual(self._read_raw(file_path), original)

    def test_process_json_4(self):
        file_path = self._path('nested_keep.json')
        self._write_raw(file_path, {
            'user': {'name': 'alice', 'tags': ['a', 'b']},
            'active': True,
            'score': 3.5,
        })

        result = self.processor.process_json(file_path, 'active')

        self.assertEqual(result, 1)
        self.assertEqual(self._read_raw(file_path), {
            'user': {'name': 'alice', 'tags': ['a', 'b']},
            'score': 3.5,
        })

    def test_process_json_5(self):
        file_path = self._path('single_key.json')
        self._write_raw(file_path, {'only': 'value'})

        result = self.processor.process_json(file_path, 'only')

        self.assertEqual(result, 1)
        self.assertEqual(self._read_raw(file_path), {})