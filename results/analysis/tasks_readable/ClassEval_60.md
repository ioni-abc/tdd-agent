# ClassEval_60

## Skeleton (what the agent sees)

```python
import sqlite3

class MovieTicketDB:
    """
    This is a class for movie database operations, which allows for inserting movie information, searching for movie information by name, and deleting movie information by name.
    """

    def __init__(self, db_name):
        """
        Initializes the MovieTicketDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()


    def create_table(self):
        """
        Creates a "tickets" table in the database if it does not exist already.Fields include ID of type int, movie name of type str, theater name of type str, seat number of type str, and customer name of type str
        :return: None
        """

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :param movie_name: str, the name of the movie.
        :param theater_name: str, the name of the theater.
        :param seat_number: str, the seat number.
        :param customer_name: str, the name of the customer.
        :return: None
        """

    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> result = ticket_db.search_tickets_by_customer("John Doe")
        len(result) = 1
        """

    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to delete.
        :return: None
        """
```

## Method `create_table`

### Docstring

```python
def create_table(self):
        """
        Creates a "tickets" table in the database if it does not exist already.Fields include ID of type int, movie name of type str, theater name of type str, seat number of type str, and customer name of type str
        :return: None
        """
```

### Reference code (`solution_code`)

```python
def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                movie_name TEXT,
                theater_name TEXT,
                seat_number TEXT,
                customer_name TEXT
            )
        ''')
        self.connection.commit()
```

### Tests (`MovieTicketDBTestInsertTicket`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = 'test_database.db'
    self.db = MovieTicketDB(self.db_name)
```

**test_insert_ticket_1**: `other_inconsistency`
- reason: The test is filed under create_table but only exercises insert_ticket and search_tickets_by_customer, and it never checks that create_table creates the table.

```python
def test_insert_ticket_1(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'John Doe')
    tickets = self.db.search_tickets_by_customer('John Doe')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'John Doe')
```

**test_insert_ticket_2**: `other_inconsistency`
- reason: The test exercises `insert_ticket` and `search_tickets_by_customer` and never calls `create_table`, so it is filed under the wrong method and does not test what the `create_table` docstring describes.

```python
def test_insert_ticket_2(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'aaa')
    tickets = self.db.search_tickets_by_customer('aaa')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'aaa')
```

**test_insert_ticket_3**: `other_inconsistency`
- reason: The test exercises `insert_ticket` and `search_tickets_by_customer` rather than `create_table`, so it is filed under the wrong method and does not check what the `create_table` docstring describes.

```python
def test_insert_ticket_3(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'bbb')
    tickets = self.db.search_tickets_by_customer('bbb')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'bbb')
```

**test_insert_ticket_4**: `other_inconsistency`
- reason: The test exercises `insert_ticket` and `search_tickets_by_customer`, but it is filed under `create_table`, whose docstring only covers creating the table.

```python
def test_insert_ticket_4(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'ccc')
    tickets = self.db.search_tickets_by_customer('ccc')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'ccc')
```

**test_insert_ticket_5**: `other_inconsistency`
- reason: The test exercises insert_ticket and search_tickets_by_customer, but it is filed under create_table, whose docstring only describes creating the tickets table.

```python
def test_insert_ticket_5(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'ddd')
    tickets = self.db.search_tickets_by_customer('ddd')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'ddd')
```

## Method `insert_ticket`

### Docstring

```python
def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :param movie_name: str, the name of the movie.
        :param theater_name: str, the name of the theater.
        :param seat_number: str, the seat number.
        :param customer_name: str, the name of the customer.
        :return: None
        """
```

### Reference code (`solution_code`)

```python
def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        self.cursor.execute('''
            INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
            VALUES (?, ?, ?, ?)
        ''', (movie_name, theater_name, seat_number, customer_name))
        self.connection.commit()
```

### Tests (`MovieTicketDBTestSearchTicketsByCustomer`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = 'test_database.db'
    self.db = MovieTicketDB(self.db_name)
```

**test_search_tickets_by_customer_1**: `unstated`
- reason: The docstring says the ticket is inserted with the four given fields, but the test also depends on an unstated row layout (an id column at index 0, then the four fields in order) and on the shape of what the search method returns, so a correct insert could still fail the index checks.
- missing: The docstring should state the column layout of stored records, including any auto-generated key and the order of fields, and the format of rows returned when they are read back.

```python
def test_search_tickets_by_customer_1(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'John Doe')
    tickets = self.db.search_tickets_by_customer('John Doe')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'John Doe')
```

**test_search_tickets_by_customer_2**: `other_inconsistency`
- reason: The test is named and structured as a search test, and its assertions check the row layout returned by `search_tickets_by_customer`, not the behaviour of `insert_ticket`, which only needs to store the four fields.

```python
def test_search_tickets_by_customer_2(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'aaa')
    tickets = self.db.search_tickets_by_customer('aaa')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'aaa')
```

**test_search_tickets_by_customer_3**: `other_inconsistency`
- reason: The test is named and filed as a search test, and its main assertions check what `search_tickets_by_customer` returns (including an id at index 0), which `insert_ticket`'s docstring does not describe.

```python
def test_search_tickets_by_customer_3(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'bbb')
    tickets = self.db.search_tickets_by_customer('bbb')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'bbb')
```

**test_search_tickets_by_customer_4**: `other_inconsistency`
- reason: Test-filing mismatch: the test is named and assertions focus on `search_tickets_by_customer`, while the docstring describes only `insert_ticket`, which the test merely uses as setup.

```python
def test_search_tickets_by_customer_4(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'ccc')
    tickets = self.db.search_tickets_by_customer('ccc')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'ccc')
```

**test_search_tickets_by_customer_5**: `unstated`
- reason: The docstring says only that the method inserts a row with the four given values, but the test also depends on how a later search returns that row, with an auto-generated id at index 0 followed by the four values, and nothing in the docstring says so.
- missing: The docstring should state the layout of stored records as read back by query methods, including any generated id column and its position, so a correct implementation can match what the test indexes.

```python
def test_search_tickets_by_customer_5(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'ddd')
    tickets = self.db.search_tickets_by_customer('ddd')
    self.assertEqual(len(tickets), 1)
    ticket = tickets[0]
    self.assertEqual(ticket[1], 'Avengers: Endgame')
    self.assertEqual(ticket[2], 'Cinema 1')
    self.assertEqual(ticket[3], 'A1')
    self.assertEqual(ticket[4], 'ddd')
```

## Method `search_tickets_by_customer`

### Docstring

```python
def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> result = ticket_db.search_tickets_by_customer("John Doe")
        len(result) = 1
        """
