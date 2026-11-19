import unittest
import os




class DocFileHandlerTestReadText(unittest.TestCase):
    def test_read_text_1(self):
        self.file_path = "test_example.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("Initial content")
        doc.save(self.file_path)

        text_content = self.handler.read_text()
        expected_content = "Initial content"
        self.assertEqual(text_content, expected_content)

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_read_text_2(self):
        self.file_path = "test_example.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("111")
        doc.save(self.file_path)

        text_content = self.handler.read_text()
        expected_content = "111"
        self.assertEqual(text_content, expected_content)

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_read_text_3(self):
        self.file_path = "test_example.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("aaa")
        doc.save(self.file_path)

        text_content = self.handler.read_text()
        expected_content = "aaa"
        self.assertEqual(text_content, expected_content)

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

import unittest

import os

from docx import Document

class AgentTest_read_text(unittest.TestCase):
    def test_read_text_1(self):
        self.file_path = "test_example_empty.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.save(self.file_path)

        try:
            text_content = self.handler.read_text()
            self.assertIsInstance(text_content, str)
            self.assertEqual(text_content, "")
        finally:
            if os.path.exists(self.file_path):
                os.remove(self.file_path)

    def test_read_text_2(self):
        self.file_path = "test_example_two_paragraphs.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("First paragraph")
        doc.add_paragraph("Second paragraph")
        doc.save(self.file_path)

        try:
            text_content = self.handler.read_text()
            self.assertIsInstance(text_content, str)
            self.assertIn("First paragraph", text_content)
            self.assertIn("Second paragraph", text_content)
            self.assertLess(text_content.index("First paragraph"),
                            text_content.index("Second paragraph"))
        finally:
            if os.path.exists(self.file_path):
                os.remove(self.file_path)

class DocFileHandlerTestAddHeading(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_example.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("Initial content")
        doc.save(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_heading_1(self):
        heading = "Test Heading 1"
        self.handler.add_heading(heading)
        doc = Document(self.file_path)
        headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
        self.assertIn(heading, headings)

    def test_add_heading_2(self):
        heading = "Test Heading 2"
        self.handler.add_heading(heading)
        doc = Document(self.file_path)
        headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
        self.assertIn(heading, headings)

    def test_add_heading_3(self):
        heading = "Test Heading 3"
        self.handler.add_heading(heading)
        doc = Document(self.file_path)
        headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
        self.assertIn(heading, headings)

import unittest

import os

from docx import Document

class AgentTest_add_heading(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_example_add_heading.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("Initial content")
        doc.save(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_heading_1(self):
        heading = "Default Level Heading"
        self.handler.add_heading(heading)
        doc = Document(self.file_path)
        matches = [p for p in doc.paragraphs if p.text == heading]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].style.name, "Heading 1")

    def test_add_heading_2(self):
        heading = "Level Two Heading"
        result = self.handler.add_heading(heading, level=2)
        self.assertIs(result, True)
        doc = Document(self.file_path)
        matches = [p for p in doc.paragraphs if p.text == heading]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].style.name, "Heading 2")

