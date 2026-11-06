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

    @staticmethod
    def _quote(identifier):
        return '"' + str(identifier).replace('"', '""') + '"'

    def _name_column(self, cursor, table_name):
        """Return the name of the second column (key1), which holds the name value."""
        cursor.execute(f"PRAGMA table_info({self._quote(table_name)})")
        columns = cursor.fetchall()
        if len(columns) < 2:
            raise ValueError(f"Table '{table_name}' does not have the expected columns.")
        return columns[1][1]

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
            cursor = conn.cursor()
            query = (
                f"CREATE TABLE IF NOT EXISTS {self._quote(table_name)} ("
                f"id INTEGER PRIMARY KEY, "
                f"{self._quote(key1)} TEXT, "
                f"{self._quote(key2)} INTEGER)"
            )
            cursor.execute(query)
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
            cursor = conn.cursor()
            for row in data:
                columns = list(row.keys())
                cols_sql = ", ".join(self._quote(c) for c in columns)
                placeholders = ", ".join("?" for _ in columns)
                query = (
                    f"INSERT INTO {self._quote(table_name)} ({cols_sql}) "
                    f"VALUES ({placeholders})"
                )
                cursor.execute(query, tuple(row[c] for c in columns))
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
            cursor = conn.cursor()
            name_col = self._name_column(cursor, table_name)
            query = (
                f"SELECT * FROM {self._quote(table_name)} "
                f"WHERE {self._quote(name_col)} = ?"
            )
            cursor.execute(query, (name,))
            rows = cursor.fetchall()
            return rows if rows else None
        finally:
            conn.close()

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
        conn = sqlite3.connect(self.database_name)
        try:
            cursor = conn.cursor()
            name_col = self._name_column(cursor, table_name)
            query = (
                f"DELETE FROM {self._quote(table_name)} "
                f"WHERE {self._quote(name_col)} = ?"
            )
            cursor.execute(query, (name,))
            conn.commit()
        finally:
            conn.close()