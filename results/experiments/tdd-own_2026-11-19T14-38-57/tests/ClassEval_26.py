import unittest


import csv

import os

import tempfile

import unittest

class AgentTest_read_csv(unittest.TestCase):

    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp_dir.cleanup)
        self.processor = CSVProcessor()

    def _path(self, name):
        return os.path.join(self.tmp_dir.name, name)

    def _write_file(self, name, rows):
        path = self._path(name)
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        return path

    def test_read_csv_1(self):
        # Example from the docstring: read_test.csv
        path = self._write_file('read_test.csv', [
            ['a', 'b', 'c', 'd'],
            ['hElLo', 'YoU', 'ME', 'LoW'],
        ])
        title, data = self.processor.read_csv(path)
        self.assertEqual(title, ['a', 'b', 'c', 'd'])
        self.assertEqual(data, [['hElLo', 'YoU', 'ME', 'LoW']])

    def test_read_csv_2(self):
        # First row is title, all following rows are data, in order
        path = self._write_file('multi_rows.csv', [
            ['name', 'age', 'city'],
            ['Alice', '30', 'Paris'],
            ['Bob', '25', 'Berlin'],
            ['Carol', '41', 'Rome'],
        ])
        title, data = self.processor.read_csv(path)
        self.assertEqual(title, ['name', 'age', 'city'])
        self.assertEqual(data, [
            ['Alice', '30', 'Paris'],
            ['Bob', '25', 'Berlin'],
            ['Carol', '41', 'Rome'],
        ])

    def test_read_csv_3(self):
        # File containing only a title row: data is an empty list
        path = self._write_file('title_only.csv', [
            ['x', 'y', 'z'],
        ])
        title, data = self.processor.read_csv(path)
        self.assertEqual(title, ['x', 'y', 'z'])
        self.assertEqual(data, [])

    def test_read_csv_4(self):
        # Return value is a tuple of (title list, data list)
        path = self._write_file('types.csv', [
            ['a', 'b'],
            ['1', '2'],
        ])
        result = self.processor.read_csv(path)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        title, data = result
        self.assertIsInstance(title, list)
        self.assertIsInstance(data, list)
        self.assertEqual(title, ['a', 'b'])
        self.assertEqual(data, [['1', '2']])

    def test_read_csv_5(self):
        # Values are read as they are stored in the file (no case changes
        # or other modifications); the title row is not included in data
        path = self._write_file('mixed.csv', [
            ['Title One', 'TITLE two'],
            ['MiXeD Case', 'lower'],
            ['UPPER', 'Some Value'],
        ])
        title, data = self.processor.read_csv(path)
        self.assertEqual(title, ['Title One', 'TITLE two'])
        self.assertNotIn(['Title One', 'TITLE two'], data)
        self.assertEqual(data, [
            ['MiXeD Case', 'lower'],
            ['UPPER', 'Some Value'],
        ])

import csv

import os

import tempfile

import unittest

class AgentTest_write_csv(unittest.TestCase):

    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp_dir.cleanup)
        self.processor = CSVProcessor()

    def _path(self, name):
        return os.path.join(self.tmp_dir.name, name)

    def _read_rows(self, path):
        with open(path, 'r', newline='') as f:
            return [row for row in csv.reader(f)]

    def test_write_csv_1(self):
        # Example from the docstring: writing two rows returns 1 on success
        path = self._path('write_test.csv')
        result = self.processor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], path)
        self.assertEqual(result, 1)

    def test_write_csv_2(self):
        # The file named by file_name is created and contains the given rows in order
        path = self._path('write_test.csv')
        self.processor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], path)
        self.assertTrue(os.path.exists(path))
        self.assertEqual(self._read_rows(path), [['a', 'b', 'c', 'd'], ['1', '2', '3', '4']])

    def test_write_csv_3(self):
        # Return value is an int (1 for success)
        path = self._path('types_out.csv')
        result = self.processor.write_csv([['x', 'y'], ['p', 'q']], path)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_write_csv_4(self):
        # Values containing commas, quotes and spaces are stored so that reading
        # the file back as CSV gives the original values
        path = self._path('special.csv')
        data = [
            ['name', 'note'],
            ['Smith, John', 'said "hello"'],
            ['Mary Ann', 'plain text'],
        ]
        result = self.processor.write_csv(data, path)
        self.assertEqual(result, 1)
        self.assertEqual(self._read_rows(path), data)

    def test_write_csv_5(self):
        # Writing to a location that cannot be created (missing directory)
        # returns 0 on failure
        path = os.path.join(self.tmp_dir.name, 'missing_dir', 'out.csv')
        result = self.processor.write_csv([['a', 'b'], ['1', '2']], path)
        self.assertEqual(result, 0)

