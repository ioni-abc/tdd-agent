# ClassEval_80

## Skeleton (what the agent sees)

```python
class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """


    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
        """

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
```

## Method `select`

### Docstring

```python
def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
```

### Reference code (`solution_code`)

```python
def select(table, columns='*', where=None):
        if columns != '*':
            columns = ', '.join(columns)
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
```

### Tests (`SQLQueryBuilderTestSelect`)

**test_select_1**: `stated`
- reason: The docstring's example shows a list of columns comma-joined after SELECT and a dict condition rendered as `key='value'` after WHERE, which is exactly what this test checks with one column list and one condition.

```python
def test_select_1(self):
    self.assertEqual(
        SQLQueryBuilder.select('users', ["id", "name"], {'age': 30}),
        "SELECT id, name FROM users WHERE age='30'"
    )
```

**test_select_2**: `stated`
- reason: The docstring example shows the same behaviour the test checks: a list of columns is joined with ", " and a dict condition becomes `key='value'` after WHERE, so a programmer following it would produce the expected string.

```python
def test_select_2(self):
    self.assertEqual(
        SQLQueryBuilder.select('students', ["id", "name"], {'age': 18}),
        "SELECT id, name FROM students WHERE age='18'"
    )
```

**test_select_3**: `stated`
- reason: The docstring shows the column list joined with ", " and each where value wrapped in single quotes, so a programmer would produce "price='1.0'" by formatting the float with its normal string form.

```python
def test_select_3(self):
    self.assertEqual(
        SQLQueryBuilder.select('items', ["id", "name"], {'price': 1.0}),
        "SELECT id, name FROM items WHERE price='1.0'"
    )
```

**test_select_4**: `stated`
- reason: The docstring example shows a column list joined with commas and a dict condition rendered as `key='value'`, which a programmer would apply to the single-column, single-condition, integer-value case in this test, giving `age='30'`.

```python
def test_select_4(self):
    self.assertEqual(
        SQLQueryBuilder.select('users', ["id"], {'age': 30}),
        "SELECT id FROM users WHERE age='30'"
    )
```

**test_select_5**: `stated`
- reason: The docstring's example shows the same format (a column list joined by commas, and a where dict rendered as `key='value'`), so a programmer following it would produce `SELECT name FROM users WHERE age='30'`.

```python
def test_select_5(self):
    self.assertEqual(
        SQLQueryBuilder.select('users', ["name"], {'age': 30}),
        "SELECT name FROM users WHERE age='30'"
    )
```

**test_select_6**: `stated`
- reason: The docstring's signature and example show a list of columns rendered as a comma-separated `SELECT ... FROM table` statement, so a programmer following it would produce "SELECT name FROM users" for a single-column list with no condition.

```python
def test_select_6(self):
    self.assertEqual(
        SQLQueryBuilder.select('users', ["name"]),
        "SELECT name FROM users"
    )
```

**test_select_7**: `stated`
- reason: The docstring's signature defaults `columns` to `'*'` and its example shows the plain `SELECT ... FROM table` output form, so a programmer would produce `SELECT * FROM users` for this call.

```python
def test_select_7(self):
    self.assertEqual(
        SQLQueryBuilder.select('users', "*"),
        "SELECT * FROM users"
    )
```

## Method `insert`

### Docstring

```python
@staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def insert(table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        return f"INSERT INTO {table} ({keys}) VALUES ({values})"
```

### Tests (`SQLQueryBuilderTestInsert`)

**test_insert_1**: `stated`
- reason: The docstring gives the exact format for an insert with a table name and a dict of values, including the doctest showing that values are quoted as strings, so the test's case (table 'users' with name and integer age) is covered by the described behaviour.

```python
def test_insert_1(self):
    self.assertEqual(
        SQLQueryBuilder.insert('users', {'name': 'Tom', 'age': 30}),
        "INSERT INTO users (name, age) VALUES ('Tom', '30')"
    )
```

**test_insert_2**: `stated`
- reason: The docstring example shows the same format (keys comma-joined, each value wrapped in single quotes, with the integer age quoted as '14'), so a programmer following it would produce the expected string for this test.

