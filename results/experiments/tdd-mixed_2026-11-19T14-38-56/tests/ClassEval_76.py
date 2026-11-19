import unittest




class SignInSystemTestAddUser(unittest.TestCase):
    def test_add_user_1(self):
        signin_system = SignInSystem()
        result = signin_system.add_user("user1")
        self.assertTrue(result)

    def test_add_user_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        result = signin_system.add_user("user1")
        self.assertFalse(result)

    def test_add_user_3(self):
        signin_system = SignInSystem()
        result = signin_system.add_user("aaa")
        self.assertTrue(result)

class AgentTest_add_user(unittest.TestCase):
    def test_add_user_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        self.assertFalse(signin_system.check_sign_in("user1"))

    def test_add_user_2(self):
        signin_system = SignInSystem()
        first = signin_system.add_user("alice")
        second = signin_system.add_user("bob")
        self.assertTrue(first)
        self.assertTrue(second)
        self.assertFalse(signin_system.check_sign_in("alice"))
        self.assertFalse(signin_system.check_sign_in("bob"))

class SignInSystemTestSignIn(unittest.TestCase):
    def test_sign_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        result = signin_system.sign_in("user1")
        self.assertTrue(result)

    def test_sign_in_2(self):
        signin_system = SignInSystem()
        result = signin_system.sign_in("user1")
        self.assertFalse(result)

    def test_sign_in_3(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        result = signin_system.sign_in("aaa")
        self.assertTrue(result)

import unittest

class AgentTest_sign_in(unittest.TestCase):
    def test_sign_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("mike")
        signin_system.sign_in("mike")
        self.assertTrue(signin_system.check_sign_in("mike"))

    def test_sign_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("alice")
        signin_system.add_user("bob")
        signin_system.sign_in("alice")
        self.assertTrue(signin_system.check_sign_in("alice"))
        self.assertFalse(signin_system.check_sign_in("bob"))

class SignInSystemTestCheckSignIn(unittest.TestCase):
    # has signed in
    def test_check_sign_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.sign_in("user1")
        result = signin_system.check_sign_in("user1")
        self.assertTrue(result)

    def test_check_sign_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        result = signin_system.check_sign_in("user1")
        self.assertFalse(result)

    def test_check_sign_in_3(self):
        signin_system = SignInSystem()
        result = signin_system.check_sign_in("user1")
        self.assertFalse(result)

import unittest

class AgentTest_check_sign_in(unittest.TestCase):
    def test_check_sign_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("mike")
        self.assertIs(signin_system.check_sign_in("mike"), False)
        signin_system.sign_in("mike")
        self.assertIs(signin_system.check_sign_in("mike"), True)

    def test_check_sign_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("jack")
        self.assertFalse(signin_system.check_sign_in("jack"))
        self.assertFalse(signin_system.check_sign_in("jack"))
        signin_system.sign_in("jack")
        self.assertTrue(signin_system.check_sign_in("jack"))
        self.assertTrue(signin_system.check_sign_in("jack"))

class SignInSystemTestAllSignedIn(unittest.TestCase):
    def test_all_signed_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.sign_in("user1")
        result = signin_system.all_signed_in()
        self.assertTrue(result)

    def test_all_signed_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        result = signin_system.all_signed_in()
        self.assertFalse(result)

    def test_all_signed_in_3(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        signin_system.sign_in("aaa")
        result = signin_system.all_signed_in()
        self.assertTrue(result)

class AgentTest_all_signed_in(unittest.TestCase):
    def test_all_signed_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("alice")
        signin_system.add_user("bob")
        signin_system.sign_in("alice")
        result = signin_system.all_signed_in()
        self.assertFalse(result)

    def test_all_signed_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("alice")
        signin_system.add_user("bob")
        signin_system.add_user("carol")
        signin_system.sign_in("alice")
        signin_system.sign_in("bob")
        signin_system.sign_in("carol")
        result = signin_system.all_signed_in()
        self.assertTrue(result)

class SignInSystemTestAllNotSignedIn(unittest.TestCase):
    def test_all_not_signed_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.sign_in("user1")
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)

    def test_all_not_signed_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.add_user("user2")
        result = signin_system.all_not_signed_in()
        self.assertEqual(["user1", "user2"], result)

    def test_all_not_signed_in_3(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        signin_system.sign_in("aaa")
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)

import unittest

class AgentTest_all_not_signed_in(unittest.TestCase):
    def test_all_not_signed_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("a")
        signin_system.add_user("b")
        signin_system.add_user("c")
        signin_system.sign_in("b")
        result = signin_system.all_not_signed_in()
        self.assertEqual(["a", "c"], result)

    def test_all_not_signed_in_2(self):
        signin_system = SignInSystem()
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)