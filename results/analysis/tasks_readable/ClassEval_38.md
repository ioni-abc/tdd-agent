# ClassEval_38

## Skeleton (what the agent sees)

```python
import openpyxl


class ExcelProcessor:
    """
    This is a class for processing excel files, including readring and writing excel data, as well as processing specific operations and saving as a new excel file.
    """

    def __init__(self):
        pass

    def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name:str, Excel file name to read
        :return:list of data, Data in Excel
        """


    def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 0 or 1, 1 represents successful writing, 0 represents failed writing
        >>> processor = ExcelProcessor()
        >>> new_data = [
        >>>     ('Name', 'Age', 'Country'),
        >>>     ('John', 25, 'USA'),
        >>>     ('Alice', 30, 'Canada'),
        >>>     ('Bob', 35, 'Australia'),
        >>>     ('Julia', 28, 'Germany')
        >>> ]
        >>> data = processor.write_excel(new_data, 'test_data.xlsx')
        """


    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
```

## Method `read_excel`

### Docstring

```python
def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name:str, Excel file name to read
        :return:list of data, Data in Excel
        """
```

### Reference code (`solution_code`)

```python
def read_excel(self, file_name):
        data = []
        try:
            workbook = openpyxl.load_workbook(file_name)
            sheet = workbook.active
            for row in sheet.iter_rows(values_only=True):
                data.append(row)
            workbook.close()
            return data
        except:
            return None
```

### Tests (`ExcelProcessorTestReadExcel`)

**test_read_excel_1**: `unstated`
- reason: The docstring says only "list of data", so a programmer could reasonably return each row as a list, but the test expects each row as a tuple, as openpyxl's `values_only` iteration produces.
- missing: The docstring should say the container type of each returned row (for example, tuples of cell values as opposed to lists) and which worksheet's rows are returned, including what happens when reading fails.

```python
def test_read_excel_1(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Age', 'Country'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'Canada'],
            ['Bob', 35, 'Australia']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    data = processor.read_excel(self.test_file_name)
    expected_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA'),
        ('Alice', 30, 'Canada'),
        ('Bob', 35, 'Australia')
    ]
    self.assertEqual(data, expected_data)
```

**test_read_excel_2**: `unstated`
- reason: The docstring says only "list of data", but the test expects each row as a tuple, which a programmer could reasonably replace with a list and fail.
- missing: The docstring should specify the type of each row in the returned list (for example, tuples versus lists) and how cell values are represented.

```python
def test_read_excel_2(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Age'],
            ['John', 25],
            ['Alice', 30],
            ['Bob', 35]]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    data = processor.read_excel(self.test_file_name)
    expected_data = [
        ('Name', 'Age'),
        ('John', 25),
        ('Alice', 30),
        ('Bob', 35)
    ]
    self.assertEqual(data, expected_data)
```

**test_read_excel_3**: `unstated`
- reason: The docstring says only "list of data", but the test expects each row as a tuple of cell values, so a programmer returning lists of lists would fail the equality check.
- missing: The docstring should specify the container type of each returned row (for example, a tuple of cell values per row) and which sheet is read, since a plain "list of data" leaves the row type open.

```python
def test_read_excel_3(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name'],
            ['John'],
            ['Alice'],
            ['Bob']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    data = processor.read_excel(self.test_file_name)
    expected_data = [
        ('Name',),
        ('John',),
        ('Alice',),
        ('Bob',)
    ]
    self.assertEqual(data, expected_data)
```

**test_read_excel_4**: `unstated`
- reason: The docstring says only "list of data", so a programmer could reasonably return each row as a list, while the test expects each row as a tuple.
- missing: The docstring should specify the type of each returned row (for example, tuples of cell values) and which worksheet is read when the workbook has several.

```python
def test_read_excel_4(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Country'],
            ['John', 'USA'],
            ['Alice', 'Canada'],
            ['Bob', 'Australia']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    data = processor.read_excel(self.test_file_name)
    expected_data = [
        ('Name', 'Country'),
        ('John', 'USA'),
        ('Alice', 'Canada'),
        ('Bob', 'Australia')
    ]
    self.assertEqual(data, expected_data)
```

**test_read_excel_5**: `unstated`
- reason: The docstring says only "list of data", so a programmer could reasonably return each row as a list, while the test expects each row as a tuple of cell values, which would fail the equality check.
- missing: The docstring should specify the exact container type for each row (for example, tuples versus lists), which sheet is read, and how empty or missing cells are represented.

