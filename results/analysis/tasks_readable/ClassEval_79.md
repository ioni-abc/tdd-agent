# ClassEval_79

## Skeleton (what the agent sees)

```python
class SQLGenerator:
    """
    This class generates SQL statements for common operations on a table, such as SELECT, INSERT, UPDATE, and DELETE.
    """

    def __init__(self, table_name):
        """
        Initialize the table name.
        :param table_name: str
        """
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        >>> sql = SQLGenerator('table1')
        >>> sql.select(['field1', 'field2'], 'filed3 = value1')
        'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
        """

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
        "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
        """


    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
        "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        """

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        >>> sql.delete("field1 = value1")
        'DELETE FROM table1 WHERE field1 = value1;'
        """

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        >>> sql.select_female_under_age(30)
        "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        """

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :param min_age: int. The minimum age.
        :param max_age: int. The maximum age.
        :return: str. The generated SQL statement.
        >>> sql.select_by_age_range(20, 30)
        'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
        """
```

## Method `select`

### Docstring

```python
def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        >>> sql = SQLGenerator('table1')
        >>> sql.select(['field1', 'field2'], 'filed3 = value1')
        'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
        """
```

### Reference code (`solution_code`)

```python
def select(self, fields=None, condition=None):
        if fields is None:
            fields = "*"
        else:
            fields = ", ".join(fields)
        sql = f"SELECT {fields} FROM {self.table_name}"
        if condition is not None:
            sql += f" WHERE {condition}"
        return sql + ";"
```

### Tests (`SQLGeneratorTestSelect`)

**test_select_1**: `stated`
- reason: The docstring specifies that fields are joined into the SELECT list and the condition is appended as a WHERE clause ending with a semicolon, which is exactly what the test checks with a single field and condition.

```python
def test_select_1(self):
    sql = SQLGenerator('table1')
    result = sql.select(['field1'], "field2 = value1")
    self.assertEqual(result, "SELECT field1 FROM table1 WHERE field2 = value1;")
```

**test_select_2**: `stated`
- reason: The docstring's example shows the same behaviour the test checks: a field list is joined with commas, the condition is appended after WHERE, and the statement ends with a semicolon.

```python
def test_select_2(self):
    sql = SQLGenerator('table1')
    result = sql.select(['field1', 'field2'], "field3 = value1")
    self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1;")
```

**test_select_3**: `stated`
- reason: The docstring says `fields` is a list joined into the SELECT clause and `condition` is appended after WHERE, with a trailing semicolon, so a straightforward implementation produces the expected string.

```python
def test_select_3(self):
    sql = SQLGenerator('table1')
    result = sql.select(['field1, field2'], "field3 = value1")
    self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1;")
```

**test_select_4**: `stated`
- reason: A programmer following the docstring would join the list with ", " and append the condition verbatim after WHERE, which produces exactly the expected string even though one list element already contains a comma.

```python
def test_select_4(self):
    sql = SQLGenerator('table1')
    result = sql.select(['field1, field2'], "field3 = value1, field4 = value2")
    self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1, field4 = value2;")
```

**test_select_5**: `stated`
- reason: The docstring says the fields are listed after SELECT, the condition is appended after WHERE, and the statement ends with a semicolon, which is exactly what the test expects for a single field and a comma-containing condition inserted verbatim.

```python
def test_select_5(self):
    sql = SQLGenerator('table1')
    result = sql.select(['field1'], "field2 = value1, field3 = value2")
    self.assertEqual(result, "SELECT field1 FROM table1 WHERE field2 = value1, field3 = value2;")
```

**test_select_6**: `stated`
- reason: A programmer reading that `condition` is optional with default None and that the statement is built from the fields and conditions would omit the WHERE clause when no condition is given, which is what this test expects.

```python
def test_select_6(self):
    sql = SQLGenerator('table1')
    result = sql.select(['field1'])
    self.assertEqual(result, "SELECT field1 FROM table1;")
```

## Method `insert`

### Docstring

```python
def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
        "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
        """
```

### Reference code (`solution_code`)

```python
def insert(self, data):
        fields = ", ".join(data.keys())
        values = ", ".join([f"'{value}'" for value in data.values()])
        sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({values})"
        return sql + ";"
```

### Tests (`SQLGeneratorTestInsert`)

**test_insert**: `stated`
- reason: The docstring's example shows the same output format (INSERT INTO table1 with the keys, then quoted values and a trailing semicolon), so a programmer following it would produce the string this test expects.

```python
def test_insert(self):
    sql = SQLGenerator('table1')
    result = sql.insert({'field1': 'value1', 'field2': 'value2'})
    self.assertEqual(result, "INSERT INTO table1 (field1, field2) VALUES ('value1', 'value2');")
```

