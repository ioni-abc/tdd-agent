# ClassEval_28

## Skeleton (what the agent sees)

```python
import sqlite3
import pandas as pd

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """


    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name


    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        >>> db.create_table('user', 'name', 'age')
        """


    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        >>> db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        """


    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """


    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
```

## Method `create_table`

### Docstring

```python
def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        >>> db.create_table('user', 'name', 'age')
        """
```

### Reference code (`solution_code`)

```python
def create_table(self, table_name, key1, key2):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {key1} TEXT, {key2} INTEGER)"
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
```

### Tests (`DatabaseProcessorTestCreateTable`)

setUp (runs before each test):

```python
def setUp(self):
    self.database_name = "test.db"
    self.processor = DatabaseProcessor(self.database_name)
```

**test_create_table_1**: `stated`
- reason: The docstring says the method creates a new table named by `table_name` if it doesn't exist, which is exactly what the test checks by querying sqlite_master for that table name.

```python
def test_create_table_1(self):
    table_name = "test_table"
    self.processor.create_table(table_name, 'name', 'age')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    conn.close()

    self.assertIsNotNone(result)
    self.assertEqual(result[0], table_name)
```

**test_create_table_2**: `stated`
- reason: The docstring says the method creates a table named `table_name` if it doesn't exist, which is exactly what the test checks by querying `sqlite_master` for that name.

```python
def test_create_table_2(self):
    table_name = "test_table2"
    self.processor.create_table(table_name, 'name', 'age')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    conn.close()

    self.assertIsNotNone(result)
    self.assertEqual(result[0], table_name)
```

**test_create_table_3**: `stated`
- reason: The docstring says the method creates the table in the database, and the test only checks that a table with the given name exists afterward, which a programmer following the docstring would satisfy.

```python
def test_create_table_3(self):
    table_name = "test_table3"
    self.processor.create_table(table_name, 'name', 'age')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    conn.close()

    self.assertIsNotNone(result)
    self.assertEqual(result[0], table_name)
```

**test_create_table_4**: `stated`
- reason: The docstring says the method creates a table with the given name if it doesn't exist, which is exactly what the test checks by querying sqlite_master for that table name.

```python
def test_create_table_4(self):
    table_name = "test_table4"
    self.processor.create_table(table_name, 'name', 'age')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    conn.close()

    self.assertIsNotNone(result)
    self.assertEqual(result[0], table_name)
```

**test_create_table_5**: `stated`
- reason: The docstring says create_table creates the named table in the database if it doesn't exist, which is exactly what the test checks by querying sqlite_master for the table name.

```python
def test_create_table_5(self):
    table_name = "test_table5"
    self.processor.create_table(table_name, 'name', 'age')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    conn.close()

    self.assertIsNotNone(result)
    self.assertEqual(result[0], table_name)
```

## Method `insert_into_database`

### Docstring

```python
def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        >>> db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        """
```

### Reference code (`solution_code`)

```python
def insert_into_database(self, table_name, data):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        for item in data:
            insert_query = f"INSERT INTO {table_name} (name, age) VALUES (?, ?)"
            cursor.execute(insert_query, (item['name'], item['age']))

        conn.commit()
        conn.close()
```

### Tests (`DatabaseProcessorTestInsertIntoDatabase`)

setUp (runs before each test):

```python
def setUp(self):
    self.database_name = "test.db"
    self.processor = DatabaseProcessor(self.database_name)
```

**test_insert_into_database_1**: `unstated`
- reason: A programmer following the docstring would insert each dict's name and age into the table, but the test's assertion on `result[0][2]` depends on the storage layout (an auto-increment id column placed before name and age), which the docstring never mentions.
- missing: The docstring should state the column layout of stored rows, including any generated id column and its position relative to the inserted fields, and which columns each dictionary key maps to.

```python
def test_insert_into_database_1(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), len(data))
    self.assertEqual(result[0][2], 25)
```

**test_insert_into_database_2**: `unstated`
- reason: The docstring never says how the table is laid out, so a correct implementation could store rows differently and fail the check that the inserted age appears at index 2 of each fetched row.
- missing: The docstring should state the stored column layout, including any automatically generated id column and the order in which each dictionary's fields become columns in the table.

```python
def test_insert_into_database_2(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 15},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), len(data))
    self.assertEqual(result[0][2], 15)
```

**test_insert_into_database_3**: `stated`
- reason: The docstring says to insert a list of row dictionaries into the named table, and the example uses the same `name` and `age` fields the test inserts, so a programmer following it would store both rows and pass the row-count and age checks.

```python
def test_insert_into_database_3(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 16},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), len(data))
    self.assertEqual(result[0][2], 16)
```

**test_insert_into_database_4**: `unstated`
- reason: The test checks that the stored age lands in the third column of the fetched row, which depends on the table layout created by `create_table` (an id column ahead of name and age), and the docstring never describes the stored row layout or column order.
- missing: The docstring should state the column layout of the target table, including any auto-generated columns and their position, and that each dict's keys map to the table's named columns, so an implementation can match the expected stored row structure.

```python
def test_insert_into_database_4(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 17},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), len(data))
    self.assertEqual(result[0][2], 17)
```

**test_insert_into_database_5**: `unstated`
- reason: The test expects the stored row's age at index 2, which assumes an implicit id column ahead of name and age from create_table, and the docstring says nothing about the table layout or row ordering.
- missing: The docstring should state the stored row layout, including any automatically generated id column and its position, and that rows are returned in insertion order when read back.

