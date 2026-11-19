import unittest
import os




class ZipFileProcessorTestReadZipFile(unittest.TestCase):
    def test_read_zip_file_1(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example1.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example1.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_read_zip_file_2(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example2.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example2.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_read_zip_file_3(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example3.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example3.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_read_zip_file_4(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example4.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example4.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

import unittest

import os

import tempfile

class AgentTest_read_zip_file(unittest.TestCase):
    def test_read_zip_file_1(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing_zip_path = os.path.join(temp_dir, 'does_not_exist.zip')
            self.assertFalse(os.path.exists(missing_zip_path))

            processor = ZipFileProcessor(missing_zip_path)

            result = processor.read_zip_file()
            self.assertIsNone(result)

    def test_read_zip_file_2(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            not_a_zip_path = os.path.join(temp_dir, 'not_really_a_zip.zip')
            with open(not_a_zip_path, 'w') as file:
                file.write('This is plain text, not a zip archive.')

            processor = ZipFileProcessor(not_a_zip_path)

            result = processor.read_zip_file()
            self.assertIsNone(result)

class ZipFileProcessorTestExtractAll(unittest.TestCase):
    def test_extract_all_1(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example1.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example1.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_all_2(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example2.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example2.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_all_3(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example3.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example3.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_all_4(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example4.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example4.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

import unittest

import os

import tempfile

import zipfile

class AgentTest_extract_all(unittest.TestCase):
    def test_extract_all_1(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_dir = os.path.join(temp_dir, 'source')
            os.makedirs(source_dir)
            first_path = os.path.join(source_dir, 'first.txt')
            second_path = os.path.join(source_dir, 'second.txt')
            with open(first_path, 'w') as file:
                file.write('First file content.')
            with open(second_path, 'w') as file:
                file.write('Second file content.')

            zip_file_name = os.path.join(temp_dir, 'multi.zip')
            with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
                zip_file.write(first_path, 'first.txt')
                zip_file.write(second_path, 'second.txt')

            output_directory = os.path.join(temp_dir, 'output_multi')
            processor = ZipFileProcessor(zip_file_name)

            success = processor.extract_all(output_directory)
            self.assertTrue(success)

            extracted_first = os.path.join(output_directory, 'first.txt')
            extracted_second = os.path.join(output_directory, 'second.txt')
            self.assertTrue(os.path.exists(extracted_first))
            self.assertTrue(os.path.exists(extracted_second))

            with open(extracted_first, 'r') as file:
                self.assertEqual(file.read(), 'First file content.')
            with open(extracted_second, 'r') as file:
                self.assertEqual(file.read(), 'Second file content.')

    def test_extract_all_2(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing_zip_path = os.path.join(temp_dir, 'does_not_exist.zip')
            self.assertFalse(os.path.exists(missing_zip_path))

            output_directory = os.path.join(temp_dir, 'output_missing')
            processor = ZipFileProcessor(missing_zip_path)

            success = processor.extract_all(output_directory)
            self.assertFalse(success)

class ZipFileProcessorTestExtractFile(unittest.TestCase):
    def test_extract_file_1(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example1.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_file('example1.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example1.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_file_2(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example2.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_file('example2.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example2.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_file_3(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example3.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_file('example3.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example3.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_file_4(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example4.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_file('example4.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example4.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

import unittest

import os

import tempfile

import zipfile

class AgentTest_extract_file(unittest.TestCase):
    def test_extract_file_1(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = os.path.join(temp_dir, 'present.txt')
            with open(source_path, 'w') as file:
                file.write('Present file content.')

            zip_file_name = os.path.join(temp_dir, 'single.zip')
            with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
                zip_file.write(source_path, 'present.txt')

            output_directory = os.path.join(temp_dir, 'output_missing_member')
            processor = ZipFileProcessor(zip_file_name)

            success = processor.extract_file('absent.txt', output_directory)
            self.assertFalse(success)
            self.assertFalse(os.path.exists(os.path.join(output_directory, 'absent.txt')))

    def test_extract_file_2(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            first_path = os.path.join(temp_dir, 'first.txt')
            second_path = os.path.join(temp_dir, 'second.txt')
            with open(first_path, 'w') as file:
                file.write('First file content.')
            with open(second_path, 'w') as file:
                file.write('Second file content.')

            zip_file_name = os.path.join(temp_dir, 'multi.zip')
            with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
                zip_file.write(first_path, 'first.txt')
                zip_file.write(second_path, 'second.txt')

            output_directory = os.path.join(temp_dir, 'output_selective')
            processor = ZipFileProcessor(zip_file_name)

            success = processor.extract_file('second.txt', output_directory)
            self.assertTrue(success)

            extracted_second = os.path.join(output_directory, 'second.txt')
            self.assertTrue(os.path.exists(extracted_second))
            with open(extracted_second, 'r') as file:
                self.assertEqual(file.read(), 'Second file content.')

            self.assertFalse(os.path.exists(os.path.join(output_directory, 'first.txt')))

class ZipFileProcessorTestCreateZipFile(unittest.TestCase):
    def test_create_zip_file_1(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example1.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_create_zip_file_2(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example2.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_create_zip_file_3(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example3.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_create_zip_file_4(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example4.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

import unittest

import os

import tempfile

import zipfile

class AgentTest_create_zip_file(unittest.TestCase):
    def test_create_zip_file_1(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            first_path = os.path.join(temp_dir, 'bbb.txt')
            second_path = os.path.join(temp_dir, 'ddd.txt')
            with open(first_path, 'w') as file:
                file.write('First file content.')
            with open(second_path, 'w') as file:
                file.write('Second file content.')

            output_file_name = os.path.join(temp_dir, 'multi_output.zip')
            processor = ZipFileProcessor(os.path.join(temp_dir, 'unused.zip'))

            success = processor.create_zip_file([first_path, second_path], output_file_name)
            self.assertTrue(success)
            self.assertTrue(os.path.exists(output_file_name))

            with zipfile.ZipFile(output_file_name, 'r') as zip_file:
                names = set(zip_file.namelist())
                self.assertEqual(names, {'bbb.txt', 'ddd.txt'})
                self.assertEqual(zip_file.read('bbb.txt').decode(), 'First file content.')
                self.assertEqual(zip_file.read('ddd.txt').decode(), 'Second file content.')

    def test_create_zip_file_2(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            present_path = os.path.join(temp_dir, 'present.txt')
            missing_path = os.path.join(temp_dir, 'missing.txt')
            with open(present_path, 'w') as file:
                file.write('Present file content.')
            self.assertFalse(os.path.exists(missing_path))

            output_file_name = os.path.join(temp_dir, 'failed_output.zip')
            processor = ZipFileProcessor(os.path.join(temp_dir, 'unused.zip'))

            success = processor.create_zip_file([present_path, missing_path], output_file_name)
            self.assertFalse(success)