**test_insert_2**: `stated`
- reason: The docstring's example shows the exact format (comma-separated field names, single-quoted values, and a trailing semicolon), so a programmer following it would produce the three-field output this test expects.

```python
def test_insert_2(self):
    sql = SQLGenerator('table1')
    result = sql.insert({'field1': 'value1', 'field2': 'value2', 'field3': 'value3'})
    self.assertEqual(result, "INSERT INTO table1 (field1, field2, field3) VALUES ('value1', 'value2', 'value3');")
```

**test_insert_3**: `stated`
- reason: The docstring's example shows the full format (table name, comma-separated field list, single-quoted values, trailing semicolon), and a programmer following it would produce the test's four-field output.

```python
def test_insert_3(self):
    sql = SQLGenerator('table1')
    result = sql.insert({'field1': 'value1', 'field2': 'value2', 'field3': 'value3', 'field4': 'value4'})
    self.assertEqual(result,
                     "INSERT INTO table1 (field1, field2, field3, field4) VALUES ('value1', 'value2', 'value3', 'value4');")
```

**test_insert_4**: `stated`
- reason: The docstring's example shows the same pattern the test checks (comma-space separated field names, each value single-quoted, and a trailing semicolon), so a programmer generalising to five fields would produce the expected string.

```python
def test_insert_4(self):
    sql = SQLGenerator('table1')
    result = sql.insert({'field1': 'value1', 'field2': 'value2', 'field3': 'value3', 'field4': 'value4',
                         'field5': 'value5'})
    self.assertEqual(result,
                     "INSERT INTO table1 (field1, field2, field3, field4, field5) VALUES ('value1', 'value2', 'value3', 'value4', 'value5');")
```

**test_insert_5**: `stated`
- reason: The docstring's example shows the exact format the test checks (field names comma-separated, each value single-quoted, the table name from the constructor, and a trailing semicolon), and the test just applies that same format to six fields.

```python
def test_insert_5(self):
    sql = SQLGenerator('table1')
    result = sql.insert({'field1': 'value1', 'field2': 'value2', 'field3': 'value3', 'field4': 'value4',
                         'field5': 'value5', 'field6': 'value6'})
    self.assertEqual(result,
                     "INSERT INTO table1 (field1, field2, field3, field4, field5, field6) VALUES ('value1', 'value2', 'value3', 'value4', 'value5', 'value6');")
```

## Method `update`

### Docstring

```python
def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
        "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        """
```

### Reference code (`solution_code`)

```python
def update(self, data, condition):
        set_clause = ", ".join([f"{field} = '{value}'" for field, value in data.items()])
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}"
        return sql + ";"
```

### Tests (`SQLGeneratorTestUpdate`)

**test_update**: `stated`
- reason: The docstring's example output matches the test exactly, showing the table name, quoted SET values, the WHERE clause, and the trailing semicolon.

```python
def test_update(self):
    sql = SQLGenerator('table1')
    result = sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
    self.assertEqual(result,
                     "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;")
```

**test_update_2**: `stated`
- reason: The docstring's example shows the exact format (quoted values, comma-joined SET clause, WHERE condition, trailing semicolon, table name from the object), so a programmer generalising to three fields would produce the expected string.

```python
def test_update_2(self):
    sql = SQLGenerator('table1')
    result = sql.update({'field1': 'new_value1', 'field2': 'new_value2', 'field3': 'new_value3'},
                        "field4 = value1")
    self.assertEqual(result,
                     "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2', field3 = 'new_value3' WHERE field4 = value1;")
```

**test_update_3**: `stated`
- reason: The docstring's example shows the same output format (quoted values, comma-joined SET clause, WHERE clause, trailing semicolon) that this four-field test checks, so a programmer following it would pass.

```python
def test_update_3(self):
    sql = SQLGenerator('table1')
    result = sql.update({'field1': 'new_value1', 'field2': 'new_value2', 'field3': 'new_value3',
                         'field4': 'new_value4'}, "field5 = value1")
    self.assertEqual(result,
                     "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2', field3 = 'new_value3', field4 = 'new_value4' WHERE field5 = value1;")
```

**test_update_4**: `stated`
- reason: The docstring specifies the UPDATE format with SET clause of "field = 'value'" pairs joined by commas, WHERE condition, and trailing semicolon, which the test with five fields exercises directly, so a programmer following it would produce the expected string.

```python
def test_update_4(self):
    sql = SQLGenerator('table1')
    result = sql.update({'field1': 'new_value1', 'field2': 'new_value2', 'field3': 'new_value3',
                         'field4': 'new_value4', 'field5': 'new_value5'}, "field6 = value1")
    self.assertEqual(result,
                     "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2', field3 = 'new_value3', field4 = 'new_value4', field5 = 'new_value5' WHERE field6 = value1;")
```

