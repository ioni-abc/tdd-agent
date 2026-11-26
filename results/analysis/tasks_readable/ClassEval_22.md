# ClassEval_22

## Skeleton (what the agent sees)

```python
class ClassRegistrationSystem:
    """
    This is a class as a class registration system, allowing to register students, register them for classes, retrieve students by major, get a list of all majors, and determine the most popular class within a specific major.
    """


    def __init__(self):
        """
        Initialize the registration system with the attribute students and students_registration_class.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students_registration_class is a dictionaries, key is the student name, value is a list of class names
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        """

    def register_class(self, student_name, class_name):
        """
        register a class to the student.
        :param student_name: str
        :param class_name: str
        :return a list of class names that the student has registered
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.register_class(student_name="John", class_name="CS101")
        >>> registration_system.register_class(student_name="John", class_name="CS102")
        ["CS101", "CS102"]

    def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        >>> registration_system = ClassRegistrationSystem()
        >>> student1 = {"name": "John", "major": "Computer Science"}
        >>> registration_system.register_student(student1)
        >>> registration_system.get_students_by_major("Computer Science")
        ["John"]
        """

    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """

    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"},
                                             {"name": "Bob", "major": "Computer Science"},
                                             {"name": "Alice", "major": "Computer Science"}]
        >>> registration_system.students_registration_classes = {"John": ["Algorithms", "Data Structures"],
                                            "Bob": ["Operating Systems", "Data Structures", "Algorithms"]}
        >>> registration_system.get_most_popular_class_in_major("Computer Science")
        "Data Structures"
        """
```

## Method `register_student`

### Docstring

```python
def register_student(self, student):
        """
        register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        """
```

### Reference code (`solution_code`)

```python
def register_student(self, student):
        if student in self.students:
            return 0
        else:
            self.students.append(student)
            return 1
```

### Tests (`ClassRegistrationSystemTestRegisterStudent`)

setUp (runs before each test):

```python
def setUp(self):
    self.registration_system = ClassRegistrationSystem()
```

**test_register_student**: `stated`
- reason: The docstring says a new student is added to the list and 1 is returned when the student is not already registered, which is exactly what this test checks with a fresh student in an empty system.

```python
def test_register_student(self):
    student1 = {"name": "John", "major": "Computer Science"}
    self.assertEqual(self.registration_system.register_student(student1), 1)
```

**test_register_student2**: `stated`
- reason: The docstring says that registering an already-registered student returns 0, which is exactly what the test checks when the same student dict is registered twice.

```python
def test_register_student2(self):
    student1 = {"name": "John", "major": "Computer Science"}
    self.registration_system.register_student(student1)
    self.assertEqual(self.registration_system.register_student(student1), 0)
```

**test_register_student3**: `stated`
- reason: The docstring says to add the student to the list and return 0 if already registered or 1 otherwise, which is exactly what the test checks: new students return 1, and re-registering student2 returns 0.

```python
def test_register_student3(self):
    student1 = {"name": "John", "major": "Computer Science"}
    student2 = {"name": "Alice", "major": "Mathematics"}
    self.assertEqual(self.registration_system.register_student(student1), 1)
    self.assertEqual(self.registration_system.register_student(student2), 1)
    self.assertEqual(self.registration_system.register_student(student2), 0)
```

## Method `register_class`

### Docstring

```python
def register_class(self, student_name, class_name):
        """
        register a class to the student.
        :param student_name: str
        :param class_name: str
        :return a list of class names that the student has registered
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.register_class(student_name="John", class_name="CS101")
        >>> registration_system.register_class(student_name="John", class_name="CS102")
        ["CS101", "CS102"]
```

### Reference code (`solution_code`)

```python
def register_class(self, student_name, class_name):
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]
        return self.students_registration_classes[student_name]
```

### Tests (`ClassRegistrationSystemTestRegisterClass`)

setUp (runs before each test):

```python
def setUp(self):
    self.registration_system = ClassRegistrationSystem()
```

**test_register_class**: `stated`
- reason: The docstring says the method returns the list of classes the student has registered, and its example shows a first registration growing that list, so a programmer following it would return ["CS101"] for a new student's first class.

```python
def test_register_class(self):
    self.assertEqual(self.registration_system.register_class(student_name="John", class_name="CS101"), ["CS101"])
```

**test_register_class2**: `stated`
- reason: The docstring says the method registers a class for the student and returns the list of that student's registered class names, and its example shows the list growing with each registration, so a programmer would append each class and return the full list, which is what the test checks.

```python
def test_register_class2(self):
    self.registration_system.register_class(student_name="John", class_name="CS101")
    self.registration_system.register_class(student_name="John", class_name="CS102")
    self.assertEqual(self.registration_system.register_class(student_name="John", class_name="CS103"), ["CS101", "CS102", "CS103"])
```

**test_register_class3**: `stated`
- reason: The docstring says the method returns the list of classes the student has registered, and the example shows repeated calls for one student accumulating, so a per-student list that ignores other students' registrations would pass this test.

