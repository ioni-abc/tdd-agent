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
        conn = sqlite3.connect(self.database_name)
        try:
            conn.execute(
                f'CREATE TABLE IF NOT EXISTS "{table_name}" ('
                f'"id" INTEGER PRIMARY KEY, '
                f'"{key1}" TEXT, '
                f'"{key2}" INTEGER)'
            )
            conn.commit()
        finally:
            conn.close()


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
        if not data:
            return
        conn = sqlite3.connect(self.database_name)
        try:
            for row in data:
                columns = list(row.keys())
                column_sql = ', '.join(f'"{col}"' for col in columns)
                placeholders = ', '.join('?' for _ in columns)
                values = [row[col] for col in columns]
                conn.execute(
                    f'INSERT INTO "{table_name}" ({column_sql}) VALUES ({placeholders})',
                    values
                )
            conn.commit()
        finally:
            conn.close()


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
        conn = sqlite3.connect(self.database_name)
        try:
            info = conn.execute(f'PRAGMA table_info("{table_name}")').fetchall()
            # Column index 1 is the first user-defined column (key1), after 'id'.
            name_column = info[1][1]
            cursor = conn.execute(
                f'SELECT * FROM "{table_name}" WHERE "{name_column}" = ? ORDER BY id',
                (name,)
            )
            rows = cursor.fetchall()
        finally:
            conn.close()
        return rows if rows else None


    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
        conn = sqlite3.connect(self.database_name)
        try:
            info = conn.execute(f'PRAGMA table_info("{table_name}")').fetchall()
            if len(info) < 2:
                return
            # Column index 1 is the first user-defined column (key1), after 'id'.
            name_column = info[1][1]
            conn.execute(
                f'DELETE FROM "{table_name}" WHERE "{name_column}" = ?',
                (name,)
            )
            conn.commit()
        finally:
            conn.close()