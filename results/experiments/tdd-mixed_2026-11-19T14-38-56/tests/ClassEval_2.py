import unittest



class ArgumentParserTestGetArgument(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_get_argument_1(self):
        self.parser.arguments = {"name": "John"}
        result = self.parser.get_argument("name")
        self.assertEqual(result, "John")

    def test_get_argument_2(self):
        self.parser.arguments = {"name": "John", "age": 25}
        result = self.parser.get_argument("age")
        self.assertEqual(result, 25)

    def test_get_argument_3(self):
        self.parser.arguments = {"name": "John", "age": "25", "verbose": True}
        result = self.parser.get_argument("verbose")
        self.assertEqual(result, True)

import unittest

class AgentTest_get_argument(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_get_argument_1(self):
        # Spec: returns None if the argument does not exist (empty parser).
        result = self.parser.get_argument("missing")
        self.assertIsNone(result)

    def test_get_argument_2(self):
        # Spec: returns None for a missing argument, and does not alter stored arguments.
        self.parser.arguments = {"arg1": "value1", "option1": True}
        result = self.parser.get_argument("arg2")
        self.assertIsNone(result)
        self.assertEqual(self.parser.arguments, {"arg1": "value1", "option1": True})

class ArgumentParserTestAddArgument(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_add_argument(self):
        self.parser.add_argument("name")
        self.parser.add_argument("age", required=True, arg_type=int)

        self.assertEqual(self.parser.required, {"age"})
        self.assertEqual(self.parser.types, {"name": str, "age": int})

    def test_add_argument_2(self):
        self.parser.add_argument("name")
        self.parser.add_argument("age", required=False, arg_type=int)
        self.parser.add_argument("verbose", arg_type=bool)

        self.assertEqual(self.parser.required, set())
        self.assertEqual(self.parser.types, {"name": str, "age": int, "verbose": bool})

    def test_add_argument_3(self):
        self.parser.add_argument("name")
        self.parser.add_argument("age", required=False, arg_type=int)
        self.parser.add_argument("verbose", arg_type=bool)
        self.parser.add_argument("d")

        self.assertEqual(self.parser.required, set())
        self.assertEqual(self.parser.types, {"name": str, "age": int, "verbose": bool, "d": str})

import unittest

class AgentTest_add_argument(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_add_argument_1(self):
        # Spec docstring example: positional call add_argument('arg1', True, 'int')
        # gives required == {'arg1'} and types == {'arg1': 'int'}.
        self.parser.add_argument('arg1', True, 'int')

        self.assertEqual(self.parser.required, {'arg1'})
        self.assertEqual(self.parser.types, {'arg1': 'int'})

    def test_add_argument_2(self):
        # Spec: only arguments set as required are added to the required set,
        # while every argument's type is stored in the types dictionary.
        self.parser.add_argument('arg1', True, 'int')
        self.parser.add_argument('arg2', True, 'type2')
        self.parser.add_argument('arg3', False, 'type3')

        self.assertEqual(self.parser.required, {'arg1', 'arg2'})
        self.assertEqual(
            self.parser.types,
            {'arg1': 'int', 'arg2': 'type2', 'arg3': 'type3'}
        )

class ArgumentParserTestConvertType(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_convert_type_1(self):
        self.parser.types = {"age": int}
        result = self.parser._convert_type("age", "25")
        self.assertEqual(result, 25)

    def test_convert_type_2(self):
        self.parser.types = {"age": int}
        result = self.parser._convert_type("age", "twenty-five")
        self.assertEqual(result, "twenty-five")

    def test_convert_type_3(self):
        self.parser.types = {"age": int}
        result = self.parser._convert_type("age", "25")
        self.assertEqual(result, 25)

import unittest

class AgentTest__convert_type(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test__convert_type_1(self):
        # Spec: if the argument is not in self.types, the input value is returned unchanged.
        self.parser.types = {"age": int}
        result = self.parser._convert_type("height", "180")
        self.assertEqual(result, "180")

    def test__convert_type_2(self):
        # Spec: the value is converted to the type stored in self.types for that argument.
        self.parser.types = {"price": float}
        result = self.parser._convert_type("price", "3.5")
        self.assertEqual(result, 3.5)
        self.assertIsInstance(result, float)

class ArgumentParserTestParseArguments(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_parse_arguments_1(self):
        command_str = "script --name=John --age=25"
        self.parser.add_argument("name")
        self.parser.add_argument("age", arg_type=int)

        result, missing_args = self.parser.parse_arguments(command_str)

        self.assertTrue(result)
        self.assertIsNone(missing_args)
        self.assertEqual(self.parser.get_argument("name"), "John")
        self.assertEqual(self.parser.get_argument("age"), 25)

    def test_parse_arguments_2(self):
        command_str = "script --verbose -d"
        self.parser.add_argument("verbose", arg_type=bool)
        self.parser.add_argument("d", arg_type=bool)

        result, missing_args = self.parser.parse_arguments(command_str)

        self.assertTrue(result)
        self.assertIsNone(missing_args)
        self.assertEqual(self.parser.get_argument("verbose"), True)
        self.assertEqual(self.parser.get_argument("d"), True)

    def test_parse_arguments_3(self):
        command_str = "script --name=John"
        self.parser.add_argument("name")
        self.parser.add_argument("age", required=True, arg_type=int)

        result, missing_args = self.parser.parse_arguments(command_str)

        self.assertFalse(result)
        self.assertEqual(missing_args, {"age"})

import unittest

class AgentTest_parse_arguments(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_parse_arguments_1(self):
        # Spec docstring example: "-arg2 value2" (single dash, space-separated value)
        # and "--option1" / "-option2" (flags with no value) are stored in arguments,
        # and parsing succeeds with (True, None).
        command_str = "python script.py --arg1=value1 -arg2 value2 --option1 -option2"

        result = self.parser.parse_arguments(command_str)

        self.assertEqual(result, (True, None))
        self.assertEqual(
            self.parser.arguments,
            {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        )

    def test_parse_arguments_2(self):
        # Spec: when several required arguments are missing, parsing returns False
        # with the set of all missing argument names.
        self.parser.add_argument("host", required=True)
        self.parser.add_argument("port", required=True, arg_type=int)
        self.parser.add_argument("debug")
        command_str = "python script.py --debug"

        result, missing_args = self.parser.parse_arguments(command_str)

        self.assertFalse(result)
        self.assertEqual(missing_args, {"host", "port"})