import unittest
import os




class XMLProcessorTestReadXml(unittest.TestCase):
    def test_read_xml_1(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n    <item>orange</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        root = self.processor.read_xml()
        self.assertIsNotNone(root)
        lst = root.findall('item')
        self.assertEqual(lst[0].text, 'apple')
        self.assertEqual(lst[1].text, 'banana')
        self.assertEqual(lst[2].text, 'orange')

        os.remove('test.xml')

    def test_read_xml_2(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>aaa</item>\n    <item>bbb</item>\n    <item>ccc</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        root = self.processor.read_xml()
        self.assertIsNotNone(root)
        lst = root.findall('item')
        self.assertEqual(lst[0].text, 'aaa')
        self.assertEqual(lst[1].text, 'bbb')
        self.assertEqual(lst[2].text, 'ccc')

        os.remove('test.xml')

    def test_read_xml_3(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        root = self.processor.read_xml()
        self.assertIsNotNone(root)
        lst = root.findall('item')
        self.assertEqual(lst[0].text, 'apple')

        os.remove('test.xml')

    def test_read_xml_4(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        root = self.processor.read_xml()
        self.assertIsNotNone(root)
        lst = root.findall('item')
        self.assertEqual(lst[0].text, 'apple')
        self.assertEqual(lst[1].text, 'banana')

        os.remove('test.xml')

import unittest

import os

import xml.etree.ElementTree as ET

class AgentTest_read_xml(unittest.TestCase):
    def test_read_xml_1(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n    <item>orange</item>\n</root>')
        try:
            processor = XMLProcessor('test.xml')
            root = processor.read_xml()
            self.assertIsInstance(root, ET.Element)
            self.assertEqual(root.tag, 'root')
        finally:
            os.remove('test.xml')

    def test_read_xml_2(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>red</item>\n    <item>green</item>\n</root>')
        try:
            processor = XMLProcessor('test.xml')
            self.assertIsNone(processor.root)
            root = processor.read_xml()
            self.assertIsNotNone(root)
            lst = root.findall('item')
            self.assertEqual(len(lst), 2)
            self.assertEqual(lst[0].text, 'red')
            self.assertEqual(lst[1].text, 'green')
        finally:
            os.remove('test.xml')

class XMLProcessorTestWriteXml(unittest.TestCase):
    def test_write_xml_1(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n    <item>orange</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        file_name = 'output.xml'
        result = self.processor.write_xml(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'apple')
        self.assertEqual(lst[1].text, 'banana')
        self.assertEqual(lst[2].text, 'orange')

        os.remove('output.xml')
        os.remove('test.xml')

    def test_write_xml_2(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        file_name = 'output.xml'
        result = self.processor.write_xml(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'apple')
        self.assertEqual(lst[1].text, 'banana')

        os.remove('output.xml')
        os.remove('test.xml')

    def test_write_xml_3(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        file_name = 'output.xml'
        result = self.processor.write_xml(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'apple')

        os.remove('output.xml')
        os.remove('test.xml')

    def test_write_xml_4(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>aaa</item>\n    <item>bbb</item>\n    <item>ccc</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        file_name = 'output.xml'
        result = self.processor.write_xml(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'aaa')
        self.assertEqual(lst[1].text, 'bbb')
        self.assertEqual(lst[2].text, 'ccc')

        os.remove('output.xml')
        os.remove('test.xml')

import unittest

import os

import xml.etree.ElementTree as ET

class AgentTest_write_xml(unittest.TestCase):
    def test_write_xml_1(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n</root>')
        try:
            processor = XMLProcessor('test.xml')
            processor.read_xml()
            bad_path = os.path.join('no_such_directory_for_test', 'output.xml')
            result = processor.write_xml(bad_path)
            self.assertIsInstance(result, bool)
            self.assertFalse(result)
            self.assertFalse(os.path.exists(bad_path))
        finally:
            os.remove('test.xml')

    def test_write_xml_2(self):
        with open('test.xml', 'w') as f:
            f.write('<catalog version="2"><book id="1"><title>Dune</title></book>'
                    '<book id="2"><title>Emma</title></book></catalog>')
        try:
            processor = XMLProcessor('test.xml')
            processor.read_xml()
            result = processor.write_xml('output.xml')
            self.assertTrue(result)

            written = ET.parse('output.xml').getroot()
            self.assertEqual(written.tag, 'catalog')
            self.assertEqual(written.get('version'), '2')
            books = written.findall('book')
            self.assertEqual(len(books), 2)
            self.assertEqual(books[0].get('id'), '1')
            self.assertEqual(books[0].find('title').text, 'Dune')
            self.assertEqual(books[1].get('id'), '2')
            self.assertEqual(books[1].find('title').text, 'Emma')
        finally:
            if os.path.exists('output.xml'):
                os.remove('output.xml')
            os.remove('test.xml')

class XMLProcessorTestProcessXmlData(unittest.TestCase):
    def test_process_xml_data_1(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n    <item>orange</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        file_name = 'processed.xml'
        result = self.processor.process_xml_data(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'APPLE')
        self.assertEqual(lst[1].text, 'BANANA')
        self.assertEqual(lst[2].text, 'ORANGE')

        os.remove('processed.xml')
        os.remove('test.xml')

    def test_process_xml_data_2(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        file_name = 'processed.xml'
        result = self.processor.process_xml_data(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'APPLE')
        self.assertEqual(lst[1].text, 'BANANA')

        os.remove('processed.xml')
        os.remove('test.xml')

    def test_process_xml_data_3(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        file_name = 'processed.xml'
        result = self.processor.process_xml_data(file_name)
        self.assertTrue(result)

        processor1 = XMLProcessor(file_name)
        tree1 = ET.parse(processor1.file_name)
        processor1.root = tree1.getroot()

        self.assertIsNotNone(processor1.root)
        lst = processor1.root.findall('item')
        self.assertEqual(lst[0].text, 'APPLE')

        os.remove('processed.xml')
        os.remove('test.xml')

import unittest

import os

import xml.etree.ElementTree as ET

class AgentTest_process_xml_data(unittest.TestCase):
    def test_process_xml_data_1(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n</root>')
        try:
            processor = XMLProcessor('test.xml')
            processor.read_xml()
            bad_path = os.path.join('no_such_directory_for_test', 'processed.xml')
            result = processor.process_xml_data(bad_path)
            self.assertIsInstance(result, bool)
            self.assertFalse(result)
            self.assertFalse(os.path.exists(bad_path))
        finally:
            os.remove('test.xml')

    def test_process_xml_data_2(self):
        with open('test.xml', 'w') as f:
            f.write('<catalog version="2"><book id="1"><title>Dune</title></book>'
                    '<book id="2"><title>Emma</title></book></catalog>')
        try:
            processor = XMLProcessor('test.xml')
            processor.read_xml()
            result = processor.process_xml_data('processed.xml')
            self.assertTrue(result)

            processed = ET.parse('processed.xml').getroot()
            self.assertEqual(processed.tag, 'catalog')
            books = processed.findall('book')
            self.assertEqual(len(books), 2)
            self.assertIsNotNone(books[0].find('title'))
            self.assertIsNotNone(books[1].find('title'))
        finally:
            if os.path.exists('processed.xml'):
                os.remove('processed.xml')
            os.remove('test.xml')

class XMLProcessorTestFindElement(unittest.TestCase):
    def test_find_element_1(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n    <item>orange</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        element_name = 'item'
        root = self.processor.read_xml()
        elements = self.processor.find_element(element_name)
        self.assertEqual(len(elements), 3)
        self.assertEqual(elements[0].text, 'apple')
        self.assertEqual(elements[1].text, 'banana')
        self.assertEqual(elements[2].text, 'orange')

        os.remove('test.xml')

    def test_find_element_2(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        element_name = 'item'
        root = self.processor.read_xml()
        elements = self.processor.find_element(element_name)
        self.assertEqual(len(elements), 2)
        self.assertEqual(elements[0].text, 'apple')
        self.assertEqual(elements[1].text, 'banana')

        os.remove('test.xml')

    def test_find_element_3(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n</root>')
        self.xml_file = 'test.xml'
        self.processor = XMLProcessor(self.xml_file)
        tree = ET.parse(self.processor.file_name)
        self.processor.root = tree.getroot()

        element_name = 'item'
        root = self.processor.read_xml()
        elements = self.processor.find_element(element_name)
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0].text, 'apple')

        os.remove('test.xml')

import unittest

import os

import xml.etree.ElementTree as ET

class AgentTest_find_element(unittest.TestCase):
    def test_find_element_1(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <item>banana</item>\n</root>')
        try:
            processor = XMLProcessor('test.xml')
            processor.read_xml()
            elements = processor.find_element('color')
            self.assertIsInstance(elements, list)
            self.assertEqual(len(elements), 0)
        finally:
            os.remove('test.xml')

    def test_find_element_2(self):
        with open('test.xml', 'w') as f:
            f.write('<root>\n    <item>apple</item>\n    <name>x</name>\n    <item>banana</item>\n</root>')
        try:
            processor = XMLProcessor('test.xml')
            processor.read_xml()

            items = processor.find_element('item')
            self.assertIsInstance(items, list)
            self.assertEqual(len(items), 2)
            for element in items:
                self.assertIsInstance(element, ET.Element)
                self.assertEqual(element.tag, 'item')
            self.assertEqual(items[0].text, 'apple')
            self.assertEqual(items[1].text, 'banana')

            names = processor.find_element('name')
            self.assertIsInstance(names, list)
            self.assertEqual(len(names), 1)
            self.assertEqual(names[0].tag, 'name')
            self.assertEqual(names[0].text, 'x')
        finally:
            os.remove('test.xml')