import unittest



class AssessmentSystemTestAddStudent(unittest.TestCase):
    def test_add_student(self):
        assessment_system = AssessmentSystem()
        assessment_system.add_student("Alice", 3, "Mathematics")
        self.assertEqual(assessment_system.students["Alice"],
                         {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}})

    def test_add_student_2(self):
        assessment_system = AssessmentSystem()
        assessment_system.add_student("Alice", 3, "Mathematics")
        assessment_system.add_student("Bob", 2, "Science")
        self.assertEqual(assessment_system.students,
                         {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}},
                          'Bob': {'name': 'Bob', 'grade': 2, 'major': 'Science', 'courses': {}}})

    def test_add_student_3(self):
        assessment_system = AssessmentSystem()
        assessment_system.add_student("Alice", 3, "Mathematics")
        assessment_system.add_student("Bob", 2, "Science")
        assessment_system.add_student("Charlie", 4, "Chemistry")
        self.assertEqual(assessment_system.students,
                         {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}},
                          'Bob': {'name': 'Bob', 'grade': 2, 'major': 'Science', 'courses': {}},
                          'Charlie': {'name': 'Charlie', 'grade': 4, 'major': 'Chemistry', 'courses': {}}})

import unittest

class AgentTest_add_student(unittest.TestCase):
    def test_add_student_1(self):
        # Docstring example: add_student('student 1', 3, 'SE')
        assessment_system = AssessmentSystem()
        assessment_system.add_student('student 1', 3, 'SE')
        self.assertEqual(assessment_system.students,
                         {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {}}})

    def test_add_student_2(self):
        # Adding another student must not change an already stored student's record
        assessment_system = AssessmentSystem()
        assessment_system.add_student('Alice', 3, 'Mathematics')
        first_record = dict(assessment_system.students['Alice'])
        assessment_system.add_student('Bob', 1, 'Physics')
        self.assertEqual(assessment_system.students['Alice'], first_record)
        self.assertEqual(assessment_system.students['Alice'],
                         {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}})

class AssessmentSystemTestAddCourseScore(unittest.TestCase):
    def test_add_course_score(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {"Alice": {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}}
        assessment_system.add_course_score("Alice", "Math", 90)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Math"], 90)

    def test_add_course_score_2(self):
        assessment_system = AssessmentSystem()
        assessment_system.students["Alice"] = {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}
        assessment_system.add_course_score("Alice", "Math", 90)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Math"], 90)

    def test_add_course_score_3(self):
        assessment_system = AssessmentSystem()
        assessment_system.students["Alice"] = {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}
        assessment_system.add_course_score("Alice", "Math", 90)
        assessment_system.add_course_score("Alice", "Science", 80)
        assessment_system.add_course_score("Alice", "Math", 95)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Math"], 95)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Science"], 80)

import unittest

class AgentTest_add_course_score(unittest.TestCase):
    def test_add_course_score_1(self):
        # Adding a score for one student must leave other students' records untouched
        # and must not change the target student's name, grade or major.
        assessment_system = AssessmentSystem()
        assessment_system.add_student('Alice', 3, 'Mathematics')
        assessment_system.add_student('Bob', 2, 'Science')
        assessment_system.add_course_score('Alice', 'Math', 90)
        self.assertEqual(assessment_system.students['Bob'],
                         {'name': 'Bob', 'grade': 2, 'major': 'Science', 'courses': {}})
        self.assertEqual(assessment_system.students['Alice']['name'], 'Alice')
        self.assertEqual(assessment_system.students['Alice']['grade'], 3)
        self.assertEqual(assessment_system.students['Alice']['major'], 'Mathematics')

    def test_add_course_score_2(self):
        # Docstring-style example: student added with add_student, then a multi-word course is scored.
        assessment_system = AssessmentSystem()
        assessment_system.add_student('student 1', 3, 'SE')
        assessment_system.add_course_score('student 1', 'Computer Network', 92)
        self.assertEqual(assessment_system.students,
                         {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE',
                                        'courses': {'Computer Network': 92}}})

class AssessmentSystemTestGetGPA(unittest.TestCase):
    def test_get_gpa_1(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90, 'Science': 80}}}
        self.assertEqual(assessment_system.get_gpa("Alice"), 85.0)

    def test_get_gpa_2(self):
        assessment_system = AssessmentSystem()
        self.assertEqual(assessment_system.get_gpa('Alice'), None)

    def test_get_gpa_3(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}}
        self.assertEqual(assessment_system.get_gpa('Alice'), None)

