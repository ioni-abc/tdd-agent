# ClassEval_34

## Skeleton (what the agent sees)

```python
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


class DocFileHandler:
    """
    This is a class that handles Word documents and provides functionalities for reading, writing, and modifying the content of Word documents.
    """

    def __init__(self, file_path):
        """
        Initializes the DocFileHandler object with the specified file path.
        :param file_path: str, the path to the Word document file.
        """
        self.file_path = file_path

    def read_text(self):
        """
        Reads the content of a Word document and returns it as a string.
        :return: str, the content of the Word document.
        """

    def write_text(self, content, font_size=12, alignment='left'):
        """
        Writes the specified content to a Word document.
        :param content: str, the text content to write.
        :param font_size: int, optional, the font size of the text (default is 12).
        :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
        :return: bool, True if the write operation is successful, False otherwise.
        """

    def add_heading(self, heading, level=1):
        """
        Adds a heading to the Word document.
        :param heading: str, the text of the heading.
        :param level: int, optional, the level of the heading (1, 2, 3, etc.; default is 1).
        :return: bool, True if the heading is successfully added, False otherwise.
        """

    def add_table(self, data):
        """
        Adds a table to the Word document with the specified data.
        :param data: list of lists, the data to populate the table.
        :return: bool, True if the table is successfully added, False otherwise.
        """

    def _get_alignment_value(self, alignment):
        """
        Returns the alignment value corresponding to the given alignment string.
        :param alignment: str, the alignment string ('left', 'center', or 'right').
        :return: int, the alignment value.
        """
```

## Method `read_text`

### Docstring

```python
def read_text(self):
        """
        Reads the content of a Word document and returns it as a string.
        :return: str, the content of the Word document.
        """
```

### Reference code (`solution_code`)

```python
def read_text(self):
        doc = Document(self.file_path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        return "\n".join(text)
```

### Tests (`DocFileHandlerTestReadText`)

**test_read_text_1**: `stated`
- reason: The test adds one paragraph and expects its text back, which any reasonable reading of "returns the content as a string" produces, so no separator or format convention is needed.

```python
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
```

**test_read_text_2**: `stated`
- reason: The docstring says read_text returns the Word document's content as a string, and a programmer would extract the paragraph text, which for a single paragraph "111" gives exactly the expected "111".

```python
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
```

**test_read_text_3**: `stated`
- reason: The docstring asks for the document's content as a string, and the test checks that a document with one paragraph of text returns exactly that text, which any reasonable extraction would produce.

```python
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
```

**test_read_text_4**: `stated`
- reason: A programmer reading "returns the content of the Word document as a string" would extract the document's paragraph text, and this single-paragraph test expects exactly that text, so the docstring covers the behaviour being checked.

```python
def test_read_text_4(self):
    self.file_path = "test_example.docx"
    self.handler = DocFileHandler(self.file_path)
    doc = Document()
    doc.add_paragraph("aaa\nbbb")
    doc.save(self.file_path)

    text_content = self.handler.read_text()
    expected_content = "aaa\nbbb"
    self.assertEqual(text_content, expected_content)

    if os.path.exists(self.file_path):
        os.remove(self.file_path)
```

**test_read_text_5**: `stated`
- reason: The docstring says the method returns the document's content as a string, and a programmer who extracts the paragraph text from a single empty paragraph would naturally return an empty string, which is what the test expects.

```python
def test_read_text_5(self):
    self.file_path = "test_example.docx"
    self.handler = DocFileHandler(self.file_path)
    doc = Document()
    doc.add_paragraph("")
    doc.save(self.file_path)

    text_content = self.handler.read_text()
    expected_content = ""
    self.assertEqual(text_content, expected_content)

    if os.path.exists(self.file_path):
        os.remove(self.file_path)
```

## Method `write_text`

### Docstring

```python
def write_text(self, content, font_size=12, alignment='left'):
        """
        Writes the specified content to a Word document.
        :param content: str, the text content to write.
        :param font_size: int, optional, the font size of the text (default is 12).
        :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
        :return: bool, True if the write operation is successful, False otherwise.
        """
```

### Reference code (`solution_code`)

```python
def write_text(self, content, font_size=12, alignment='left'):
        try:
            doc = Document()
            paragraph = doc.add_paragraph()
            run = paragraph.add_run(content)
            font = run.font
            font.size = Pt(font_size)
            alignment_value = self._get_alignment_value(alignment)
            paragraph.alignment = alignment_value
            doc.save(self.file_path)
            return True
        except:
            return False
```

### Tests (`DocFileHandlerTestWriteText`)

setUp (runs before each test):

```python
def setUp(self):
    self.file_path = "test_example.docx"
    self.handler = DocFileHandler(self.file_path)
    doc = Document()
    doc.add_paragraph("Initial content")
    doc.save(self.file_path)
```

**test_write_text_1**: `unstated`
- reason: The test expects `write_text` to replace the file's existing contents, so reading back returns only the new text, but the docstring only says the content is "written to a Word document" and does not say whether that overwrites or appends to existing text.
- missing: The docstring should state that each call replaces the whole document with a new document containing only the given content, discarding any previously existing paragraphs in the file.

