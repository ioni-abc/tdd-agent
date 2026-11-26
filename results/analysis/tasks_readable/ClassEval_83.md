# ClassEval_83

## Skeleton (what the agent sees)

```python
import sqlite3

class StudentDatabaseProcessor:
    """
    This is a class with database operation, including inserting student information, searching for student information by name, and deleting student information by name.
    """

    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor object with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        """

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        """

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.search_student_by_name("John")
        """

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> processor.delete_student_by_name("John")
        """
```

## Method `create_student_table`

### Docstring

```python
def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        """
```

### Reference code (`solution_code`)

```python
def create_student_table(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        )
        """
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()
```

### Tests (`StudentDatabaseProcessorTestInsertStudent`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = StudentDatabaseProcessor("test_database.db")
    self.processor.create_student_table()
```

**test_insert_student_1**: `other_inconsistency`
- reason: Test-method mismatch: the test is filed under create_student_table but exercises insert_student, whose behaviour the create_student_table docstring never describes.

```python
def test_insert_student_1(self):
    student_data = {
        'name': 'Alice',
        'age': 20,
        'gender': 'female',
        'grade': 90
    }
    self.processor.insert_student(student_data)

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('Alice',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'Alice')
```

**test_insert_student_2**: `other_inconsistency`
- reason: Test-filed-under-wrong-method: the test exercises `insert_student`, but it is filed under `create_student_table`, whose docstring only covers creating the table.

```python
def test_insert_student_2(self):
    student_data = {
        'name': 'aaa',
        'age': 20,
        'gender': 'female',
        'grade': 90
    }
    self.processor.insert_student(student_data)

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('aaa',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'aaa')
```

**test_insert_student_3**: `other_inconsistency`
- reason: The test is filed under create_student_table but its only assertions exercise insert_student, which the create_student_table docstring never mentions; create_student_table is only called in setUp.

```python
def test_insert_student_3(self):
    student_data = {
        'name': 'bbb',
        'age': 20,
        'gender': 'female',
        'grade': 90
    }
    self.processor.insert_student(student_data)

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('bbb',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'bbb')
```

**test_insert_student_4**: `other_inconsistency`
- reason: Wrong method under test: the test exercises insert_student (inserting a row and reading it back), but it is filed under create_student_table, whose docstring only describes creating the table.

```python
def test_insert_student_4(self):
    student_data = {
        'name': 'ccc',
        'age': 20,
        'gender': 'female',
        'grade': 90
    }
    self.processor.insert_student(student_data)

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('ccc',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'ccc')
```

**test_insert_student_5**: `other_inconsistency`
- reason: Test-target mismatch: the test's body exercises `insert_student` (inserting a row and querying it back), while the docstring covers only creating the table, so the test does not check `create_student_table`.

```python
def test_insert_student_5(self):
    student_data = {
        'name': 'ddd',
        'age': 20,
        'gender': 'female',
        'grade': 90
    }
    self.processor.insert_student(student_data)

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('ddd',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'ddd')
```

## Method `insert_student`

### Docstring

```python
def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        """
```

### Reference code (`solution_code`)

```python
def insert_student(self, student_data):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO students (name, age, gender, grade)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query,
                       (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))

        conn.commit()
        conn.close()
```

### Tests (`StudentDatabaseProcessorTestSearchStudentByName`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = StudentDatabaseProcessor("test_database.db")
    self.processor.create_student_table()
```

**test_search_student_by_name_1**: `other_inconsistency`
- reason: The test is named and built around `search_student_by_name`, so it checks search behaviour, and `insert_student` only serves as setup for it.

```python
def test_search_student_by_name_1(self):
    student_data = {
        'name': 'Bob',
        'age': 19,
        'gender': 'male',
        'grade': 85
    }
    self.processor.insert_student(student_data)

    result = self.processor.search_student_by_name('Bob')

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'Bob')
```

**test_search_student_by_name_2**: `other_inconsistency`
- reason: The test is a search test (`test_search_student_by_name_2`) that calls `search_student_by_name` and checks its returned rows, while `insert_student`'s docstring only covers inserting a row and returns None.

```python
def test_search_student_by_name_2(self):
    student_data = {
        'name': 'aaa',
        'age': 19,
        'gender': 'male',
        'grade': 85
    }
    self.processor.insert_student(student_data)

    result = self.processor.search_student_by_name('aaa')

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'aaa')
```

**test_search_student_by_name_3**: `other_inconsistency`
- reason: The test is named and asserts on `search_student_by_name` results after an insert, so it exercises a different method than the `insert_student` docstring describes.

```python
def test_search_student_by_name_3(self):
    student_data = {
        'name': 'bbb',
        'age': 19,
        'gender': 'male',
        'grade': 85
    }
    self.processor.insert_student(student_data)

    result = self.processor.search_student_by_name('bbb')

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'bbb')
```

**test_search_student_by_name_4**: `other_inconsistency`
- reason: The test is filed under insert_student but its real assertions check search_student_by_name's return value (row count and the name at index 1), which the insert docstring does not describe.

```python
def test_search_student_by_name_4(self):
    student_data = {
        'name': 'ccc',
        'age': 19,
        'gender': 'male',
        'grade': 85
    }
    self.processor.insert_student(student_data)

    result = self.processor.search_student_by_name('ccc')

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'ccc')
```

**test_search_student_by_name_5**: `other_inconsistency`
- reason: The test is named for and asserts on `search_student_by_name`, so it targets a different method than `insert_student`, which it only uses for setup.

```python
def test_search_student_by_name_5(self):
    student_data = {
        'name': 'ddd',
        'age': 19,
        'gender': 'male',
        'grade': 85
    }
    self.processor.insert_student(student_data)

    result = self.processor.search_student_by_name('ddd')

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'ddd')
```

## Method `search_student_by_name`

### Docstring

```python
def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.search_student_by_name("John")
        """
