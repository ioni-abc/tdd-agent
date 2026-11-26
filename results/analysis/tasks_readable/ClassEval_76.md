# ClassEval_76

## Skeleton (what the agent sees)

```python
class SignInSystem:
    """
    This is a class as sigin in system, including adding users, signing in/out, checking sign-in status, and retrieving signed-in/not signed-in users.
    """

    def __init__(self):
        """
        Initialize the sign-in system.
        """
        self.users = {}

    def add_user(self, username):
        """
        Add a user to the sign-in system if the user wasn't in the self.users.
        And the initial state is False.
        :param username: str, the username to be added.
        :return: bool, True if the user is added successfully, False if the user already exists.
        >>> signInSystem.add_user("mike")
        True
        >>> signInSystem.add_user("mike")
        False
        """

    def sign_in(self, username):
        """
        Sign in a user if the user was in the self.users and change the state to True.
        :param username: str, the username to be signed in.
        :return: bool, True if the user is signed in successfully, False if the user does not exist.
        >>> signInSystem.sign_in("mike")
        True
        >>> signInSystem.sign_in("mik")
        False
        """

    def check_sign_in(self, username):
        """
        Check if a user is signed in.
        :param username: str, the username to be checked.
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        >>> signInSystem.check_sign_in("jack")
        False
        >>> signInSystem.add_user("jack")
        >>> signInSystem.check_sign_in("jack")
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.check_sign_in("jack")
        True
        """

    def all_signed_in(self):
        """
        Check if all users are signed in.
        :return: bool, True if all users are signed in, False otherwise.
        >>> signInSystem.add_user("jack")
        True
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.all_signed_in()
        True
        """

    def all_not_signed_in(self):
        """
        Get a list of usernames that are not signed in.
        :return: list[str], a list of usernames that are not signed in.
        >>> signInSystem = SignInSystem()
        >>> signInSystem.add_user("a")
        True
        >>> signInSystem.add_user("b")
        True
        >>> signInSystem.all_not_signed_in()
        ['a', 'b']
        """
```

## Method `add_user`

### Docstring

```python
def add_user(self, username):
        """
        Add a user to the sign-in system if the user wasn't in the self.users.
        And the initial state is False.
        :param username: str, the username to be added.
        :return: bool, True if the user is added successfully, False if the user already exists.
        >>> signInSystem.add_user("mike")
        True
        >>> signInSystem.add_user("mike")
        False
        """
```

### Reference code (`solution_code`)

```python
def add_user(self, username):
        if username in self.users:
            return False
        else:
            self.users[username] = False
            return True
```

### Tests (`SignInSystemTestAddUser`)

**test_add_user_1**: `stated`
- reason: The docstring says add_user returns True when a new user is added, and this test adds a fresh username and expects True, which a programmer following the docstring would pass.

```python
def test_add_user_1(self):
    signin_system = SignInSystem()
    result = signin_system.add_user("user1")
    self.assertTrue(result)
```

**test_add_user_2**: `stated`
- reason: The docstring says add_user returns False when the user already exists, and the test adds the same username twice and expects False on the second call, which a programmer following the docstring would pass.

```python
def test_add_user_2(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    result = signin_system.add_user("user1")
    self.assertFalse(result)
```

**test_add_user_3**: `stated`
- reason: The docstring says add_user returns True when a new user is added to an empty or non-existing set, so a programmer following it would return True for a first-time username and pass this test.

```python
def test_add_user_3(self):
    signin_system = SignInSystem()
    result = signin_system.add_user("aaa")
    self.assertTrue(result)
```

**test_add_user_4**: `stated`
- reason: The docstring says add_user returns True when the user is added successfully to a system where the user did not already exist, which is exactly what this fresh-system test checks.

```python
def test_add_user_4(self):
    signin_system = SignInSystem()
    result = signin_system.add_user("bbb")
    self.assertTrue(result)
```

**test_add_user_5**: `stated`
- reason: The docstring says add_user returns True when the user is not already present and adds them, so a fresh system adding a new username should return True, which is what the test checks.

```python
def test_add_user_5(self):
    signin_system = SignInSystem()
    result = signin_system.add_user("ccc")
    self.assertTrue(result)
```

## Method `sign_in`

### Docstring

```python
def sign_in(self, username):
        """
        Sign in a user if the user was in the self.users and change the state to True.
        :param username: str, the username to be signed in.
        :return: bool, True if the user is signed in successfully, False if the user does not exist.
        >>> signInSystem.sign_in("mike")
        True
        >>> signInSystem.sign_in("mik")
        False
        """
```

### Reference code (`solution_code`)

```python
def sign_in(self, username):
        if username not in self.users:
            return False
        else:
            self.users[username] = True
            return True
```

### Tests (`SignInSystemTestSignIn`)

**test_sign_in_1**: `stated`
- reason: The docstring says sign_in returns True and sets the user's state when the user exists in self.users, which is exactly what the test checks for a user added via add_user.

