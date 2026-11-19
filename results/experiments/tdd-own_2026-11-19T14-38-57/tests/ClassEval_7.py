import unittest


import unittest

class AgentTest_clear_expr(unittest.TestCase):

    def test_clear_expr_1(self):
        b = BalancedBrackets("a(b)c")
        b.clear_expr()
        self.assertEqual(b.expr, '()')

    def test_clear_expr_2(self):
        b = BalancedBrackets("([{}])")
        b.clear_expr()
        self.assertEqual(b.expr, "([{}])")

    def test_clear_expr_3(self):
        b = BalancedBrackets("abc 123 xyz")
        b.clear_expr()
        self.assertEqual(b.expr, "")

    def test_clear_expr_4(self):
        b = BalancedBrackets("x{ y [z] } w")
        b.clear_expr()
        self.assertEqual(b.expr, "{[]}")

    def test_clear_expr_5(self):
        b = BalancedBrackets("")
        result = b.clear_expr()
        self.assertEqual(b.expr, "")
        self.assertIsNone(result)

import unittest

class AgentTest_check_balanced_brackets(unittest.TestCase):

    def test_check_balanced_brackets_1(self):
        b = BalancedBrackets("a(b)c")
        self.assertTrue(b.check_balanced_brackets())

    def test_check_balanced_brackets_2(self):
        b = BalancedBrackets("(")
        self.assertFalse(b.check_balanced_brackets())

    def test_check_balanced_brackets_3(self):
        b = BalancedBrackets("([)]")
        self.assertFalse(b.check_balanced_brackets())

    def test_check_balanced_brackets_4(self):
        b = BalancedBrackets("x{ y [z] } w")
        self.assertTrue(b.check_balanced_brackets())

    def test_check_balanced_brackets_5(self):
        b = BalancedBrackets(")(")
        self.assertFalse(b.check_balanced_brackets())