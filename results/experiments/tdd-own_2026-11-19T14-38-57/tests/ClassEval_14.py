import unittest


import unittest

import os

import sqlite3

import tempfile

class AgentTest_create_table(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_create_table.db")
        self.book_db = None

    def tearDown(self):
        if self.book_db is not None:
            try:
                self.book_db.connection.close()
            except Exception:
                pass
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _table_exists(self, connection):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='book'"
        )
        return cursor.fetchone() is not None

    def test_create_table_1(self):
        # After initialization, the book table should exist in the database.
        self.book_db = BookManagementDB(self.db_path)
        self.assertTrue(self._table_exists(self.book_db.connection))

    def test_create_table_2(self):
        # create_table should create the book table when it is missing.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.connection.execute("DROP TABLE IF EXISTS book")
        self.book_db.connection.commit()
        self.assertFalse(self._table_exists(self.book_db.connection))

        self.book_db.create_table()

        self.assertTrue(self._table_exists(self.book_db.connection))

    def test_create_table_3(self):
        # Calling create_table when the table already exists should not raise an error.
        self.book_db = BookManagementDB(self.db_path)
        try:
            self.book_db.create_table()
            self.book_db.create_table()
        except Exception as e:
            self.fail(f"create_table raised an exception on existing table: {e}")
        self.assertTrue(self._table_exists(self.book_db.connection))

    def test_create_table_4(self):
        # Calling create_table on an existing table should not remove existing rows.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.connection.execute(
            "INSERT INTO book (title, author, availability) VALUES (?, ?, ?)",
            ("book1", "author", 1),
        )
        self.book_db.connection.commit()

        self.book_db.create_table()

        rows = self.book_db.connection.execute("SELECT * FROM book").fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1:], ("book1", "author", 1))

    def test_create_table_5(self):
        # The created table should hold four fields per book:
        # id, title, author and availability.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.connection.execute("DROP TABLE IF EXISTS book")
        self.book_db.connection.commit()

        self.book_db.create_table()

        columns = self.book_db.connection.execute(
            "PRAGMA table_info(book)"
        ).fetchall()
        self.assertEqual(len(columns), 4)
        column_names = [column[1] for column in columns]
        self.assertIn("title", column_names)
        self.assertIn("author", column_names)

import unittest

import os

import sqlite3

import tempfile

class AgentTest_add_book(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_add_book.db")
        self.book_db = None

    def tearDown(self):
        if self.book_db is not None:
            try:
                self.book_db.connection.close()
            except Exception:
                pass
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _fetch_all_rows(self):
        # Read through a separate connection to confirm the data reached the database file.
        conn = sqlite3.connect(self.db_path)
        try:
            return conn.execute("SELECT id, title, author, availability FROM book").fetchall()
        finally:
            conn.close()

    def test_add_book_1(self):
        # add_book should store a row with the given title and author in the book table.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1:3], ("book1", "author"))

    def test_add_book_2(self):
        # A newly added book should have availability 1, meaning free to borrow.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][3], 1)

    def test_add_book_3(self):
        # Each added book should receive its own id, and the first book should get id 1.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 2)
        ids = [row[0] for row in rows]
        self.assertEqual(len(set(ids)), 2)
        self.assertEqual(ids[0], 1)

    def test_add_book_4(self):
        # Adding several books should keep all of them, each with its own title and author.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")
        self.book_db.add_book("book3", "author3")

        rows = self._fetch_all_rows()
        self.assertEqual(
            [row[1:] for row in rows],
            [("book1", "author1", 1), ("book2", "author2", 1), ("book3", "author3", 1)],
        )

    def test_add_book_5(self):
        # Books added with add_book should be returned by search_books in the
        # format (id, title, author, availability), as in the specification example.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")

        books = self.book_db.search_books()
        self.assertEqual(books, [(1, "book1", "author", 1)])

import unittest

import os

import sqlite3

import tempfile

class AgentTest_remove_book(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_remove_book.db")
        self.book_db = None

    def tearDown(self):
        if self.book_db is not None:
            try:
                self.book_db.connection.close()
            except Exception:
                pass
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _fetch_all_rows(self):
        # Read through a separate connection to confirm the change reached the database file.
        conn = sqlite3.connect(self.db_path)
        try:
            return conn.execute("SELECT id, title, author, availability FROM book").fetchall()
        finally:
            conn.close()

    def test_remove_book_1(self):
        # remove_book(1) should delete the book whose ID is 1 from the database.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")

        self.book_db.remove_book(1)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 0)

    def test_remove_book_2(self):
        # Removing one book should leave the other books' title, author and availability unchanged.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")

        self.book_db.remove_book(1)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1:], ("book2", "author2", 1))

    def test_remove_book_3(self):
        # Only the book with the given ID should be removed; the other IDs should stay the same.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")
        self.book_db.add_book("book3", "author3")

        self.book_db.remove_book(2)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 2)
        self.assertEqual([row[0] for row in rows], [1, 3])
        self.assertEqual([row[1] for row in rows], ["book1", "book3"])

    def test_remove_book_4(self):
        # A removed book should no longer be returned by search_books.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")

        self.book_db.remove_book(1)

        books = self.book_db.search_books()
        self.assertEqual(books, [(2, "book2", "author2", 1)])

    def test_remove_book_5(self):
        # Removing every book one by one should leave the book table empty.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")

        self.book_db.remove_book(1)
        self.book_db.remove_book(2)

        self.assertEqual(self._fetch_all_rows(), [])
        self.assertEqual(self.book_db.search_books(), [])

