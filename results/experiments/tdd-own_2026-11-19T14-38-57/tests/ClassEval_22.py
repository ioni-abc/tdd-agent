import unittest


import unittest

class AgentTest_register_student(unittest.TestCase):

    def test_register_student_1(self):
        registration_system = ClassRegistrationSystem()
        student1 = {"name": "John", "major": "Computer Science"}
        result = registration_system.register_student(student1)
        self.assertEqual(result, 1)

    def test_register_student_2(self):
        registration_system = ClassRegistrationSystem()
        student1 = {"name": "John", "major": "Computer Science"}
        registration_system.register_student(student1)
        self.assertIn(student1, registration_system.students)
        self.assertEqual(len(registration_system.students), 1)

    def test_register_student_3(self):
        registration_system = ClassRegistrationSystem()
        student1 = {"name": "John", "major": "Computer Science"}
        registration_system.register_student(student1)
        result = registration_system.register_student(student1)
        self.assertEqual(result, 0)

    def test_register_student_4(self):
        registration_system = ClassRegistrationSystem()
        student1 = {"name": "John", "major": "Computer Science"}
        registration_system.register_student(student1)
        registration_system.register_student(student1)
        self.assertEqual(len(registration_system.students), 1)

    def test_register_student_5(self):
        registration_system = ClassRegistrationSystem()
        student1 = {"name": "John", "major": "Computer Science"}
        student2 = {"name": "Bob", "major": "Mathematics"}
        student3 = {"name": "Alice", "major": "Computer Science"}
        self.assertEqual(registration_system.register_student(student1), 1)
        self.assertEqual(registration_system.register_student(student2), 1)
        self.assertEqual(registration_system.register_student(student3), 1)
        self.assertEqual(len(registration_system.students), 3)
        self.assertIn(student1, registration_system.students)
        self.assertIn(student2, registration_system.students)
        self.assertIn(student3, registration_system.students)

import unittest

