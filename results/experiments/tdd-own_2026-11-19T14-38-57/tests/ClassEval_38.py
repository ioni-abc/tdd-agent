import unittest


import os

import tempfile

import unittest

import openpyxl

class AgentTest_read_excel(unittest.TestCase):

    def _make_xlsx(self, directory, file_name, rows):
        path = os.path.join(directory, file_name)
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        for row in rows:
            worksheet.append(list(row))
        workbook.save(path)
        return path

    def test_read_excel_1(self):
        processor = ExcelProcessor()
        with tempfile.TemporaryDirectory() as directory:
            path = self._make_xlsx(directory, 'data.xlsx', [
                ('Name', 'Age', 'Country'),
                ('John', 25, 'USA'),
            ])
            result = processor.read_excel(path)
        self.assertIsInstance(result, list)

    def test_read_excel_2(self):
        processor = ExcelProcessor()
        rows = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
            ('Bob', 35, 'Australia'),
            ('Julia', 28, 'Germany'),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = self._make_xlsx(directory, 'test_data.xlsx', rows)
            result = processor.read_excel(path)
        self.assertEqual([tuple(row) for row in result], rows)

    def test_read_excel_3(self):
        processor = ExcelProcessor()
        rows = [
            ('Item', 'Price', 'Quantity'),
            ('Pen', 1.5, 10),
            ('Notebook', 3.25, 4),
            ('Bag', 20.0, 1),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = self._make_xlsx(directory, 'mixed.xlsx', rows)
            result = processor.read_excel(path)
        self.assertEqual([tuple(row) for row in result], rows)
        self.assertIsInstance(result[1][1], float)
        self.assertIsInstance(result[1][2], int)

    def test_read_excel_4(self):
        processor = ExcelProcessor()
        rows = [('Row', 'Value')] + [(f'r{i}', i * 2) for i in range(1, 100)]
        with tempfile.TemporaryDirectory() as directory:
            path = self._make_xlsx(directory, 'many_rows.xlsx', rows)
            result = processor.read_excel(path)
        self.assertEqual(len(result), len(rows))
        self.assertEqual(tuple(result[0]), ('Row', 'Value'))
        self.assertEqual(tuple(result[-1]), ('r99', 198))

    def test_read_excel_5(self):
        processor = ExcelProcessor()
        with tempfile.TemporaryDirectory() as directory:
            path = self._make_xlsx(directory, 'empty.xlsx', [])
            result = processor.read_excel(path)
        self.assertEqual(result, [])

import os

import tempfile

import openpyxl

class AgentTest_write_excel(unittest.TestCase):

    def _read_rows(self, path):
        workbook = openpyxl.load_workbook(path)
        worksheet = workbook.active
        return [tuple(row) for row in worksheet.iter_rows(values_only=True)]

    def test_write_excel_1(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
            ('Bob', 35, 'Australia'),
            ('Julia', 28, 'Germany'),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'test_data.xlsx')
            result = processor.write_excel(new_data, path)
        self.assertEqual(result, 1)

    def test_write_excel_2(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
            ('Bob', 35, 'Australia'),
            ('Julia', 28, 'Germany'),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'test_data.xlsx')
            processor.write_excel(new_data, path)
            self.assertTrue(os.path.exists(path))
            rows = self._read_rows(path)
        self.assertEqual(rows, new_data)

    def test_write_excel_3(self):
        processor = ExcelProcessor()
        new_data = [
            ('Item', 'Price', 'Quantity'),
            ('Pen', 1.5, 10),
            ('Notebook', 3.25, 4),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'mixed.xlsx')
            processor.write_excel(new_data, path)
            rows = self._read_rows(path)
        self.assertEqual(rows, new_data)
        self.assertIsInstance(rows[1][1], float)
        self.assertIsInstance(rows[1][2], int)

    def test_write_excel_4(self):
        processor = ExcelProcessor()
        new_data = [('Only', 'Row')]
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'single.xlsx')
            result = processor.write_excel(new_data, path)
            self.assertEqual(result, 1)
            rows = self._read_rows(path)
        self.assertEqual(rows, new_data)

    def test_write_excel_5(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age'),
            ('John', 25),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'missing_dir', 'output.xlsx')
            result = processor.write_excel(new_data, path)
        self.assertEqual(result, 0)

import os

import tempfile

import openpyxl

