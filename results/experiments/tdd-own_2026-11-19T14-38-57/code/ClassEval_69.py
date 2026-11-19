import PyPDF2


def _install_legacy_aliases():
    """Expose PyPDF2 1.x-style names on top of PyPDF2 3.x classes when needed."""
    modern_writer = getattr(PyPDF2, "PdfWriter", None)
    if modern_writer is not None:
        class _LegacyPdfFileWriter(modern_writer):
            def addBlankPage(self, width=612, height=792):
                return self.add_blank_page(width, height)

            def addPage(self, page):
                return self.add_page(page)

        PyPDF2.PdfFileWriter = _LegacyPdfFileWriter

    modern_reader = getattr(PyPDF2, "PdfReader", None)
    if modern_reader is not None:
        class _LegacyPdfFileReader(modern_reader):
            @property
            def numPages(self):
                return len(self.pages)

            def getPage(self, index):
                return self.pages[index]

            def getNumPages(self):
                return len(self.pages)

        PyPDF2.PdfFileReader = _LegacyPdfFileReader


_install_legacy_aliases()


def _get_reader_cls():
    reader_cls = getattr(PyPDF2, "PdfReader", None)
    if reader_cls is None:
        reader_cls = getattr(PyPDF2, "PdfFileReader")
    return reader_cls


def _get_writer_cls():
    writer_cls = getattr(PyPDF2, "PdfWriter", None)
    if writer_cls is None:
        writer_cls = getattr(PyPDF2, "PdfFileWriter")
    return writer_cls


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
        reader_cls = _get_reader_cls()
        self.readers = [reader_cls(fp) for fp in filepaths]

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
        writer_cls = _get_writer_cls()
        writer = writer_cls()
        add_page = getattr(writer, "add_page", None) or writer.addPage

        for reader in self.readers:
            pages = reader.pages
            for page in pages:
                add_page(page)

        with open(output_filepath, "wb") as f:
            writer.write(f)

        return "Merged PDFs saved at {}".format(output_filepath)

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
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            pdf_texts.append(text)
        return pdf_texts