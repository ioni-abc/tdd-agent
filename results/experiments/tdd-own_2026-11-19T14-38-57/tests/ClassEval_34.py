import unittest


import unittest

import os

import shutil

import tempfile

from docx import Document

class AgentTest_read_text(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir, ignore_errors=True)

    def _make_docx(self, name, paragraphs):
        path = os.path.join(self.temp_dir, name)
        doc = Document()
        for text in paragraphs:
            doc.add_paragraph(text)
        doc.save(path)
        return path

    def test_read_text_1(self):
        path = self._make_docx("single.docx", ["Hello world"])
        handler = DocFileHandler(path)
        result = handler.read_text()
        self.assertIsInstance(result, str)

    def test_read_text_2(self):
        path = self._make_docx("single_content.docx", ["Hello world"])
        handler = DocFileHandler(path)
        result = handler.read_text()
        self.assertIn("Hello world", result)

    def test_read_text_3(self):
        path = self._make_docx(
            "multi.docx", ["First paragraph", "Second paragraph", "Third paragraph"]
        )
        handler = DocFileHandler(path)
        result = handler.read_text()
        self.assertIn("First paragraph", result)
        self.assertIn("Second paragraph", result)
        self.assertIn("Third paragraph", result)
        self.assertLess(result.index("First paragraph"), result.index("Second paragraph"))
        self.assertLess(result.index("Second paragraph"), result.index("Third paragraph"))

    def test_read_text_4(self):
        path = self._make_docx("empty.docx", [])
        handler = DocFileHandler(path)
        result = handler.read_text()
        self.assertIsInstance(result, str)
        self.assertEqual(result.strip(), "")

    def test_read_text_5(self):
        text = "Café — naïve 日本語 ünïcödé"
        path = self._make_docx("unicode.docx", [text])
        handler = DocFileHandler(path)
        result = handler.read_text()
        self.assertIn(text, result)

import unittest

import os

import shutil

import tempfile

from docx import Document

class AgentTest_add_heading(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir, ignore_errors=True)

    def _make_empty_docx(self, name):
        path = os.path.join(self.temp_dir, name)
        doc = Document()
        doc.save(path)
        return path

    def _find_paragraph(self, path, text):
        doc = Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text == text:
                return paragraph
        return None

    def test_add_heading_1(self):
        path = self._make_empty_docx("returns_bool.docx")
        handler = DocFileHandler(path)
        result = handler.add_heading("Introduction")
        self.assertIs(result, True)

    def test_add_heading_2(self):
        path = self._make_empty_docx("heading_text.docx")
        handler = DocFileHandler(path)
        handler.add_heading("Introduction")
        paragraph = self._find_paragraph(path, "Introduction")
        self.assertIsNotNone(paragraph)
        self.assertEqual(paragraph.text, "Introduction")

    def test_add_heading_3(self):
        path = self._make_empty_docx("default_level.docx")
        handler = DocFileHandler(path)
        handler.add_heading("Default Level Heading")
        paragraph = self._find_paragraph(path, "Default Level Heading")
        self.assertIsNotNone(paragraph)
        self.assertEqual(paragraph.style.name, "Heading 1")

    def test_add_heading_4(self):
        path = self._make_empty_docx("level_two.docx")
        handler = DocFileHandler(path)
        handler.add_heading("Second Level Heading", level=2)
        paragraph = self._find_paragraph(path, "Second Level Heading")
        self.assertIsNotNone(paragraph)
        self.assertEqual(paragraph.style.name, "Heading 2")

    def test_add_heading_5(self):
        path = self._make_empty_docx("level_three.docx")
        handler = DocFileHandler(path)
        handler.add_heading("Third Level Heading", level=3)
        paragraph = self._find_paragraph(path, "Third Level Heading")
        self.assertIsNotNone(paragraph)
        self.assertEqual(paragraph.style.name, "Heading 3")

import unittest

import os

import shutil

import tempfile

from docx import Document