```python
def test_register_class3(self):
    self.registration_system.register_class(student_name="John", class_name="CS101")
    self.registration_system.register_class(student_name="Tom", class_name="CS102")
    self.assertEqual(self.registration_system.register_class(student_name="John", class_name="CS103"), ["CS101", "CS103"])
```

## Method `get_students_by_major`

### Docstring

```python
def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        >>> registration_system = ClassRegistrationSystem()
        >>> student1 = {"name": "John", "major": "Computer Science"}
        >>> registration_system.register_student(student1)
        >>> registration_system.get_students_by_major("Computer Science")
        ["John"]
        """
```

### Reference code (`solution_code`)

```python
def get_students_by_major(self, major):
        student_list = []
        for student in self.students:
            if student["major"] == major:
                student_list.append(student["name"])
        return student_list
```

### Tests (`ClassRegistrationSystemTestGetStudent`)

setUp (runs before each test):

```python
def setUp(self):
    self.registration_system = ClassRegistrationSystem()
```

**test_get_students_by_major**: `stated`
- reason: The docstring says to return the names of all students in the given major as a list, which is what the test checks when two students share that major, and a natural filter over the stored students keeps their storage order, matching the expected ["John", "Bob"].

```python
def test_get_students_by_major(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                         {"name": "Bob", "major": "Computer Science"}]

    cs_students = self.registration_system.get_students_by_major("Computer Science")

    self.assertEqual(cs_students, ["John", "Bob"])
```

**test_get_students_by_major2**: `stated`
- reason: The docstring says the method returns a list of names of all students in the given major, which is what a programmer would implement, and the test checks that behaviour with several matches and with no match, both of which that implementation returns.

```python
def test_get_students_by_major2(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                         {"name": "Bob", "major": "Computer Science"}]

    cs_students = self.registration_system.get_students_by_major("Computer Science")
    math_students = self.registration_system.get_students_by_major("Mathematics")

    self.assertEqual(cs_students, ["John", "Bob"])
    self.assertEqual(math_students, [])
```

**test_get_students_by_major3**: `stated`
- reason: The docstring says the method returns the names of all students in the given major, which is exactly what the test checks: it filters by major and returns the matching names, and a natural implementation keeps the stored order.

```python
def test_get_students_by_major3(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                         {"name": "Bob", "major": "Computer Science"},
                                            {"name": "Alice", "major": "Mathematics"}]

    cs_students = self.registration_system.get_students_by_major("Computer Science")
    math_students = self.registration_system.get_students_by_major("Mathematics")

    self.assertEqual(cs_students, ["John", "Bob"])
    self.assertEqual(math_students, ["Alice"])
```

**test_get_students_by_major4**: `stated`
- reason: The docstring says to return all students in the major as a list of names, and a programmer filtering the registered students in order would produce exactly the order the test expects.

```python
def test_get_students_by_major4(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                         {"name": "Bob", "major": "Computer Science"},
                                         {"name": "Alice", "major": "Mathematics"},
                                         {"name": "Tom", "major": "Mathematics"},
                                         {"name": "Jerry", "major": "Mathematics"}]

    cs_students = self.registration_system.get_students_by_major("Computer Science")
    math_students = self.registration_system.get_students_by_major("Mathematics")
    self.assertEqual(cs_students, ["John", "Bob"])
    self.assertEqual(math_students, ["Alice", "Tom", "Jerry"])
```

## Method `get_all_major`

### Docstring

```python
def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """
```

### Reference code (`solution_code`)

```python
def get_all_major(self):
        major_list = []
        for student in self.students:
            if student["major"] not in major_list:
                major_list.append(student["major"])
        return major_list
```

### Tests (`ClassRegistrationSystemTestGetMajor`)

setUp (runs before each test):

```python
def setUp(self):
    self.registration_system = ClassRegistrationSystem()
```

**test_get_all_major**: `unstated`
- reason: The docstring says only "get all majors in the system" and gives a one-student example, so a programmer could reasonably return one entry per student and fail the test, which expects duplicate majors to be collapsed.
- missing: The docstring should say whether each major appears once even when several students share it, and in what order the majors are returned.

```python
def test_get_all_major(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                         {"name": "Bob", "major": "Computer Science"}]

    majors = self.registration_system.get_all_major()

    self.assertEqual(majors, ["Computer Science"])
```

**test_get_all_major2**: `unstated`
- reason: The docstring says only "get all majors in the system," so a programmer could reasonably return duplicates or use a different order, while the test expects each major once in first-appearance order.
- missing: The docstring should say that each major appears only once in the result, and that majors are listed in the order they first appear in the students list.

```python
def test_get_all_major2(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                         {"name": "Bob", "major": "Computer Science"},
                                         {"name": "Alice", "major": "Mathematics"}]

    majors = self.registration_system.get_all_major()

    self.assertEqual(majors, ["Computer Science", "Mathematics"])
```

