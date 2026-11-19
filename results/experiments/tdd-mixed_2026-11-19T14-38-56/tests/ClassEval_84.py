import unittest
import json
from unittest.mock import MagicMock
import os




class TextFileProcessorTestReadFileAsJson(unittest.TestCase):
    def setUp(self):
        self.files = ['test_1.txt', 'test_2.txt', 'test_3.txt', 'test_4.txt', 'test_5.txt']
        self.contents = ['{\n    "name": "test",\n    "age": 12\n}', '12345', '\"hello\"', '\"aaa\"', '\"bbb\"']
        for index, file in enumerate(self.files):
            with open(file, 'w') as f:
                f.write(self.contents[index])

    def test_read_file_as_json_1(self):
        textFileProcessor = TextFileProcessor(self.files[0])
        data = textFileProcessor.read_file_as_json()
        expected = {"name": "test", "age": 12}
        self.assertEqual(dict, type(data))
        self.assertEqual(expected, data)

    def test_read_file_as_json_2(self):
        textFileProcessor = TextFileProcessor(self.files[1])
        data = textFileProcessor.read_file_as_json()
        expected = 12345
        self.assertEqual(int, type(data))
        self.assertEqual(expected, data)

    def test_read_file_as_json_3(self):
        textFileProcessor = TextFileProcessor(self.files[2])
        data = textFileProcessor.read_file_as_json()
        expected = 'hello'
        self.assertEqual(str, type(data))
        self.assertEqual(expected, data)

import json

import os

import unittest

class AgentTest_read_file_as_json(unittest.TestCase):
    def setUp(self):
        self.files = ['agent_read_json_1.txt', 'agent_read_json_2.txt']

    def tearDown(self):
        for file in self.files:
            if os.path.exists(file):
                os.remove(file)

    def test_read_file_as_json_1(self):
        with open(self.files[0], 'w') as f:
            f.write('3.5')
        textFileProcessor = TextFileProcessor(self.files[0])
        data = textFileProcessor.read_file_as_json()
        expected = 3.5
        self.assertEqual(float, type(data))
        self.assertEqual(expected, data)

    def test_read_file_as_json_2(self):
        with open(self.files[1], 'w') as f:
            f.write('{"name": "test", "age": ')
        textFileProcessor = TextFileProcessor(self.files[1])
        with self.assertRaises(ValueError):
            textFileProcessor.read_file_as_json()

class TextFileProcessorTestReadFile(unittest.TestCase):
    def setUp(self) -> None:
        self.files = ['test_1.txt', 'test_2.txt', 'test_3.txt', 'test_4.txt', 'test_5.txt']
        self.contents = ['123aac\n&^(*&43)', '12345', 'aaa', 'bbb', 'ccc']
        for index, file in enumerate(self.files):
            with open(file, 'w') as f:
                f.write(self.contents[index])

    def test_read_file_1(self):
        textFileProcessor = TextFileProcessor(self.files[0])
        data = textFileProcessor.read_file()
        self.assertEqual(str, type(data))
        self.assertEqual(data, self.contents[0])

    def test_read_file_2(self):
        textFileProcessor = TextFileProcessor(self.files[1])
        data = textFileProcessor.read_file()
        self.assertEqual(str, type(data))
        self.assertEqual(data, self.contents[1])

    def test_read_file_3(self):
        textFileProcessor = TextFileProcessor(self.files[2])
        data = textFileProcessor.read_file()
        self.assertEqual(str, type(data))
        self.assertEqual(data, self.contents[2])

import json

import os

import unittest

class AgentTest_read_file(unittest.TestCase):
    def setUp(self):
        self.files = ['agent_read_file_1.txt', 'agent_read_file_2.txt']

    def tearDown(self):
        for file in self.files:
            if os.path.exists(file):
                os.remove(file)

    def test_read_file_1(self):
        content = '{\n    "name": "test",\n    "age": 12\n}'
        with open(self.files[0], 'w') as f:
            f.write(content)
        textFileProcessor = TextFileProcessor(self.files[0])
        data = textFileProcessor.read_file()
        self.assertEqual(str, type(data))
        self.assertEqual('{\n    "name": "test",\n    "age": 12\n}', data)

    def test_read_file_2(self):
        with open(self.files[1], 'w') as f:
            f.write('')
        textFileProcessor = TextFileProcessor(self.files[1])
        data = textFileProcessor.read_file()
        self.assertEqual(str, type(data))
        self.assertEqual('', data)

