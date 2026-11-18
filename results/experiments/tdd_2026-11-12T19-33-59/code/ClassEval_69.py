import PyPDF2

try:
    from PyPDF2 import PdfReader as _PdfReader, PdfWriter as _PdfWriter
except ImportError:
    from PyPDF2 import PdfFileReader as _PdfReader, PdfFileWriter as _PdfWriter

# Provide legacy names on newer PyPDF2 releases so code importing
# PdfFileReader/PdfFileWriter from PyPDF2 keeps working.
if not hasattr(PyPDF2, "PdfFileReader") and hasattr(PyPDF2, "PdfReader"):
    PyPDF2.PdfFileReader = PyPDF2.PdfReader
if not hasattr(PyPDF2, "PdfFileWriter") and hasattr(PyPDF2, "PdfWriter"):
    PyPDF2.PdfFileWriter = PyPDF2.PdfWriter


def _add_page(writer, page):
    if hasattr(writer, "add_page"):
        return writer.add_page(page)
    return writer.addPage(page)


def _extract_page_text(page):
    if hasattr(page, "extract_text"):
        return page.extract_text() or ""
    return page.extractText() or ""


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
        self.readers = [_PdfReader(fp) for fp in filepaths]

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
        writer = _PdfWriter()
        for reader in self.readers:
            for page in reader.pages:
                _add_page(writer, page)

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
            text = "".join(_extract_page_text(page) for page in reader.pages)
            pdf_texts.append(text)
        return pdf_texts