import csv

import os

import tempfile

import unittest

class AgentTest_process_csv_data(unittest.TestCase):

    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp_dir.cleanup)
        self.processor = CSVProcessor()

    def _path(self, name):
        return os.path.join(self.tmp_dir.name, name)

    def _write_file(self, name, rows):
        path = self._path(name)
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        return path

    def _read_rows(self, path):
        with open(path, 'r', newline='') as f:
            return [row for row in csv.reader(f)]

    def test_process_csv_data_1(self):
        # Example from the docstring: keep column 0, capitalize it, and save
        # to '<name>_process.csv' with the title row kept
        path = self._write_file('read_test.csv', [
            ['a', 'b', 'c', 'd'],
            ['hElLo', 'YoU', 'ME', 'LoW'],
        ])
        result = self.processor.process_csv_data(0, path)
        self.assertEqual(result, 1)
        processed_path = self._path('read_test_process.csv')
        self.assertTrue(os.path.exists(processed_path))
        title, data = self.processor.read_csv(processed_path)
        self.assertEqual(title, ['a', 'b', 'c', 'd'])
        self.assertEqual(data, [['HELLO']])

    def test_process_csv_data_2(self):
        # The N th column (from 0) is the one kept, not the first column
        path = self._write_file('pick_column.csv', [
            ['a', 'b', 'c', 'd'],
            ['hElLo', 'YoU', 'ME', 'LoW'],
        ])
        result = self.processor.process_csv_data(1, path)
        self.assertEqual(result, 1)
        title, data = self.processor.read_csv(self._path('pick_column_process.csv'))
        self.assertEqual(title, ['a', 'b', 'c', 'd'])
        self.assertEqual(data, [['YOU']])

    def test_process_csv_data_3(self):
        # Every data row is processed in order: the N th value of each row is
        # kept and capitalized, and the title row is not treated as data
        path = self._write_file('multi.csv', [
            ['name', 'age', 'city'],
            ['alice', '30', 'paris'],
            ['Bob', '25', 'Berlin'],
            ['cArOl', '41', 'rome'],
        ])
        result = self.processor.process_csv_data(2, path)
        self.assertEqual(result, 1)
        title, data = self.processor.read_csv(self._path('multi_process.csv'))
        self.assertEqual(title, ['name', 'age', 'city'])
        self.assertEqual(data, [['PARIS'], ['BERLIN'], ['ROME']])

    def test_process_csv_data_4(self):
        # Return value is an int, and the new file name adds '_process' after
        # the old file name, keeping its extension
        path = self._write_file('sales.csv', [
            ['item', 'price'],
            ['pen', 'cheap'],
        ])
        result = self.processor.process_csv_data(1, path)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)
        self.assertTrue(os.path.exists(self._path('sales_process.csv')))
        self.assertFalse(os.path.exists(self._path('sales_process_process.csv')))
        title, data = self.processor.read_csv(self._path('sales_process.csv'))
        self.assertEqual(title, ['item', 'price'])
        self.assertEqual(data, [['CHEAP']])

    def test_process_csv_data_5(self):
        # When the file to be processed does not exist, the method returns 0
        path = self._path('does_not_exist.csv')
        result = self.processor.process_csv_data(0, path)
        self.assertEqual(result, 0)