class TextFileProcessorTestWriteFile(unittest.TestCase):
    def setUp(self) -> None:
        self.files = ['test_1.txt', 'test_2.txt', 'test_3.txt', 'test_4.txt', 'test_5.txt']
        self.contents = ['123aac\n&^(*&43)', '12345', 'aaa', 'bbb', 'ccc']

    def tearDown(self) -> None:
        for file in self.files:
            if os.path.exists(file):
                os.remove(file)

    def test_write_file_1(self):
        textFileProcessor = TextFileProcessor(self.files[0])
        textFileProcessor.write_file(self.contents[0])
        with open(self.files[0], 'r') as f:
            data = f.read()
        self.assertEqual(data, self.contents[0])

    def test_write_file_2(self):
        textFileProcessor = TextFileProcessor(self.files[1])
        textFileProcessor.write_file(self.contents[1])
        with open(self.files[1], 'r') as f:
            data = f.read()
        self.assertEqual(data, self.contents[1])

    def test_write_file_3(self):
        textFileProcessor = TextFileProcessor(self.files[2])
        textFileProcessor.write_file(self.contents[2])
        with open(self.files[2], 'r') as f:
            data = f.read()
        self.assertEqual(data, self.contents[2])

import os

import unittest

class AgentTest_write_file(unittest.TestCase):
    def setUp(self):
        self.files = ['agent_write_file_1.txt', 'agent_write_file_2.txt']

    def tearDown(self):
        for file in self.files:
            if os.path.exists(file):
                os.remove(file)

    def test_write_file_1(self):
        # Existing file content must be overwritten, not appended to.
        with open(self.files[0], 'w') as f:
            f.write('This is a much longer original content that existed before.')
        textFileProcessor = TextFileProcessor(self.files[0])
        textFileProcessor.write_file('short')
        with open(self.files[0], 'r') as f:
            data = f.read()
        self.assertEqual('short', data)

    def test_write_file_2(self):
        # Content written by write_file should be returned by read_file, as in the docstring example.
        textFileProcessor = TextFileProcessor(self.files[1])
        textFileProcessor.write_file('Hello world!')
        data = textFileProcessor.read_file()
        self.assertEqual(str, type(data))
        self.assertEqual('Hello world!', data)

class TextFileProcessorTestProcessFile(unittest.TestCase):
    def test_process_file_1(self):
        self.file = 'test.txt'
        self.content = 'Hello, 123 World!'
        self.expected_result = 'HelloWorld'

        textFileProcessor = TextFileProcessor(self.file)
        textFileProcessor.read_file = MagicMock(return_value=self.content)
        textFileProcessor.write_file = MagicMock()

        result = textFileProcessor.process_file()
        self.assertEqual(result, self.expected_result)
        textFileProcessor.read_file.assert_called_once()
        textFileProcessor.write_file.assert_called_once_with(self.expected_result)

    def test_process_file_2(self):
        self.file = 'test.txt'
        self.content = 'Hello, abc World!'
        self.expected_result = 'HelloabcWorld'

        textFileProcessor = TextFileProcessor(self.file)
        textFileProcessor.read_file = MagicMock(return_value=self.content)
        textFileProcessor.write_file = MagicMock()

        result = textFileProcessor.process_file()
        self.assertEqual(result, self.expected_result)
        textFileProcessor.read_file.assert_called_once()
        textFileProcessor.write_file.assert_called_once_with(self.expected_result)

    def test_process_file_3(self):
        self.file = 'test.txt'
        self.content = ', 123 !'
        self.expected_result = ''

        textFileProcessor = TextFileProcessor(self.file)
        textFileProcessor.read_file = MagicMock(return_value=self.content)
        textFileProcessor.write_file = MagicMock()

        result = textFileProcessor.process_file()
        self.assertEqual(result, self.expected_result)
        textFileProcessor.read_file.assert_called_once()
        textFileProcessor.write_file.assert_called_once_with(self.expected_result)

import os

import unittest

class AgentTest_process_file(unittest.TestCase):
    def setUp(self):
        self.files = ['agent_process_file_1.txt', 'agent_process_file_2.txt']

    def tearDown(self):
        for file in self.files:
            if os.path.exists(file):
                os.remove(file)

    def test_process_file_1(self):
        # Docstring example: the JSON-formatted file is processed in place and
        # the result is both returned and stored back into the same file.
        content = '{\n    "name": "test",\n    "age": 12\n}'
        with open(self.files[0], 'w') as f:
            f.write(content)
        textFileProcessor = TextFileProcessor(self.files[0])
        result = textFileProcessor.process_file()
        self.assertEqual(str, type(result))
        self.assertEqual('nametestage', result)
        self.assertEqual('nametestage', textFileProcessor.read_file())

    def test_process_file_2(self):
        # Spaces, newlines, punctuation and digits are all removed from the
        # file on disk, and the file's previous content is replaced.
        content = 'Hi there!\nNew-line_42 ok'
        with open(self.files[1], 'w') as f:
            f.write(content)
        textFileProcessor = TextFileProcessor(self.files[1])
        result = textFileProcessor.process_file()
        self.assertEqual('Hitherenewlineok', result)
        with open(self.files[1], 'r') as f:
            data = f.read()
        self.assertEqual('Hitherenewlineok', data)