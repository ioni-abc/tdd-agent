import unittest


import unittest

class AgentTest___iter__(unittest.TestCase):

    def test___iter___1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        iterator = camelize_map.__iter__()
        self.assertTrue(hasattr(iterator, '__next__'))
        self.assertEqual(next(iterator), 'firstName')

    def test___iter___2(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(list(camelize_map), [])

    def test___iter___3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        keys = list(camelize_map)
        self.assertEqual(len(keys), 3)

    def test___iter___4(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        self.assertEqual(set(camelize_map), {'firstName', 'lastName', 'age'})

    def test___iter___5(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        del camelize_map['first_name']
        keys = list(camelize_map)
        self.assertEqual(len(keys), 1)
        self.assertNotIn('firstName', keys)
        self.assertIn('lastName', keys)

import unittest

class AgentTest___len__(unittest.TestCase):

    def test___len___1(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map.__len__(), 0)

    def test___len___2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        self.assertEqual(camelize_map.__len__(), 3)

    def test___len___3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        self.assertEqual(len(camelize_map), 3)

    def test___len___4(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        self.assertIsInstance(camelize_map.__len__(), int)

    def test___len___5(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        del camelize_map['first_name']
        self.assertEqual(camelize_map.__len__(), 2)
        del camelize_map['last_name']
        del camelize_map['age']
        self.assertEqual(camelize_map.__len__(), 0)

class AgentTest__to_camel_case(unittest.TestCase):

    def test__to_camel_case_1(self):
        self.assertEqual(CamelCaseMap._to_camel_case('first_name'), 'firstName')

    def test__to_camel_case_2(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._to_camel_case('first_name'), 'firstName')

    def test__to_camel_case_3(self):
        self.assertEqual(CamelCaseMap._to_camel_case('age'), 'age')

    def test__to_camel_case_4(self):
        self.assertEqual(CamelCaseMap._to_camel_case('first_middle_last'), 'firstMiddleLast')

    def test__to_camel_case_5(self):
        result = CamelCaseMap._to_camel_case('last_name')
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'lastName')

import unittest

class AgentTest__convert_key(unittest.TestCase):

    def test__convert_key_1(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('first_name'), 'firstName')

    def test__convert_key_2(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('age'), 'age')

    def test__convert_key_3(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('first_middle_last'), 'firstMiddleLast')

    def test__convert_key_4(self):
        camelize_map = CamelCaseMap()
        result = camelize_map._convert_key('last_name')
        self.assertIsInstance(result, str)

    def test__convert_key_5(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        self.assertEqual(camelize_map._convert_key('first_name'), 'firstName')
        self.assertEqual(camelize_map['first_name'], 'John')

import unittest

class AgentTest___getitem__(unittest.TestCase):

    def test___getitem___1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        self.assertEqual(camelize_map['first_name'], 'John')

    def test___getitem___2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        self.assertEqual(camelize_map['last_name'], 'Doe')
        self.assertEqual(camelize_map['age'], 30)

    def test___getitem___3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['first_name'] = 'new name'
        self.assertEqual(camelize_map['first_name'], 'new name')

    def test___getitem___4(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_middle_last'] = 'Ann'
        self.assertEqual(camelize_map['first_middle_last'], 'Ann')

    def test___getitem___5(self):
        camelize_map = CamelCaseMap()
        camelize_map['age'] = 30
        result = camelize_map['age']
        self.assertEqual(result, 30)
        self.assertIsInstance(result, int)

import unittest

class AgentTest___setitem__(unittest.TestCase):

    def test___setitem___1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        self.assertEqual(camelize_map['first_name'], 'John')

    def test___setitem___2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['first_name'] = 'new name'
        self.assertEqual(camelize_map['first_name'], 'new name')
        self.assertEqual(len(camelize_map), 1)

    def test___setitem___3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_middle_last'] = 'Ann'
        self.assertEqual(list(camelize_map), ['firstMiddleLast'])
        self.assertEqual(camelize_map['first_middle_last'], 'Ann')

    def test___setitem___4(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        self.assertEqual(len(camelize_map), 3)
        self.assertEqual(set(camelize_map), {'firstName', 'lastName', 'age'})

    def test___setitem___5(self):
        camelize_map = CamelCaseMap()
        result = camelize_map.__setitem__('first_name', 'John')
        self.assertIsNone(result)
        self.assertEqual(camelize_map['first_name'], 'John')

import unittest

class AgentTest___delitem__(unittest.TestCase):

    def test___delitem___1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        result = camelize_map.__delitem__('first_name')
        self.assertIsNone(result)
        flag = 'first_name' in camelize_map
        self.assertFalse(flag)

    def test___delitem___2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        del camelize_map['first_name']
        self.assertEqual(len(camelize_map), 2)

    def test___delitem___3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        del camelize_map['last_name']
        self.assertEqual(camelize_map['first_name'], 'John')
        self.assertEqual(camelize_map['age'], 30)
        self.assertEqual(set(camelize_map), {'firstName', 'age'})

    def test___delitem___4(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        del camelize_map['first_name']
        camelize_map['first_name'] = 'Jane'
        self.assertEqual(camelize_map['first_name'], 'Jane')
        self.assertEqual(len(camelize_map), 1)
        self.assertEqual(list(camelize_map), ['firstName'])

    def test___delitem___5(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_middle_last'] = 'Ann'
        del camelize_map['first_middle_last']
        self.assertEqual(len(camelize_map), 0)
        self.assertEqual(list(camelize_map), [])
        self.assertFalse('first_middle_last' in camelize_map)