class AgentTest_register_class(unittest.TestCase):

    def test_register_class_1(self):
        registration_system = ClassRegistrationSystem()
        result = registration_system.register_class(student_name="John", class_name="CS101")
        self.assertEqual(result, ["CS101"])

    def test_register_class_2(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_class(student_name="John", class_name="CS101")
        result = registration_system.register_class(student_name="John", class_name="CS102")
        self.assertEqual(result, ["CS101", "CS102"])

    def test_register_class_3(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_class(student_name="John", class_name="CS101")
        registration_system.register_class(student_name="John", class_name="CS102")
        self.assertEqual(registration_system.students_registration_classes["John"], ["CS101", "CS102"])

    def test_register_class_4(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_class(student_name="John", class_name="CS101")
        result = registration_system.register_class(student_name="Bob", class_name="CS102")
        self.assertEqual(result, ["CS102"])
        self.assertEqual(registration_system.students_registration_classes["John"], ["CS101"])
        self.assertEqual(registration_system.students_registration_classes["Bob"], ["CS102"])

    def test_register_class_5(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_class(student_name="John", class_name="CS101")
        registration_system.register_class(student_name="John", class_name="CS102")
        result = registration_system.register_class(student_name="John", class_name="Algorithms")
        self.assertEqual(result, ["CS101", "CS102", "Algorithms"])
        self.assertEqual(len(result), 3)

import unittest

class AgentTest_get_students_by_major(unittest.TestCase):

    def test_get_students_by_major_1(self):
        registration_system = ClassRegistrationSystem()
        student1 = {"name": "John", "major": "Computer Science"}
        registration_system.register_student(student1)
        result = registration_system.get_students_by_major("Computer Science")
        self.assertEqual(result, ["John"])

    def test_get_students_by_major_2(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Computer Science"})
        registration_system.register_student({"name": "Alice", "major": "Computer Science"})
        result = registration_system.get_students_by_major("Computer Science")
        self.assertEqual(len(result), 3)
        self.assertCountEqual(result, ["John", "Bob", "Alice"])

    def test_get_students_by_major_3(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Mathematics"})
        registration_system.register_student({"name": "Alice", "major": "Computer Science"})
        result = registration_system.get_students_by_major("Computer Science")
        self.assertCountEqual(result, ["John", "Alice"])
        self.assertNotIn("Bob", result)

    def test_get_students_by_major_4(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Mathematics"})
        result = registration_system.get_students_by_major("Physics")
        self.assertEqual(result, [])

    def test_get_students_by_major_5(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Mathematics"})
        result = registration_system.get_students_by_major("Mathematics")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], str)
        self.assertEqual(result[0], "Bob")

import unittest

class AgentTest_get_all_major(unittest.TestCase):

    def test_get_all_major_1(self):
        registration_system = ClassRegistrationSystem()
        result = registration_system.get_all_major()
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])

    def test_get_all_major_2(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        result = registration_system.get_all_major()
        self.assertEqual(result, ["Computer Science"])

    def test_get_all_major_3(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Mathematics"})
        registration_system.register_student({"name": "Alice", "major": "Physics"})
        result = registration_system.get_all_major()
        self.assertEqual(len(set(result)), 3)
        self.assertCountEqual(set(result), {"Computer Science", "Mathematics", "Physics"})

    def test_get_all_major_4(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Mathematics"})
        result = registration_system.get_all_major()
        self.assertIsInstance(result, list)
        for major in result:
            self.assertIsInstance(major, str)
        self.assertNotIn("John", result)
        self.assertNotIn("Bob", result)

    def test_get_all_major_5(self):
        registration_system = ClassRegistrationSystem()
        registration_system.students = [{"name": "John", "major": "Computer Science"}]
        result = registration_system.get_all_major()
        self.assertEqual(result, ["Computer Science"])

import unittest

class AgentTest_get_most_popular_class_in_major(unittest.TestCase):

    def test_get_most_popular_class_in_major_1(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Computer Science"})
        registration_system.register_student({"name": "Alice", "major": "Computer Science"})
        registration_system.register_class(student_name="John", class_name="Algorithms")
        registration_system.register_class(student_name="John", class_name="Data Structures")
        registration_system.register_class(student_name="Bob", class_name="Data Structures")
        registration_system.register_class(student_name="Bob", class_name="Operating Systems")
        registration_system.register_class(student_name="Alice", class_name="Data Structures")
        result = registration_system.get_most_popular_class_in_major("Computer Science")
        self.assertEqual(result, "Data Structures")

    def test_get_most_popular_class_in_major_2(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Computer Science"})
        registration_system.register_student({"name": "Carl", "major": "Mathematics"})
        registration_system.register_student({"name": "Dana", "major": "Mathematics"})
        registration_system.register_student({"name": "Eve", "major": "Mathematics"})
        registration_system.register_class(student_name="John", class_name="Algorithms")
        registration_system.register_class(student_name="John", class_name="Operating Systems")
        registration_system.register_class(student_name="Bob", class_name="Algorithms")
        registration_system.register_class(student_name="Carl", class_name="Calculus")
        registration_system.register_class(student_name="Dana", class_name="Calculus")
        registration_system.register_class(student_name="Eve", class_name="Calculus")
        result = registration_system.get_most_popular_class_in_major("Computer Science")
        self.assertEqual(result, "Algorithms")

    def test_get_most_popular_class_in_major_3(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Computer Science"})
        registration_system.register_class(student_name="John", class_name="Algorithms")
        registration_system.register_class(student_name="Bob", class_name="Algorithms")
        result = registration_system.get_most_popular_class_in_major("Computer Science")
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Algorithms")

    def test_get_most_popular_class_in_major_4(self):
        registration_system = ClassRegistrationSystem()
        registration_system.register_student({"name": "John", "major": "Computer Science"})
        registration_system.register_student({"name": "Bob", "major": "Computer Science"})
        registration_system.register_student({"name": "Alice", "major": "Computer Science"})
        registration_system.register_class(student_name="John", class_name="AI")
        registration_system.register_class(student_name="John", class_name="Machine Learning")
        registration_system.register_class(student_name="Alice", class_name="Machine Learning")
        result = registration_system.get_most_popular_class_in_major("Computer Science")
        self.assertEqual(result, "Machine Learning")

    def test_get_most_popular_class_in_major_5(self):
        registration_system = ClassRegistrationSystem()
        registration_system.students = [{"name": "John", "major": "Computer Science"},
                                        {"name": "Bob", "major": "Computer Science"},
                                        {"name": "Alice", "major": "Computer Science"}]
        registration_system.students_registration_classes = {
            "John": ["Algorithms", "Data Structures"],
            "Bob": ["Operating Systems", "Data Structures"],
            "Alice": ["Data Structures"]
        }
        result = registration_system.get_most_popular_class_in_major("Computer Science")
        self.assertEqual(result, "Data Structures")