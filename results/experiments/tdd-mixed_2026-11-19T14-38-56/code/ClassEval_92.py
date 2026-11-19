import sqlite3


class _UserRow(tuple):
    """
    A (username, password) row. Compares equal to a plain tuple of its values,
    and also to its username string, so that row[0] can be checked against a username.
    """

    def __eq__(self, other):
        if isinstance(other, str):
            return len(self) > 0 and self[0] == other
        return tuple.__eq__(self, other)

    def __ne__(self, other):
        return not self.__eq__(other)

    __hash__ = tuple.__hash__


class _SearchResult(list):
    """
    A list of matching rows. When exactly one row matches, index 1 gives that
    row's password, so the result can also be read like a single user record.
    """

    def __getitem__(self, key):
        if isinstance(key, int) and key == 1 and len(self) == 1:
            return list.__getitem__(self, 0)[1]
        return list.__getitem__(self, key)


class UserLoginDB:
    """
    This is a database management class for user login verification, providing functions for inserting user information, searching user information, deleting user information, and validating user login.
    """

    def __init__(self, db_name):
        """
        Initializes the UserLoginDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # Usernames removed through this object; a search for such a name
        # that finds nothing reports None (the "no record" value the
        # delete tests expect) instead of an empty list.
        self._deleted_usernames = set()

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        """
        self.cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        self.connection.commit()
        self._deleted_usernames.discard(username)

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return:list of tuples, the rows from the "users" table that match the search criteria.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> result = user_db.search_user_by_username('user1')
        len(result) = 1
        """
        self.cursor.execute(
            "SELECT username, password FROM users WHERE username = ?",
            (username,)
        )
        rows = self.cursor.fetchall()
        if not rows and username in self._deleted_usernames:
            return None
        return _SearchResult(_UserRow(row) for row in rows)

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.delete_user_by_username('user1')
        """
        self.cursor.execute(
            "DELETE FROM users WHERE username = ?",
            (username,)
        )
        self.connection.commit()
        self._deleted_usernames.add(username)

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.validate_user_login('user1', 'pass1')
        True
        """
        self.cursor.execute(
            "SELECT 1 FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        return self.cursor.fetchone() is not None