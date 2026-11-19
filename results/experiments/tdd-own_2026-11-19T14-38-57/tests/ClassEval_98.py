import unittest


import unittest

import os

import tempfile

import xml.etree.ElementTree as ET

class AgentTest_read_xml(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.created_files = []

    def tearDown(self):
        for path in self.created_files:
            if os.path.exists(path):
                os.remove(path)
        os.rmdir(self.temp_dir)

    def _create_xml_file(self, name, content):
        path = os.path.join(self.temp_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        self.created_files.append(path)
        return path

    def test_read_xml_1(self):
        # read_xml returns an Element whose tag is the root element's name
        path = self._create_xml_file('test.xml', '<root></root>')
        processor = XMLProcessor(path)
        root_element = processor.read_xml()
        self.assertIsInstance(root_element, ET.Element)
        self.assertEqual(root_element.tag, 'root')

    def test_read_xml_2(self):
        # The returned root element gives access to its child elements and their text
        content = (
            '<root>'
            '<item>apple</item>'
            '<item>banana</item>'
            '<item>orange</item>'
            '</root>'
        )
        path = self._create_xml_file('fruits.xml', content)
        processor = XMLProcessor(path)
        root_element = processor.read_xml()
        texts = [child.text for child in root_element.iter('item')]
        self.assertEqual(texts, ['apple', 'banana', 'orange'])

    def test_read_xml_3(self):
        # Attributes of the root element in the file are preserved on the returned element
        path = self._create_xml_file(
            'attrs.xml', '<root version="1.0" lang="en"></root>'
        )
        processor = XMLProcessor(path)
        root_element = processor.read_xml()
        self.assertEqual(root_element.tag, 'root')
        self.assertEqual(root_element.get('version'), '1.0')
        self.assertEqual(root_element.get('lang'), 'en')

    def test_read_xml_4(self):
        # Nested structure of the file is represented in the returned element tree
        content = (
            '<library>'
            '<book><title>Dune</title></book>'
            '<book><title>Emma</title></book>'
            '</library>'
        )
        path = self._create_xml_file('library.xml', content)
        processor = XMLProcessor(path)
        root_element = processor.read_xml()
        self.assertEqual(root_element.tag, 'library')
        books = root_element.findall('book')
        self.assertEqual(len(books), 2)
        titles = [book.find('title').text for book in books]
        self.assertEqual(titles, ['Dune', 'Emma'])

    def test_read_xml_5(self):
        # Each processor reads its own file and returns the root of that file
        path_a = self._create_xml_file('first.xml', '<alpha><x>1</x></alpha>')
        path_b = self._create_xml_file('second.xml', '<beta><y>2</y></beta>')
        root_a = XMLProcessor(path_a).read_xml()
        root_b = XMLProcessor(path_b).read_xml()
        self.assertEqual(root_a.tag, 'alpha')
        self.assertEqual(root_a.find('x').text, '1')
        self.assertEqual(root_b.tag, 'beta')
        self.assertEqual(root_b.find('y').text, '2')

import os

import tempfile

import xml.etree.ElementTree as ET

class AgentTest_write_xml(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.created_files = []

    def tearDown(self):
        for path in self.created_files:
            if os.path.exists(path):
                os.remove(path)
        os.rmdir(self.temp_dir)

    def _create_xml_file(self, name, content):
        path = os.path.join(self.temp_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        self.created_files.append(path)
        return path

    def _output_path(self, name):
        path = os.path.join(self.temp_dir, name)
        self.created_files.append(path)
        return path

    def test_write_xml_1(self):
        # write_xml returns True on success and the file is created at the given name
        source = self._create_xml_file('source.xml', '<root><item>apple</item></root>')
        output = self._output_path('output.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        success = processor.write_xml(output)
        self.assertIs(success, True)
        self.assertTrue(os.path.exists(output))

    def test_write_xml_2(self):
        # The written file contains the root element and its child text
        content = (
            '<root>'
            '<item>apple</item>'
            '<item>banana</item>'
            '<item>orange</item>'
            '</root>'
        )
        source = self._create_xml_file('fruits.xml', content)
        output = self._output_path('fruits_out.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        processor.write_xml(output)
        written_root = ET.parse(output).getroot()
        self.assertEqual(written_root.tag, 'root')
        texts = [child.text for child in written_root.iter('item')]
        self.assertEqual(texts, ['apple', 'banana', 'orange'])

    def test_write_xml_3(self):
        # Attributes and nested structure of the read root are present in the written file
        content = (
            '<library version="2.0">'
            '<book id="b1"><title>Dune</title></book>'
            '<book id="b2"><title>Emma</title></book>'
            '</library>'
        )
        source = self._create_xml_file('library.xml', content)
        output = self._output_path('library_out.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        self.assertTrue(processor.write_xml(output))
        written_root = ET.parse(output).getroot()
        self.assertEqual(written_root.tag, 'library')
        self.assertEqual(written_root.get('version'), '2.0')
        books = written_root.findall('book')
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].get('id'), 'b1')
        self.assertEqual([book.find('title').text for book in books], ['Dune', 'Emma'])

    def test_write_xml_4(self):
        # write_xml returns False when the file cannot be written (missing directory)
        source = self._create_xml_file('source4.xml', '<root></root>')
        missing_dir = os.path.join(self.temp_dir, 'does_not_exist')
        output = os.path.join(missing_dir, 'output.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        success = processor.write_xml(output)
        self.assertIs(success, False)
        self.assertFalse(os.path.exists(output))

    def test_write_xml_5(self):
        # A file written by write_xml can be read back by read_xml with the same content
        content = '<config><setting name="mode">fast</setting></config>'
        source = self._create_xml_file('config.xml', content)
        output = self._output_path('config_out.xml')
        writer = XMLProcessor(source)
        writer.read_xml()
        self.assertTrue(writer.write_xml(output))
        reader = XMLProcessor(output)
        root = reader.read_xml()
        self.assertEqual(root.tag, 'config')
        setting = root.find('setting')
        self.assertIsNotNone(setting)
        self.assertEqual(setting.get('name'), 'mode')
        self.assertEqual(setting.text, 'fast')

import os

import tempfile

import xml.etree.ElementTree as ET

class AgentTest_process_xml_data(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.created_files = []

    def tearDown(self):
        for path in self.created_files:
            if os.path.exists(path):
                os.remove(path)
        os.rmdir(self.temp_dir)

    def _create_xml_file(self, name, content):
        path = os.path.join(self.temp_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        self.created_files.append(path)
        return path

    def _output_path(self, name):
        path = os.path.join(self.temp_dir, name)
        self.created_files.append(path)
        return path

    def test_process_xml_data_1(self):
        # process_xml_data returns True on success and creates the file at the given name
        source = self._create_xml_file('source.xml', '<root><item>apple</item></root>')
        output = self._output_path('processed.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        success = processor.process_xml_data(output)
        self.assertIs(success, True)
        self.assertTrue(os.path.exists(output))

    def test_process_xml_data_2(self):
        # The file written by process_xml_data is well-formed XML with the same root element name
        content = (
            '<root>'
            '<item>apple</item>'
            '<item>banana</item>'
            '<item>orange</item>'
            '</root>'
        )
        source = self._create_xml_file('fruits.xml', content)
        output = self._output_path('fruits_processed.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        self.assertIs(processor.process_xml_data(output), True)
        written_root = ET.parse(output).getroot()
        self.assertEqual(written_root.tag, 'root')
        self.assertEqual(len(written_root.findall('item')), 3)

    def test_process_xml_data_3(self):
        # The output is written to a new file, so the source file is still present afterwards
        source = self._create_xml_file('source3.xml', '<root><item>apple</item></root>')
        output = self._output_path('output3.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        self.assertIs(processor.process_xml_data(output), True)
        self.assertTrue(os.path.exists(source))
        self.assertTrue(os.path.exists(output))
        self.assertNotEqual(os.path.abspath(source), os.path.abspath(output))

    def test_process_xml_data_4(self):
        # process_xml_data returns False when the file cannot be written (missing directory)
        source = self._create_xml_file('source4.xml', '<root></root>')
        missing_dir = os.path.join(self.temp_dir, 'does_not_exist')
        output = os.path.join(missing_dir, 'processed.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        success = processor.process_xml_data(output)
        self.assertIs(success, False)
        self.assertFalse(os.path.exists(output))

    def test_process_xml_data_5(self):
        # The processed file can be read back by read_xml and keeps its nested structure
        content = (
            '<library>'
            '<book><title>Dune</title></book>'
            '<book><title>Emma</title></book>'
            '</library>'
        )
        source = self._create_xml_file('library.xml', content)
        output = self._output_path('library_processed.xml')
        processor = XMLProcessor(source)
        processor.read_xml()
        self.assertIs(processor.process_xml_data(output), True)
        reader = XMLProcessor(output)
        root = reader.read_xml()
        self.assertIsInstance(root, ET.Element)
        self.assertEqual(root.tag, 'library')
        books = root.findall('book')
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].find('title').text, 'Dune')
        self.assertEqual(books[1].find('title').text, 'Emma')

import os

import tempfile

import xml.etree.ElementTree as ET

class AgentTest_find_element(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.created_files = []

    def tearDown(self):
        for path in self.created_files:
            if os.path.exists(path):
                os.remove(path)
        os.rmdir(self.temp_dir)

    def _create_xml_file(self, name, content):
        path = os.path.join(self.temp_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        self.created_files.append(path)
        return path

    def test_find_element_1(self):
        # find_element returns a list of the matching elements, in document order, with their text
        content = (
            '<root>'
            '<item>apple</item>'
            '<item>banana</item>'
            '<item>orange</item>'
            '</root>'
        )
        path = self._create_xml_file('fruits.xml', content)
        processor = XMLProcessor(path)
        processor.read_xml()
        items = processor.find_element('item')
        self.assertIsInstance(items, list)
        self.assertEqual(len(items), 3)
        for item in items:
            self.assertIsInstance(item, ET.Element)
        self.assertEqual([item.text for item in items], ['apple', 'banana', 'orange'])

    def test_find_element_2(self):
        # Only elements whose name matches exactly are returned, other elements are excluded
        content = (
            '<root>'
            '<item>apple</item>'
            '<other>pear</other>'
            '<items>kiwi</items>'
            '<item>banana</item>'
            '</root>'
        )
        path = self._create_xml_file('mixed.xml', content)
        processor = XMLProcessor(path)
        processor.read_xml()
        items = processor.find_element('item')
        self.assertEqual(len(items), 2)
        self.assertEqual([item.tag for item in items], ['item', 'item'])
        self.assertEqual([item.text for item in items], ['apple', 'banana'])

    def test_find_element_3(self):
        # When no element has the specified name, an empty list is returned
        content = '<root><item>apple</item><item>banana</item></root>'
        path = self._create_xml_file('none.xml', content)
        processor = XMLProcessor(path)
        processor.read_xml()
        result = processor.find_element('vegetable')
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])

    def test_find_element_4(self):
        # Matching elements are found at any depth of the document, not only among the root's direct children
        content = (
            '<root>'
            '<group><item>apple</item></group>'
            '<item>banana</item>'
            '<section><sub><item>orange</item></sub></section>'
            '</root>'
        )
        path = self._create_xml_file('nested.xml', content)
        processor = XMLProcessor(path)
        processor.read_xml()
        items = processor.find_element('item')
        self.assertEqual(len(items), 3)
        self.assertEqual([item.text for item in items], ['apple', 'banana', 'orange'])

    def test_find_element_5(self):
        # The returned elements keep their attributes and child elements from the file
        content = (
            '<library>'
            '<book id="b1"><title>Dune</title></book>'
            '<book id="b2"><title>Emma</title></book>'
            '</library>'
        )
        path = self._create_xml_file('library.xml', content)
        processor = XMLProcessor(path)
        processor.read_xml()
        books = processor.find_element('book')
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].get('id'), 'b1')
        self.assertEqual(books[1].get('id'), 'b2')
        self.assertEqual(books[0].find('title').text, 'Dune')
        self.assertEqual(books[1].find('title').text, 'Emma')