```python
def test_read_excel_5(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Country'],
            ['John', 'USA']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    data = processor.read_excel(self.test_file_name)
    expected_data = [
        ('Name', 'Country'),
        ('John', 'USA')
    ]
    self.assertEqual(data, expected_data)
```

**test_read_excel_6**: `unstated`
- reason: The docstring says the method returns a list of data but says nothing about failure, so a programmer would likely raise an error or return an empty list for an empty file name, while the test expects `None`.
- missing: The docstring should say what the method returns when the file cannot be read (for example an empty file name or a missing or invalid file), and state that the return value is `None` in that case.

```python
def test_read_excel_6(self):
    self.test_file_name = ''
    processor = ExcelProcessor()
    res = processor.read_excel(self.test_file_name)
    self.assertEqual(res, None)
```

## Method `write_excel`

### Docstring

```python
def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 0 or 1, 1 represents successful writing, 0 represents failed writing
        >>> processor = ExcelProcessor()
        >>> new_data = [
        >>>     ('Name', 'Age', 'Country'),
        >>>     ('John', 25, 'USA'),
        >>>     ('Alice', 30, 'Canada'),
        >>>     ('Bob', 35, 'Australia'),
        >>>     ('Julia', 28, 'Germany')
        >>> ]
        >>> data = processor.write_excel(new_data, 'test_data.xlsx')
        """
```

### Reference code (`solution_code`)

```python
def write_excel(self, data, file_name):
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            for row in data:
                sheet.append(row)
            workbook.save(file_name)
            workbook.close()
            return 1
        except:
            return 0
```

### Tests (`ExcelProcessorTestWriteExcel`)

**test_write_excel_1**: `stated`
- reason: The docstring says the method writes the given rows to the named file and returns 1 on success, which is what the test checks: the return value, the file's existence, and a read-back that matches the input rows.

```python
def test_write_excel_1(self):
    processor = ExcelProcessor()
    new_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA'),
        ('Alice', 30, 'Canada'),
        ('Bob', 35, 'Australia'),
        ('Julia', 28, 'Germany')
    ]
    save_file_name = 'test_output.xlsx'
    success = processor.write_excel(new_data, save_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.exists(save_file_name))
    saved_data = processor.read_excel(save_file_name)
    self.assertEqual(saved_data, new_data)
    os.remove(save_file_name)
```

**test_write_excel_2**: `stated`
- reason: The docstring says the method writes the data to the named Excel file and returns 1 on success, which is what the test checks through its truthy return, file existence, and read-back comparison.

```python
def test_write_excel_2(self):
    processor = ExcelProcessor()
    new_data = [
        ('Name', 'Age'),
        ('John', 25),
        ('Alice', 30),
        ('Bob', 35),
        ('Julia', 28)
    ]
    save_file_name = 'test_output.xlsx'
    success = processor.write_excel(new_data, save_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.exists(save_file_name))
    saved_data = processor.read_excel(save_file_name)
    self.assertEqual(saved_data, new_data)
    os.remove(save_file_name)
```

**test_write_excel_3**: `stated`
- reason: The docstring says write_excel writes the data to the named file and returns 1 on success, which is what the test checks through its truthy result, the file's existence, and the round-trip read.

```python
def test_write_excel_3(self):
    processor = ExcelProcessor()
    new_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA'),
        ('Alice', 30, 'Canada'),
        ('Bob', 35, 'Australia')
    ]
    save_file_name = 'test_output.xlsx'
    success = processor.write_excel(new_data, save_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.exists(save_file_name))
    saved_data = processor.read_excel(save_file_name)
    self.assertEqual(saved_data, new_data)
    os.remove(save_file_name)
```

**test_write_excel_4**: `stated`
- reason: The docstring says the method writes the given data to the named Excel file and returns 1 on success, which is the behaviour this test checks, and its example shows a list of row tuples written out, so a programmer following it would pass.

```python
def test_write_excel_4(self):
    processor = ExcelProcessor()
    new_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA'),
        ('Alice', 30, 'Canada')
    ]
    save_file_name = 'test_output.xlsx'
    success = processor.write_excel(new_data, save_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.exists(save_file_name))
    saved_data = processor.read_excel(save_file_name)
    self.assertEqual(saved_data, new_data)
    os.remove(save_file_name)
```

**test_write_excel_5**: `stated`
- reason: The docstring says the method writes the given data to the named Excel file and returns 1 on success, which is what the test's success, file-existence, and round-trip checks rely on.

