import unittest
import os




class ExcelProcessorTestReadExcel(unittest.TestCase):
    def test_read_excel_1(self):
        self.test_file_name = 'test_data.xlsx'
        data = [['Name', 'Age', 'Country'],
                ['John', 25, 'USA'],
                ['Alice', 30, 'Canada'],
                ['Bob', 35, 'Australia']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        processor = ExcelProcessor()
        data = processor.read_excel(self.test_file_name)
        expected_data = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
            ('Bob', 35, 'Australia')
        ]
        self.assertEqual(data, expected_data)

    def test_read_excel_2(self):
        self.test_file_name = 'test_data.xlsx'
        data = [['Name', 'Age'],
                ['John', 25],
                ['Alice', 30],
                ['Bob', 35]]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        processor = ExcelProcessor()
        data = processor.read_excel(self.test_file_name)
        expected_data = [
            ('Name', 'Age'),
            ('John', 25),
            ('Alice', 30),
            ('Bob', 35)
        ]
        self.assertEqual(data, expected_data)

    def test_read_excel_3(self):
        self.test_file_name = 'test_data.xlsx'
        data = [['Name'],
                ['John'],
                ['Alice'],
                ['Bob']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        processor = ExcelProcessor()
        data = processor.read_excel(self.test_file_name)
        expected_data = [
            ('Name',),
            ('John',),
            ('Alice',),
            ('Bob',)
        ]
        self.assertEqual(data, expected_data)

    def test_read_excel_4(self):
        self.test_file_name = 'test_data.xlsx'
        data = [['Name', 'Country'],
                ['John', 'USA'],
                ['Alice', 'Canada'],
                ['Bob', 'Australia']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        processor = ExcelProcessor()
        data = processor.read_excel(self.test_file_name)
        expected_data = [
            ('Name', 'Country'),
            ('John', 'USA'),
            ('Alice', 'Canada'),
            ('Bob', 'Australia')
        ]
        self.assertEqual(data, expected_data)

import unittest

import os

import openpyxl

class AgentTest_read_excel(unittest.TestCase):
    def test_read_excel_1(self):
        self.test_file_name = 'test_read_single_row.xlsx'
        data = [['Name', 'Age', 'Country']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        try:
            processor = ExcelProcessor()
            result = processor.read_excel(self.test_file_name)
            expected_data = [
                ('Name', 'Age', 'Country')
            ]
            self.assertIsInstance(result, list)
            self.assertEqual(result, expected_data)
        finally:
            if os.path.exists(self.test_file_name):
                os.remove(self.test_file_name)

    def test_read_excel_2(self):
        self.test_file_name = 'test_read_float_and_blank.xlsx'
        data = [['Name', 'Score', 'Country'],
                ['John', 3.5, None],
                ['Alice', None, 'Canada']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        try:
            processor = ExcelProcessor()
            result = processor.read_excel(self.test_file_name)
            expected_data = [
                ('Name', 'Score', 'Country'),
                ('John', 3.5, None),
                ('Alice', None, 'Canada')
            ]
            self.assertEqual(result, expected_data)
        finally:
            if os.path.exists(self.test_file_name):
                os.remove(self.test_file_name)

class ExcelProcessorTestWriteExcel(unittest.TestCase):
    def test_write_excel_1(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
            ('Bob', 35, 'Australia'),
            ('Julia', 28, 'Germany')
        ]
        save_file_name = 'test_output.xlsx'
        success = processor.write_excel(new_data, save_file_name)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(save_file_name))
        saved_data = processor.read_excel(save_file_name)
        self.assertEqual(saved_data, new_data)
        os.remove(save_file_name)

    def test_write_excel_2(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age'),
            ('John', 25),
            ('Alice', 30),
            ('Bob', 35),
            ('Julia', 28)
        ]
        save_file_name = 'test_output.xlsx'
        success = processor.write_excel(new_data, save_file_name)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(save_file_name))
        saved_data = processor.read_excel(save_file_name)
        self.assertEqual(saved_data, new_data)
        os.remove(save_file_name)

    def test_write_excel_3(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada'),
            ('Bob', 35, 'Australia')
        ]
        save_file_name = 'test_output.xlsx'
        success = processor.write_excel(new_data, save_file_name)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(save_file_name))
        saved_data = processor.read_excel(save_file_name)
        self.assertEqual(saved_data, new_data)
        os.remove(save_file_name)

    def test_write_excel_4(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA'),
            ('Alice', 30, 'Canada')
        ]
        save_file_name = 'test_output.xlsx'
        success = processor.write_excel(new_data, save_file_name)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(save_file_name))
        saved_data = processor.read_excel(save_file_name)
        self.assertEqual(saved_data, new_data)
        os.remove(save_file_name)

import unittest

import os

class AgentTest_write_excel(unittest.TestCase):
    def test_write_excel_1(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA')
        ]
        save_file_name = 'test_output_return_value.xlsx'
        try:
            success = processor.write_excel(new_data, save_file_name)
            self.assertEqual(success, 1)
            self.assertTrue(os.path.exists(save_file_name))
        finally:
            if os.path.exists(save_file_name):
                os.remove(save_file_name)

    def test_write_excel_2(self):
        processor = ExcelProcessor()
        new_data = [
            ('Name', 'Age', 'Country'),
            ('John', 25, 'USA')
        ]
        save_file_name = os.path.join('nonexistent_directory_for_test', 'test_output_failed.xlsx')
        success = processor.write_excel(new_data, save_file_name)
        self.assertEqual(success, 0)
        self.assertFalse(os.path.exists(save_file_name))