```python
def test_sign_in_1(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    result = signin_system.sign_in("user1")
    self.assertTrue(result)
```

**test_sign_in_2**: `stated`
- reason: The docstring says sign_in returns False when the user does not exist, and a fresh SignInSystem with no registered "user1" hits exactly that case, so a programmer following it would return False and pass.

```python
def test_sign_in_2(self):
    signin_system = SignInSystem()
    result = signin_system.sign_in("user1")
    self.assertFalse(result)
```

**test_sign_in_3**: `stated`
- reason: The docstring says sign_in returns True when the user exists and is signed in, which is exactly what this test checks after add_user("aaa") and sign_in("aaa").

```python
def test_sign_in_3(self):
    signin_system = SignInSystem()
    signin_system.add_user("aaa")
    result = signin_system.sign_in("aaa")
    self.assertTrue(result)
```

**test_sign_in_4**: `stated`
- reason: The docstring says sign_in returns True when the user exists in self.users and is signed in, which is exactly what this test checks after adding "bbb" and signing it in.

```python
def test_sign_in_4(self):
    signin_system = SignInSystem()
    signin_system.add_user("bbb")
    result = signin_system.sign_in("bbb")
    self.assertTrue(result)
```

**test_sign_in_5**: `stated`
- reason: The docstring says sign_in returns False when the user does not exist, and a fresh system with no "ccc" user should return False, which is what the test checks.

```python
def test_sign_in_5(self):
    signin_system = SignInSystem()
    result = signin_system.sign_in("ccc")
    self.assertFalse(result)
```

## Method `check_sign_in`

### Docstring

```python
def check_sign_in(self, username):
        """
        Check if a user is signed in.
        :param username: str, the username to be checked.
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        >>> signInSystem.check_sign_in("jack")
        False
        >>> signInSystem.add_user("jack")
        >>> signInSystem.check_sign_in("jack")
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.check_sign_in("jack")
        True
        """
```

### Reference code (`solution_code`)

```python
def check_sign_in(self, username):
        if username not in self.users:
            return False
        else:
            if self.users[username]:
                return True
            else:
                return False
```

### Tests (`SignInSystemTestCheckSignIn`)

**test_check_sign_in_1**: `stated`
- reason: The docstring says the method returns True when the user is signed in, and the test checks exactly that after add_user and sign_in, which a programmer following the docstring would pass.

```python
def test_check_sign_in_1(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    signin_system.sign_in("user1")
    result = signin_system.check_sign_in("user1")
    self.assertTrue(result)
```

**test_check_sign_in_2**: `stated`
- reason: The docstring says the method returns False when the user is not signed in, and this test adds a user without signing them in and expects False, which a programmer following the docstring would pass.

```python
def test_check_sign_in_2(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    result = signin_system.check_sign_in("user1")
    self.assertFalse(result)
```

**test_check_sign_in_3**: `stated`
- reason: The docstring says the method returns False when the user does not exist, and the test checks exactly that case, with a fresh system and an unregistered username.

```python
def test_check_sign_in_3(self):
    signin_system = SignInSystem()
    result = signin_system.check_sign_in("user1")
    self.assertFalse(result)
```

**test_check_sign_in_4**: `stated`
- reason: The docstring says the method returns True when the user is signed in, which is exactly what the test checks after adding and signing in a user.

```python
def test_check_sign_in_4(self):
    signin_system = SignInSystem()
    signin_system.add_user("aaa")
    signin_system.sign_in("aaa")
    result = signin_system.check_sign_in("aaa")
    self.assertTrue(result)
```

**test_check_sign_in_5**: `stated`
- reason: The docstring says the method returns True when the user is signed in, and the test adds a user, signs them in, and expects True, which a programmer following the docstring would pass.

```python
def test_check_sign_in_5(self):
    signin_system = SignInSystem()
    signin_system.add_user("bbb")
    signin_system.sign_in("bbb")
    result = signin_system.check_sign_in("bbb")
    self.assertTrue(result)
```

## Method `all_signed_in`

### Docstring

```python
def all_signed_in(self):
        """
        Check if all users are signed in.
        :return: bool, True if all users are signed in, False otherwise.
        >>> signInSystem.add_user("jack")
        True
        >>> signInSystem.sign_in("jack")
        >>> signInSystem.all_signed_in()
        True
        """
```

### Reference code (`solution_code`)

```python
def all_signed_in(self):
        if all(self.users.values()):
            return True
        else:
            return False
```

### Tests (`SignInSystemTestAllSignedIn`)

**test_all_signed_in_1**: `stated`
- reason: The docstring says all_signed_in returns True when all users are signed in, and the test adds one user, signs them in, and expects True, which a programmer following the docstring would produce.

```python
def test_all_signed_in_1(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    signin_system.sign_in("user1")
    result = signin_system.all_signed_in()
    self.assertTrue(result)
```