```python
def test_write_excel_5(self):
    processor = ExcelProcessor()
    new_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA')
    ]
    save_file_name = 'test_output.xlsx'
    success = processor.write_excel(new_data, save_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.exists(save_file_name))
    saved_data = processor.read_excel(save_file_name)
    self.assertEqual(saved_data, new_data)
    os.remove(save_file_name)
```

**test_write_excel_6**: `stated`
- reason: The docstring says 0 means failed writing, and writing to an empty file name is a failure a programmer would naturally catch and report as 0, so a faithful implementation passes this test.

```python
def test_write_excel_6(self):
    processor = ExcelProcessor()
    new_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA')
    ]
    save_file_name = ''
    success = processor.write_excel(new_data, save_file_name)
    self.assertEqual(success, 0)
```

## Method `process_excel_data`

### Docstring

```python
def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
```

### Reference code (`solution_code`)

```python
def process_excel_data(self, N, save_file_name):
        data = self.read_excel(save_file_name)
        if data is None or N >= len(data[0]):
            return 0
        new_data = []
        for row in data:
            new_row = list(row[:])
            if not str(row[N]).isdigit():
                new_row.append(str(row[N]).upper())
            else:
                new_row.append(row[N])
            new_data.append(new_row)
        new_file_name = save_file_name.split('.')[0] + '_process.xlsx'
        success = self.write_excel(new_data, new_file_name)
        return success, new_file_name
```

### Tests (`ExcelProcessorTestProcessExcelData`)

**test_process_excel_data_1**: `unstated`
- reason: The docstring says to change the column to uppercase in place, but the test expects a new uppercased column appended at the end of each row, including the header, with numeric cells kept as they are.
- missing: The docstring should state that the processed column is written as a new last column in every row (header included), that its text values are uppercased, and that values whose string form is all digits are copied unchanged.

```python
def test_process_excel_data_1(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Age', 'Country'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'Canada'],
            ['Bob', 35, 'Australia']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    N = 1
    success, output_file = processor.process_excel_data(N, self.test_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.isfile(output_file))
    processed_data = processor.read_excel(output_file)
    expected_processed_data = [
        ('Name', 'Age', 'Country', 'AGE'),
        ('John', 25, 'USA', 25),
        ('Alice', 30, 'Canada', 30),
        ('Bob', 35, 'Australia', 35)
    ]
    self.assertEqual(processed_data, expected_processed_data)
    os.remove(output_file)
```

**test_process_excel_data_2**: `unstated`
- reason: The docstring says to "change the specified column" in place, but the test expects the original columns kept and an uppercased copy appended as a new column in a newly named output file, which a programmer following the docstring would not produce.
- missing: The docstring should state that the method writes a new file containing all original columns plus an appended column holding the uppercased text of the chosen column (with purely numeric values copied unchanged), and that the output name is the input name without its extension plus a "_process.xlsx" suffix.

```python
def test_process_excel_data_2(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Age', 'Country'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'Canada'],
            ['Bob', 35, 'Australia']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    N = 0
    success, output_file = processor.process_excel_data(N, self.test_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.isfile(output_file))
    processed_data = processor.read_excel(output_file)
    expected_processed_data = [
        ('Name', 'Age', 'Country', 'NAME'),
        ('John', 25, 'USA', 'JOHN'),
        ('Alice', 30, 'Canada', 'ALICE'),
        ('Bob', 35, 'Australia', 'BOB')
    ]
    self.assertEqual(processed_data, expected_processed_data)
    os.remove(output_file)
```

**test_process_excel_data_3**: `unstated`
- reason: The docstring says the column is "changed" to uppercase, but the test expects the uppercased values (including the header) to be appended as a new last column while the original column is kept, and a programmer reading "change the column" would plausibly overwrite it in place and fail.
- missing: The docstring should state that each row gets a new column appended at the end holding the uppercased value of the chosen column (header included, numeric-looking values copied unchanged), that the original columns are kept, and that the output is saved under the input name with a `_process.xlsx` suffix.

```python
def test_process_excel_data_3(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Age', 'Country'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'Canada'],
            ['Bob', 35, 'Australia']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    N = 2
    success, output_file = processor.process_excel_data(N, self.test_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.isfile(output_file))
    processed_data = processor.read_excel(output_file)
    expected_processed_data = [
        ('Name', 'Age', 'Country', 'COUNTRY'),
        ('John', 25, 'USA', 'USA'),
        ('Alice', 30, 'Canada', 'CANADA'),
        ('Bob', 35, 'Australia', 'AUSTRALIA')
    ]
    self.assertEqual(processed_data, expected_processed_data)
    os.remove(output_file)
```

