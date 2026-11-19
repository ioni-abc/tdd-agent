import unittest


import unittest

class AgentTest_get_argument(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()
        self.parser.arguments = {
            'arg1': 'value1',
            'arg2': 'value2',
            'option1': True,
            'option2': True,
        }

    def test_get_argument_1(self):
        self.assertEqual(self.parser.get_argument('arg2'), 'value2')

    def test_get_argument_2(self):
        self.assertEqual(self.parser.get_argument('arg1'), 'value1')

    def test_get_argument_3(self):
        self.assertIs(self.parser.get_argument('option1'), True)
        self.assertIs(self.parser.get_argument('option2'), True)

    def test_get_argument_4(self):
        self.assertIsNone(self.parser.get_argument('missing_arg'))

    def test_get_argument_5(self):
        empty_parser = ArgumentParser()
        self.assertIsNone(empty_parser.get_argument('arg1'))

import unittest

class AgentTest_add_argument(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_add_argument_1(self):
        self.parser.add_argument('arg1', True, 'int')
        self.assertEqual(self.parser.required, {'arg1'})
        self.assertEqual(self.parser.types, {'arg1': 'int'})

    def test_add_argument_2(self):
        self.parser.add_argument('arg1', False, 'int')
        self.assertEqual(self.parser.required, set())
        self.assertEqual(self.parser.types, {'arg1': 'int'})

    def test_add_argument_3(self):
        self.parser.add_argument('arg2')
        self.assertEqual(self.parser.required, set())
        self.assertIs(self.parser.types['arg2'], str)

    def test_add_argument_4(self):
        self.parser.add_argument('arg1', True, 'int')
        self.parser.add_argument('arg2', True, 'float')
        self.parser.add_argument('arg3', True, 'str')
        self.assertEqual(self.parser.required, {'arg1', 'arg2', 'arg3'})
        self.assertEqual(
            self.parser.types,
            {'arg1': 'int', 'arg2': 'float', 'arg3': 'str'}
        )

    def test_add_argument_5(self):
        self.parser.add_argument('arg1', True, 'int')
        self.parser.add_argument('option1', arg_type='bool')
        self.assertEqual(self.parser.required, {'arg1'})
        self.assertEqual(
            self.parser.types,
            {'arg1': 'int', 'option1': 'bool'}
        )

import unittest

class AgentTest__convert_type(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test__convert_type_1(self):
        self.parser.types = {'arg1': int}
        result = self.parser._convert_type('arg1', '21')
        self.assertEqual(result, 21)
        self.assertIsInstance(result, int)

    def test__convert_type_2(self):
        self.parser.types = {'arg1': float}
        result = self.parser._convert_type('arg1', '3.5')
        self.assertEqual(result, 3.5)
        self.assertIsInstance(result, float)

    def test__convert_type_3(self):
        self.parser.types = {'arg1': int}
        self.assertEqual(self.parser._convert_type('arg1', 'abc'), 'abc')

    def test__convert_type_4(self):
        self.parser.types = {'arg1': int}
        self.assertEqual(self.parser._convert_type('missing_arg', '21'), '21')

    def test__convert_type_5(self):
        self.parser.types = {'arg1': int, 'arg2': str}
        self.assertEqual(self.parser._convert_type('arg2', '21'), '21')
        self.assertEqual(self.parser._convert_type('arg1', '21'), 21)

import unittest

class AgentTest_parse_arguments(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_parse_arguments_1(self):
        result = self.parser.parse_arguments(
            "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        )
        self.assertEqual(result, (True, None))
        self.assertEqual(
            self.parser.arguments,
            {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        )

    def test_parse_arguments_2(self):
        self.parser.add_argument('arg1', arg_type=int)
        result = self.parser.parse_arguments("python script.py --arg1=21")
        self.assertEqual(result, (True, None))
        self.assertEqual(self.parser.arguments['arg1'], 21)
        self.assertIsInstance(self.parser.arguments['arg1'], int)

    def test_parse_arguments_3(self):
        self.parser.add_argument('arg1', True)
        result = self.parser.parse_arguments("python script.py --option1")
        self.assertEqual(result, (False, {'arg1'}))

    def test_parse_arguments_4(self):
        self.parser.add_argument('arg1', True)
        result = self.parser.parse_arguments("python script.py --arg1=value1")
        self.assertEqual(result, (True, None))
        self.assertEqual(self.parser.arguments['arg1'], 'value1')

    def test_parse_arguments_5(self):
        self.parser.add_argument('arg1', True)
        self.parser.add_argument('arg2', True)
        self.parser.add_argument('arg3')
        result = self.parser.parse_arguments("python script.py -arg3 x")
        self.assertEqual(result, (False, {'arg1', 'arg2'}))