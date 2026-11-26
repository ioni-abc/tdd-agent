# ClassEval_21

## Skeleton (what the agent sees)

```python
from datetime import datetime

class Classroom:
    """
    This is a class representing a classroom, capable of adding and removing courses, checking availability at a given time, and detecting conflicts when scheduling new courses.
    """

    def __init__(self, id):
        """
        Initialize the classroom management system.
        :param id: int, the id of classroom
        """
        self.id = id
        self.courses = []

    def add_course(self, course):
        """
        Add course to self.courses list if the course wasn't in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
```

## Method `add_course`

### Docstring

```python
def add_course(self, course):
        """
        Add course to self.courses list if the course wasn't in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
```

### Reference code (`solution_code`)

```python
def add_course(self, course):

        if course not in self.courses:
            self.courses.append(course)
```

### Tests (`ClassroomTestAddCourse`)

**test_add_course_1**: `stated`
- reason: The docstring says the course is added to the courses list if it wasn't already there, and the test adds a new course and checks it is present in the list, which a programmer following the docstring would pass.

```python
def test_add_course_1(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    self.assertIn(course, classroom.courses)
```

**test_add_course_2**: `stated`
- reason: The docstring says the course is added to `self.courses` if it isn't already there, which is exactly what the test checks when it adds a new course and asserts it appears in the list.

```python
def test_add_course_2(self):
    classroom = Classroom(1)
    course = {'name': 'Chinese', 'start_time': '10:00', 'end_time': '11:00'}
    classroom.add_course(course)
    self.assertIn(course, classroom.courses)
```

**test_add_course_3**: `stated`
- reason: The docstring says the course is added to `self.courses` when it is not already there, which is exactly what this test checks by adding a new course and asserting it appears in the list.

```python
def test_add_course_3(self):
    classroom = Classroom(1)
    course = {'name': 'English', 'start_time': '11:00', 'end_time': '12:00'}
    classroom.add_course(course)
    self.assertIn(course, classroom.courses)
```

**test_add_course_4**: `stated`
- reason: The docstring says the course is added to `self.courses` when it isn't already there, which is exactly what this test checks by adding a new course and asserting it appears in the list.

```python
def test_add_course_4(self):
    classroom = Classroom(1)
    course = {'name': 'Art', 'start_time': '14:00', 'end_time': '15:00'}
    classroom.add_course(course)
    self.assertIn(course, classroom.courses)
```

**test_add_course_5**: `stated`
- reason: The docstring says the course is added to `self.courses` when it isn't already there, which is exactly what the test checks by adding a new course and asserting it appears in the list.

```python
def test_add_course_5(self):
    classroom = Classroom(1)
    course = {'name': 'P.E.', 'start_time': '15:00', 'end_time': '16:00'}
    classroom.add_course(course)
    self.assertIn(course, classroom.courses)
```

**test_add_course_6**: `stated`
- reason: The docstring says the course is added to the list only if it wasn't already there, so a programmer would skip the duplicate and the test's assertIn on the course would pass.

```python
def test_add_course_6(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    classroom.add_course(course)
    self.assertIn(course, classroom.courses)
```

## Method `remove_course`

### Docstring

```python
def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
```

### Reference code (`solution_code`)

```python
def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
```

### Tests (`ClassroomTestRemoveCourse`)

**test_remove_course_1**: `stated`
- reason: The docstring says the course is removed from `self.courses` if it was present, which is exactly what the test checks by adding a course, removing it, and asserting it is gone.

```python
def test_remove_course_1(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    classroom.remove_course(course)
    self.assertNotIn(course, classroom.courses)
```

**test_remove_course_2**: `stated`
- reason: The docstring says the course is removed from self.courses if it was there, which is exactly what the test checks: a course added and then removed should no longer be in the list.

```python
def test_remove_course_2(self):
    classroom = Classroom(1)
    course = {'name': 'Chinese', 'start_time': '10:00', 'end_time': '11:00'}
    classroom.add_course(course)
    classroom.remove_course(course)
    self.assertNotIn(course, classroom.courses)
```

