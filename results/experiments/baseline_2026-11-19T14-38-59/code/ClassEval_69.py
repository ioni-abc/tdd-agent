import PyPDF2


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
        self.readers = []
        for fp in filepaths:
            f = open(fp, "rb")
            if hasattr(PyPDF2, "PdfFileReader"):
                self.readers.append(PyPDF2.PdfFileReader(f))
            else:
                self.readers.append(PyPDF2.PdfReader(f))

    @staticmethod
    def _num_pages(reader):
        if hasattr(reader, "getNumPages"):
            return reader.getNumPages()
        return len(reader.pages)

    @staticmethod
    def _get_page(reader, index):
        if hasattr(reader, "getPage"):
            return reader.getPage(index)
        return reader.pages[index]

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
        if hasattr(PyPDF2, "PdfFileWriter"):
            writer = PyPDF2.PdfFileWriter()
        else:
            writer = PyPDF2.PdfWriter()

        for reader in self.readers:
            for i in range(self._num_pages(reader)):
                page = self._get_page(reader, i)
                if hasattr(writer, "addPage"):
                    writer.addPage(page)
                else:
                    writer.add_page(page)

        with open(output_filepath, "wb") as out:
            writer.write(out)

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
            texts = []
            for i in range(self._num_pages(reader)):
                page = self._get_page(reader, i)
                if hasattr(page, "extractText"):
                    texts.append(page.extractText() or "")
                else:
                    texts.append(page.extract_text() or "")
            pdf_texts.append("".join(texts))
        return pdf_texts