**test_update_5**: `stated`
- reason: The docstring's example shows the same format the test checks (quoted values, comma-separated SET clause, WHERE condition, trailing semicolon), so a programmer following it would produce the expected string for six fields.

```python
def test_update_5(self):
    sql = SQLGenerator('table1')
    result = sql.update({'field1': 'new_value1', 'field2': 'new_value2', 'field3': 'new_value3',
                         'field4': 'new_value4', 'field5': 'new_value5', 'field6': 'new_value6'},
                        "field7 = value1")
    self.assertEqual(result,
                     "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2', field3 = 'new_value3', field4 = 'new_value4', field5 = 'new_value5', field6 = 'new_value6' WHERE field7 = value1;")
```

## Method `delete`

### Docstring

```python
def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        >>> sql.delete("field1 = value1")
        'DELETE FROM table1 WHERE field1 = value1;'
        """
```

### Reference code (`solution_code`)

```python
def delete(self, condition):
        sql = f"DELETE FROM {self.table_name} WHERE {condition}"
        return sql + ";"
```

### Tests (`SQLGeneratorTestDelete`)

**test_delete**: `stated`
- reason: The docstring gives the exact format "DELETE FROM table1 WHERE field1 = value1;" for the condition-based delete, which is what the test checks, so a programmer following it would produce the expected string.

```python
def test_delete(self):
    sql = SQLGenerator('table1')
    result = sql.delete("field1 = value1")
    self.assertEqual(result, "DELETE FROM table1 WHERE field1 = value1;")
```

**test_delete_2**: `stated`
- reason: The docstring says delete generates "DELETE FROM table1 WHERE field1 = value1;" from a condition string, so a programmer would produce the same output with a compound AND condition, which the test expects.

```python
def test_delete_2(self):
    sql = SQLGenerator('table1')
    result = sql.delete("field1 = value1 AND field2 = value2")
    self.assertEqual(result, "DELETE FROM table1 WHERE field1 = value1 AND field2 = value2;")
```

**test_delete_3**: `stated`
- reason: The docstring specifies the output format, including the table name, the verbatim condition, and the trailing semicolon, so a programmer following it would produce the expected string for a compound AND condition.

```python
def test_delete_3(self):
    sql = SQLGenerator('table1')
    result = sql.delete("field1 = value1 AND field2 = value2 AND field3 = value3")
    self.assertEqual(result, "DELETE FROM table1 WHERE field1 = value1 AND field2 = value2 AND field3 = value3;")
```

**test_delete_4**: `stated`
- reason: The docstring says the method builds a DELETE statement from the given condition string, so a programmer would insert the condition verbatim after WHERE and append a semicolon, which is what this compound AND test expects.

```python
def test_delete_4(self):
    sql = SQLGenerator('table1')
    result = sql.delete("field1 = value1 AND field2 = value2 AND field3 = value3 AND field4 = value4")
    self.assertEqual(result,
                     "DELETE FROM table1 WHERE field1 = value1 AND field2 = value2 AND field3 = value3 AND field4 = value4;")
```

**test_delete_5**: `stated`
- reason: The docstring gives the output format `DELETE FROM <table> WHERE <condition>;` with the condition inserted as-is, so a programmer following it would produce the exact string this test expects for a multi-clause AND condition.

```python
def test_delete_5(self):
    sql = SQLGenerator('table1')
    result = sql.delete("field1 = value1 AND field2 = value2 AND field3 = value3 AND field4 = value4 AND field5 = value5")
    self.assertEqual(result,
                     "DELETE FROM table1 WHERE field1 = value1 AND field2 = value2 AND field3 = value3 AND field4 = value4 AND field5 = value5;")
```

## Method `select_female_under_age`

### Docstring

```python
def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        >>> sql.select_female_under_age(30)
        "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        """
```

### Reference code (`solution_code`)

```python
def select_female_under_age(self, age):
        condition = f"age < {age} AND gender = 'female'"
        return self.select(condition=condition)
```

### Tests (`SQLGeneratorTestSelectFemaleUnderAge`)

**test_select_female_under_age**: `stated`
- reason: The docstring's example gives the exact expected output for `select_female_under_age(30)` on `table1`, which is the same string the test asserts.

```python
def test_select_female_under_age(self):
    sql = SQLGenerator('table1')
    result = sql.select_female_under_age(30)
    self.assertEqual(result, "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';")
```

**test_select_female_under_age_2**: `stated`
- reason: The docstring specifies that the method produces a SQL SELECT of all columns from the table where age is less than the given value and gender is 'female', with the example showing the exact format, so a programmer following it would produce the test's expected string for age 40.

```python
def test_select_female_under_age_2(self):
    sql = SQLGenerator('table1')
    result = sql.select_female_under_age(40)
    self.assertEqual(result,"SELECT * FROM table1 WHERE age < 40 AND gender = 'female';")
```

