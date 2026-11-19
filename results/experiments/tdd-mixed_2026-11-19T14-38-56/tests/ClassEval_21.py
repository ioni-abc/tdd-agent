import unittest
from datetime import datetime




class ClassroomTestAddCourse(unittest.TestCase):
    def test_add_course_1(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(course)
        self.assertIn(course, classroom.courses)

    def test_add_course_2(self):
        classroom = Classroom(1)
        course = {'name': 'Chinese', 'start_time': '10:00', 'end_time': '11:00'}
        classroom.add_course(course)
        self.assertIn(course, classroom.courses)

    def test_add_course_3(self):
        classroom = Classroom(1)
        course = {'name': 'English', 'start_time': '11:00', 'end_time': '12:00'}
        classroom.add_course(course)
        self.assertIn(course, classroom.courses)

    def test_add_course_4(self):
        classroom = Classroom(1)
        course = {'name': 'Art', 'start_time': '14:00', 'end_time': '15:00'}
        classroom.add_course(course)
        self.assertIn(course, classroom.courses)

import unittest

from datetime import datetime

class AgentTest_add_course(unittest.TestCase):
    def test_add_course_1(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        classroom.add_course(course)
        classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        self.assertEqual(len(classroom.courses), 1)

    def test_add_course_2(self):
        classroom = Classroom(1)
        math = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        se = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'}
        classroom.add_course(math)
        classroom.add_course(se)
        self.assertEqual(len(classroom.courses), 2)
        self.assertIn(math, classroom.courses)
        self.assertIn(se, classroom.courses)

class ClassroomTestRemoveCourse(unittest.TestCase):
    def test_remove_course_1(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

    def test_remove_course_2(self):
        classroom = Classroom(1)
        course = {'name': 'Chinese', 'start_time': '10:00', 'end_time': '11:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

    def test_remove_course_3(self):
        classroom = Classroom(1)
        course = {'name': 'English', 'start_time': '11:00', 'end_time': '12:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

    def test_remove_course_4(self):
        classroom = Classroom(1)
        course = {'name': 'Art', 'start_time': '14:00', 'end_time': '15:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

import unittest

from datetime import datetime

class AgentTest_remove_course(unittest.TestCase):
    def test_remove_course_1(self):
        classroom = Classroom(1)
        math = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        se = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'}
        classroom.add_course(math)
        classroom.add_course(se)
        classroom.remove_course(math)
        self.assertEqual(classroom.courses, [se])

    def test_remove_course_2(self):
        classroom = Classroom(1)
        math = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        se = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'}
        classroom.add_course(math)
        classroom.remove_course(se)
        self.assertEqual(classroom.courses, [math])

class ClassroomTestIsFreeAt(unittest.TestCase):
    def test_is_free_at_1(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(course)
        check_time = '11:00'
        result = classroom.is_free_at(check_time)
        self.assertTrue(result)

    def test_is_free_at_2(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(course)
        check_time = '09:30'
        result = classroom.is_free_at(check_time)
        self.assertFalse(result)

    def test_is_free_at_3(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(course)
        check_time = '12:00'
        result = classroom.is_free_at(check_time)
        self.assertTrue(result)

import unittest

from datetime import datetime

class AgentTest_is_free_at(unittest.TestCase):
    def test_is_free_at_1(self):
        classroom = Classroom(1)
        math = {'name': 'math', 'start_time': '8:00', 'end_time': '9:40'}
        se = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:40'}
        classroom.add_course(math)
        classroom.add_course(se)
        self.assertTrue(classroom.is_free_at('9:50'))
        self.assertFalse(classroom.is_free_at('10:30'))

    def test_is_free_at_2(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(course)
        self.assertFalse(classroom.is_free_at('9:30'))

class ClassroomTestCheckCourseConflict(unittest.TestCase):
    def test_check_course_conflict_1(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '10:30', 'end_time': '11:30'}
        result = classroom.check_course_conflict(new_course)
        self.assertTrue(result)

    def test_check_course_conflict_2(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '09:30', 'end_time': '10:30'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)

    def test_check_course_conflict_3(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:30'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)

    def test_check_course_conflict_4(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '09:40', 'end_time': '10:40'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)

import unittest

from datetime import datetime

class AgentTest_check_course_conflict(unittest.TestCase):
    def test_check_course_conflict_1(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '08:00', 'end_time': '11:00'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)

    def test_check_course_conflict_2(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '08:00', 'end_time': '09:00'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)