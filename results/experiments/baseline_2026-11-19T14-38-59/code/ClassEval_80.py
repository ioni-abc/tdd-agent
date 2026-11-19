class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements.
    """

    @staticmethod
    def _format_value(value):
        return "'{}'".format(value)

    @staticmethod
    def _build_conditions(where, joiner=" AND "):
        return joiner.join(
            "{}={}".format(key, SQLQueryBuilder._format_value(value))
            for key, value in where.items()
        )

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
        if isinstance(columns, (list, tuple)):
            cols = ", ".join(columns)
        else:
            cols = columns
        query = "SELECT {} FROM {}".format(cols, table)
        if where:
            query += " WHERE " + SQLQueryBuilder._build_conditions(where)
        return query

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
        """
        columns = ", ".join(data.keys())
        values = ", ".join(SQLQueryBuilder._format_value(v) for v in data.values())
        return "INSERT INTO {} ({}) VALUES ({})".format(table, columns, values)

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
        query = "DELETE FROM {}".format(table)
        if where:
            query += " WHERE " + SQLQueryBuilder._build_conditions(where)
        return query

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
        assignments = SQLQueryBuilder._build_conditions(data, joiner=", ")
        query = "UPDATE {} SET {}".format(table, assignments)
        if where:
            query += " WHERE " + SQLQueryBuilder._build_conditions(where)
        return query