**test_select_female_under_age_3**: `stated`
- reason: The docstring gives the exact output format "SELECT * FROM table1 WHERE age < N AND gender = 'female';" for a given age, so a programmer following it would produce the same string the test expects for age 20.

```python
def test_select_female_under_age_3(self):
    sql = SQLGenerator('table1')
    result = sql.select_female_under_age(20)
    self.assertEqual(result,"SELECT * FROM table1 WHERE age < 20 AND gender = 'female';")
```

**test_select_female_under_age_4**: `stated`
- reason: The docstring gives the exact output format, `SELECT * FROM table1 WHERE age < N AND gender = 'female';`, so a programmer substituting 10 for the age would produce the expected string.

```python
def test_select_female_under_age_4(self):
    sql = SQLGenerator('table1')
    result = sql.select_female_under_age(10)
    self.assertEqual(result,"SELECT * FROM table1 WHERE age < 10 AND gender = 'female';")
```

**test_select_female_under_age_5**: `stated`
- reason: The docstring gives the exact output format "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';" for an age argument, so a programmer following it would produce the test's expected string for age 50 with table1.

```python
def test_select_female_under_age_5(self):
    sql = SQLGenerator('table1')
    result = sql.select_female_under_age(50)
    self.assertEqual(result,"SELECT * FROM table1 WHERE age < 50 AND gender = 'female';")
```

## Method `select_by_age_range`

### Docstring

```python
def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :param min_age: int. The minimum age.
        :param max_age: int. The maximum age.
        :return: str. The generated SQL statement.
        >>> sql.select_by_age_range(20, 30)
        'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
        """
```

### Reference code (`solution_code`)

```python
def select_by_age_range(self, min_age, max_age):
        condition = f"age BETWEEN {min_age} AND {max_age}"
        return self.select(condition=condition)
```

### Tests (`SQLGeneratorTestSelectByAgeRange`)

**test_select_by_age_range**: `stated`
- reason: The docstring specifies that the method returns a SQL SELECT statement with a BETWEEN clause on age using the given bounds, and the docstring example matches the test's expected output exactly, so a programmer following it would produce the tested string.

```python
def test_select_by_age_range(self):
    sql = SQLGenerator('table1')
    result = sql.select_by_age_range(20, 30)
    self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;")
```

**test_select_by_age_range_2**: `stated`
- reason: The docstring gives the exact output format 'SELECT * FROM table1 WHERE age BETWEEN lo AND hi;' with the bounds inserted, so a programmer following it would produce the test's expected string for inputs 10 and 20.

```python
def test_select_by_age_range_2(self):
    sql = SQLGenerator('table1')
    result = sql.select_by_age_range(10, 20)
    self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 10 AND 20;")
```

**test_select_by_age_range_3**: `stated`
- reason: The docstring specifies the output format "SELECT * FROM table1 WHERE age BETWEEN min AND max;" with the bounds inserted, so a programmer following it would produce exactly the expected string for (30, 40).

```python
def test_select_by_age_range_3(self):
    sql = SQLGenerator('table1')
    result = sql.select_by_age_range(30, 40)
    self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 30 AND 40;")
```

**test_select_by_age_range_4**: `stated`
- reason: The docstring gives the exact output format "SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;" for a range call, so a programmer following it would produce the same SQL for the 40-to-50 case.

```python
def test_select_by_age_range_4(self):
    sql = SQLGenerator('table1')
    result = sql.select_by_age_range(40, 50)
    self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 40 AND 50;")
```

**test_select_by_age_range_5**: `stated`
- reason: The docstring gives the exact output format "SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;" for a range, so a programmer following it would produce the same string for 50 and 60.

```python
def test_select_by_age_range_5(self):
    sql = SQLGenerator('table1')
    result = sql.select_by_age_range(50, 60)
    self.assertEqual(result, "SELECT * FROM table1 WHERE age BETWEEN 50 AND 60;")
```

## Tests in no method's test class

### `SQLGeneratorTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    sql = SQLGenerator('table1')
    self.assertEqual(sql.select(['field1', 'field2'], "field3 = value1"),
                     "SELECT field1, field2 FROM table1 WHERE field3 = value1;")
    self.assertEqual(sql.insert({'field1': 'value1', 'field2': 'value2'}),
                     "INSERT INTO table1 (field1, field2) VALUES ('value1', 'value2');")
    self.assertEqual(sql.update({'field1': 'new_value1', 'field2': 'new_value2'},
                                "field3 = value1"),
                     "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;")
    self.assertEqual(sql.delete("field1 = value1"),
                     "DELETE FROM table1 WHERE field1 = value1;")
    self.assertEqual(sql.select_female_under_age(30),
                     "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';")
    self.assertEqual(sql.select_by_age_range(20, 30),
                     "SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;")
```