import unittest

import os

import sqlite3

import tempfile

class AgentTest_borrow_book(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_borrow_book.db")
        self.book_db = None

    def tearDown(self):
        if self.book_db is not None:
            try:
                self.book_db.connection.close()
            except Exception:
                pass
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _fetch_all_rows(self):
        # Read through a separate connection to confirm the change reached the database file.
        conn = sqlite3.connect(self.db_path)
        try:
            return conn.execute("SELECT id, title, author, availability FROM book ORDER BY id").fetchall()
        finally:
            conn.close()

    def test_borrow_book_1(self):
        # Borrowing a book should mark it as borrowed, so it is no longer free to borrow (availability 1).
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")

        self.book_db.borrow_book(1)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 1)
        self.assertNotEqual(rows[0][3], 1)

    def test_borrow_book_2(self):
        # Only the book with the given ID should be marked as borrowed; the others stay free (availability 1).
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")
        self.book_db.add_book("book3", "author3")

        self.book_db.borrow_book(2)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0][3], 1)
        self.assertNotEqual(rows[1][3], 1)
        self.assertEqual(rows[2][3], 1)

    def test_borrow_book_3(self):
        # Borrowing a book should leave its title and author unchanged.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")

        self.book_db.borrow_book(1)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1:3], ("book1", "author1"))

    def test_borrow_book_4(self):
        # Borrowing a book should not remove it from the database; it should still be found by search_books.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")

        self.book_db.borrow_book(1)

        books = self.book_db.search_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0][0], 1)
        self.assertEqual(books[0][1:3], ("book1", "author"))
        self.assertNotEqual(books[0][3], 1)

    def test_borrow_book_5(self):
        # Borrowing a book should not affect the availability of books that are not borrowed,
        # and the change should be visible to search_books for the borrowed book only.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")

        self.book_db.borrow_book(1)

        books = self.book_db.search_books()
        self.assertEqual(len(books), 2)
        book_by_id = {book[0]: book for book in books}
        self.assertNotEqual(book_by_id[1][3], 1)
        self.assertEqual(book_by_id[2], (2, "book2", "author2", 1))

import unittest

import os

import sqlite3

import tempfile

