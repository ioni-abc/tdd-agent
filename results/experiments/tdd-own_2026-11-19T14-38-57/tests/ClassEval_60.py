import unittest


import unittest

import sqlite3

class AgentTest_create_table(unittest.TestCase):

    def setUp(self):
        self.db = MovieTicketDB(":memory:")

    def tearDown(self):
        self.db.connection.close()

    def test_create_table_1(self):
        # After initialization, create_table should have created the "tickets" table.
        self.db.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='tickets'"
        )
        row = self.db.cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], "tickets")

    def test_create_table_2(self):
        # The "tickets" table should have exactly five fields:
        # ID, movie name, theater name, seat number and customer name.
        self.db.cursor.execute("PRAGMA table_info(tickets)")
        columns = self.db.cursor.fetchall()
        self.assertEqual(len(columns), 5)

    def test_create_table_3(self):
        # Field types: ID is int; movie name, theater name, seat number and
        # customer name are str (TEXT in SQLite).
        self.db.cursor.execute("PRAGMA table_info(tickets)")
        columns = self.db.cursor.fetchall()
        declared_types = [str(col[2]).upper() for col in columns]
        int_columns = [t for t in declared_types if "INT" in t]
        text_columns = [t for t in declared_types if "TEXT" in t]
        self.assertEqual(len(int_columns), 1)
        self.assertEqual(len(text_columns), 4)

    def test_create_table_4(self):
        # create_table should be safe to call again when the table already exists
        # ("if it does not exist already"): no error, and the table is unchanged.
        try:
            self.db.create_table()
        except Exception as e:
            self.fail(f"create_table raised an exception on repeated call: {e}")
        self.db.cursor.execute("PRAGMA table_info(tickets)")
        columns = self.db.cursor.fetchall()
        self.assertEqual(len(columns), 5)

    def test_create_table_5(self):
        # create_table should return None according to its specification.
        result = self.db.create_table()
        self.assertIsNone(result)

class AgentTest_insert_ticket(unittest.TestCase):

    def setUp(self):
        self.db = MovieTicketDB(":memory:")

    def tearDown(self):
        self.db.connection.close()

    def test_insert_ticket_1(self):
        # After inserting one ticket, the "tickets" table should contain exactly one row
        # holding the movie name, theater name, seat number and customer name given.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.cursor.execute("SELECT * FROM tickets")
        rows = self.db.cursor.fetchall()
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(len(row), 5)
        self.assertIn("Movie A", row)
        self.assertIn("Theater 1", row)
        self.assertIn("A1", row)
        self.assertIn("John Doe", row)

    def test_insert_ticket_2(self):
        # insert_ticket should return None according to its specification.
        result = self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.assertIsNone(result)

    def test_insert_ticket_3(self):
        # Each call inserts a new ticket, so two calls should give two rows.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.insert_ticket("Movie B", "Theater 2", "B7", "Jane Roe")
        self.db.cursor.execute("SELECT COUNT(*) FROM tickets")
        count = self.db.cursor.fetchone()[0]
        self.assertEqual(count, 2)

    def test_insert_ticket_4(self):
        # An inserted ticket should be findable by its customer name.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        result = self.db.search_tickets_by_customer("John Doe")
        self.assertEqual(len(result), 1)

    def test_insert_ticket_5(self):
        # The ID field is of type int, so the ID of an inserted ticket should be an int.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.cursor.execute("SELECT * FROM tickets")
        row = self.db.cursor.fetchone()
        self.assertIsInstance(row[0], int)

