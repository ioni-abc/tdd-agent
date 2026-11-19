import unittest


import unittest

from datetime import datetime

class AgentTest_add_course(unittest.TestCase):

    def test_add_course_1(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        classroom.add_course(course)
        self.assertIn(course, classroom.courses)

    def test_add_course_2(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        classroom.add_course(course)
        classroom.add_course(course)
        self.assertEqual(len(classroom.courses), 1)
        self.assertEqual(classroom.courses, [course])

    def test_add_course_3(self):
        classroom = Classroom(1)
        math = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        se = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'}
        classroom.add_course(math)
        classroom.add_course(se)
        self.assertEqual(len(classroom.courses), 2)
        self.assertIn(math, classroom.courses)
        self.assertIn(se, classroom.courses)

    def test_add_course_4(self):
        classroom = Classroom(1)
        self.assertEqual(classroom.courses, [])
        course = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        classroom.add_course(course)
        self.assertEqual(classroom.courses, [course])
        self.assertEqual(classroom.courses[0]['name'], 'math')
        self.assertEqual(classroom.courses[0]['start_time'], '8:00')
        self.assertEqual(classroom.courses[0]['end_time'], '9:40')

    def test_add_course_5(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        self.assertFalse(classroom.is_free_at('9:00'))
        self.assertTrue(classroom.is_free_at('10:00'))

import unittest

class AgentTest_remove_course(unittest.TestCase):

    def test_remove_course_1(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)
        self.assertEqual(classroom.courses, [])

    def test_remove_course_2(self):
        classroom = Classroom(1)
        math = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        se = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'}
        classroom.add_course(math)
        classroom.add_course(se)
        classroom.remove_course(math)
        self.assertEqual(len(classroom.courses), 1)
        self.assertNotIn(math, classroom.courses)
        self.assertIn(se, classroom.courses)

    def test_remove_course_3(self):
        classroom = Classroom(1)
        math = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        se = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'}
        classroom.add_course(math)
        classroom.remove_course(se)
        self.assertEqual(classroom.courses, [math])

    def test_remove_course_4(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        classroom.remove_course(course)
        self.assertEqual(classroom.courses, [])

    def test_remove_course_5(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        classroom.add_course(course)
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertEqual(classroom.courses, [])
        self.assertTrue(classroom.is_free_at('9:00'))

import unittest

from datetime import datetime

class AgentTest_is_free_at(unittest.TestCase):

    def test_is_free_at_1(self):
        classroom = Classroom(1)
        self.assertTrue(classroom.is_free_at('9:00'))

    def test_is_free_at_2(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        self.assertFalse(classroom.is_free_at('9:00'))

    def test_is_free_at_3(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        self.assertTrue(classroom.is_free_at('10:00'))

    def test_is_free_at_4(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        self.assertTrue(classroom.is_free_at('7:00'))

    def test_is_free_at_5(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        classroom.add_course({'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'})
        self.assertFalse(classroom.is_free_at('11:00'))
        self.assertTrue(classroom.is_free_at('12:00'))
        self.assertTrue(classroom.is_free_at('7:00'))

import unittest

from datetime import datetime

class AgentTest_check_course_conflict(unittest.TestCase):

    def test_check_course_conflict_1(self):
        classroom = Classroom(1)
        new_course = {'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'}
        self.assertTrue(classroom.check_course_conflict(new_course))

    def test_check_course_conflict_2(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        new_course = {'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'}
        self.assertFalse(classroom.check_course_conflict(new_course))

    def test_check_course_conflict_3(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        new_course = {'name': 'SE', 'start_time': '9:00', 'end_time': '10:00'}
        self.assertFalse(classroom.check_course_conflict(new_course))

    def test_check_course_conflict_4(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        new_course = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:00'}
        self.assertTrue(classroom.check_course_conflict(new_course))
        new_course_before = {'name': 'English', 'start_time': '6:00', 'end_time': '7:30'}
        self.assertTrue(classroom.check_course_conflict(new_course_before))

    def test_check_course_conflict_5(self):
        classroom = Classroom(1)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        classroom.add_course({'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'})
        new_course = {'name': 'AI', 'start_time': '11:00', 'end_time': '12:00'}
        self.assertFalse(classroom.check_course_conflict(new_course))