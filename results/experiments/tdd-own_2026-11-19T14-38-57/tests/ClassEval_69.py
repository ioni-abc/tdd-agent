import unittest


import os

import tempfile

import unittest

import PyPDF2

def _make_blank_pdf(path, num_pages):
    writer = PyPDF2.PdfFileWriter()
    for _ in range(num_pages):
        writer.addBlankPage(612, 792)
    with open(path, "wb") as f:
        writer.write(f)
    return path

class AgentTest_merge_pdfs(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def _path(self, name):
        return os.path.join(self.dir, name)

    def test_merge_pdfs_1(self):
        a = _make_blank_pdf(self._path("a.pdf"), 2)
        b = _make_blank_pdf(self._path("b.pdf"), 3)
        out = self._path("out.pdf")
        handler = PDFHandler([a, b])
        result = handler.merge_pdfs(out)
        self.assertEqual(result, "Merged PDFs saved at {}".format(out))

    def test_merge_pdfs_2(self):
        a = _make_blank_pdf(self._path("a.pdf"), 1)
        b = _make_blank_pdf(self._path("b.pdf"), 1)
        out = self._path("merged.pdf")
        handler = PDFHandler([a, b])
        handler.merge_pdfs(out)
        self.assertTrue(os.path.isfile(out))

    def test_merge_pdfs_3(self):
        a = _make_blank_pdf(self._path("a.pdf"), 2)
        b = _make_blank_pdf(self._path("b.pdf"), 3)
        out = self._path("out.pdf")
        handler = PDFHandler([a, b])
        handler.merge_pdfs(out)
        merged = PyPDF2.PdfFileReader(out)
        self.assertEqual(merged.numPages, 5)

    def test_merge_pdfs_4(self):
        paths = [
            _make_blank_pdf(self._path("a.pdf"), 1),
            _make_blank_pdf(self._path("b.pdf"), 4),
            _make_blank_pdf(self._path("c.pdf"), 2),
        ]
        out = self._path("all.pdf")
        handler = PDFHandler(paths)
        handler.merge_pdfs(out)
        merged = PyPDF2.PdfFileReader(out)
        self.assertEqual(merged.numPages, 7)

    def test_merge_pdfs_5(self):
        a = _make_blank_pdf(self._path("single.pdf"), 3)
        out = self._path("copy.pdf")
        handler = PDFHandler([a])
        result = handler.merge_pdfs(out)
        self.assertEqual(result, "Merged PDFs saved at {}".format(out))
        merged = PyPDF2.PdfFileReader(out)
        self.assertEqual(merged.numPages, 3)

import os

import tempfile

import unittest

import PyPDF2

def _make_text_pdf(path, text):
    content = "BT /F1 24 Tf 72 700 Td ({}) Tj ET".format(text)
    objects = [
        "<< /Type /Catalog /Pages 2 0 R >>",
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        "/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        "<< /Length {} >>\nstream\n{}\nendstream".format(len(content), content),
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(out))
        out += "{} 0 obj\n{}\nendobj\n".format(i, obj).encode("latin-1")
    xref_pos = len(out)
    out += "xref\n0 {}\n".format(len(objects) + 1).encode("latin-1")
    out += b"0000000000 65535 f \n"
    for off in offsets:
        out += "{:010d} 00000 n \n".format(off).encode("latin-1")
    out += (
        "trailer\n<< /Size {} /Root 1 0 R >>\nstartxref\n{}\n%%EOF\n".format(
            len(objects) + 1, xref_pos
        )
    ).encode("latin-1")
    with open(path, "wb") as f:
        f.write(bytes(out))
    return path

class AgentTest_extract_text_from_pdfs(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def _path(self, name):
        return os.path.join(self.dir, name)

    def test_extract_text_from_pdfs_1(self):
        a = _make_text_pdf(self._path("a.pdf"), "Test a.pdf")
        b = _make_text_pdf(self._path("b.pdf"), "Test b.pdf")
        handler = PDFHandler([a, b])
        texts = handler.extract_text_from_pdfs()
        self.assertIsInstance(texts, list)
        self.assertEqual(len(texts), 2)

    def test_extract_text_from_pdfs_2(self):
        a = _make_text_pdf(self._path("a.pdf"), "Test a.pdf")
        b = _make_text_pdf(self._path("b.pdf"), "Test b.pdf")
        handler = PDFHandler([a, b])
        texts = handler.extract_text_from_pdfs()
        for item in texts:
            self.assertIsInstance(item, str)

    def test_extract_text_from_pdfs_3(self):
        a = _make_text_pdf(self._path("a.pdf"), "Test a.pdf")
        b = _make_text_pdf(self._path("b.pdf"), "Test b.pdf")
        handler = PDFHandler([a, b])
        texts = handler.extract_text_from_pdfs()
        self.assertEqual(texts, ["Test a.pdf", "Test b.pdf"])

    def test_extract_text_from_pdfs_4(self):
        a = _make_text_pdf(self._path("a.pdf"), "Test a.pdf")
        b = _make_text_pdf(self._path("b.pdf"), "Test b.pdf")
        c = _make_text_pdf(self._path("c.pdf"), "Test c.pdf")
        handler = PDFHandler([c, a, b])
        texts = handler.extract_text_from_pdfs()
        self.assertEqual(texts, ["Test c.pdf", "Test a.pdf", "Test b.pdf"])

    def test_extract_text_from_pdfs_5(self):
        a = _make_text_pdf(self._path("a.pdf"), "Test a.pdf")
        handler = PDFHandler([a])
        texts = handler.extract_text_from_pdfs()
        self.assertEqual(texts, ["Test a.pdf"])