class ExcelProcessorTestProcessExcelData(unittest.TestCase):
    def test_process_excel_data_1(self):
        self.test_file_name = 'test_data.xlsx'
        data = [['Name', 'Age', 'Country'],
                ['John', 25, 'USA'],
                ['Alice', 30, 'Canada'],
                ['Bob', 35, 'Australia']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        processor = ExcelProcessor()
        N = 1
        success, output_file = processor.process_excel_data(N, self.test_file_name)
        self.assertTrue(success)
        self.assertTrue(os.path.isfile(output_file))
        processed_data = processor.read_excel(output_file)
        expected_processed_data = [
            ('Name', 'Age', 'Country', 'AGE'),
            ('John', 25, 'USA', 25),
            ('Alice', 30, 'Canada', 30),
            ('Bob', 35, 'Australia', 35)
        ]
        self.assertEqual(processed_data, expected_processed_data)
        os.remove(output_file)

    def test_process_excel_data_2(self):
        self.test_file_name = 'test_data.xlsx'
        data = [['Name', 'Age', 'Country'],
                ['John', 25, 'USA'],
                ['Alice', 30, 'Canada'],
                ['Bob', 35, 'Australia']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        processor = ExcelProcessor()
        N = 0
        success, output_file = processor.process_excel_data(N, self.test_file_name)
        self.assertTrue(success)
        self.assertTrue(os.path.isfile(output_file))
        processed_data = processor.read_excel(output_file)
        expected_processed_data = [
            ('Name', 'Age', 'Country', 'NAME'),
            ('John', 25, 'USA', 'JOHN'),
            ('Alice', 30, 'Canada', 'ALICE'),
            ('Bob', 35, 'Australia', 'BOB')
        ]
        self.assertEqual(processed_data, expected_processed_data)
        os.remove(output_file)

    def test_process_excel_data_3(self):
        self.test_file_name = 'test_data.xlsx'
        data = [['Name', 'Age', 'Country'],
                ['John', 25, 'USA'],
                ['Alice', 30, 'Canada'],
                ['Bob', 35, 'Australia']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        processor = ExcelProcessor()
        N = 2
        success, output_file = processor.process_excel_data(N, self.test_file_name)
        self.assertTrue(success)
        self.assertTrue(os.path.isfile(output_file))
        processed_data = processor.read_excel(output_file)
        expected_processed_data = [
            ('Name', 'Age', 'Country', 'COUNTRY'),
            ('John', 25, 'USA', 'USA'),
            ('Alice', 30, 'Canada', 'CANADA'),
            ('Bob', 35, 'Australia', 'AUSTRALIA')
        ]
        self.assertEqual(processed_data, expected_processed_data)
        os.remove(output_file)

    def test_process_excel_data_4(self):
        self.test_file_name = 'test_data.xlsx'
        data = [['Name', 'Age', 'COUNTRY'],
                ['John', 25, 'USA'],
                ['Alice', 30, 'CANADA'],
                ['Bob', 35, 'AUSTRALIA']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(self.test_file_name)
        workbook.close()

        processor = ExcelProcessor()
        N = 2
        success, output_file = processor.process_excel_data(N, self.test_file_name)
        self.assertTrue(success)
        self.assertTrue(os.path.isfile(output_file))
        processed_data = processor.read_excel(output_file)
        expected_processed_data = [
            ('Name', 'Age', 'COUNTRY', 'COUNTRY'),
            ('John', 25, 'USA', 'USA'),
            ('Alice', 30, 'CANADA', 'CANADA'),
            ('Bob', 35, 'AUSTRALIA', 'AUSTRALIA')
        ]
        self.assertEqual(processed_data, expected_processed_data)
        os.remove(output_file)

import unittest

import os

import openpyxl

class AgentTest_process_excel_data(unittest.TestCase):
    def test_process_excel_data_1(self):
        source_file = 'test_process_return_types.xlsx'
        output_file = None
        data = [['Name', 'Age', 'Country'],
                ['John', 25, 'USA'],
                ['Alice', 30, 'Canada']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(source_file)
        workbook.close()

        try:
            processor = ExcelProcessor()
            success, output_file = processor.process_excel_data(1, source_file)
            self.assertIsInstance(success, int)
            self.assertEqual(success, 1)
            self.assertIsInstance(output_file, str)
            self.assertTrue(os.path.isfile(output_file))
        finally:
            if os.path.exists(source_file):
                os.remove(source_file)
            if output_file is not None and os.path.exists(output_file):
                os.remove(output_file)

    def test_process_excel_data_2(self):
        source_file = 'test_process_source_unchanged.xlsx'
        output_file = None
        data = [['Name', 'Age', 'Country'],
                ['john', 25, 'usa'],
                ['alice', 30, 'Canada']]
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(source_file)
        workbook.close()

        try:
            processor = ExcelProcessor()
            success, output_file = processor.process_excel_data(2, source_file)
            self.assertEqual(success, 1)
            self.assertNotEqual(output_file, source_file)
            self.assertTrue(os.path.isfile(source_file))
            original_data = processor.read_excel(source_file)
            expected_original_data = [
                ('Name', 'Age', 'Country'),
                ('john', 25, 'usa'),
                ('alice', 30, 'Canada')
            ]
            self.assertEqual(original_data, expected_original_data)
        finally:
            if os.path.exists(source_file):
                os.remove(source_file)
            if output_file is not None and os.path.exists(output_file):
                os.remove(output_file)