class AgentTest_return_book(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_return_book.db")
        self.book_db = None

    def tearDown(self):
        if self.book_db is not None:
            try:
                self.book_db.connection.close()
            except Exception:
                pass
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def _fetch_all_rows(self):
        # Read through a separate connection to confirm the change reached the database file.
        conn = sqlite3.connect(self.db_path)
        try:
            return conn.execute("SELECT id, title, author, availability FROM book ORDER BY id").fetchall()
        finally:
            conn.close()

    def test_return_book_1(self):
        # Returning a borrowed book should mark it as returned, i.e. free to borrow (availability 1).
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")
        self.book_db.borrow_book(1)

        self.book_db.return_book(1)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][3], 1)

    def test_return_book_2(self):
        # Only the book with the given ID should be marked as returned; the other borrowed book stays borrowed.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")
        self.book_db.borrow_book(1)
        self.book_db.borrow_book(2)

        self.book_db.return_book(2)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 2)
        self.assertNotEqual(rows[0][3], 1)
        self.assertEqual(rows[1][3], 1)

    def test_return_book_3(self):
        # Returning a book should leave its title and author unchanged.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.borrow_book(1)

        self.book_db.return_book(1)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1:3], ("book1", "author1"))

    def test_return_book_4(self):
        # Returning a book should not remove it; search_books should report it as free to borrow.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")
        self.book_db.borrow_book(1)

        self.book_db.return_book(1)

        books = self.book_db.search_books()
        self.assertEqual(books, [(1, "book1", "author", 1)])

    def test_return_book_5(self):
        # A returned book should be free to borrow again, so borrowing it after a return
        # should mark it as borrowed (availability no longer 1).
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")
        self.book_db.borrow_book(1)
        self.book_db.return_book(1)

        self.book_db.borrow_book(1)

        rows = self._fetch_all_rows()
        self.assertEqual(len(rows), 1)
        self.assertNotEqual(rows[0][3], 1)

import unittest

import os

import sqlite3

import tempfile

class AgentTest_search_books(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_search_books.db")
        self.book_db = None

    def tearDown(self):
        if self.book_db is not None:
            try:
                self.book_db.connection.close()
            except Exception:
                pass
        for name in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, name))
        os.rmdir(self.temp_dir)

    def test_search_books_1(self):
        # On an empty book database, search_books should return an empty list.
        self.book_db = BookManagementDB(self.db_path)

        books = self.book_db.search_books()

        self.assertEqual(books, [])

    def test_search_books_2(self):
        # With one book added, search_books should return it as (id, title, author, availability),
        # matching the specification example.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author")

        books = self.book_db.search_books()

        self.assertEqual(books, [(1, "book1", "author", 1)])

    def test_search_books_3(self):
        # search_books should return the information of all books in the database.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")
        self.book_db.add_book("book3", "author3")

        books = sorted(self.book_db.search_books(), key=lambda book: book[0])

        self.assertEqual(
            books,
            [(1, "book1", "author1", 1), (2, "book2", "author2", 1), (3, "book3", "author3", 1)],
        )

    def test_search_books_4(self):
        # search_books should return a list of tuples, each holding four fields:
        # id, title, author and availability.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")

        books = self.book_db.search_books()

        self.assertIsInstance(books, list)
        self.assertEqual(len(books), 2)
        for book in books:
            self.assertIsInstance(book, tuple)
            self.assertEqual(len(book), 4)

    def test_search_books_5(self):
        # search_books should reflect availability changes: a borrowed book should no longer
        # report availability 1, and a returned book should report availability 1 again.
        self.book_db = BookManagementDB(self.db_path)
        self.book_db.add_book("book1", "author1")
        self.book_db.add_book("book2", "author2")
        self.book_db.borrow_book(1)

        book_by_id = {book[0]: book for book in self.book_db.search_books()}
        self.assertEqual(book_by_id[2], (2, "book2", "author2", 1))
        self.assertNotEqual(book_by_id[1][3], 1)
        self.assertEqual(book_by_id[1][1:3], ("book1", "author1"))

        self.book_db.return_book(1)

        books = self.book_db.search_books()
        self.assertEqual(
            sorted(books, key=lambda book: book[0]),
            [(1, "book1", "author1", 1), (2, "book2", "author2", 1)],
        )