import unittest

class AgentTest_get_gpa(unittest.TestCase):
    def test_get_gpa_1(self):
        # Docstring example: average of two courses added through the public API
        assessment_system = AssessmentSystem()
        assessment_system.add_student('student 1', 3, 'SE')
        assessment_system.add_course_score('student 1', 'math', 94)
        assessment_system.add_course_score('student 1', 'Computer Network', 92)
        gpa = assessment_system.get_gpa('student 1')
        self.assertIsInstance(gpa, float)
        self.assertEqual(gpa, 93.0)

    def test_get_gpa_2(self):
        # Average over three courses with a non-integer result
        assessment_system = AssessmentSystem()
        assessment_system.add_student('Alice', 3, 'Mathematics')
        assessment_system.add_course_score('Alice', 'Math', 90)
        assessment_system.add_course_score('Alice', 'Science', 80)
        assessment_system.add_course_score('Alice', 'History', 75)
        self.assertAlmostEqual(assessment_system.get_gpa('Alice'), 245 / 3)

class AssessmentSystemTestGetAllStudentsWithFailCourse(unittest.TestCase):
    def test_get_all_students_with_fail_course(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90, 'Science': 80}},
                                'Bob': {'name': 'Bob', 'grade': 4, 'major': 'Physics', 'courses': {'Physics': 50}},
                                'Charlie': {'name': 'Charlie', 'grade': 2, 'major': 'Chemistry', 'courses': {'Chemistry': 70}},
                                'David': {'name': 'David', 'grade': 1, 'major': 'Physics', 'courses': {'Physics': 60}},
                                'Eve': {'name': 'Eve', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90}}}
        self.assertEqual(assessment_system.get_all_students_with_fail_course(), ['Bob'])

    def test_get_all_students_with_fail_course_2(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90, 'Science': 80}},
                                'Bob': {'name': 'Bob', 'grade': 4, 'major': 'Physics', 'courses': {'Physics': 70}},
                                'Charlie': {'name': 'Charlie', 'grade': 2, 'major': 'Chemistry', 'courses': {'Chemistry': 70}},
                                'David': {'name': 'David', 'grade': 1, 'major': 'Physics', 'courses': {'Physics': 70}},
                                'Eve': {'name': 'Eve', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90}}}
        self.assertEqual(assessment_system.get_all_students_with_fail_course(), [])

    def test_get_all_students_with_fail_course_3(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {}
        self.assertEqual(assessment_system.get_all_students_with_fail_course(), [])

import unittest

class AgentTest_get_all_students_with_fail_course(unittest.TestCase):
    def test_get_all_students_with_fail_course_1(self):
        # Docstring example through the public API: a single score of 59 is a failing score.
        assessment_system = AssessmentSystem()
        assessment_system.add_student('student 1', 3, 'SE')
        assessment_system.add_course_score('student 1', 'Society', 59)
        self.assertEqual(assessment_system.get_all_students_with_fail_course(), ['student 1'])

    def test_get_all_students_with_fail_course_2(self):
        # A student with several failing courses is listed once; a score of exactly 60
        # is not below 60, so that student is not listed.
        assessment_system = AssessmentSystem()
        assessment_system.add_student('Alice', 3, 'Mathematics')
        assessment_system.add_course_score('Alice', 'Math', 10)
        assessment_system.add_course_score('Alice', 'Science', 59)
        assessment_system.add_student('Bob', 2, 'Science')
        assessment_system.add_course_score('Bob', 'Math', 60)
        assessment_system.add_course_score('Bob', 'Science', 95)
        result = assessment_system.get_all_students_with_fail_course()
        self.assertCountEqual(result, ['Alice'])
        self.assertEqual(len(result), 1)

class AssessmentSystemTestGetCourseAverage(unittest.TestCase):

    def test_get_course_average_1(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90, 'Science': 80}},
                                'Bob': {'name': 'Bob', 'grade': 4, 'major': 'Physics', 'courses': {'Physics': 90}},
                                'Charlie': {'name': 'Charlie', 'grade': 2, 'major': 'Chemistry', 'courses': {'Chemistry': 70,'Physics': 80}}
                                           }
        self.assertEqual(assessment_system.get_course_average("Physics"), 85.0)

    def test_get_course_average_2(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics',
                                                'courses': {'Mathematics': 90, 'Science': 80}},
                                      'Bob': {'name': 'Bob', 'grade': 4, 'major': 'Physics',
                                              'courses': {'Physics': 85}},
                                      'Charlie': {'name': 'Charlie', 'grade': 2, 'major': 'Chemistry',
                                                  'courses': {'Chemistry': 70,'Physics': None }}
                                      }
        self.assertEqual(assessment_system.get_course_average('Physics'), 85)

    def test_get_course_average_3(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics',
                                                'courses': {'Mathematics': 90, 'Science': 80}},
                                      'Bob': {'name': 'Bob', 'grade': 4, 'major': 'Physics',
                                              'courses': {'Physics': 85}},
                                      'Charlie': {'name': 'Charlie', 'grade': 2, 'major': 'Chemistry',
                                                  'courses': {'Chemistry': 70, 'Physics': 80}}
                                      }
        self.assertEqual(assessment_system.get_course_average('Computer'), None)