```python
def test_write_text_1(self):
    new_content = "New content 1"
    self.handler.write_text(new_content)
    text_content = self.handler.read_text()
    self.assertEqual(text_content, new_content)
```

**test_write_text_2**: `unstated`
- reason: The docstring says content is written to the Word document but not whether that replaces the file's existing content or appends to it, and the test expects the read-back text to equal only the new content even though the file already held "Initial content".
- missing: The docstring should state whether each write replaces the document's existing contents entirely or appends a new paragraph after them, and what read-back returns afterward.

```python
def test_write_text_2(self):
    new_content = "New content 2"
    self.handler.write_text(new_content)
    text_content = self.handler.read_text()
    self.assertEqual(text_content, new_content)
```

**test_write_text_3**: `unstated`
- reason: The docstring says only that content is written to the Word document, so it does not say whether this replaces the existing document text, which the test's read-back equality depends on.
- missing: The docstring should state whether writing replaces all existing text in the file or appends to it, and whether the file is created or overwritten when it already has content.

```python
def test_write_text_3(self):
    new_content = "New content 3"
    self.handler.write_text(new_content)
    text_content = self.handler.read_text()
    self.assertEqual(text_content, new_content)
```

**test_write_text_4**: `unstated`
- reason: The test expects the write to replace the document's existing "Initial content" so that reading it back returns only the new text, but the docstring only says content is written to the document and never says whether existing text is overwritten or appended to.
- missing: The docstring should state whether writing replaces any text already in the document or appends after it, and what the document contains afterward.

```python
def test_write_text_4(self):
    new_content = "New content 4"
    self.handler.write_text(new_content)
    text_content = self.handler.read_text()
    self.assertEqual(text_content, new_content)
```

**test_write_text_5**: `stated`
- reason: The docstring says write_text writes the given content string to the Word document, so a programmer would write an empty string and read back an empty result, which is what the test asserts.

```python
def test_write_text_5(self):
    new_content = ""
    self.handler.write_text(new_content)
    text_content = self.handler.read_text()
    self.assertEqual(text_content, new_content)
```

## Method `add_heading`

### Docstring

```python
def add_heading(self, heading, level=1):
        """
        Adds a heading to the Word document.
        :param heading: str, the text of the heading.
        :param level: int, optional, the level of the heading (1, 2, 3, etc.; default is 1).
        :return: bool, True if the heading is successfully added, False otherwise.
        """
```

### Reference code (`solution_code`)

```python
def add_heading(self, heading, level=1):
        try:
            doc = Document(self.file_path)
            doc.add_heading(heading, level)
            doc.save(self.file_path)
            return True
        except:
            return False
```

### Tests (`DocFileHandlerTestAddHeading`)

setUp (runs before each test):

```python
def setUp(self):
    self.file_path = "test_example.docx"
    self.handler = DocFileHandler(self.file_path)
    doc = Document()
    doc.add_paragraph("Initial content")
    doc.save(self.file_path)
```

**test_add_heading_1**: `stated`
- reason: The docstring says it adds a heading to the Word document with a default level of 1, which is what the test checks: a heading paragraph with the given text, where "heading" in Word means a paragraph in a Heading style.

```python
def test_add_heading_1(self):
    heading = "Test Heading 1"
    self.handler.add_heading(heading)
    doc = Document(self.file_path)
    headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
    self.assertIn(heading, headings)
```

**test_add_heading_2**: `stated`
- reason: The docstring says the method adds a heading at a default level of 1, so a programmer would produce a Word heading paragraph whose style starts with "Heading", which is what the test checks.

```python
def test_add_heading_2(self):
    heading = "Test Heading 2"
    self.handler.add_heading(heading)
    doc = Document(self.file_path)
    headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
    self.assertIn(heading, headings)
```

**test_add_heading_3**: `stated`
- reason: The docstring says add_heading adds a heading with a default level of 1 and returns True on success, so a programmer would produce a Heading-styled paragraph containing the text, which is what the test checks.

```python
def test_add_heading_3(self):
    heading = "Test Heading 3"
    self.handler.add_heading(heading)
    doc = Document(self.file_path)
    headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
    self.assertIn(heading, headings)
```

**test_add_heading_4**: `stated`
- reason: The docstring says the method adds a heading with a default level of 1, so a programmer would call the heading API with that level and the test's check that a paragraph with a Heading-style name contains the text would pass.

```python
def test_add_heading_4(self):
    heading = "Test Heading 4"
    self.handler.add_heading(heading)
    doc = Document(self.file_path)
    headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
    self.assertIn(heading, headings)
```

**test_add_heading_5**: `stated`
- reason: The docstring says the method adds a heading with a default level of 1, so a programmer would call Word's heading function with that level, which produces a paragraph in a "Heading" style that the test checks for.