**test_process_excel_data_4**: `unstated`
- reason: The docstring says the column is "changed to uppercase" but does not say the result is appended as a new last column with the original kept, which is what the test expects.
- missing: The docstring should state that the uppercased values are written as a new column added after all existing columns (original columns unchanged), and that the output file name is the input file's base name with "_process.xlsx" appended.

```python
def test_process_excel_data_4(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Age', 'COUNTRY'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'CANADA'],
            ['Bob', 35, 'AUSTRALIA']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    N = 2
    success, output_file = processor.process_excel_data(N, self.test_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.isfile(output_file))
    processed_data = processor.read_excel(output_file)
    expected_processed_data = [
        ('Name', 'Age', 'COUNTRY', 'COUNTRY'),
        ('John', 25, 'USA', 'USA'),
        ('Alice', 30, 'CANADA', 'CANADA'),
        ('Bob', 35, 'AUSTRALIA', 'AUSTRALIA')
    ]
    self.assertEqual(processed_data, expected_processed_data)
    os.remove(output_file)
```

**test_process_excel_data_5**: `unstated`
- reason: The docstring says to change the specified column to uppercase, so a programmer would likely overwrite that column in place, but the test expects the original data kept and a new uppercase column appended at the end, with numeric-looking values copied unchanged.
- missing: The docstring should state that the output keeps all original columns, appends a new last column containing the uppercase text of the chosen column, and copies values that look like digits over unchanged rather than uppercasing them.

```python
def test_process_excel_data_5(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'AGE', 'COUNTRY'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'CANADA'],
            ['Bob', 35, 'AUSTRALIA']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    N = 1
    success, output_file = processor.process_excel_data(N, self.test_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.isfile(output_file))
    processed_data = processor.read_excel(output_file)
    expected_processed_data = [
        ('Name', 'AGE', 'COUNTRY', 'AGE'),
        ('John', 25, 'USA', 25),
        ('Alice', 30, 'CANADA', 30),
        ('Bob', 35, 'AUSTRALIA', 35)
    ]
    self.assertEqual(processed_data, expected_processed_data)
    os.remove(output_file)
```

**test_process_excel_data_6**: `contradicts`
- reason: The docstring says the method returns an (int, str) tuple, but the test expects a bare `0` when the column index is out of range, which the reference code returns.

```python
def test_process_excel_data_6(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'AGE', 'COUNTRY'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'CANADA'],
            ['Bob', 35, 'AUSTRALIA']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    res = processor.process_excel_data(100, self.test_file_name)
    self.assertEqual(res, 0)
```

## Tests in no method's test class

### `ExcelProcessorTest`

**test_ExcelProcessor**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_ExcelProcessor(self):
    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Age', 'Country'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'Canada'],
            ['Bob', 35, 'Australia']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    data = processor.read_excel(self.test_file_name)
    expected_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA'),
        ('Alice', 30, 'Canada'),
        ('Bob', 35, 'Australia')
    ]
    self.assertEqual(data, expected_data)

    processor = ExcelProcessor()
    new_data = [
        ('Name', 'Age', 'Country'),
        ('John', 25, 'USA'),
        ('Alice', 30, 'Canada'),
        ('Bob', 35, 'Australia'),
        ('Julia', 28, 'Germany')
    ]
    save_file_name = 'test_output.xlsx'
    success = processor.write_excel(new_data, save_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.exists(save_file_name))
    saved_data = processor.read_excel(save_file_name)
    self.assertEqual(saved_data, new_data)
    os.remove(save_file_name)

    self.test_file_name = 'test_data.xlsx'
    data = [['Name', 'Age', 'Country'],
            ['John', 25, 'USA'],
            ['Alice', 30, 'Canada'],
            ['Bob', 35, 'Australia']]
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(self.test_file_name)
    workbook.close()

    processor = ExcelProcessor()
    N = 1
    success, output_file = processor.process_excel_data(N, self.test_file_name)
    self.assertTrue(success)
    self.assertTrue(os.path.isfile(output_file))
    processed_data = processor.read_excel(output_file)
    expected_processed_data = [
        ('Name', 'Age', 'Country', 'AGE'),
        ('John', 25, 'USA', 25),
        ('Alice', 30, 'Canada', 30),
        ('Bob', 35, 'Australia', 35)
    ]
    self.assertEqual(processed_data, expected_processed_data)
    os.remove(output_file)
```
