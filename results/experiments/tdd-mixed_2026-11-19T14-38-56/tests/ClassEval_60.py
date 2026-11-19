import unittest
import os




class MovieTicketDBTestInsertTicket(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_database.db'
        self.db = MovieTicketDB(self.db_name)

    def tearDown(self):
        self.db.connection.close()
        os.remove(self.db_name)

    def test_insert_ticket_1(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'John Doe')
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertEqual(ticket[1], 'Avengers: Endgame')
        self.assertEqual(ticket[2], 'Cinema 1')
        self.assertEqual(ticket[3], 'A1')
        self.assertEqual(ticket[4], 'John Doe')

    def test_insert_ticket_2(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'aaa')
        tickets = self.db.search_tickets_by_customer('aaa')
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertEqual(ticket[1], 'Avengers: Endgame')
        self.assertEqual(ticket[2], 'Cinema 1')
        self.assertEqual(ticket[3], 'A1')
        self.assertEqual(ticket[4], 'aaa')

    def test_insert_ticket_3(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'bbb')
        tickets = self.db.search_tickets_by_customer('bbb')
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertEqual(ticket[1], 'Avengers: Endgame')
        self.assertEqual(ticket[2], 'Cinema 1')
        self.assertEqual(ticket[3], 'A1')
        self.assertEqual(ticket[4], 'bbb')

import unittest

import os

import sqlite3

class AgentTest_create_table(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_create_table_database.db'
        self.db = MovieTicketDB(self.db_name)

    def tearDown(self):
        self.db.connection.close()
        os.remove(self.db_name)

    def test_create_table_1(self):
        cursor = self.db.connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='tickets'"
        )
        self.assertIsNotNone(cursor.fetchone())

        cursor.execute("PRAGMA table_info(tickets)")
        columns = cursor.fetchall()
        self.assertEqual(len(columns), 5)

        column_types = [column[2].upper() for column in columns]
        self.assertIn('INT', column_types[0])
        for column_type in column_types[1:]:
            self.assertIn('TEXT', column_type)

    def test_create_table_2(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'John Doe')
        self.db.create_table()
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertEqual(ticket[1], 'Avengers: Endgame')
        self.assertEqual(ticket[2], 'Cinema 1')
        self.assertEqual(ticket[3], 'A1')
        self.assertEqual(ticket[4], 'John Doe')

class MovieTicketDBTestSearchTicketsByCustomer(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_database.db'
        self.db = MovieTicketDB(self.db_name)

    def tearDown(self):
        self.db.connection.close()
        os.remove(self.db_name)

    def test_search_tickets_by_customer_1(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'John Doe')
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertEqual(ticket[1], 'Avengers: Endgame')
        self.assertEqual(ticket[2], 'Cinema 1')
        self.assertEqual(ticket[3], 'A1')
        self.assertEqual(ticket[4], 'John Doe')

    def test_search_tickets_by_customer_2(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'aaa')
        tickets = self.db.search_tickets_by_customer('aaa')
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertEqual(ticket[1], 'Avengers: Endgame')
        self.assertEqual(ticket[2], 'Cinema 1')
        self.assertEqual(ticket[3], 'A1')
        self.assertEqual(ticket[4], 'aaa')

    def test_search_tickets_by_customer_3(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'bbb')
        tickets = self.db.search_tickets_by_customer('bbb')
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertEqual(ticket[1], 'Avengers: Endgame')
        self.assertEqual(ticket[2], 'Cinema 1')
        self.assertEqual(ticket[3], 'A1')
        self.assertEqual(ticket[4], 'bbb')

import unittest

import os

class AgentTest_insert_ticket(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_insert_ticket_database.db'
        self.db = MovieTicketDB(self.db_name)

    def tearDown(self):
        self.db.connection.close()
        os.remove(self.db_name)

    def test_insert_ticket_1(self):
        self.db.insert_ticket('Movie A', 'Theater 1', 'A1', 'John Doe')
        self.db.insert_ticket('Movie B', 'Theater 2', 'B7', 'John Doe')
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 2)
        movie_names = sorted(ticket[1] for ticket in tickets)
        self.assertEqual(movie_names, ['Movie A', 'Movie B'])
        seat_numbers = sorted(ticket[3] for ticket in tickets)
        self.assertEqual(seat_numbers, ['A1', 'B7'])

    def test_insert_ticket_2(self):
        self.db.insert_ticket('Movie A', 'Theater 1', 'A1', 'John Doe')
        self.db.insert_ticket('Movie A', 'Theater 1', 'A2', 'John Doe')
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 2)
        for ticket in tickets:
            self.assertIsInstance(ticket[0], int)
        self.assertNotEqual(tickets[0][0], tickets[1][0])

class MovieTicketDBTestDeleteTicket(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_database.db'
        self.db = MovieTicketDB(self.db_name)

    def tearDown(self):
        self.db.connection.close()
        os.remove(self.db_name)

    def test_delete_ticket_1(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'John Doe')
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 1)
        ticket_id = tickets[0][0]
        self.db.delete_ticket(ticket_id)
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 0)

    def test_delete_ticket_2(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'aaa')
        tickets = self.db.search_tickets_by_customer('aaa')
        self.assertEqual(len(tickets), 1)
        ticket_id = tickets[0][0]
        self.db.delete_ticket(ticket_id)
        tickets = self.db.search_tickets_by_customer('aaa')
        self.assertEqual(len(tickets), 0)

    def test_delete_ticket_3(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'bbb')
        tickets = self.db.search_tickets_by_customer('bbb')
        self.assertEqual(len(tickets), 1)
        ticket_id = tickets[0][0]
        self.db.delete_ticket(ticket_id)
        tickets = self.db.search_tickets_by_customer('bbb')
        self.assertEqual(len(tickets), 0)