import unittest

class AgentTest_get_course_average(unittest.TestCase):
    def test_get_course_average_1(self):
        # Nobody in the system has any records at all, so there is no average to report.
        assessment_system = AssessmentSystem()
        self.assertEqual(assessment_system.get_course_average('Physics'), None)

    def test_get_course_average_2(self):
        # Scores added through the public API for several students; the average of
        # 90, 91 and 70 is a non-integer float.
        assessment_system = AssessmentSystem()
        assessment_system.add_student('Alice', 3, 'Mathematics')
        assessment_system.add_student('Bob', 2, 'Science')
        assessment_system.add_student('Charlie', 4, 'Chemistry')
        assessment_system.add_course_score('Alice', 'Math', 90)
        assessment_system.add_course_score('Bob', 'Math', 91)
        assessment_system.add_course_score('Charlie', 'Math', 70)
        average = assessment_system.get_course_average('Math')
        self.assertIsInstance(average, float)
        self.assertAlmostEqual(average, 251 / 3)

class AssessmentSystemTestGetTopStudent(unittest.TestCase):
    def test_get_top_student(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics',
                                                'courses': {'Mathematics': 90}},
                                      'Bob': {'name': 'Bob', 'grade': 4, 'major': 'Physics',
                                              'courses': {'Physics': 85}}
                                      }
        self.assertEqual(assessment_system.get_top_student(), "Alice")

    def test_get_top_student_2(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics',
                                                'courses': { }},
                                      'Bob': {'name': 'Bob', 'grade': 4, 'major': 'Physics',
                                              'courses': {'Physics': 85}},
                                      'Charlie': {'name': 'Charlie', 'grade': 2, 'major': 'Chemistry',
                                                  'courses': {'Chemistry': 70, 'Physics': 80}}
                                      }
        self.assertEqual(assessment_system.get_top_student(), "Bob")

    def test_get_top_student_3(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {}
        self.assertEqual(assessment_system.get_top_student(), None)

import unittest

class AgentTest_get_top_student(unittest.TestCase):
    def test_get_top_student_1(self):
        # The top student is chosen by average course score (get_gpa), not by the highest
        # single score. 'student 1' has a higher best score (95) but a lower average
        # (77.5) than 'student 2' (80.0).
        assessment_system = AssessmentSystem()
        assessment_system.add_student('student 1', 3, 'SE')
        assessment_system.add_student('student 2', 2, 'SE')
        assessment_system.add_course_score('student 1', 'math', 95)
        assessment_system.add_course_score('student 1', 'Society', 60)
        assessment_system.add_course_score('student 2', 'math', 80)
        self.assertEqual(assessment_system.get_top_student(), 'student 2')

    def test_get_top_student_2(self):
        # When only one student has any course scores, that student is the top student,
        # even though another student was added earlier with no courses.
        assessment_system = AssessmentSystem()
        assessment_system.add_student('Alice', 3, 'Mathematics')
        assessment_system.add_student('Bob', 2, 'Science')
        assessment_system.add_course_score('Bob', 'Physics', 55)
        self.assertEqual(assessment_system.get_top_student(), 'Bob')