```

### Reference code (`solution_code`)

```python
def search_tickets_by_customer(self, customer_name):
        self.cursor.execute('''
            SELECT * FROM tickets WHERE customer_name = ?
        ''', (customer_name,))
        tickets = self.cursor.fetchall()
        return tickets
```

### Tests (`MovieTicketDBTestDeleteTicket`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = 'test_database.db'
    self.db = MovieTicketDB(self.db_name)
```

**test_delete_ticket_1**: `other_inconsistency`
- reason: The test is named `test_delete_ticket_1` and exercises `delete_ticket`, while it is filed under `search_tickets_by_customer`, so its main purpose is not the method this docstring describes.

```python
def test_delete_ticket_1(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'John Doe')
    tickets = self.db.search_tickets_by_customer('John Doe')
    self.assertEqual(len(tickets), 1)
    ticket_id = tickets[0][0]
    self.db.delete_ticket(ticket_id)
    tickets = self.db.search_tickets_by_customer('John Doe')
    self.assertEqual(len(tickets), 0)
```

**test_delete_ticket_2**: `stated`
- reason: The docstring says the method returns the rows from "tickets" whose customer name matches, and the test checks exactly that: one match before deletion and none after, which follows from the same rule once the row is gone.

```python
def test_delete_ticket_2(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'aaa')
    tickets = self.db.search_tickets_by_customer('aaa')
    self.assertEqual(len(tickets), 1)
    ticket_id = tickets[0][0]
    self.db.delete_ticket(ticket_id)
    tickets = self.db.search_tickets_by_customer('aaa')
    self.assertEqual(len(tickets), 0)
```

**test_delete_ticket_3**: `unstated`
- reason: The test depends on the first column of each returned row being the ticket id, which the docstring never says. It only says the method returns the matching rows from the "tickets" table.
- missing: The docstring should state the column layout of each returned row, including which field comes first and that it is the unique ticket id, so callers can rely on it.

```python
def test_delete_ticket_3(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'bbb')
    tickets = self.db.search_tickets_by_customer('bbb')
    self.assertEqual(len(tickets), 1)
    ticket_id = tickets[0][0]
    self.db.delete_ticket(ticket_id)
    tickets = self.db.search_tickets_by_customer('bbb')
    self.assertEqual(len(tickets), 0)
```

**test_delete_ticket_4**: `other_inconsistency`
- reason: The test is named `test_delete_ticket_4` and its core check is that `delete_ticket` removes a row, yet it is filed under `search_tickets_by_customer`, whose docstring says nothing about deletion.

```python
def test_delete_ticket_4(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'ccc')
    tickets = self.db.search_tickets_by_customer('ccc')
    self.assertEqual(len(tickets), 1)
    ticket_id = tickets[0][0]
    self.db.delete_ticket(ticket_id)
    tickets = self.db.search_tickets_by_customer('ccc')
    self.assertEqual(len(tickets), 0)
```

**test_delete_ticket_5**: `unstated`
- reason: The docstring says the method returns matching rows, but it does not say that each row's first column is the record's id, which the test depends on to call delete_ticket.
- missing: The docstring should state the column layout of the returned rows, including that the first column is the record's unique identifier, so callers can use it to address that record.

```python
def test_delete_ticket_5(self):
    self.db.insert_ticket('Avengers: Endgame', 'Cinema 1', 'A1', 'ddd')
    tickets = self.db.search_tickets_by_customer('ddd')
    self.assertEqual(len(tickets), 1)
    ticket_id = tickets[0][0]
    self.db.delete_ticket(ticket_id)
    tickets = self.db.search_tickets_by_customer('ddd')
    self.assertEqual(len(tickets), 0)
```

## Method `delete_ticket`

### Docstring

```python
def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to delete.
        :return: None
        """
```

### Reference code (`solution_code`)

```python
def delete_ticket(self, ticket_id):
        self.cursor.execute('''
            DELETE FROM tickets WHERE id = ?
        ''', (ticket_id,))
        self.connection.commit()
```

### Tests (`MovieTicketDBTest`)

setUp (runs before each test):

```python
def setUp(self):
    self.db_name = 'test_database.db'
    self.db = MovieTicketDB(self.db_name)
```

**test_MovieTicketDB**: `stated`
- reason: The docstring says delete_ticket removes the ticket with the given ID from the "tickets" table, which is exactly what the test checks by deleting a ticket and confirming the customer's search returns nothing.

```python
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
```
