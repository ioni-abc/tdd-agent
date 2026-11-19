import unittest


import unittest

class AgentTest_add_user(unittest.TestCase):

    def setUp(self):
        self.system = SignInSystem()

    def test_add_user_1(self):
        # Adding a new user returns True.
        result = self.system.add_user("mike")
        self.assertIs(result, True)

    def test_add_user_2(self):
        # Adding a user that already exists returns False.
        self.system.add_user("mike")
        result = self.system.add_user("mike")
        self.assertIs(result, False)

    def test_add_user_3(self):
        # A newly added user is stored in self.users with the initial state False.
        self.system.add_user("jack")
        self.assertIn("jack", self.system.users)
        self.assertIs(self.system.users["jack"], False)

    def test_add_user_4(self):
        # Several different users can be added, each returning True.
        self.assertIs(self.system.add_user("a"), True)
        self.assertIs(self.system.add_user("b"), True)
        self.assertIs(self.system.add_user("c"), True)
        self.assertEqual(set(self.system.users.keys()), {"a", "b", "c"})

    def test_add_user_5(self):
        # Adding an existing user must not overwrite its current state.
        self.system.users["mike"] = True
        result = self.system.add_user("mike")
        self.assertIs(result, False)
        self.assertIs(self.system.users["mike"], True)

import unittest

class AgentTest_sign_in(unittest.TestCase):

    def setUp(self):
        self.system = SignInSystem()

    def test_sign_in_1(self):
        # Signing in an existing user returns True.
        self.system.add_user("mike")
        result = self.system.sign_in("mike")
        self.assertIs(result, True)

    def test_sign_in_2(self):
        # Signing in a user that does not exist returns False.
        self.system.add_user("mike")
        result = self.system.sign_in("mik")
        self.assertIs(result, False)

    def test_sign_in_3(self):
        # Signing in an existing user changes its state in self.users to True.
        self.system.add_user("jack")
        self.system.sign_in("jack")
        self.assertIs(self.system.users["jack"], True)

    def test_sign_in_4(self):
        # Signing in a user that does not exist does not add that user to self.users.
        result = self.system.sign_in("ghost")
        self.assertIs(result, False)
        self.assertNotIn("ghost", self.system.users)

    def test_sign_in_5(self):
        # Signing in one user does not change the state of other users.
        self.system.add_user("mike")
        self.system.add_user("jack")
        self.system.sign_in("mike")
        self.assertIs(self.system.users["mike"], True)
        self.assertIs(self.system.users["jack"], False)

class AgentTest_check_sign_in(unittest.TestCase):

    def setUp(self):
        self.system = SignInSystem()

    def test_check_sign_in_1(self):
        # A user that was never added is not signed in, so the result is False.
        result = self.system.check_sign_in("jack")
        self.assertIs(result, False)

    def test_check_sign_in_2(self):
        # A newly added user who has not signed in yet is reported as not signed in.
        self.system.add_user("jack")
        result = self.system.check_sign_in("jack")
        self.assertIs(result, False)

    def test_check_sign_in_3(self):
        # After a user is added and signed in, check_sign_in returns True.
        self.system.add_user("jack")
        self.system.sign_in("jack")
        result = self.system.check_sign_in("jack")
        self.assertIs(result, True)

    def test_check_sign_in_4(self):
        # Checking a user that does not exist returns False and does not add that user to self.users.
        result = self.system.check_sign_in("ghost")
        self.assertIs(result, False)
        self.assertNotIn("ghost", self.system.users)

    def test_check_sign_in_5(self):
        # Checking one user does not depend on other users: only the signed-in user returns True.
        self.system.add_user("mike")
        self.system.add_user("jack")
        self.system.sign_in("mike")
        self.assertIs(self.system.check_sign_in("mike"), True)
        self.assertIs(self.system.check_sign_in("jack"), False)

import unittest

class AgentTest_all_signed_in(unittest.TestCase):

    def setUp(self):
        self.system = SignInSystem()

    def test_all_signed_in_1(self):
        # A single added user who has signed in means all users are signed in, so the result is True.
        self.system.add_user("jack")
        self.system.sign_in("jack")
        result = self.system.all_signed_in()
        self.assertIs(result, True)

    def test_all_signed_in_2(self):
        # A single added user who has not signed in means not all users are signed in, so the result is False.
        self.system.add_user("jack")
        result = self.system.all_signed_in()
        self.assertIs(result, False)

    def test_all_signed_in_3(self):
        # When several users exist and only one of them is signed in, the result is False.
        self.system.add_user("mike")
        self.system.add_user("jack")
        self.system.sign_in("mike")
        result = self.system.all_signed_in()
        self.assertIs(result, False)

    def test_all_signed_in_4(self):
        # When several users exist and all of them are signed in, the result is True.
        self.system.add_user("mike")
        self.system.add_user("jack")
        self.system.add_user("anna")
        self.system.sign_in("mike")
        self.system.sign_in("jack")
        self.system.sign_in("anna")
        result = self.system.all_signed_in()
        self.assertIs(result, True)

    def test_all_signed_in_5(self):
        # The result changes from False to True once the last user that was not signed in signs in.
        self.system.add_user("mike")
        self.system.add_user("jack")
        self.system.sign_in("mike")
        self.assertIs(self.system.all_signed_in(), False)
        self.system.sign_in("jack")
        self.assertIs(self.system.all_signed_in(), True)

import unittest

class AgentTest_all_not_signed_in(unittest.TestCase):

    def setUp(self):
        self.system = SignInSystem()

    def test_all_not_signed_in_1(self):
        # With no users in the system, there are no users that are not signed in, so the result is an empty list.
        result = self.system.all_not_signed_in()
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])

    def test_all_not_signed_in_2(self):
        # Newly added users have not signed in, so all of them are returned in the order they were added.
        self.system.add_user("a")
        self.system.add_user("b")
        result = self.system.all_not_signed_in()
        self.assertEqual(result, ["a", "b"])

    def test_all_not_signed_in_3(self):
        # After one user signs in, only the users who have not signed in are returned.
        self.system.add_user("a")
        self.system.add_user("b")
        self.system.sign_in("a")
        result = self.system.all_not_signed_in()
        self.assertEqual(result, ["b"])

    def test_all_not_signed_in_4(self):
        # When every user has signed in, no usernames are returned, so the result is an empty list.
        self.system.add_user("mike")
        self.system.add_user("jack")
        self.system.sign_in("mike")
        self.system.sign_in("jack")
        result = self.system.all_not_signed_in()
        self.assertEqual(result, [])

    def test_all_not_signed_in_5(self):
        # A user added after others have signed in is not signed in, so it appears in the list
        # while the signed-in users do not.
        self.system.add_user("mike")
        self.system.add_user("jack")
        self.system.sign_in("mike")
        self.system.sign_in("jack")
        self.system.add_user("anna")
        result = self.system.all_not_signed_in()
        self.assertEqual(result, ["anna"])