```python
def test_insert_2(self):
    self.assertEqual(
        SQLQueryBuilder.insert('students', {'name': 'Tom', 'age': 18}),
        "INSERT INTO students (name, age) VALUES ('Tom', '18')"
    )
```

**test_insert_3**: `stated`
- reason: The docstring's example shows every value, including the integer 14, wrapped in single quotes as its plain string form, so a programmer would produce `'1.0'` for the float 1.0 by the same rule.

```python
def test_insert_3(self):
    self.assertEqual(
        SQLQueryBuilder.insert('items', {'name': 'apple', 'price': 1.0}),
        "INSERT INTO items (name, price) VALUES ('apple', '1.0')"
    )
```

**test_insert_4**: `stated`
- reason: The docstring's example and its description of the `data` dict (keys become column names, values are quoted) fully determine the single-key output `INSERT INTO users (name) VALUES ('Tom')`, so a programmer following it would produce this result.

```python
def test_insert_4(self):
    self.assertEqual(
        SQLQueryBuilder.insert('users', {'name': 'Tom'}),
        "INSERT INTO users (name) VALUES ('Tom')"
    )
```

**test_insert_5**: `stated`
- reason: The docstring's example shows the same format the test checks (comma-separated column names, every value wrapped in single quotes including the integer, and the `INSERT INTO table (...) VALUES (...)` layout), so a programmer following it would produce the expected string for three columns.

```python
def test_insert_5(self):
    self.assertEqual(
        SQLQueryBuilder.insert('users', {'name': 'Tom', 'age': 30, 'region': 'USA'}),
        "INSERT INTO users (name, age, region) VALUES ('Tom', '30', 'USA')"
    )
```

## Method `delete`

### Docstring

```python
@staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def delete(table, where=None):
        query = f"DELETE FROM {table}"
        if where:
            query += " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
```

### Tests (`SQLQueryBuilderTestDetele`)

**test_delete_1**: `stated`
- reason: The docstring gives the DELETE format with a WHERE clause of key='value' pairs joined by AND, and the test with a single condition follows that same format, so a programmer following it would produce the expected string.

```python
def test_delete_1(self):
    self.assertEqual(
        SQLQueryBuilder.delete('users', {'name': 'Tom'}),
        "DELETE FROM users WHERE name='Tom'"
    )
```

**test_delete_2**: `stated`
- reason: The docstring's example shows the DELETE format with a WHERE clause built from key=value pairs quoted with single quotes, which a programmer would follow to produce "DELETE FROM students WHERE name='Tom'" for a single condition.

```python
def test_delete_2(self):
    self.assertEqual(
        SQLQueryBuilder.delete('students', {'name': 'Tom'}),
        "DELETE FROM students WHERE name='Tom'"
    )
```

**test_delete_3**: `stated`
- reason: The docstring's example and description specify the `DELETE FROM table WHERE key='value'` format with quoted values, so a programmer following it would produce the single-condition output this test expects.

```python
def test_delete_3(self):
    self.assertEqual(
        SQLQueryBuilder.delete('items', {'name': 'apple'}),
        "DELETE FROM items WHERE name='apple'"
    )
```

**test_delete_4**: `stated`
- reason: The docstring's example shows the same format (`DELETE FROM table WHERE key='value'`, with values quoted and conditions joined by AND), so a programmer following it would produce the expected single-condition output.

```python
def test_delete_4(self):
    self.assertEqual(
        SQLQueryBuilder.delete('items', {'name': 'aaa'}),
        "DELETE FROM items WHERE name='aaa'"
    )
```

**test_delete_5**: `stated`
- reason: The docstring's example shows the same format (`DELETE FROM table WHERE key='value'` with values quoted and conditions joined by AND), so a programmer following it would produce the single-condition output this test expects.

```python
def test_delete_5(self):
    self.assertEqual(
        SQLQueryBuilder.delete('items', {'name': 'bbb'}),
        "DELETE FROM items WHERE name='bbb'"
    )
```

**test_delete_6**: `unstated`
- reason: The docstring never says what the statement should look like when `where` is omitted, so a programmer could reasonably add a WHERE clause or raise an error instead of returning the bare DELETE statement the test expects.
- missing: The docstring should state that when `where` is omitted or empty, the statement has no WHERE clause and applies to every row in the table.

