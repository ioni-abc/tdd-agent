# ClassEval_26

## Skeleton (what the agent sees)

```python
import csv

class CSVProcessor:
    """
    This is a class for processing CSV files, including readring and writing CSV data, as well as processing specific operations and saving as a new CSV file.
    """


    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        >>> csvProcessor.process_csv_data(0, 'read_test.csv')
        1
        >>> csvProcessor.read_csv('read_test_process.csv')
        (['a', 'b', 'c', 'd'], [['HELLO']])
        """
```

## Method `read_csv`

### Docstring

```python
def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
```

### Reference code (`solution_code`)

```python
def read_csv(self, file_name):
        data = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            title = next(reader)
            for row in reader:
                data.append(row)
        return title, data
```

### Tests (`CSVProcessorTestReadCSV`)

**test_read_csv_1**: `stated`
- reason: The docstring says the first row is returned as the title and the remaining rows as data, which is exactly what the test checks for a simple header-plus-one-row file.

```python
def test_read_csv_1(self):
    self.file = 'read_test.csv'

    with open(self.file, 'w') as f:
        f.write('a,b,c,d\nhElLo,YoU,ME,LoW')

    expected_title = ['a', 'b', 'c', 'd']
    expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
    csvProcessor = CSVProcessor()
    title, data = csvProcessor.read_csv(self.file)
    self.assertEqual(expected_data, data)
    self.assertEqual(expected_title, title)
```

**test_read_csv_2**: `stated`
- reason: The docstring says the first row is the title and the rest is data, which is exactly what the test checks: a one-line header `1234` becomes the title and the following row becomes the data.

```python
def test_read_csv_2(self):
    self.file = 'read_test.csv'
    with open(self.file, 'w') as f:
        f.write('1234\nhElLo,YoU,ME,LoW')

    expected_title = ['1234']
    expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
    csvProcessor = CSVProcessor()
    title, data = csvProcessor.read_csv(self.file)
    self.assertEqual(expected_data, data)
    self.assertEqual(expected_title, title)
```

**test_read_csv_3**: `stated`
- reason: The docstring says the first row is the title and the remaining rows are data, which is exactly what this test checks for a file with a one-column title row followed by one data row.

```python
def test_read_csv_3(self):
    self.file = 'read_test.csv'

    with open(self.file, 'w') as f:
        f.write('title\nhElLo,YoU,ME,LoW')

    expected_title = ['title']
    expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
    csvProcessor = CSVProcessor()
    title, data = csvProcessor.read_csv(self.file)
    self.assertEqual(expected_data, data)
    self.assertEqual(expected_title, title)
```

**test_read_csv_4**: `stated`
- reason: The docstring says the first row is the title and the remaining rows are data, which is exactly what this test checks: a one-column title row followed by one data row.

```python
def test_read_csv_4(self):
    self.file = 'read_test.csv'

    with open(self.file, 'w') as f:
        f.write('title4\nhElLo,YoU,ME,LoW')

    expected_title = ['title4']
    expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
    csvProcessor = CSVProcessor()
    title, data = csvProcessor.read_csv(self.file)
    self.assertEqual(expected_data, data)
    self.assertEqual(expected_title, title)
```

**test_read_csv_5**: `stated`
- reason: The docstring says the first row is the title and the rest is data, which is exactly what the test checks: a one-cell title row followed by one data row.

```python
def test_read_csv_5(self):
    self.file = 'read_test.csv'

    with open(self.file, 'w') as f:
        f.write('title5\nhElLo,YoU,ME,LoW')

    expected_title = ['title5']
    expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
    csvProcessor = CSVProcessor()
    title, data = csvProcessor.read_csv(self.file)
    self.assertEqual(expected_data, data)
    self.assertEqual(expected_title, title)
```

## Method `write_csv`

### Docstring

```python
def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
```

### Reference code (`solution_code`)

```python
def write_csv(self, data, file_name):
        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 1
        except:
            return 0
```

### Tests (`CSVProcessorTestWriteCSV`)

**test_write_csv_1**: `stated`
- reason: The docstring says write_csv writes data to a csv file and returns 1 on success, which is what the test checks, and the read-back only confirms the rows were written as given.

```python
def test_write_csv_1(self):
    self.file = 'read_test.csv'

    file_path = self.file
    csvProcessor = CSVProcessor()
    data = [['a', 'b', 'c', 'd'], ['1', '2', '3', '4']]
    # assert return value
    self.assertEqual(1, csvProcessor.write_csv(data, file_path))

    # read to test if write correctly
    read_title, read_data = csvProcessor.read_csv(file_path)
    self.assertEqual(read_title, data[0])
    self.assertEqual(read_data[0], data[1])
    os.remove(file_path)
```

