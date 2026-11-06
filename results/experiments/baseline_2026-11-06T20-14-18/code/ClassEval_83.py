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
        conn = sqlite3.connect(self.database_name)
        try:
            with conn:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS students (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        age INTEGER,
                        gender TEXT,
                        grade INTEGER
                    )
                    """
                )
        finally:
            conn.close()

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
        conn = sqlite3.connect(self.database_name)
        try:
            with conn:
                conn.execute(
                    "INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)",
                    (
                        student_data.get('name'),
                        student_data.get('age'),
                        student_data.get('gender'),
                        student_data.get('grade'),
                    ),
                )
        finally:
            conn.close()

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.search_student_by_name("John")
        """
        conn = sqlite3.connect(self.database_name)
        try:
            cursor = conn.execute(
                "SELECT * FROM students WHERE name = ?", (name,)
            )
            return cursor.fetchall()
        finally:
            conn.close()

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
        conn = sqlite3.connect(self.database_name)
        try:
            with conn:
                conn.execute("DELETE FROM students WHERE name = ?", (name,))
        finally:
            conn.close()