import unittest


import unittest

class AgentTest_add_student(unittest.TestCase):

    def setUp(self):
        self.system = AssessmentSystem()

    def test_add_student_1(self):
        self.system.add_student('student 1', 3, 'SE')
        self.assertEqual(
            self.system.students,
            {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {}}}
        )

    def test_add_student_2(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.assertIn('student 1', self.system.students)
        self.assertIn('student 2', self.system.students)
        self.assertEqual(len(self.system.students), 2)
        self.assertEqual(self.system.students['student 2']['name'], 'student 2')
        self.assertEqual(self.system.students['student 2']['grade'], 2)
        self.assertEqual(self.system.students['student 2']['major'], 'SE')

    def test_add_student_3(self):
        self.system.add_student('student 1', 3, 'SE')
        self.assertEqual(self.system.students['student 1']['courses'], {})

    def test_add_student_4(self):
        self.system.add_student('student 1', 3, 'SE')
        before = {
            'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {}}
        }
        self.system.add_student('student 2', 1, 'CS')
        self.assertEqual(self.system.students['student 1'], before['student 1'])
        self.assertEqual(
            self.system.students['student 2'],
            {'name': 'student 2', 'grade': 1, 'major': 'CS', 'courses': {}}
        )

    def test_add_student_5(self):
        self.assertEqual(self.system.students, {})
        self.system.add_student('Alice', 4, 'Math')
        student = self.system.students['Alice']
        self.assertEqual(student['name'], 'Alice')
        self.assertEqual(student['grade'], 4)
        self.assertEqual(student['major'], 'Math')
        self.assertEqual(set(student.keys()), {'name', 'grade', 'major', 'courses'})

import unittest

class AgentTest_add_course_score(unittest.TestCase):

    def setUp(self):
        self.system = AssessmentSystem()

    def test_add_course_score_1(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        self.assertEqual(
            self.system.students,
            {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {'math': 94}}}
        )

    def test_add_course_score_2(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        self.system.add_course_score('student 1', 'Computer Network', 92)
        self.assertEqual(
            self.system.students['student 1']['courses'],
            {'math': 94, 'Computer Network': 92}
        )

    def test_add_course_score_3(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        self.assertEqual(self.system.students['student 2']['courses'], {})
        self.assertEqual(self.system.students['student 1']['courses'], {'math': 94})

    def test_add_course_score_4(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'Society', 59)
        self.assertEqual(self.system.students['student 1']['courses']['Society'], 59)

    def test_add_course_score_5(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        student = self.system.students['student 1']
        self.assertEqual(student['name'], 'student 1')
        self.assertEqual(student['grade'], 3)
        self.assertEqual(student['major'], 'SE')
        self.assertEqual(set(student.keys()), {'name', 'grade', 'major', 'courses'})

import unittest

class AgentTest_get_gpa(unittest.TestCase):

    def setUp(self):
        self.system = AssessmentSystem()

    def test_get_gpa_1(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        self.system.add_course_score('student 1', 'Computer Network', 92)
        self.assertEqual(self.system.get_gpa('student 1'), 93.0)

    def test_get_gpa_2(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        self.assertIsNone(self.system.get_gpa('student 2'))

    def test_get_gpa_3(self):
        self.system.add_student('student 1', 3, 'SE')
        self.assertIsNone(self.system.get_gpa('student 1'))

    def test_get_gpa_4(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        gpa = self.system.get_gpa('student 1')
        self.assertIsInstance(gpa, float)
        self.assertEqual(gpa, 94.0)

    def test_get_gpa_5(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_course_score('student 1', 'math', 90)
        self.system.add_course_score('student 1', 'Computer Network', 80)
        self.system.add_course_score('student 1', 'Society', 70)
        self.system.add_course_score('student 2', 'math', 10)
        self.assertEqual(self.system.get_gpa('student 1'), 80.0)

import unittest

class AgentTest_get_all_students_with_fail_course(unittest.TestCase):

    def setUp(self):
        self.system = AssessmentSystem()

    def test_get_all_students_with_fail_course_1(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'Society', 59)
        self.assertEqual(self.system.get_all_students_with_fail_course(), ['student 1'])

    def test_get_all_students_with_fail_course_2(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        self.system.add_course_score('student 1', 'Computer Network', 92)
        self.assertEqual(self.system.get_all_students_with_fail_course(), [])

    def test_get_all_students_with_fail_course_3(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'Society', 60)
        self.assertEqual(self.system.get_all_students_with_fail_course(), [])

    def test_get_all_students_with_fail_course_4(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_student('student 3', 1, 'CS')
        self.system.add_course_score('student 1', 'math', 94)
        self.system.add_course_score('student 1', 'Society', 55)
        self.system.add_course_score('student 2', 'math', 80)
        self.system.add_course_score('student 3', 'math', 45)
        self.system.add_course_score('student 3', 'Computer Network', 99)
        self.assertCountEqual(
            self.system.get_all_students_with_fail_course(),
            ['student 1', 'student 3']
        )

    def test_get_all_students_with_fail_course_5(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 30)
        self.system.add_course_score('student 1', 'Society', 40)
        self.system.add_course_score('student 1', 'Computer Network', 90)
        self.assertEqual(self.system.get_all_students_with_fail_course(), ['student 1'])

import unittest

class AgentTest_get_course_average(unittest.TestCase):

    def setUp(self):
        self.system = AssessmentSystem()

    def test_get_course_average_1(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        avg = self.system.get_course_average('math')
        self.assertIsInstance(avg, float)
        self.assertEqual(avg, 94.0)

    def test_get_course_average_2(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_course_score('student 1', 'math', 90)
        self.system.add_course_score('student 2', 'math', 80)
        self.assertEqual(self.system.get_course_average('math'), 85.0)

    def test_get_course_average_3(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 94)
        self.assertIsNone(self.system.get_course_average('Society'))

    def test_get_course_average_4(self):
        self.assertIsNone(self.system.get_course_average('math'))

    def test_get_course_average_5(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_student('student 3', 1, 'CS')
        self.system.add_course_score('student 1', 'math', 90)
        self.system.add_course_score('student 1', 'Society', 10)
        self.system.add_course_score('student 2', 'math', 70)
        self.assertEqual(self.system.get_course_average('math'), 80.0)

import unittest

class AgentTest_get_top_student(unittest.TestCase):

    def setUp(self):
        self.system = AssessmentSystem()

    def test_get_top_student_1(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_course_score('student 1', 'Computer Network', 92)
        self.system.add_course_score('student 2', 'Computer Network', 97)
        self.assertEqual(self.system.get_top_student(), 'student 2')

    def test_get_top_student_2(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_course_score('student 1', 'math', 90)
        self.system.add_course_score('student 1', 'Society', 90)
        self.system.add_course_score('student 2', 'math', 95)
        self.assertEqual(self.system.get_top_student(), 'student 2')

    def test_get_top_student_3(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_course_score('student 1', 'math', 75)
        self.assertEqual(self.system.get_top_student(), 'student 1')

    def test_get_top_student_4(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_student('student 3', 1, 'CS')
        self.system.add_course_score('student 1', 'math', 98)
        self.system.add_course_score('student 2', 'math', 85)
        self.system.add_course_score('student 3', 'math', 70)
        self.assertEqual(self.system.get_top_student(), 'student 1')

    def test_get_top_student_5(self):
        self.system.add_student('student 1', 3, 'SE')
        self.system.add_student('student 2', 2, 'SE')
        self.system.add_student('student 3', 1, 'CS')
        self.system.add_course_score('student 1', 'math', 60)
        self.system.add_course_score('student 1', 'Society', 70)
        self.system.add_course_score('student 2', 'math', 88)
        self.system.add_course_score('student 2', 'Society', 92)
        self.system.add_course_score('student 3', 'math', 80)
        top = self.system.get_top_student()
        self.assertIsInstance(top, str)
        self.assertEqual(top, 'student 2')