**test_write_csv_2**: `stated`
- reason: The docstring says write_csv writes data into a csv file and returns 1 on success, which is what the test checks: a successful write returns 1 and the rows can be read back in order.

```python
def test_write_csv_2(self):
    self.file = 'read_test.csv'

    file_path = self.file
    csvProcessor = CSVProcessor()
    data = [['aa', 'bb', 'cc', 'dd'], ['1', '2', '3', '4']]
    # assert return value
    self.assertEqual(1, csvProcessor.write_csv(data, file_path))

    # read to test if write correctly
    read_title, read_data = csvProcessor.read_csv(file_path)
    self.assertEqual(read_title, data[0])
    self.assertEqual(read_data[0], data[1])
    os.remove(file_path)
```

**test_write_csv_3**: `stated`
- reason: The docstring says the method writes the data to a CSV file and returns 1 on success, which is what the test checks, and writing rows with a standard CSV writer lets the test's read-back of the header and first row pass.

```python
def test_write_csv_3(self):
    self.file = 'read_test.csv'

    file_path = self.file
    csvProcessor = CSVProcessor()
    data = [['a', 'b', 'c', 'd'], ['11', '22', '33', '44']]
    # assert return value
    self.assertEqual(1, csvProcessor.write_csv(data, file_path))

    # read to test if write correctly
    read_title, read_data = csvProcessor.read_csv(file_path)
    self.assertEqual(read_title, data[0])
    self.assertEqual(read_data[0], data[1])
    os.remove(file_path)
```

**test_write_csv_4**: `stated`
- reason: The docstring says the method writes the data into a CSV file and returns 1 on success, which is the return value the test asserts, and the read-back check relies only on standard CSV writing that a programmer would naturally implement.

```python
def test_write_csv_4(self):
    self.file = 'read_test.csv'

    file_path = self.file
    csvProcessor = CSVProcessor()
    data = [['e', 'f', 'g', 'h'], ['1', '2', '3', '4']]
    # assert return value
    self.assertEqual(1, csvProcessor.write_csv(data, file_path))

    # read to test if write correctly
    read_title, read_data = csvProcessor.read_csv(file_path)
    self.assertEqual(read_title, data[0])
    self.assertEqual(read_data[0], data[1])
    os.remove(file_path)
```

**test_write_csv_5**: `stated`
- reason: The docstring says write_csv writes the data into a CSV file and returns 1 on success, which is what the test checks: the return value is 1 and the file reads back with the same rows.

```python
def test_write_csv_5(self):
    self.file = 'read_test.csv'

    file_path = self.file
    csvProcessor = CSVProcessor()
    data = [['a', 'b', 'c', 'd'], ['5', '6', '7', '8']]
    # assert return value
    self.assertEqual(1, csvProcessor.write_csv(data, file_path))

    # read to test if write correctly
    read_title, read_data = csvProcessor.read_csv(file_path)
    self.assertEqual(read_title, data[0])
    self.assertEqual(read_data[0], data[1])
    os.remove(file_path)
```

**test_write_csv_6**: `stated`
- reason: The docstring says write_csv returns 0 whenever the write does not succeed, and opening a file with an empty name fails, so a programmer following it would return 0 as the test expects.

```python
def test_write_csv_6(self):
    self.file = ''
    file_path = self.file
    csvProcessor = CSVProcessor()
    # assert return value
    self.assertEqual(0, csvProcessor.write_csv([], file_path))
```

## Method `process_csv_data`

### Docstring

```python
def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        >>> csvProcessor.process_csv_data(0, 'read_test.csv')
        1
        >>> csvProcessor.read_csv('read_test_process.csv')
        (['a', 'b', 'c', 'd'], [['HELLO']])
        """
```

### Reference code (`solution_code`)

```python
def process_csv_data(self, N, save_file_name):
        title, data = self.read_csv(save_file_name)
        column_data = [row[N] for row in data]
        column_data = [row.upper() for row in column_data]
        new_data = [title, column_data]
        return self.write_csv(new_data, save_file_name.split('.')[0] + '_process.csv')
```

### Tests (`CSVProcessorTestProcessCSVData`)

setUp (runs before each test):