**test_get_all_major3**: `unstated`
- reason: The docstring says only "get all majors" and returns "a list of majors", so a programmer could reasonably return duplicates or sort the result, while the test expects each major once in order of first appearance.
- missing: The docstring should say that each major appears only once in the returned list, ordered by when it first appears in the students list.

```python
def test_get_all_major3(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                         {"name": "Bob", "major": "Computer Science"},
                                         {"name": "Alice", "major": "Mathematics"},
                                         {"name": "Tom", "major": "Mathematics"},
                                         {"name": "Jerry", "major": "Physics"}]

    majors = self.registration_system.get_all_major()

    self.assertEqual(majors, ["Computer Science", "Mathematics", "Physics"])
```

## Method `get_most_popular_class_in_major`

### Docstring

```python
def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"},
                                             {"name": "Bob", "major": "Computer Science"},
                                             {"name": "Alice", "major": "Computer Science"}]
        >>> registration_system.students_registration_classes = {"John": ["Algorithms", "Data Structures"],
                                            "Bob": ["Operating Systems", "Data Structures", "Algorithms"]}
        >>> registration_system.get_most_popular_class_in_major("Computer Science")
        "Data Structures"
        """
```

### Reference code (`solution_code`)

```python
def get_most_popular_class_in_major(self, major):
        class_list = []
        for student in self.students:
            if student["major"] == major:
                class_list += self.students_registration_classes[student["name"]]
        most_popular_class = max(set(class_list), key=class_list.count)
        return most_popular_class
```

### Tests (`ClassRegistrationSystemTestPopularClass`)

setUp (runs before each test):

```python
def setUp(self):
    self.registration_system = ClassRegistrationSystem()
```

**test_get_most_popular_class_in_major**: `stated`
- reason: The docstring says to return the class with the highest enrollment in the major, which a programmer would implement as counting each student's classes across students in that major and returning the most frequent one, and this test expects that.

```python
def test_get_most_popular_class_in_major(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                         {"name": "Bob", "major": "Computer Science"},
                                         {"name": "Alice", "major": "Computer Science"}]

    self.registration_system.students_registration_classes = {"John": ["Algorithms", "Data Structures"],
                                        "Bob": ["Operating Systems", "Data Structures", "Algorithms"],
                                        "Alice": ["Data Structures", "Operating Systems", "Calculus"]}

    cs_most_popular_class = self.registration_system.get_most_popular_class_in_major("Computer Science")

    self.assertEqual(cs_most_popular_class, "Data Structures")
```

**test_get_most_popular_class_in_major2**: `stated`
- reason: The docstring says to return the class with the highest enrollment in the major, which a programmer would implement by counting each class across students in that major and returning the most frequent one, exactly what the test checks for both majors.

```python
def test_get_most_popular_class_in_major2(self):
    self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                            {"name": "Bob", "major": "Computer Science"},
                                            {"name": "Alice", "major": "Computer Science"},
                                            {"name": "Tom", "major": "Mathematics"},
                                            {"name": "Jerry", "major": "Mathematics"}]

    self.registration_system.students_registration_classes = {"John": ["Algorithms", "Data Structures"],
                                                              "Bob": ["Data Structures", "Algorithms",
                                                                      "Operating Systems"],
                                                              "Alice": ["Data Structures", "Operating Systems",
                                                                        "Calculus"],
                                                                "Tom": ["Calculus", "Linear Algebra"],
                                                                "Jerry": ["Linear Algebra", "Statistics"]}

    cs_most_popular_class = self.registration_system.get_most_popular_class_in_major("Computer Science")
    math_most_popular_class = self.registration_system.get_most_popular_class_in_major("Mathematics")
    self.assertEqual(cs_most_popular_class, "Data Structures")
    self.assertEqual(math_most_popular_class, "Linear Algebra")
```

## Tests in no method's test class

### `ClassRegistrationSystemTest`

setUp (runs before each test):

```python
def setUp(self):
    self.registration_system = ClassRegistrationSystem()
```

**test**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test(self):
    student1 = {"name": "John", "major": "Computer Science"}
    student2 = {"name": "Bob", "major": "Computer Science"}
    student3 = {"name": "Alice", "major": "Mathematics"}
    student4 = {"name": "Tom", "major": "Mathematics"}
    self.registration_system.register_student(student1)
    self.registration_system.register_student(student2)
    self.registration_system.register_student(student3)
    self.registration_system.register_student(student4)
    self.registration_system.register_class("John", "Algorithms")
    self.registration_system.register_class("John", "Data Structures")
    self.registration_system.register_class("Bob", "Operating Systems")
    self.registration_system.register_class("Bob", "Data Structures")
    self.assertEqual(self.registration_system.get_students_by_major("Computer Science"), ["John", "Bob"])
    self.assertEqual(self.registration_system.get_students_by_major("Mathematics"), ["Alice", "Tom"])
    self.assertEqual(self.registration_system.get_all_major(), ["Computer Science", "Mathematics"])
    self.assertEqual(self.registration_system.get_most_popular_class_in_major("Computer Science"), "Data Structures")
```
