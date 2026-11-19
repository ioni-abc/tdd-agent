try:
    import PyPDF2
except ImportError:  # pragma: no cover - fallback for environments that only ship pypdf
    import pypdf as PyPDF2

# Compatibility shim: newer PyPDF2 releases renamed PdfFileReader to PdfReader
# (and PdfFileWriter to PdfWriter). Expose the legacy names so code importing
# them from PyPDF2 still works.
if not hasattr(PyPDF2, "PdfFileReader") and hasattr(PyPDF2, "PdfReader"):
    PyPDF2.PdfFileReader = PyPDF2.PdfReader
if not hasattr(PyPDF2, "PdfFileWriter") and hasattr(PyPDF2, "PdfWriter"):
    PyPDF2.PdfFileWriter = PyPDF2.PdfWriter


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
        if hasattr(PyPDF2, "PdfReader"):
            reader_cls = PyPDF2.PdfReader
        else:
            reader_cls = PyPDF2.PdfFileReader
        self.readers = [reader_cls(fp) for fp in filepaths]

    @staticmethod
    def _pages(reader):
        """Return a list of pages for a reader (works with old and new PyPDF2 APIs)."""
        if hasattr(reader, "pages"):
            return list(reader.pages)
        return [reader.getPage(i) for i in range(reader.getNumPages())]

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
            add = writer.add_page
        else:
            writer = PyPDF2.PdfFileWriter()
            add = writer.addPage
        for reader in self.readers:
            for page in self._pages(reader):
                add(page)
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
            text = ""
            for page in self._pages(reader):
                if hasattr(page, "extract_text"):
                    text += page.extract_text() or ""
                else:
                    text += page.extractText() or ""
            pdf_texts.append(text)
        return pdf_texts