class AgentTest_search_tickets_by_customer(unittest.TestCase):

    def setUp(self):
        self.db = MovieTicketDB(":memory:")

    def tearDown(self):
        self.db.connection.close()

    def test_search_tickets_by_customer_1(self):
        # search_tickets_by_customer should return a list of tuples.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        result = self.db.search_tickets_by_customer("John Doe")
        self.assertIsInstance(result, list)
        for row in result:
            self.assertIsInstance(row, tuple)

    def test_search_tickets_by_customer_2(self):
        # Following the docstring example: one ticket for "John Doe" gives a result of length 1.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        result = self.db.search_tickets_by_customer("John Doe")
        self.assertEqual(len(result), 1)

    def test_search_tickets_by_customer_3(self):
        # All tickets belonging to the searched customer should be returned, not just one.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.insert_ticket("Movie B", "Theater 2", "B7", "John Doe")
        self.db.insert_ticket("Movie C", "Theater 3", "C3", "John Doe")
        result = self.db.search_tickets_by_customer("John Doe")
        self.assertEqual(len(result), 3)

    def test_search_tickets_by_customer_4(self):
        # Only rows matching the customer name should be returned; other customers' tickets are excluded.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.insert_ticket("Movie B", "Theater 2", "B7", "Jane Roe")
        self.db.insert_ticket("Movie C", "Theater 3", "C3", "John Doe")
        result = self.db.search_tickets_by_customer("John Doe")
        self.assertEqual(len(result), 2)
        for row in result:
            self.assertIn("John Doe", row)
            self.assertNotIn("Jane Roe", row)

    def test_search_tickets_by_customer_5(self):
        # Each returned tuple should be a full row of the "tickets" table:
        # ID, movie name, theater name, seat number and customer name.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        result = self.db.search_tickets_by_customer("John Doe")
        self.assertEqual(len(result), 1)
        row = result[0]
        self.assertEqual(len(row), 5)
        self.assertIsInstance(row[0], int)
        self.assertEqual(row[1:], ("Movie A", "Theater 1", "A1", "John Doe"))

class AgentTest_delete_ticket(unittest.TestCase):

    def setUp(self):
        self.db = MovieTicketDB(":memory:")

    def tearDown(self):
        self.db.connection.close()

    def test_delete_ticket_1(self):
        # After deleting the only ticket by its ID, the "tickets" table should be empty.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.cursor.execute("SELECT * FROM tickets")
        ticket_id = self.db.cursor.fetchone()[0]
        self.db.delete_ticket(ticket_id)
        self.db.cursor.execute("SELECT COUNT(*) FROM tickets")
        count = self.db.cursor.fetchone()[0]
        self.assertEqual(count, 0)

    def test_delete_ticket_2(self):
        # delete_ticket should return None according to its specification.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.cursor.execute("SELECT * FROM tickets")
        ticket_id = self.db.cursor.fetchone()[0]
        result = self.db.delete_ticket(ticket_id)
        self.assertIsNone(result)

    def test_delete_ticket_3(self):
        # Deleting one ticket out of two should leave exactly one row in the table.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.insert_ticket("Movie B", "Theater 2", "B7", "Jane Roe")
        self.db.cursor.execute("SELECT * FROM tickets")
        ticket_id = self.db.cursor.fetchall()[0][0]
        self.db.delete_ticket(ticket_id)
        self.db.cursor.execute("SELECT COUNT(*) FROM tickets")
        count = self.db.cursor.fetchone()[0]
        self.assertEqual(count, 1)

    def test_delete_ticket_4(self):
        # The deleted ticket should no longer be found by customer name.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.cursor.execute("SELECT * FROM tickets")
        ticket_id = self.db.cursor.fetchone()[0]
        self.db.delete_ticket(ticket_id)
        result = self.db.search_tickets_by_customer("John Doe")
        self.assertEqual(len(result), 0)

    def test_delete_ticket_5(self):
        # Only the ticket with the given ID should be removed; the other ticket's
        # row (with its own ID, movie, theater, seat and customer) should remain intact.
        self.db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        self.db.insert_ticket("Movie B", "Theater 2", "B7", "Jane Roe")
        self.db.cursor.execute("SELECT * FROM tickets")
        rows = self.db.cursor.fetchall()
        first_id = rows[0][0]
        second_row = rows[1]
        self.db.delete_ticket(first_id)
        self.db.cursor.execute("SELECT * FROM tickets")
        remaining = self.db.cursor.fetchall()
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0], second_row)