# ClassEval_14

## Skeleton (what the agent sees)

```python
import sqlite3

class BookManagementDB:
    """
    This is a database class as a book management system, used to handle the operations of adding, removing, updating, and searching books.
    """


    def __init__(self, db_name):
        """
        Initializes the class by creating a database connection and cursor, 
        and creates the book table if it does not already exist
        :param db_name: str, the name of db file
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates the book table in the database if it does not already exist.
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
    

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        >>> book_db.add_book('book1', 'author')
        """

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
```

## Method `create_table`

### Docstring

```python
def create_table(self):
        """
        Creates the book table in the database if it does not already exist.
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
```

### Reference code (`solution_code`)

```python
def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                available INTEGER
            )
        ''')
        self.connection.commit()
```

### Tests (`BookManagementDBTestCreateTable`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = "test.db"
    self.db = BookManagementDB(self.db_name)
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()
```

**test_create_table_1**: `unstated`
- reason: The docstring says only "the book table" without giving its name, so a correct implementation using a different name would fail the test's lookup in sqlite_master.
- missing: The docstring should state the exact name and column schema of the table to create, and that the change must be committed so a separate connection can see it.

```python
def test_create_table_1(self):
    # Check if the table exists
    self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
    result = self.cursor.fetchone()
    self.assertIsNotNone(result)
```

**test_create_table_2**: `unstated`
- reason: The docstring only says the books table is created if missing, while the test requires the exact column names and their order (id, title, author, available), which a programmer following the docstring could not know.
- missing: The docstring should list the table's columns, with their names, types and order, that the created table must contain.

```python
def test_create_table_2(self):
    self.db.create_table()
    # Check if the table has the correct columns
    self.cursor.execute("PRAGMA table_info(books)")
    columns = self.cursor.fetchall()
    column_names = [column[1] for column in columns]
    expected_column_names = ['id', 'title', 'author', 'available']
    self.assertEqual(column_names, expected_column_names)
```

## Method `add_book`

### Docstring

```python
def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        >>> book_db.add_book('book1', 'author')
        """
```

### Reference code (`solution_code`)

```python
def add_book(self, title, author):
        self.cursor.execute('''
            INSERT INTO books (title, author, available)
            VALUES (?, ?, 1)
        ''', (title, author))
        self.connection.commit()
```

### Tests (`BookManagementDBTestAddBook`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = "test.db"
    self.db = BookManagementDB(self.db_name)
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()
```

**test_add_book**: `stated`
- reason: The docstring says add_book stores the given title and author with availability set to 1, which is exactly what the test checks, and the row-id lookup is ordinary SQLite auto-increment behaviour a programmer would expect.

```python
def test_add_book(self):
    title = "Introduction to Python"
    author = "John Smith"
    self.db.add_book(title, author)

    # Check if the book was added correctly
    self.cursor.execute("SELECT title, author, available FROM books WHERE id=1")
    result = self.cursor.fetchone()
    self.assertIsNotNone(result)
    self.assertEqual(result[0], title)
    self.assertEqual(result[1], author)
    self.assertEqual(result[2], 1)
```

## Method `remove_book`

### Docstring

```python
def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
```

### Reference code (`solution_code`)

```python
def remove_book(self, book_id):
        self.cursor.execute('''
            DELETE FROM books WHERE id = ?
        ''', (book_id,))
        self.connection.commit()
```

### Tests (`BookManagementDBTestRemoveBook`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = "test.db"
    self.db = BookManagementDB(self.db_name)
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()
    # Add a book for testing removal
    self.db.add_book("Book to Remove", "John Doe")
```

**test_remove_book**: `stated`
- reason: The docstring says remove_book deletes the book with the given ID from the database, which is exactly what the test checks by confirming no row with id=1 remains afterward.

```python
def test_remove_book(self):
    self.db.remove_book(1)

    # Check if the book was removed correctly
    self.cursor.execute("SELECT * FROM books WHERE id=1")
    result = self.cursor.fetchone()
    self.assertIsNone(result)
```

## Method `borrow_book`

### Docstring

```python
def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
```

### Reference code (`solution_code`)

```python
def borrow_book(self, book_id):
        self.cursor.execute('''
            UPDATE books SET available = 0 WHERE id = ?
        ''', (book_id,))
        self.connection.commit()
```

### Tests (`BookManagementDBTestBorrowBook`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = "test.db"
    self.db = BookManagementDB(self.db_name)
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()
    # Add a book for testing borrowing
    self.db.add_book("Book to Borrow", "Jane Smith")
```

**test_borrow_book**: `unstated`
- reason: The docstring says the book is "marked as borrowed in the database" but does not name the column or value that records this, while the test expects the `available` column to become 0, so a correct implementation using a different representation could fail.
- missing: The docstring should name the database field that tracks borrowing status and the exact value that means "borrowed" (for example, which column is changed and to what value).

```python
def test_borrow_book(self):
    self.db.borrow_book(1)

    # Check if the book was marked as unavailable
    self.cursor.execute("SELECT available FROM books WHERE id=1")
    result = self.cursor.fetchone()
    self.assertEqual(result[0], 0)
```

## Method `return_book`

### Docstring

```python
def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
```

### Reference code (`solution_code`)

```python
def return_book(self, book_id):
        self.cursor.execute('''
            UPDATE books SET available = 1 WHERE id = ?
        ''', (book_id,))
        self.connection.commit()
```

### Tests (`BookManagementDBTestReturnBook`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = "test.db"
    self.db = BookManagementDB(self.db_name)
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()
    # Add a book for testing returning
    self.db.add_book("Book to Return", "James Smith")
    self.db.borrow_book(1)
```

**test_return_book**: `unstated`
- reason: The docstring says only that the book is "marked as returned," but the test checks a specific `available` column set to 1, which a programmer could reasonably implement differently (e.g., a separate borrowed flag or deleting a borrow record).
- missing: The docstring should name the column or field that records the return and the value it must take after a return (for example, which column tracks availability and whether returned books must be set to 1 or 0).

```python
def test_return_book(self):
    self.db.return_book(1)

    # Check if the book was marked as available again
    self.cursor.execute("SELECT available FROM books WHERE id=1")
    result = self.cursor.fetchone()
    self.assertEqual(result[0], 1)
```

## Method `search_books`

### Docstring

```python
def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
```

### Reference code (`solution_code`)

```python
def search_books(self):
        self.cursor.execute('''
            SELECT * FROM books
        ''')
        books = self.cursor.fetchall()
        return books
```

### Tests (`BookManagementDBTestSearchBooks`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = "test.db"
    self.db = BookManagementDB(self.db_name)
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()
    # Add some books for testing search
    self.db.add_book("Book 1", "Author 1")
    self.db.add_book("Book 2", "Author 2")
    self.db.add_book("Book 3", "Author 3")
```

**test_search_books**: `unstated`
- reason: The test expects books in insertion order and a fourth field equal to 1 for newly added books, but the docstring only gives one example row and says nothing about ordering or how those fields are set.
- missing: The docstring should state the order in which rows are returned (e.g., insertion order) and what each tuple field means, including the default value a newly added record gets for each field.

```python
def test_search_books(self):
    books = self.db.search_books()

    # Ensure that all books were retrieved
    self.assertEqual(len(books), 3)

    # Ensure that the correct book information is retrieved
    self.assertEqual(books[0][1], "Book 1")
    self.assertEqual(books[1][2], "Author 2")
    self.assertEqual(books[2][3], 1)
```