**test_remove_course_3**: `stated`
- reason: The docstring says the course is removed from self.courses if it was in it, and the test adds a course then removes it and checks it is no longer present, which a programmer following the docstring would pass.

```python
def test_remove_course_3(self):
    classroom = Classroom(1)
    course = {'name': 'English', 'start_time': '11:00', 'end_time': '12:00'}
    classroom.add_course(course)
    classroom.remove_course(course)
    self.assertNotIn(course, classroom.courses)
```

**test_remove_course_4**: `stated`
- reason: The docstring says the course is removed from `self.courses` if it was there, which is exactly what this test checks: add a course, remove it, and confirm it is gone.

```python
def test_remove_course_4(self):
    classroom = Classroom(1)
    course = {'name': 'Art', 'start_time': '14:00', 'end_time': '15:00'}
    classroom.add_course(course)
    classroom.remove_course(course)
    self.assertNotIn(course, classroom.courses)
```

**test_remove_course_5**: `stated`
- reason: The docstring says the course is removed from `self.courses` if it was in it, which is exactly what this test checks: add the course, remove it, and confirm it is gone.

```python
def test_remove_course_5(self):
    classroom = Classroom(1)
    course = {'name': 'P.E.', 'start_time': '15:00', 'end_time': '16:00'}
    classroom.add_course(course)
    classroom.remove_course(course)
    self.assertNotIn(course, classroom.courses)
```

**test_remove_course_6**: `stated`
- reason: The docstring says the course is removed from the list if it was there, so a programmer implementing that would leave the list without the course, which is what this test checks even when the course was never added.

```python
def test_remove_course_6(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.remove_course(course)
    self.assertNotIn(course, classroom.courses)
```

## Method `is_free_at`

### Docstring

```python
def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """
```

### Reference code (`solution_code`)

```python
def is_free_at(self, check_time):
        check_time = datetime.strptime(check_time, '%H:%M')

        for course in self.courses:
            if datetime.strptime(course['start_time'], '%H:%M') <= check_time <= datetime.strptime(course['end_time'],
                                                                                                   '%H:%M'):
                return False
        return True
```

### Tests (`ClassroomTestIsFreeAt`)

**test_is_free_at_1**: `stated`
- reason: The docstring says is_free_at returns True when the check time does not fall within any course's time range, and 11:00 is outside the 09:00–10:00 course, so a programmer following it would return True and pass.

```python
def test_is_free_at_1(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    check_time = '11:00'
    result = classroom.is_free_at(check_time)
    self.assertTrue(result)
```

**test_is_free_at_2**: `stated`
- reason: The docstring says it returns False when the check time conflicts with a course time, and its example shows a time inside a course's span (9:00 within 8:00-9:40) returning False, so a programmer would return False for 09:30 inside 09:00-10:00.

```python
def test_is_free_at_2(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    check_time = '09:30'
    result = classroom.is_free_at(check_time)
    self.assertFalse(result)
```

**test_is_free_at_3**: `stated`
- reason: The docstring says the method returns True when the check time does not conflict with any course time, so a programmer would return True for 12:00 when the only course runs 09:00 to 10:00, matching the test.

```python
def test_is_free_at_3(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    check_time = '12:00'
    result = classroom.is_free_at(check_time)
    self.assertTrue(result)
```

**test_is_free_at_4**: `stated`
- reason: The docstring says the method returns True when the check time does not conflict with any course time, so a free time well outside the single course's span (14:00 against 9:00 to 10:00) should return True, which is what the test expects.

```python
def test_is_free_at_4(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    check_time = '14:00'
    result = classroom.is_free_at(check_time)
    self.assertTrue(result)
```

**test_is_free_at_5**: `stated`
- reason: The docstring says the method returns False when the check time conflicts with a course time, so a programmer would return False for 09:40 inside the 09:00–10:00 course, matching the test.

```python
def test_is_free_at_5(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    check_time = '09:40'
    result = classroom.is_free_at(check_time)
    self.assertFalse(result)
```

## Method `check_course_conflict`

### Docstring

```python
def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
```

### Reference code (`solution_code`)

