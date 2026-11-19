import PyPDF2


def _open_reader(filepath):
    """Open a PDF with whichever PyPDF2 reader class the installed version provides."""
    if hasattr(PyPDF2, "PdfReader"):
        return PyPDF2.PdfReader(filepath)
    return PyPDF2.PdfFileReader(filepath)


def _page_extract_text(page):
    """Extract text from a page using whichever API the installed PyPDF2 provides."""
    if hasattr(page, "extract_text"):
        return page.extract_text() or ""
    return page.extractText() or ""


if hasattr(PyPDF2, "PdfReader"):
    # Provide legacy (PyPDF2 < 3.0) compatibility aliases on top of the new API.
    # PyPDF2 3.x keeps a stub extractText that raises DeprecationError, so it must
    # be overridden unconditionally.
    def _legacy_extract_text(self):
        return self.extract_text()
    PyPDF2.PageObject.extractText = _legacy_extract_text

    class _LegacyPdfFileReader:
        """Minimal legacy PdfFileReader wrapper around PdfReader."""

        def __init__(self, stream, *args, **kwargs):
            self._reader = PyPDF2.PdfReader(stream, *args, **kwargs)

        @property
        def pages(self):
            return self._reader.pages

        def getPage(self, index):
            return self._reader.pages[index]

        def getNumPages(self):
            return len(self._reader.pages)

        def extractText(self):
            return "".join(_page_extract_text(p) for p in self._reader.pages)

    PyPDF2.PdfFileReader = _LegacyPdfFileReader


class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.filepaths = filepaths
        self.readers = [_open_reader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
        if hasattr(PyPDF2, "PdfWriter"):
            writer = PyPDF2.PdfWriter()
            add_page = writer.add_page
        else:
            writer = PyPDF2.PdfFileWriter()
            add_page = writer.addPage

        for reader in self.readers:
            for page in reader.pages:
                add_page(page)

        with open(output_filepath, "wb") as output_file:
            writer.write(output_file)

        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        pdf_texts = []
        for reader in self.readers:
            pdf_texts.append("".join(_page_extract_text(page) for page in reader.pages))
        return pdf_texts