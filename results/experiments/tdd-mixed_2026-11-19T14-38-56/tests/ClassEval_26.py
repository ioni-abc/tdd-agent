import unittest
import os




class CSVProcessorTestReadCSV(unittest.TestCase):
    def test_read_csv_1(self):
        self.file = 'read_test.csv'

        with open(self.file, 'w') as f:
            f.write('a,b,c,d\nhElLo,YoU,ME,LoW')

        expected_title = ['a', 'b', 'c', 'd']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        csvProcessor = CSVProcessor()
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)

    def test_read_csv_2(self):
        self.file = 'read_test.csv'
        with open(self.file, 'w') as f:
            f.write('1234\nhElLo,YoU,ME,LoW')

        expected_title = ['1234']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        csvProcessor = CSVProcessor()
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)

    def test_read_csv_3(self):
        self.file = 'read_test.csv'

        with open(self.file, 'w') as f:
            f.write('title\nhElLo,YoU,ME,LoW')

        expected_title = ['title']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        csvProcessor = CSVProcessor()
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)

import unittest

import os

class AgentTest_read_csv(unittest.TestCase):
    def test_read_csv_1(self):
        file_name = 'read_test_multi_rows.csv'
        try:
            with open(file_name, 'w') as f:
                f.write('name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,41,Tokyo')

            expected_title = ['name', 'age', 'city']
            expected_data = [
                ['Alice', '30', 'Paris'],
                ['Bob', '25', 'London'],
                ['Carol', '41', 'Tokyo'],
            ]
            csvProcessor = CSVProcessor()
            title, data = csvProcessor.read_csv(file_name)
            self.assertEqual(expected_title, title)
            self.assertEqual(expected_data, data)
            self.assertEqual(3, len(data))
        finally:
            if os.path.exists(file_name):
                os.remove(file_name)

    def test_read_csv_2(self):
        file_name = 'read_test_title_only.csv'
        try:
            with open(file_name, 'w') as f:
                f.write('x,y,z')

            expected_title = ['x', 'y', 'z']
            expected_data = []
            csvProcessor = CSVProcessor()
            title, data = csvProcessor.read_csv(file_name)
            self.assertEqual(expected_title, title)
            self.assertEqual(expected_data, data)
        finally:
            if os.path.exists(file_name):
                os.remove(file_name)

class CSVProcessorTestWriteCSV(unittest.TestCase):
    def test_write_csv_1(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['a', 'b', 'c', 'd'], ['1', '2', '3', '4']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

    def test_write_csv_2(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['aa', 'bb', 'cc', 'dd'], ['1', '2', '3', '4']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

    def test_write_csv_3(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['a', 'b', 'c', 'd'], ['11', '22', '33', '44']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

    def test_write_csv_4(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['e', 'f', 'g', 'h'], ['1', '2', '3', '4']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

import unittest

import os

class AgentTest_write_csv(unittest.TestCase):
    def test_write_csv_1(self):
        file_name = os.path.join('no_such_directory_for_write_test', 'out.csv')
        csvProcessor = CSVProcessor()
        data = [['a', 'b', 'c', 'd'], ['1', '2', '3', '4']]
        self.assertEqual(0, csvProcessor.write_csv(data, file_name))
        self.assertFalse(os.path.exists(file_name))

    def test_write_csv_2(self):
        file_name = 'write_test_multi_rows.csv'
        try:
            csvProcessor = CSVProcessor()
            data = [
                ['name', 'age', 'city'],
                ['Alice', '30', 'Paris'],
                ['Bob', '25', 'London'],
                ['Carol', '41', 'Tokyo'],
            ]
            self.assertEqual(1, csvProcessor.write_csv(data, file_name))

            read_title, read_data = csvProcessor.read_csv(file_name)
            self.assertEqual(data[0], read_title)
            self.assertEqual(data[1:], read_data)
            self.assertEqual(3, len(read_data))
        finally:
            if os.path.exists(file_name):
                os.remove(file_name)

class CSVProcessorTestProcessCSVData(unittest.TestCase):
    def setUp(self) -> None:
        self.file = 'read_test.csv'
        self.file_process = 'read_test_process.csv'
        with open(self.file, 'w') as f:
            f.write('a,b,c,d\nhElLo,YoU,ME,LoW,aBc')

    def test_process_csv_data_1(self):
        title = ['a', 'b', 'c', 'd']
        data = ['HELLO']
        csvProcessor = CSVProcessor()
        self.assertEqual(1, csvProcessor.process_csv_data(0, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)

    def test_process_csv_data_2(self):
        title = ['a', 'b', 'c', 'd']
        data = ['YOU']
        csvProcessor = CSVProcessor()
        self.assertEqual(1, csvProcessor.process_csv_data(1, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)

    def test_process_csv_data_3(self):
        title = ['a', 'b', 'c', 'd']
        data = ['ME']
        csvProcessor = CSVProcessor()
        self.assertEqual(1, csvProcessor.process_csv_data(2, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)

import unittest

import os

import csv

class AgentTest_process_csv_data(unittest.TestCase):
    def test_process_csv_data_1(self):
        file_name = 'no_such_file_for_process_test.csv'
        output_name = 'no_such_file_for_process_test_process.csv'
        try:
            csvProcessor = CSVProcessor()
            self.assertEqual(0, csvProcessor.process_csv_data(0, file_name))
            self.assertFalse(os.path.exists(output_name))
        finally:
            if os.path.exists(output_name):
                os.remove(output_name)

    def test_process_csv_data_2(self):
        file_name = 'process_test_multi_rows.csv'
        output_name = 'process_test_multi_rows_process.csv'
        try:
            with open(file_name, 'w') as f:
                f.write('name,age,city\nalice,30,paris\nbob,25,london\ncarol,41,tokyo')

            expected_title = ['name', 'age', 'city']
            expected_data = [['PARIS'], ['LONDON'], ['TOKYO']]

            csvProcessor = CSVProcessor()
            self.assertEqual(1, csvProcessor.process_csv_data(2, file_name))

            read_title, read_data = csvProcessor.read_csv(output_name)
            self.assertEqual(expected_title, read_title)
            self.assertEqual(expected_data, read_data)
            self.assertEqual(3, len(read_data))
        finally:
            for name in (file_name, output_name):
                if os.path.exists(name):
                    os.remove(name)