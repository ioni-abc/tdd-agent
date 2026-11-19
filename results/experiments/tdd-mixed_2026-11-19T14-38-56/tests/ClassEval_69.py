import os
import unittest
from PyPDF2 import PdfFileReader
from reportlab.pdfgen import canvas




class TestPDFHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_files = ["test1.pdf", "test2.pdf"]
        cls.test_text = ["This is a test1.", "This is a test2."]
        for i in range(2):
            c = canvas.Canvas(cls.test_files[i])
            c.drawString(100, 100, cls.test_text[i])
            c.showPage()
            c.save()

    @classmethod
    def tearDownClass(cls):
        for filename in cls.test_files:
            os.remove(filename)
        os.remove("merged.pdf")

import os

import unittest

from PyPDF2 import PdfFileReader

from reportlab.pdfgen import canvas

class AgentTest_merge_pdfs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.single_file = "merge_single.pdf"
        cls.multi_file = "merge_multi.pdf"
        cls.output_file = "merge_output.pdf"
        cls.output_file_single = "merge_output_single.pdf"

        c = canvas.Canvas(cls.single_file)
        c.drawString(100, 100, "Alpha page")
        c.showPage()
        c.save()

        c = canvas.Canvas(cls.multi_file)
        c.drawString(100, 100, "Beta page 1")
        c.showPage()
        c.drawString(100, 100, "Beta page 2")
        c.showPage()
        c.save()

    @classmethod
    def tearDownClass(cls):
        for filename in (cls.single_file, cls.multi_file,
                         cls.output_file, cls.output_file_single):
            if os.path.exists(filename):
                os.remove(filename)

    def _page_texts(self, filepath):
        reader = PdfFileReader(filepath)
        return [reader.getPage(i).extractText() for i in range(reader.getNumPages())]

    def test_merge_pdfs_1(self):
        handler = PDFHandler([self.single_file, self.multi_file])
        result = handler.merge_pdfs(self.output_file)
        self.assertEqual(result, f"Merged PDFs saved at {self.output_file}")

    def test_merge_pdfs_2(self):
        handler = PDFHandler([self.single_file, self.multi_file])
        handler.merge_pdfs(self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

    def test_merge_pdfs_3(self):
        handler = PDFHandler([self.single_file, self.multi_file])
        handler.merge_pdfs(self.output_file)
        reader = PdfFileReader(self.output_file)
        self.assertEqual(reader.getNumPages(), 3)

    def test_merge_pdfs_4(self):
        handler = PDFHandler([self.single_file, self.multi_file])
        handler.merge_pdfs(self.output_file)
        combined = " ".join(self._page_texts(self.output_file))
        self.assertIn("Alpha page", combined)
        self.assertIn("Beta page 1", combined)
        self.assertIn("Beta page 2", combined)

    def test_merge_pdfs_5(self):
        handler = PDFHandler([self.single_file])
        result = handler.merge_pdfs(self.output_file_single)
        self.assertEqual(result, f"Merged PDFs saved at {self.output_file_single}")
        reader = PdfFileReader(self.output_file_single)
        self.assertEqual(reader.getNumPages(), 1)
        self.assertIn("Alpha page", self._page_texts(self.output_file_single)[0])

class PDFHandlerTestMergePdfs(unittest.TestCase):
    def setUp(self) -> None:
        TestPDFHandler.setUpClass()

    def tearDown(self) -> None:
        TestPDFHandler.tearDownClass()

    def test_merge_pdfs(self):
        TestPDFHandler.setUpClass()
        handler = PDFHandler(TestPDFHandler.test_files)
        result = handler.merge_pdfs("merged.pdf")
        self.assertEqual("Merged PDFs saved at merged.pdf", result)
        self.assertTrue(os.path.exists("merged.pdf"))