```python
def test_add_heading_5(self):
    heading = "Test Heading 5"
    self.handler.add_heading(heading)
    doc = Document(self.file_path)
    headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
    self.assertIn(heading, headings)
```

## Method `add_table`

### Docstring

```python
def add_table(self, data):
        """
        Adds a table to the Word document with the specified data.
        :param data: list of lists, the data to populate the table.
        :return: bool, True if the table is successfully added, False otherwise.
        """
```

### Reference code (`solution_code`)

```python
def add_table(self, data):
        try:
            doc = Document(self.file_path)
            table = doc.add_table(rows=len(data), cols=len(data[0]))
            for i, row in enumerate(data):
                for j, cell_value in enumerate(row):
                    table.cell(i, j).text = str(cell_value)
            doc.save(self.file_path)
            return True
        except:
            return False
```

### Tests (`DocFileHandlerTestAddTable`)

setUp (runs before each test):

```python
def setUp(self):
    self.file_path = "test_example.docx"
    self.handler = DocFileHandler(self.file_path)
    doc = Document()
    doc.add_paragraph("Initial content")
    doc.save(self.file_path)
```

**test_add_table_1**: `stated`
- reason: The docstring says the table is populated with the given list of lists, so a programmer would naturally make one row per inner list and one column per cell, which is what the test checks.

```python
def test_add_table_1(self):
    data = [['Name', 'Age']]
    self.handler.add_table(data)
    doc = Document(self.file_path)
    table = doc.tables[0]
    self.assertEqual(len(table.rows), 1)
    self.assertEqual(len(table.columns), 2)
```

**test_add_table_2**: `stated`
- reason: The docstring says the method adds a table populated with the given list of lists, which is exactly what the test checks: a 2x2 table whose cell (1,0) reads 'John'.

```python
def test_add_table_2(self):
    data = [['Name', 'Age'], ['John', '25']]
    self.handler.add_table(data)
    doc = Document(self.file_path)
    table = doc.tables[0]
    self.assertEqual(len(table.rows), 2)
    self.assertEqual(len(table.columns), 2)
    self.assertEqual(table.cell(1, 0).text, 'John')
```

**test_add_table_3**: `stated`
- reason: The docstring says add_table adds a table populated with the given list of lists, so a programmer following it would create a table with those rows and cells in the document, which is what the test checks with string values.

```python
def test_add_table_3(self):
    data = [['Name', 'Age'], ['John', '25'], ['Emma', '30']]
    self.handler.add_table(data)
    doc = Document(self.file_path)
    table = doc.tables[0]
    self.assertEqual(len(table.rows), 3)
    self.assertEqual(len(table.columns), 2)
    self.assertEqual(table.cell(1, 0).text, 'John')
    self.assertEqual(table.cell(2, 1).text, '30')
```

**test_add_table_4**: `stated`
- reason: The docstring says the table is populated with the given list of lists, so a programmer would build a table with one row per inner list and one column per item, then check that the cell text matches the data, which is what this test asserts.

```python
def test_add_table_4(self):
    data = [['Name', 'Age'], ['aaa', '25'], ['Emma', '30']]
    self.handler.add_table(data)
    doc = Document(self.file_path)
    table = doc.tables[0]
    self.assertEqual(len(table.rows), 3)
    self.assertEqual(len(table.columns), 2)
    self.assertEqual(table.cell(1, 0).text, 'aaa')
    self.assertEqual(table.cell(2, 1).text, '30')
```

**test_add_table_5**: `stated`
- reason: The docstring says the method adds a table to the Word document populated with the given list of lists, which is what the test checks: a 3x2 table with the expected cell text, read back from the saved file.

```python
def test_add_table_5(self):
    data = [['Name', 'Age'], ['John', '25'], ['Emma', '90']]
    self.handler.add_table(data)
    doc = Document(self.file_path)
    table = doc.tables[0]
    self.assertEqual(len(table.rows), 3)
    self.assertEqual(len(table.columns), 2)
    self.assertEqual(table.cell(1, 0).text, 'John')
    self.assertEqual(table.cell(2, 1).text, '90')
```

## Method `_get_alignment_value`

### Docstring

```python
def _get_alignment_value(self, alignment):
        """
        Returns the alignment value corresponding to the given alignment string.
        :param alignment: str, the alignment string ('left', 'center', or 'right').
        :return: int, the alignment value.
        """
```

### Reference code (`solution_code`)

```python
def _get_alignment_value(self, alignment):
        alignment_options = {
            'left': WD_PARAGRAPH_ALIGNMENT.LEFT,
            'center': WD_PARAGRAPH_ALIGNMENT.CENTER,
            'right': WD_PARAGRAPH_ALIGNMENT.RIGHT
        }
        return alignment_options.get(alignment.lower(), WD_PARAGRAPH_ALIGNMENT.LEFT)
```

### Tests (`DocFileHandlerTest`)

**test_DocFileHandler**: `other_inconsistency`
- reason: Test-method mismatch: the test is `test_DocFileHandler`, which exercises read_text, write_text, add_heading and add_table, and never calls `_get_alignment_value`.

```python
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
```
