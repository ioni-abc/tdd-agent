import unittest




class CamelCaseMapTestIter(unittest.TestCase):
    def test_iter_1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        lst = ['firstName', 'lastName', 'age']
        iter = camelize_map.__iter__()
        i = 0
        for key in iter:
            self.assertEqual(key, lst[i])
            i += 1

    def test_iter_2(self):
        camelize_map = CamelCaseMap()
        camelize_map['firstname'] = 'John'
        camelize_map['lastname'] = 'Doe'
        camelize_map['age'] = 30
        lst = ['firstname', 'lastname', 'age']
        iter = camelize_map.__iter__()
        i = 0
        for key in iter:
            self.assertEqual(key, lst[i])
            i += 1

    def test_iter_3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_Name'] = 'John'
        camelize_map['last_Name'] = 'Doe'
        camelize_map['age'] = 30
        lst = ['firstName', 'lastName', 'age']
        iter = camelize_map.__iter__()
        i = 0
        for key in iter:
            self.assertEqual(key, lst[i])
            i += 1

import unittest

import collections.abc

class AgentTest___iter__(unittest.TestCase):
    def test___iter___1(self):
        camelize_map = CamelCaseMap()
        keys = list(camelize_map.__iter__())
        self.assertEqual(keys, [])

    def test___iter___2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        iterator = camelize_map.__iter__()
        self.assertIsInstance(iterator, collections.abc.Iterator)
        self.assertEqual(next(iterator), 'firstName')
        self.assertEqual(next(iterator), 'lastName')
        with self.assertRaises(StopIteration):
            next(iterator)

class CamelCaseMapTestLen(unittest.TestCase):
    def test_len_1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        self.assertEqual(camelize_map.__len__(), 1)

    def test_len_2(self):
        camelize_map = CamelCaseMap()
        camelize_map['last_name'] = 'Doe'
        self.assertEqual(camelize_map.__len__(), 1)

    def test_len_3(self):
        camelize_map = CamelCaseMap()
        camelize_map['age'] = 30
        self.assertEqual(camelize_map.__len__(), 1)

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

class CamelCaseMapTestToCamelCase(unittest.TestCase):
    def test_to_camel_case_1(self):
        self.assertEqual(CamelCaseMap._to_camel_case('aaa_bbb'), 'aaaBbb')

    def test_to_camel_case_2(self):
        self.assertEqual(CamelCaseMap._to_camel_case('first_name'), 'firstName')

    def test_to_camel_case_3(self):
        self.assertEqual(CamelCaseMap._to_camel_case('last_name'), 'lastName')

import unittest

class AgentTest__to_camel_case(unittest.TestCase):
    def test__to_camel_case_1(self):
        self.assertEqual(CamelCaseMap._to_camel_case('age'), 'age')

    def test__to_camel_case_2(self):
        self.assertEqual(CamelCaseMap._to_camel_case('first_middle_last'), 'firstMiddleLast')

class CamelCaseMapTestConvertKey(unittest.TestCase):
    def test_convert_key_1(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('aaa_bbb'), 'aaaBbb')

    def test_convert_key_2(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('first_name'), 'firstName')

    def test_convert_key_3(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('last_name'), 'lastName')

    def test_convert_key_4(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('ccc_ddd'), 'cccDdd')

import unittest

class AgentTest__convert_key(unittest.TestCase):
    def test__convert_key_1(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('age'), 'age')

    def test__convert_key_2(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('first_middle_last'), 'firstMiddleLast')

class CamelCaseMapTestGetitem(unittest.TestCase):
    def test_getitem_1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        self.assertEqual(camelize_map.__getitem__('first_name'), 'John')

    def test_getitem_2(self):
        camelize_map = CamelCaseMap()
        camelize_map['last_name'] = 'Doe'
        self.assertEqual(camelize_map.__getitem__('last_name'), 'Doe')

    def test_getitem_3(self):
        camelize_map = CamelCaseMap()
        camelize_map['age'] = 30
        self.assertEqual(camelize_map.__getitem__('age'), 30)

import unittest

class AgentTest___getitem__(unittest.TestCase):
    def test___getitem___1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_middle_last'] = 'Ann'
        self.assertEqual(camelize_map.__getitem__('first_middle_last'), 'Ann')

    def test___getitem___2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['first_name'] = 'Jane'
        self.assertEqual(camelize_map.__getitem__('first_name'), 'Jane')

class CamelCaseMapTestSetitem(unittest.TestCase):
    def test_setitem_1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map.__setitem__('first_name', 'newname')
        self.assertEqual(camelize_map['first_name'], 'newname')

    def test_setitem_2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map.__setitem__('first_name', 'John')
        self.assertEqual(camelize_map['first_name'], 'John')

    def test_setitem_3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map.__setitem__('first_Name', 'newname')
        self.assertEqual(camelize_map['first_name'], 'newname')

import unittest

class AgentTest___setitem__(unittest.TestCase):
    def test___setitem___1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['first_name'] = 'Jane'
        self.assertEqual(camelize_map['last_name'], 'Doe')
        self.assertEqual(camelize_map['first_name'], 'Jane')

    def test___setitem___2(self):
        camelize_map = CamelCaseMap()
        result = camelize_map.__setitem__('first_name', 'John')
        self.assertIsNone(result)
        self.assertEqual(camelize_map['first_name'], 'John')

class CamelCaseMapTestDelitem(unittest.TestCase):
    def test_delitem_1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map.__delitem__('first_name')
        self.assertEqual(camelize_map['last_name'], 'Doe')

    def test_delitem_2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map.__delitem__('first_name')
        self.assertEqual('first_name' in camelize_map, False)

    def test_delitem_3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map.__delitem__('first_Name')
        self.assertEqual('first_name' in camelize_map, False)

import unittest

class AgentTest___delitem__(unittest.TestCase):
    def test___delitem___1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        camelize_map.__delitem__('last_name')
        self.assertEqual(camelize_map.__len__(), 2)
        self.assertEqual(list(camelize_map.__iter__()), ['firstName', 'age'])

    def test___delitem___2(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map.__delitem__('first_name')
        camelize_map['first_name'] = 'Jane'
        self.assertEqual(camelize_map.__getitem__('first_name'), 'Jane')
        self.assertEqual(camelize_map.__len__(), 1)