```python
def test_insert_into_database_5(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 18},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), len(data))
    self.assertEqual(result[0][2], 18)
```

## Method `search_database`

### Docstring

```python
def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """
```

### Reference code (`solution_code`)

```python
def search_database(self, table_name, name):

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        select_query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(select_query, (name,))
        result = cursor.fetchall()

        if result:
            return result
        else:
            return None
```

### Tests (`DatabaseProcessorTestSearchDatabase`)

setUp (runs before each test):

```python
def setUp(self):
    self.database_name = "test.db"
    self.processor = DatabaseProcessor(self.database_name)
```

**test_search_database_1**: `stated`
- reason: The docstring says the method returns a list of tuples for rows whose name matches, which is what the test checks: one matching row with the name in the second column.

```python
def test_search_database_1(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    result = self.processor.search_database(table_name, 'John')
    self.assertIsNotNone(result)
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'John')
```

**test_search_database_2**: `stated`
- reason: The docstring says the method returns a list of tuples for rows whose name matches, or None when there are none, and the test checks exactly that for one matching row, with the name in the second column as the docstring example shows.

```python
def test_search_database_2(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    result = self.processor.search_database(table_name, 'Alice')
    self.assertIsNotNone(result)
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'Alice')
```

**test_search_database_3**: `stated`
- reason: The docstring says the method returns None when no rows match the name, and the test searches for a name absent from the table and expects None.

```python
def test_search_database_3(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    result = self.processor.search_database(table_name, 'Bob')
    self.assertIsNone(result)
```

**test_search_database_4**: `stated`
- reason: The docstring says the method returns None when no rows match the name, which is exactly what the test checks by searching for a name absent from the table.

```python
def test_search_database_4(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    result = self.processor.search_database(table_name, 'aaa')
    self.assertIsNone(result)
```

**test_search_database_5**: `stated`
- reason: The docstring says the method returns None when no rows match the name, and the test searches for a name absent from the table and asserts None, which a programmer following the docstring would pass.

```python
def test_search_database_5(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    result = self.processor.search_database(table_name, 'bbb')
    self.assertIsNone(result)
```

## Method `delete_from_database`

### Docstring

```python
def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
```

### Reference code (`solution_code`)

```python
def delete_from_database(self, table_name, name):

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        delete_query = f"DELETE FROM {table_name} WHERE name = ?"
        cursor.execute(delete_query, (name,))

        conn.commit()
        conn.close()
```

### Tests (`DatabaseProcessorTestDeteleFromDatabase`)

setUp (runs before each test):

```python
def setUp(self):
    self.database_name = "test.db"
    self.processor = DatabaseProcessor(self.database_name)
```

**test_delete_from_database_1**: `stated`
- reason: The docstring says the method deletes rows in the named table whose name matches the given name, which is exactly what the test checks by deleting 'John' and expecting only 'Alice' to remain.

```python
def test_delete_from_database_1(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    self.processor.delete_from_database(table_name, 'John')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'Alice')
```

**test_delete_from_database_2**: `stated`
- reason: The docstring says delete rows from the named table whose name matches, which is exactly what the test checks: after deleting 'Alice', only the non-matching row remains.

```python
def test_delete_from_database_2(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    self.processor.delete_from_database(table_name, 'Alice')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'John')
```

**test_delete_from_database_3**: `stated`
- reason: The docstring says to delete rows in the named table whose name matches the given name, so a programmer would implement per-name deletion, and calling it once for each name leaves the table empty as the test expects.

```python
def test_delete_from_database_3(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    self.processor.delete_from_database(table_name, 'John')
    self.processor.delete_from_database(table_name, 'Alice')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 0)
```

**test_delete_from_database_4**: `stated`
- reason: The docstring says to delete rows in the named table whose name matches, and the test checks that only the matching row is removed while the other row remains.

```python
def test_delete_from_database_4(self):
    table_name = "test_table"
    data = [
        {'name': 'John', 'age': 25},
        {'name': 'aaa', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    self.processor.delete_from_database(table_name, 'John')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'aaa')
```

**test_delete_from_database_5**: `stated`
- reason: The docstring says rows whose name matches the given value are deleted from the named table, which is exactly what the test checks: deleting 'bbb' leaves only 'Alice'.

```python
def test_delete_from_database_5(self):
    table_name = "test_table"
    data = [
        {'name': 'bbb', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.create_table(table_name, 'name', 'age')
    self.processor.insert_into_database(table_name, data)

    self.processor.delete_from_database(table_name, 'bbb')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'Alice')
```

## Tests in no method's test class

### `DatabaseProcessorTest`

setUp (runs before each test):

```python
def setUp(self):
    self.database_name = "test.db"
    self.processor = DatabaseProcessor(self.database_name)
```

**test_DatabaseProcessor**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_DatabaseProcessor(self):
    table_name = "test_table"
    self.processor.create_table(table_name, 'name', 'age')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    conn.close()

    self.assertIsNotNone(result)
    self.assertEqual(result[0], table_name)

    data = [
        {'name': 'John', 'age': 25},
        {'name': 'Alice', 'age': 30}
    ]
    self.processor.insert_into_database(table_name, data)
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), len(data))
    self.assertEqual(result[0][2], 25)

    result = self.processor.search_database(table_name, 'John')
    self.assertIsNotNone(result)
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'John')

    self.processor.delete_from_database(table_name, 'John')

    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'Alice')
```