**test_all_signed_in_2**: `stated`
- reason: The docstring says the method returns False when not all users are signed in, and the test adds one user who has not signed in and expects False.

```python
def test_all_signed_in_2(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    result = signin_system.all_signed_in()
    self.assertFalse(result)
```

**test_all_signed_in_3**: `stated`
- reason: The docstring says the method returns True when all users are signed in, and the test covers exactly that case with one user who has signed in, so a programmer following it would pass.

```python
def test_all_signed_in_3(self):
    signin_system = SignInSystem()
    signin_system.add_user("aaa")
    signin_system.sign_in("aaa")
    result = signin_system.all_signed_in()
    self.assertTrue(result)
```

**test_all_signed_in_4**: `stated`
- reason: The docstring says the method returns True when all users are signed in, and this test adds one user, signs them in, and expects True, which a programmer following the docstring would implement.

```python
def test_all_signed_in_4(self):
    signin_system = SignInSystem()
    signin_system.add_user("bbb")
    signin_system.sign_in("bbb")
    result = signin_system.all_signed_in()
    self.assertTrue(result)
```

**test_all_signed_in_5**: `stated`
- reason: The docstring says the method returns True only if all users are signed in and False otherwise, so a programmer would return False when one of two registered users has not signed in, which is what the test expects.

```python
def test_all_signed_in_5(self):
    signin_system = SignInSystem()
    signin_system.add_user("aaa")
    signin_system.add_user("bbb")
    signin_system.sign_in("aaa")
    result = signin_system.all_signed_in()
    self.assertFalse(result)
```

## Method `all_not_signed_in`

### Docstring

```python
def all_not_signed_in(self):
        """
        Get a list of usernames that are not signed in.
        :return: list[str], a list of usernames that are not signed in.
        >>> signInSystem = SignInSystem()
        >>> signInSystem.add_user("a")
        True
        >>> signInSystem.add_user("b")
        True
        >>> signInSystem.all_not_signed_in()
        ['a', 'b']
        """
```

### Reference code (`solution_code`)

```python
def all_not_signed_in(self):
        not_signed_in_users = []
        for username, signed_in in self.users.items():
            if not signed_in:
                not_signed_in_users.append(username)
        return not_signed_in_users
```

### Tests (`SignInSystemTestAllNotSignedIn`)

**test_all_not_signed_in_1**: `stated`
- reason: The docstring says the method returns the usernames that are not signed in, so a programmer would exclude the only user, who has been signed in, and return an empty list as the test expects.

```python
def test_all_not_signed_in_1(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    signin_system.sign_in("user1")
    result = signin_system.all_not_signed_in()
    self.assertEqual([], result)
```

**test_all_not_signed_in_2**: `stated`
- reason: The docstring says the method returns the usernames not signed in, and its example shows two newly added users returned in insertion order, which is what this test checks.

```python
def test_all_not_signed_in_2(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    signin_system.add_user("user2")
    result = signin_system.all_not_signed_in()
    self.assertEqual(["user1", "user2"], result)
```

**test_all_not_signed_in_3**: `stated`
- reason: The docstring defines the method as returning usernames that are not signed in, so a user who has signed in should be excluded and the empty list is the expected result.

```python
def test_all_not_signed_in_3(self):
    signin_system = SignInSystem()
    signin_system.add_user("aaa")
    signin_system.sign_in("aaa")
    result = signin_system.all_not_signed_in()
    self.assertEqual([], result)
```

**test_all_not_signed_in_4**: `stated`
- reason: The docstring says the method returns the usernames that are not signed in, so a programmer would exclude the signed-in user and return only "aaa", which is what the test expects.

```python
def test_all_not_signed_in_4(self):
    signin_system = SignInSystem()
    signin_system.add_user("user1")
    signin_system.add_user("aaa")
    signin_system.sign_in("user1")
    result = signin_system.all_not_signed_in()
    self.assertEqual(['aaa'], result)
```

**test_all_not_signed_in_5**: `stated`
- reason: The docstring says the method returns the list of usernames not signed in, so a programmer would naturally return an empty list when no users exist, which is what the test expects.

```python
def test_all_not_signed_in_5(self):
    signin_system = SignInSystem()
    result = signin_system.all_not_signed_in()
    self.assertEqual([], result)
```

## Tests in no method's test class

### `SignInSystemTestMain`

setUp (runs before each test):

```python
def setUp(self):
    self.signin_system = SignInSystem()
```

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    result = self.signin_system.add_user("user1")
    result = self.signin_system.add_user("user2")
    self.assertTrue(result)

    result = self.signin_system.sign_in("user1")
    self.assertTrue(result)

    result = self.signin_system.check_sign_in("user1")
    self.assertTrue(result)

    result = self.signin_system.all_signed_in()
    self.assertFalse(result)

    result = self.signin_system.all_not_signed_in()
    self.assertEqual(["user2"], result)
```