class AgentTest_search_tickets_by_customer(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_search_tickets_by_customer_database.db'
        self.db = MovieTicketDB(self.db_name)

    def tearDown(self):
        self.db.connection.close()
        os.remove(self.db_name)

    def test_search_tickets_by_customer_1(self):
        self.db.insert_ticket('Movie A', 'Theater 1', 'A1', 'John Doe')
        tickets = self.db.search_tickets_by_customer('Jane Roe')
        self.assertIsInstance(tickets, list)
        self.assertEqual(len(tickets), 0)

    def test_search_tickets_by_customer_2(self):
        self.db.insert_ticket('Movie A', 'Theater 1', 'A1', 'John Doe')
        self.db.insert_ticket('Movie B', 'Theater 2', 'B7', 'John Doe')
        self.db.insert_ticket('Movie C', 'Theater 3', 'C3', 'Jane Roe')
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertIsInstance(tickets, list)
        self.assertEqual(len(tickets), 2)
        for ticket in tickets:
            self.assertIsInstance(ticket, tuple)
            self.assertEqual(ticket[4], 'John Doe')
        movie_names = sorted(ticket[1] for ticket in tickets)
        self.assertEqual(movie_names, ['Movie A', 'Movie B'])

class MovieTicketDBTest(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_database.db'
        self.db = MovieTicketDB(self.db_name)

    def tearDown(self):
        self.db.connection.close()
        os.remove(self.db_name)

    def test_MovieTicketDB(self):
        self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'John Doe')
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertEqual(ticket[1], 'Avengers: Endgame')
        self.assertEqual(ticket[2], 'Cinema 1')
        self.assertEqual(ticket[3], 'A1')
        self.assertEqual(ticket[4], 'John Doe')
        ticket_id = tickets[0][0]
        self.db.delete_ticket(ticket_id)
        tickets = self.db.search_tickets_by_customer('John Doe')
        self.assertEqual(len(tickets), 0)