```

### Reference code (`solution_code`)

```python
def search_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        select_query = "SELECT * FROM students WHERE name = ?"
        cursor.execute(select_query, (name,))
        result = cursor.fetchall()

        conn.close()

        return result
```

### Tests (`StudentDatabaseProcessorTestDeleteStudentByName`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = StudentDatabaseProcessor("test_database.db")
    self.processor.create_student_table()
```

**test_delete_student_by_name_1**: `other_inconsistency`
- reason: Test-method mismatch: the test is named and filed under search_student_by_name, but it exercises delete_student_by_name and checks that no row remains, which the search docstring never mentions.

```python
def test_delete_student_by_name_1(self):
    student_data = {
        'name': 'Charlie',
        'age': 18,
        'gender': 'male',
        'grade': 95
    }
    self.processor.insert_student(student_data)

    self.processor.delete_student_by_name('Charlie')

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('Charlie',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 0)
```

**test_delete_student_by_name_2**: `other_inconsistency`
- reason: Method mismatch: the test is filed under search_student_by_name but actually exercises delete_student_by_name and checks that no rows remain, which the search docstring does not describe.

```python
def test_delete_student_by_name_2(self):
    student_data = {
        'name': 'aaa',
        'age': 18,
        'gender': 'male',
        'grade': 95
    }
    self.processor.insert_student(student_data)

    self.processor.delete_student_by_name('aaa')

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('aaa',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 0)
```

**test_delete_student_by_name_3**: `other_inconsistency`
- reason: The test is named for and exercises `delete_student_by_name`, but the documented method is `search_student_by_name`, so the test does not check the method whose docstring the agent sees.

```python
def test_delete_student_by_name_3(self):
    student_data = {
        'name': 'bbb',
        'age': 18,
        'gender': 'male',
        'grade': 95
    }
    self.processor.insert_student(student_data)

    self.processor.delete_student_by_name('bbb')

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('bbb',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 0)
```

**test_delete_student_by_name_4**: `other_inconsistency`
- reason: The test is a delete-by-name check (it calls delete_student_by_name and then verifies the row is gone), but it is filed under search_student_by_name, whose docstring describes searching and returning matching rows.

```python
def test_delete_student_by_name_4(self):
    student_data = {
        'name': 'ccc',
        'age': 18,
        'gender': 'male',
        'grade': 95
    }
    self.processor.insert_student(student_data)

    self.processor.delete_student_by_name('ccc')

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('ccc',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 0)
```

**test_delete_student_by_name_5**: `other_inconsistency`
- reason: The test is filed under search_student_by_name but actually calls delete_student_by_name and checks that the row is gone, so it does not test the method it is attached to.

```python
def test_delete_student_by_name_5(self):
    student_data = {
        'name': 'ddd',
        'age': 18,
        'gender': 'male',
        'grade': 95
    }
    self.processor.insert_student(student_data)

    self.processor.delete_student_by_name('ddd')

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('ddd',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 0)
```

## Method `delete_student_by_name`

### Docstring

```python
def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> processor.delete_student_by_name("John")
        """
```

### Reference code (`solution_code`)

```python
def delete_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        delete_query = "DELETE FROM students WHERE name = ?"
        cursor.execute(delete_query, (name,))

        conn.commit()
        conn.close()
```

### Tests (`StudentDatabaseProcessorTest`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = StudentDatabaseProcessor("test_database.db")
    self.processor.create_student_table()
```

**test_StudentDatabaseProcessor**: `stated`
- reason: The docstring says the method deletes the student with the given name from the students table, which is exactly what the test checks: after deleting "Charlie", a query for that name returns no rows.

```python
def test_StudentDatabaseProcessor(self):
    student_data = {
        'name': 'Alice',
        'age': 20,
        'gender': 'female',
        'grade': 90
    }
    self.processor.insert_student(student_data)

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('Alice',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'Alice')

    student_data = {
        'name': 'Bob',
        'age': 19,
        'gender': 'male',
        'grade': 85
    }
    self.processor.insert_student(student_data)

    result = self.processor.search_student_by_name('Bob')

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0][1], 'Bob')

    student_data = {
        'name': 'Charlie',
        'age': 18,
        'gender': 'male',
        'grade': 95
    }
    self.processor.insert_student(student_data)

    self.processor.delete_student_by_name('Charlie')

    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name=?", ('Charlie',))
    result = cursor.fetchall()
    conn.close()

    self.assertEqual(len(result), 0)
```