```python
def check_course_conflict(self, new_course):
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M')

        flag = True
        for course in self.courses:
            start_time = datetime.strptime(course['start_time'], '%H:%M')
            end_time = datetime.strptime(course['end_time'], '%H:%M')
            if start_time <= new_start_time and end_time >= new_start_time:
                flag = False
            if start_time <= new_end_time and end_time >= new_end_time:
                flag = False
        return flag
```

### Tests (`ClassroomTestCheckCourseConflict`)

**test_check_course_conflict_1**: `stated`
- reason: The docstring says the method returns True when the new course does not conflict with existing courses, and this test uses non-overlapping times (10:30–11:30 after 09:00–10:00) and expects True, so a correct implementation passes.

```python
def test_check_course_conflict_1(self):
    classroom = Classroom(1)
    existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(existing_course)
    new_course = {'name': 'SE', 'start_time': '10:30', 'end_time': '11:30'}
    result = classroom.check_course_conflict(new_course)
    self.assertTrue(result)
```

**test_check_course_conflict_2**: `stated`
- reason: The docstring says the method returns False when the new course's time conflicts with any existing course, so a partial overlap like 09:30–10:30 against 09:00–10:00 should return False, which is what the test expects.

```python
def test_check_course_conflict_2(self):
    classroom = Classroom(1)
    existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(existing_course)
    new_course = {'name': 'SE', 'start_time': '09:30', 'end_time': '10:30'}
    result = classroom.check_course_conflict(new_course)
    self.assertFalse(result)
```

**test_check_course_conflict_3**: `stated`
- reason: The docstring explicitly says a conflict includes courses that share a boundary time, and the test's new course starts exactly when the existing one ends, so a programmer following the docstring would return False.

```python
def test_check_course_conflict_3(self):
    classroom = Classroom(1)
    existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(existing_course)
    new_course = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:30'}
    result = classroom.check_course_conflict(new_course)
    self.assertFalse(result)
```

**test_check_course_conflict_4**: `stated`
- reason: The docstring says the method returns False when the new course's time conflicts with any existing course, and this test's partially overlapping times are a clear conflict under that rule, so a programmer following it would return False.

```python
def test_check_course_conflict_4(self):
    classroom = Classroom(1)
    existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(existing_course)
    new_course = {'name': 'SE', 'start_time': '09:40', 'end_time': '10:40'}
    result = classroom.check_course_conflict(new_course)
    self.assertFalse(result)
```

**test_check_course_conflict_5**: `stated`
- reason: The docstring says the method returns True when the new course does not conflict with any existing course, and this test adds a non-overlapping course and expects True.

```python
def test_check_course_conflict_5(self):
    classroom = Classroom(1)
    existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(existing_course)
    new_course = {'name': 'SE', 'start_time': '14:30', 'end_time': '15:30'}
    result = classroom.check_course_conflict(new_course)
    self.assertTrue(result)
```

**test_check_course_conflict_6**: `stated`
- reason: The docstring says the method returns False whenever the new course's time conflicts with an existing course, so a programmer implementing a general overlap check would return False for this partial overlap (new end 9:30 falls inside existing 09:00-10:00).

```python
def test_check_course_conflict_6(self):
    classroom = Classroom(1)
    existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(existing_course)
    new_course = {'name': 'SE', 'start_time': '8:30', 'end_time': '9:30'}
    result = classroom.check_course_conflict(new_course)
    self.assertFalse(result)
```

## Tests in no method's test class

### `ClassroomTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    classroom = Classroom(1)
    course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
    classroom.add_course(course)
    self.assertIn(course, classroom.courses)

    classroom.remove_course(course)
    self.assertNotIn(course, classroom.courses)

    classroom.add_course(course)
    self.assertIn(course, classroom.courses)
    check_time = '09:30'
    result = classroom.is_free_at(check_time)
    self.assertFalse(result)

    new_course = {'name': 'SE', 'start_time': '09:30', 'end_time': '10:30'}
    result = classroom.check_course_conflict(new_course)
    self.assertFalse(result)
```
