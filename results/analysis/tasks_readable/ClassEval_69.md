# ClassEval_69

## Skeleton (what the agent sees)

```python
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
        self.readers = [PyPDF2.PdfFileReader(fp) for fp in filepaths]

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

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
```

## Method `merge_pdfs`

### Docstring

```python
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
```

### Reference code (`solution_code`)

```python
def merge_pdfs(self, output_filepath):
        pdf_writer = PyPDF2.PdfWriter()

        for reader in self.readers:
            # reader.getNumPages is deprecated and was removed in PyPDF2 3.0.0. Use len(reader.pages) instead.
            for page_num in range(len(reader.pages)):
                # reader.getPage(pageNumber) is deprecated and was removed in PyPDF2 3.0.0. Use reader.pages[page_number] instead.
                page = reader.pages[page_num]
                # addPage is deprecated and was removed in PyPDF2 3.0.0. Use add_page instead.
                pdf_writer.add_page(page)

        with open(output_filepath, 'wb') as out:
            pdf_writer.write(out)
        return f"Merged PDFs saved at {output_filepath}"
```

### Tests (`TestPDFHandler`)

## Method `extract_text_from_pdfs`

### Docstring

```python
def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
```

### Reference code (`solution_code`)

```python
def extract_text_from_pdfs(self):
        pdf_texts = []
        for reader in self.readers:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                pdf_texts.append(page.extract_text())
        return pdf_texts
```

### Tests (`PDFHandlerTestMergePdfs`)

setUp (runs before each test):

```python
def setUp(self) -> None:
    TestPDFHandler.setUpClass()
```

**test_merge_pdfs**: `other_inconsistency`
- reason: The test exercises `merge_pdfs` and checks its return message and the created file, but it is filed under `extract_text_from_pdfs`, whose docstring describes returning a list of extracted page texts.

```python
def test_merge_pdfs(self):
    TestPDFHandler.setUpClass()
    handler = PDFHandler(TestPDFHandler.test_files)
    result = handler.merge_pdfs("merged.pdf")
    self.assertEqual("Merged PDFs saved at merged.pdf", result)
    self.assertTrue(os.path.exists("merged.pdf"))
```

## Tests in no method's test class

### `PDFHandlerTestExtractTextFromPdfs`

setUp (runs before each test):

```python
def setUp(self) -> None:
    TestPDFHandler.setUpClass()
```

**test_extract_text_from_pdfs**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_extract_text_from_pdfs(self):
    TestPDFHandler.setUpClass()
    handler = PDFHandler(TestPDFHandler.test_files)
    result = handler.extract_text_from_pdfs()
    self.assertEqual(result, ["This is a test1.\n", "This is a test2.\n"])
```

### `PDFHandlerTestMain`

setUp (runs before each test):

```python
def setUp(self) -> None:
    TestPDFHandler.setUpClass()
```

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    TestPDFHandler.setUpClass()
    handler = PDFHandler(TestPDFHandler.test_files)
    result = handler.merge_pdfs("merged.pdf")
    self.assertEqual("Merged PDFs saved at merged.pdf", result)
    self.assertTrue(os.path.exists("merged.pdf"))

    result = handler.extract_text_from_pdfs()
    self.assertEqual(result, ["This is a test1.\n", "This is a test2.\n"])
```