```python
def setUp(self) -> None:
    self.file = 'read_test.csv'
    self.file_process = 'read_test_process.csv'
    with open(self.file, 'w') as f:
        f.write('a,b,c,d\nhElLo,YoU,ME,LoW,aBc')
```

**test_process_csv_data_1**: `stated`
- reason: The docstring's own example shows the same behaviour the test checks: column 0 is kept, uppercased to 'HELLO', written with the title, and saved as the '_process' file, returning 1.

```python
def test_process_csv_data_1(self):
    title = ['a', 'b', 'c', 'd']
    data = ['HELLO']
    csvProcessor = CSVProcessor()
    self.assertEqual(1, csvProcessor.process_csv_data(0, self.file))

    read_title, read_data = csvProcessor.read_csv(self.file_process)
    self.assertEqual(read_title, title)
    self.assertEqual(read_data[0], data)
```

**test_process_csv_data_2**: `stated`
- reason: The docstring says to keep only the N-th column, uppercase it, and write the title plus the new data to a file with a `_process` suffix, and the docstring example shows the full uppercase result, so a programmer following it would produce the `['YOU']` row this test expects.

```python
def test_process_csv_data_2(self):
    title = ['a', 'b', 'c', 'd']
    data = ['YOU']
    csvProcessor = CSVProcessor()
    self.assertEqual(1, csvProcessor.process_csv_data(1, self.file))

    read_title, read_data = csvProcessor.read_csv(self.file_process)
    self.assertEqual(read_title, title)
    self.assertEqual(read_data[0], data)
```

**test_process_csv_data_3**: `stated`
- reason: The docstring says to keep the Nth column, capitalize it, and save it to a `_process` file returning 1, and its example shows `hElLo` becoming `HELLO`, which matches the test's expected uppercase `ME` for column 2.

```python
def test_process_csv_data_3(self):
    title = ['a', 'b', 'c', 'd']
    data = ['ME']
    csvProcessor = CSVProcessor()
    self.assertEqual(1, csvProcessor.process_csv_data(2, self.file))

    read_title, read_data = csvProcessor.read_csv(self.file_process)
    self.assertEqual(read_title, title)
    self.assertEqual(read_data[0], data)
```

**test_process_csv_data_4**: `stated`
- reason: The docstring's doctest shows that mixed-case input like 'hElLo' becomes 'HELLO', so a programmer would uppercase the selected column's values, which yields 'LOW' for the test's 'LoW' at column 3.

```python
def test_process_csv_data_4(self):
    title = ['a', 'b', 'c', 'd']
    data = ['LOW']
    csvProcessor = CSVProcessor()
    self.assertEqual(1, csvProcessor.process_csv_data(3, self.file))

    read_title, read_data = csvProcessor.read_csv(self.file_process)
    self.assertEqual(read_title, title)
    self.assertEqual(read_data[0], data)
```

**test_process_csv_data_5**: `stated`
- reason: The docstring says to keep only the Nth column of each data row, capitalize it, and write the original title with the new data to a `_process` file, which yields the title `['a','b','c','d']` and the single value `'ABC'` the test expects.

```python
def test_process_csv_data_5(self):
    title = ['a', 'b', 'c', 'd']
    data = ['ABC']
    csvProcessor = CSVProcessor()
    self.assertEqual(1, csvProcessor.process_csv_data(4, self.file))

    read_title, read_data = csvProcessor.read_csv(self.file_process)
    self.assertEqual(read_title, title)
    self.assertEqual(read_data[0], data)
```

## Tests in no method's test class

### `CSVProcessorTestMain`

setUp (runs before each test):

```python
def setUp(self) -> None:
    self.file = 'test.csv'
    self.file_process = 'test_process.csv'
    with open(self.file, 'w') as f:
        f.write('a,b,c,d\nhElLo,YoU,ME,LoW')
```

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    csvProcessor = CSVProcessor()
    data = [['a', 'b', 'c', 'd'], ['hElLo', 'YoU', 'ME', 'LoW']]
    # assert return value
    self.assertEqual(1, csvProcessor.write_csv(data, self.file))
    expected_title = ['a', 'b', 'c', 'd']
    expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
    title, data = csvProcessor.read_csv(self.file)
    self.assertEqual(expected_data, data)
    self.assertEqual(expected_title, title)

    title = ['a', 'b', 'c', 'd']
    data = ['HELLO']
    self.assertEqual(1, csvProcessor.process_csv_data(0, self.file))

    read_title, read_data = csvProcessor.read_csv(self.file_process)
    self.assertEqual(read_title, title)
    self.assertEqual(read_data[0], data)
```