class DocFileHandlerTestAddTable(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_example.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("Initial content")
        doc.save(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_table_1(self):
        data = [['Name', 'Age']]
        self.handler.add_table(data)
        doc = Document(self.file_path)
        table = doc.tables[0]
        self.assertEqual(len(table.rows), 1)
        self.assertEqual(len(table.columns), 2)

    def test_add_table_2(self):
        data = [['Name', 'Age'], ['John', '25']]
        self.handler.add_table(data)
        doc = Document(self.file_path)
        table = doc.tables[0]
        self.assertEqual(len(table.rows), 2)
        self.assertEqual(len(table.columns), 2)
        self.assertEqual(table.cell(1, 0).text, 'John')

    def test_add_table_3(self):
        data = [['Name', 'Age'], ['John', '25'], ['Emma', '30']]
        self.handler.add_table(data)
        doc = Document(self.file_path)
        table = doc.tables[0]
        self.assertEqual(len(table.rows), 3)
        self.assertEqual(len(table.columns), 2)
        self.assertEqual(table.cell(1, 0).text, 'John')
        self.assertEqual(table.cell(2, 1).text, '30')

import unittest

import os

from docx import Document

class AgentTest_add_table(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_example_add_table.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("Initial content")
        doc.save(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_table_1(self):
        data = [['Name', 'Age'], ['John', '25']]
        result = self.handler.add_table(data)
        self.assertIs(result, True)

    def test_add_table_2(self):
        data = [['Item', 'Qty', 'Price'], ['Pen', '3', '1.50'], ['Book', '2', '12.00']]
        self.handler.add_table(data)
        doc = Document(self.file_path)
        self.assertIn("Initial content", [p.text for p in doc.paragraphs])
        self.assertEqual(len(doc.tables), 1)
        table = doc.tables[0]
        for r, row in enumerate(data):
            for c, value in enumerate(row):
                self.assertEqual(table.cell(r, c).text, value)

class DocFileHandlerTest(unittest.TestCase):
    def test_DocFileHandler(self):
        self.file_path = "test_example.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("Initial content")
        doc.save(self.file_path)

        text_content = self.handler.read_text()
        expected_content = "Initial content"
        self.assertEqual(text_content, expected_content)

        new_content = "New content 1"
        self.handler.write_text(new_content)
        text_content = self.handler.read_text()
        self.assertEqual(text_content, new_content)

        heading = "Test Heading 1"
        self.handler.add_heading(heading)
        doc = Document(self.file_path)
        headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
        self.assertIn(heading, headings)

        data = [['Name', 'Age']]
        self.handler.add_table(data)
        doc = Document(self.file_path)
        table = doc.tables[0]
        self.assertEqual(len(table.rows), 1)
        self.assertEqual(len(table.columns), 2)

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

class DocFileHandlerTestWriteText(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_example.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("Initial content")
        doc.save(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write_text_1(self):
        new_content = "New content 1"
        self.handler.write_text(new_content)
        text_content = self.handler.read_text()
        self.assertEqual(text_content, new_content)

    def test_write_text_2(self):
        new_content = "New content 2"
        self.handler.write_text(new_content)
        text_content = self.handler.read_text()
        self.assertEqual(text_content, new_content)

    def test_write_text_3(self):
        new_content = "New content 3"
        self.handler.write_text(new_content)
        text_content = self.handler.read_text()
        self.assertEqual(text_content, new_content)

import unittest

import os

from docx import Document

from docx.shared import Pt

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

class AgentTest_write_text(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_example_write_text.docx"
        self.handler = DocFileHandler(self.file_path)
        doc = Document()
        doc.add_paragraph("Initial content")
        doc.save(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write_text_1(self):
        content = "Centered text"
        result = self.handler.write_text(content, font_size=20, alignment='center')
        self.assertIs(result, True)

        doc = Document(self.file_path)
        matches = [p for p in doc.paragraphs if p.text == content]
        self.assertGreaterEqual(len(matches), 1)
        paragraph = matches[0]
        self.assertEqual(paragraph.alignment, WD_PARAGRAPH_ALIGNMENT.CENTER)
        sized_runs = [r for r in paragraph.runs if r.text]
        self.assertTrue(sized_runs)
        for run in sized_runs:
            self.assertEqual(run.font.size, Pt(20))

    def test_write_text_2(self):
        content = "Right aligned text"
        result = self.handler.write_text(content, alignment='right')
        self.assertIs(result, True)

        doc = Document(self.file_path)
        matches = [p for p in doc.paragraphs if p.text == content]
        self.assertGreaterEqual(len(matches), 1)
        paragraph = matches[0]
        self.assertEqual(paragraph.alignment, WD_PARAGRAPH_ALIGNMENT.RIGHT)
        sized_runs = [r for r in paragraph.runs if r.text]
        self.assertTrue(sized_runs)
        for run in sized_runs:
            self.assertEqual(run.font.size, Pt(12))