class AgentTest_process_excel_data(unittest.TestCase):

    def _make_xlsx(self, directory, file_name, rows):
        path = os.path.join(directory, file_name)
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        for row in rows:
            worksheet.append(list(row))
        workbook.save(path)
        return path

    def _read_rows(self, path):
        workbook = openpyxl.load_workbook(path)
        worksheet = workbook.active
        return [tuple(row) for row in worksheet.iter_rows(values_only=True)]

    def _run_in_directory(self, directory, func):
        original_cwd = os.getcwd()
        os.chdir(directory)
        try:
            return func()
        finally:
            os.chdir(original_cwd)

    def test_process_excel_data_1(self):
        processor = ExcelProcessor()
        rows = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
        ]
        with tempfile.TemporaryDirectory() as directory:
            self._make_xlsx(directory, 'test_data.xlsx', rows)
            result = self._run_in_directory(
                directory,
                lambda: processor.process_excel_data(1, 'test_data.xlsx'),
            )
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        success, output_file = result
        self.assertEqual(success, 1)
        self.assertIsInstance(output_file, str)

    def test_process_excel_data_2(self):
        processor = ExcelProcessor()
        rows = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
            ('Bob', 35, 'Australia'),
            ('Julia', 28, 'Germany'),
        ]
        with tempfile.TemporaryDirectory() as directory:
            self._make_xlsx(directory, 'test_data.xlsx', rows)
            success, output_file = self._run_in_directory(
                directory,
                lambda: processor.process_excel_data(1, 'test_data.xlsx'),
            )
            self.assertTrue(os.path.exists(os.path.join(directory, output_file))
                            or os.path.exists(output_file))
            output_rows = self._run_in_directory(
                directory, lambda: self._read_rows(output_file)
            )
        self.assertEqual([row[0] for row in output_rows[1:]],
                         ['JOHN', 'ALICE', 'BOB', 'JULIA'])
        self.assertEqual([row[1:] for row in output_rows[1:]],
                         [row[1:] for row in rows[1:]])

    def test_process_excel_data_3(self):
        processor = ExcelProcessor()
        rows = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
            ('Bob', 35, 'Australia'),
            ('Julia', 28, 'Germany'),
        ]
        with tempfile.TemporaryDirectory() as directory:
            self._make_xlsx(directory, 'test_data.xlsx', rows)
            success, output_file = self._run_in_directory(
                directory,
                lambda: processor.process_excel_data(3, 'test_data.xlsx'),
            )
            output_rows = self._run_in_directory(
                directory, lambda: self._read_rows(output_file)
            )
        self.assertEqual(success, 1)
        self.assertEqual([row[2] for row in output_rows[1:]],
                         ['USA', 'CANADA', 'AUSTRALIA', 'GERMANY'])
        self.assertEqual([row[:2] for row in output_rows[1:]],
                         [row[:2] for row in rows[1:]])

    def test_process_excel_data_4(self):
        processor = ExcelProcessor()
        rows = [
            ('Code', 'Note'),
            ('a1 b', 'Mixed Case text'),
            ('x-9', 'lower only'),
        ]
        with tempfile.TemporaryDirectory() as directory:
            self._make_xlsx(directory, 'codes.xlsx', rows)
            success, output_file = self._run_in_directory(
                directory,
                lambda: processor.process_excel_data(2, 'codes.xlsx'),
            )
            output_rows = self._run_in_directory(
                directory, lambda: self._read_rows(output_file)
            )
        self.assertEqual(success, 1)
        self.assertEqual(output_rows[1][1], 'MIXED CASE TEXT')
        self.assertEqual(output_rows[2][1], 'LOWER ONLY')
        self.assertEqual(output_rows[1][0], 'a1 b')
        self.assertEqual(output_rows[2][0], 'x-9')

    def test_process_excel_data_5(self):
        processor = ExcelProcessor()
        rows = [('Name', 'City')] + [(f'person{i}', f'city{i}') for i in range(1, 11)]
        with tempfile.TemporaryDirectory() as directory:
            self._make_xlsx(directory, 'large.xlsx', rows)
            success, output_file = self._run_in_directory(
                directory,
                lambda: processor.process_excel_data(2, 'large.xlsx'),
            )
            self.assertEqual(success, 1)
            self.assertTrue(self._run_in_directory(
                directory, lambda: os.path.exists(output_file)))
            output_rows = self._run_in_directory(
                directory, lambda: self._read_rows(output_file)
            )
        self.assertEqual(len(output_rows), len(rows))
        self.assertEqual([row[1] for row in output_rows[1:]],
                         [f'CITY{i}' for i in range(1, 11)])
        self.assertEqual([row[0] for row in output_rows[1:]],
                         [f'person{i}' for i in range(1, 11)])