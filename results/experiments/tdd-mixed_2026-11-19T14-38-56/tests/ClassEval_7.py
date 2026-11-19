import unittest




class BalancedBracketsTestClearExpr(unittest.TestCase):
    def test_clear_expr(self):
        b = BalancedBrackets("a(b)c")
        b.clear_expr()
        self.assertEqual(b.expr, "()")

    def test_clear_expr_2(self):
        b = BalancedBrackets("a(b){c}")
        b.clear_expr()
        self.assertEqual(b.expr, "(){}")

    def test_clear_expr_3(self):
        b = BalancedBrackets("[a](b){c}")
        b.clear_expr()
        self.assertEqual(b.expr, "[](){}")

import unittest

class AgentTest_clear_expr(unittest.TestCase):
    def test_clear_expr_1(self):
        b = BalancedBrackets("abc 123")
        b.clear_expr()
        self.assertEqual(b.expr, "")

    def test_clear_expr_2(self):
        b = BalancedBrackets("((a)[b]{c})")
        b.clear_expr()
        self.assertEqual(b.expr, "(()[]{})")

class BalancedBracketsTestCheckBalancedBrackets(unittest.TestCase):
    def test_check_balanced_brackets(self):
        b = BalancedBrackets("a(b)c")
        self.assertEqual(b.check_balanced_brackets(), True)

    def test_check_balanced_brackets_2(self):
        b = BalancedBrackets("a(b){c}")
        self.assertEqual(b.check_balanced_brackets(), True)

    def test_check_balanced_brackets_3(self):
        b = BalancedBrackets("[a](b){c}")
        self.assertEqual(b.check_balanced_brackets(), True)

    def test_check_balanced_brackets_4(self):
        b = BalancedBrackets("[a(b){c}")
        self.assertEqual(b.check_balanced_brackets(), False)

    def test_check_balanced_brackets_5(self):
        b = BalancedBrackets("a(b{c}]")
        self.assertEqual(b.check_balanced_brackets(), False)

import unittest

class AgentTest_check_balanced_brackets(unittest.TestCase):
    def test_check_balanced_brackets_1(self):
        b = BalancedBrackets("((a)[b]{c})")
        self.assertEqual(b.check_balanced_brackets(), True)

    def test_check_balanced_brackets_2(self):
        b = BalancedBrackets(")a(")
        self.assertEqual(b.check_balanced_brackets(), False)