class AgentTest_add_table(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir, ignore_errors=True)

    def _make_empty_docx(self, name):
        path = os.path.join(self.temp_dir, name)
        doc = Document()
        doc.save(path)
        return path

    def test_add_table_1(self):
        path = self._make_empty_docx("returns_bool.docx")
        handler = DocFileHandler(path)
        result = handler.add_table([["Name", "Age"], ["Alice", "30"]])
        self.assertIs(result, True)

    def test_add_table_2(self):
        path = self._make_empty_docx("table_added.docx")
        handler = DocFileHandler(path)
        handler.add_table([["Name", "Age"], ["Alice", "30"]])
        doc = Document(path)
        self.assertEqual(len(doc.tables), 1)

    def test_add_table_3(self):
        path = self._make_empty_docx("dimensions.docx")
        handler = DocFileHandler(path)
        handler.add_table([
            ["A", "B", "C", "D"],
            ["1", "2", "3", "4"],
            ["5", "6", "7", "8"],
        ])
        doc = Document(path)
        table = doc.tables[0]
        self.assertEqual(len(table.rows), 3)
        self.assertEqual(len(table.columns), 4)

    def test_add_table_4(self):
        path = self._make_empty_docx("cell_contents.docx")
        data = [["Name", "City"], ["Alice", "Paris"], ["Bob", "Berlin"]]
        handler = DocFileHandler(path)
        handler.add_table(data)
        doc = Document(path)
        table = doc.tables[0]
        for r, row in enumerate(data):
            for c, value in enumerate(row):
                self.assertEqual(table.cell(r, c).text, value)

    def test_add_table_5(self):
        path = self._make_empty_docx("invalid_data.docx")
        handler = DocFileHandler(path)
        result = handler.add_table(None)
        self.assertIs(result, False)

import unittest

import os

import shutil

import tempfile

from docx import Document

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

class AgentTest__get_alignment_value(unittest.TestCase):

    def setUp(self):
        self.handler = DocFileHandler("dummy.docx")

    def test__get_alignment_value_1(self):
        result = self.handler._get_alignment_value('left')
        self.assertEqual(result, WD_PARAGRAPH_ALIGNMENT.LEFT)

    def test__get_alignment_value_2(self):
        result = self.handler._get_alignment_value('center')
        self.assertEqual(result, WD_PARAGRAPH_ALIGNMENT.CENTER)

    def test__get_alignment_value_3(self):
        result = self.handler._get_alignment_value('right')
        self.assertEqual(result, WD_PARAGRAPH_ALIGNMENT.RIGHT)

    def test__get_alignment_value_4(self):
        result = self.handler._get_alignment_value('center')
        self.assertIsInstance(result, int)

    def test__get_alignment_value_5(self):
        left = self.handler._get_alignment_value('left')
        center = self.handler._get_alignment_value('center')
        right = self.handler._get_alignment_value('right')
        self.assertEqual(len({left, center, right}), 3)

import unittest

import os

import shutil

import tempfile

from docx import Document

from docx.shared import Pt

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

class AgentTest_write_text(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir, ignore_errors=True)

    def _make_empty_docx(self, name):
        path = os.path.join(self.temp_dir, name)
        doc = Document()
        doc.save(path)
        return path

    def _find_paragraph(self, path, text):
        doc = Document(path)
        for paragraph in doc.paragraphs:
            if text in paragraph.text:
                return paragraph
        return None

    def test_write_text_1(self):
        path = self._make_empty_docx("returns_bool.docx")
        handler = DocFileHandler(path)
        result = handler.write_text("Hello world")
        self.assertIs(result, True)

    def test_write_text_2(self):
        path = self._make_empty_docx("content_written.docx")
        handler = DocFileHandler(path)
        handler.write_text("Hello world")
        paragraph = self._find_paragraph(path, "Hello world")
        self.assertIsNotNone(paragraph)
        self.assertIn("Hello world", paragraph.text)

    def test_write_text_3(self):
        path = self._make_empty_docx("center_alignment.docx")
        handler = DocFileHandler(path)
        handler.write_text("Centered text", alignment='center')
        paragraph = self._find_paragraph(path, "Centered text")
        self.assertIsNotNone(paragraph)
        self.assertEqual(paragraph.alignment, WD_PARAGRAPH_ALIGNMENT.CENTER)

    def test_write_text_4(self):
        path = self._make_empty_docx("font_size.docx")
        handler = DocFileHandler(path)
        handler.write_text("Big text", font_size=20)
        paragraph = self._find_paragraph(path, "Big text")
        self.assertIsNotNone(paragraph)
        text_runs = [run for run in paragraph.runs if run.text.strip()]
        self.assertTrue(text_runs)
        for run in text_runs:
            self.assertEqual(run.font.size, Pt(20))

    def test_write_text_5(self):
        path = self._make_empty_docx("invalid_path.docx")
        missing_dir_path = os.path.join(self.temp_dir, "missing_dir", "output.docx")
        handler = DocFileHandler(missing_dir_path)
        result = handler.write_text("This cannot be saved")
        self.assertIs(result, False)