```python
def test_delete_6(self):
    self.assertEqual(
        SQLQueryBuilder.delete('items'),
        "DELETE FROM items"
    )
```

## Method `update`

### Docstring

```python
@staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def update(table, data, where=None):
        update_str = ', '.join(f"{k}='{v}'" for k, v in data.items())
        query = f"UPDATE {table} SET {update_str}"
        if where:
            query += " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query
```

### Tests (`SQLQueryBuilderTestUpdate`)

**test_update_1**: `stated`
- reason: The docstring example shows the same output format (values wrapped in single quotes, including integers, joined into a `SET ... WHERE name='...'` clause), so a programmer following it would produce the test's expected string.

```python
def test_update_1(self):
    self.assertEqual(
        SQLQueryBuilder.update('users', {'age': 35}, {'name': 'Tom'}),
        "UPDATE users SET age='35' WHERE name='Tom'"
    )
```

**test_update_2**: `stated`
- reason: The docstring example shows the same format the test checks: a single data pair rendered as `key='value'` after SET and a single where pair after WHERE, so a programmer following it would produce the expected string.

```python
def test_update_2(self):
    self.assertEqual(
        SQLQueryBuilder.update('students', {'age': 18}, {'name': 'Tom'}),
        "UPDATE students SET age='18' WHERE name='Tom'"
    )
```

**test_update_3**: `stated`
- reason: The docstring example shows every value, including an integer, rendered as a quoted string in the form `key='value'`, so a programmer following it would naturally produce `price='1.0'` for the float 1.0 and the test's WHERE clause follows the same pattern.

```python
def test_update_3(self):
    self.assertEqual(
        SQLQueryBuilder.update('items', {'price': 1.0}, {'name': 'apple'}),
        "UPDATE items SET price='1.0' WHERE name='apple'"
    )
```

**test_update_4**: `stated`
- reason: The docstring example shows numeric values such as 15 rendered as quoted strings in the SET clause and a single WHERE condition rendered as `name='Test'`, so a programmer following it would produce `price='1.0'` and `WHERE name='aaa'` for this float and single-condition input.

```python
def test_update_4(self):
    self.assertEqual(
        SQLQueryBuilder.update('items', {'price': 1.0}, {'name': 'aaa'}),
        "UPDATE items SET price='1.0' WHERE name='aaa'"
    )
```

**test_update_5**: `stated`
- reason: The docstring's example shows values wrapped in single quotes as their plain string form (the integer 15 becomes '15'), so a programmer would naturally render the float 1.0 as '1.0' with the same rule.

```python
def test_update_5(self):
    self.assertEqual(
        SQLQueryBuilder.update('items', {'price': 1.0}, {'name': 'bbb'}),
        "UPDATE items SET price='1.0' WHERE name='bbb'"
    )
```

**test_update_6**: `stated`
- reason: The docstring shows every value in `data` rendered as a quoted string inside `SET`, and an omitted `where` is the default, so a programmer would naturally produce `price='1.0'` from the float `1.0` via normal string formatting.

```python
def test_update_6(self):
    self.assertEqual(
        SQLQueryBuilder.update('items', {'price': 1.0}),
        "UPDATE items SET price='1.0'"
    )
```

## Tests in no method's test class

### `SQLQueryBuilderTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    self.assertEqual(
        SQLQueryBuilder.select('users', ["id", "name"], {'age': 30}),
        "SELECT id, name FROM users WHERE age='30'"
    )
    self.assertEqual(
        SQLQueryBuilder.insert('users', {'name': 'Tom', 'age': 30}),
        "INSERT INTO users (name, age) VALUES ('Tom', '30')"
    )
    self.assertEqual(
        SQLQueryBuilder.delete('users', {'name': 'Tom'}),
        "DELETE FROM users WHERE name='Tom'"
    )
    self.assertEqual(
        SQLQueryBuilder.update('users', {'age': 35}, {'name': 'Tom'}),
        "UPDATE users SET age='35' WHERE name='Tom'"
    )
```
