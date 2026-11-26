# ClassEval_20

## Skeleton (what the agent sees)

```python
from datetime import datetime

class Chat:
    """
    This is a chat class with the functions of adding users, removing users, sending messages, and obtaining messages.
    """

    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        """
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.add_user('John')
        True
        self.users = {'John': []}
        >>> chat.add_user('John')
        False

        """

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns True, otherwise, returns False.
        >>> chat = Chat()
        >>> chat.users = {'John': []}
        >>> chat.remove_user('John')
        True
        >>> chat.remove_user('John')
        False

        """

    def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message, str.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.users = {'John': [], 'Mary': []}
        >>> chat.send_message('John', 'Mary', 'Hello')
        True
        >>> chat.send_message('John', 'Tom', 'Hello')
        False

        """

    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_messages('John')
        [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]
        >>> chat.get_messages('Mary')
        []

        """
```

## Method `add_user`

### Docstring

```python
def add_user(self, username):
        """
        Add a new user to the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.add_user('John')
        True
        self.users = {'John': []}
        >>> chat.add_user('John')
        False

        """
```

### Reference code (`solution_code`)

```python
def add_user(self, username):
        if username in self.users:
            return False
        else:
            self.users[username] = []
            return True
```

### Tests (`ChatTestAddUser`)

**test_add_user**: `stated`
- reason: The docstring says adding a new user returns True, and its stray `self.users = {'John': []}` line shows the expected storage of an empty list per user, so a programmer following it would pass both assertions.

```python
def test_add_user(self):
    chat = Chat()
    self.assertEqual(chat.add_user('John'), True)
    self.assertEqual(chat.users, {'John': []})
```

**test_add_user_2**: `stated`
- reason: The docstring says that adding a user who is already in the Chat returns False, which is exactly what this test checks by pre-populating `users` with 'John' and expecting False with no change to the dictionary.

```python
def test_add_user_2(self):
    chat = Chat()
    chat.users = {'John': []}
    self.assertEqual(chat.add_user('John'), False)
    self.assertEqual(chat.users, {'John': []})
```

**test_add_user_3**: `stated`
- reason: The docstring says add_user adds a new user to the Chat and returns True when the user is not already present, which is what the test checks, and the stray example line shows users mapping to empty lists.

```python
def test_add_user_3(self):
    chat = Chat()
    chat.users = {'John': []}
    self.assertEqual(chat.add_user('Mary'), True)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
```

**test_add_user_4**: `stated`
- reason: The docstring says adding a new user returns True and adding an existing user returns False, which is the behaviour this test checks for a new name, and "add a new user to the Chat" implies the user is stored.

```python
def test_add_user_4(self):
    chat = Chat()
    chat.users = {'John': []}
    self.assertEqual(chat.add_user('Mary'), True)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
```

**test_add_user_5**: `stated`
- reason: The docstring says adding a new username returns True, and the test's two True returns for distinct new users match that, while the stray `self.users = {'John': []}` line in the docstring hints at the stored structure the final assertion checks.

```python
def test_add_user_5(self):
    chat = Chat()
    self.assertEqual(chat.add_user('John'), True)
    self.assertEqual(chat.add_user('Mary'), True)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
```

## Method `remove_user`

### Docstring

```python
def remove_user(self, username):
        """
        Remove a user from the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns True, otherwise, returns False.
        >>> chat = Chat()
        >>> chat.users = {'John': []}
        >>> chat.remove_user('John')
        True
        >>> chat.remove_user('John')
        False

        """
```

### Reference code (`solution_code`)

```python
def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        else:
            return False
```

### Tests (`ChatTestRemoveUser`)

**test_remove_user**: `stated`
- reason: The docstring says the method removes the user and returns True when the user is in the chat, which is exactly what the test checks: removing 'John' returns True and empties the users dict.

```python
def test_remove_user(self):
    chat = Chat()
    chat.users = {'John': []}
    self.assertEqual(chat.remove_user('John'), True)
    self.assertEqual(chat.users, {})
```

**test_remove_user_2**: `stated`
- reason: The docstring says the method returns False when the user is not in the Chat, and the test removes a user who was never added, expecting False, with `users` still empty.

```python
def test_remove_user_2(self):
    chat = Chat()
    self.assertEqual(chat.remove_user('John'), False)
    self.assertEqual(chat.users, {})
```

**test_remove_user_3**: `stated`
- reason: The docstring says to remove the user from the Chat and return True when the user is present, which is exactly what the test checks: removing 'John' returns True and leaves only the other user.

```python
def test_remove_user_3(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.remove_user('John'), True)
    self.assertEqual(chat.users, {'Mary': []})
```

**test_remove_user_4**: `stated`
- reason: The docstring says the method removes the user and returns True when the user was in the chat, which is exactly what the test checks for both removals and the resulting empty user list.

```python
def test_remove_user_4(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.remove_user('Mary'), True)
    self.assertEqual(chat.remove_user('John'), True)
    self.assertEqual(chat.users, {})
```

**test_remove_user_5**: `stated`
- reason: The docstring says the method returns False when the user is not in the Chat, which covers this test's call with a name absent from the chat, and removing an absent user naturally leaves the user list unchanged.

```python
def test_remove_user_5(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.remove_user('Amy'), False)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
```

## Method `send_message`

### Docstring

```python
def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message, str.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        >>> chat = Chat()
        >>> chat.users = {'John': [], 'Mary': []}
        >>> chat.send_message('John', 'Mary', 'Hello')
        True
        >>> chat.send_message('John', 'Tom', 'Hello')
        False

        """
```

### Reference code (`solution_code`)

```python
def send_message(self, sender, receiver, message):
        if sender not in self.users or receiver not in self.users:
            return False

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_info = {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'timestamp': timestamp
        }
        self.users[sender].append(message_info)
        self.users[receiver].append(message_info)
        return True
```

### Tests (`ChatTestSendMessage`)

**test_send_message**: `unstated`
- reason: The docstring only says the method returns True when both users exist, but the test also expects the message to be stored in both users' lists as a dict with specific keys and a timestamp format, none of which a docstring-following implementation would necessarily produce.
- missing: The docstring should state that on success the message is appended to the message list of both the sender and the receiver, as a record containing the sender, receiver, message text, and a timestamp formatted as "YYYY-MM-DD HH:MM:SS".

```python
def test_send_message(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertEqual(chat.send_message('John', 'Mary', 'Hello'), True)
    self.assertEqual(chat.users, {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}], 'Mary': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]})
```

**test_send_message_2**: `unstated`
- reason: The docstring states that send_message returns False when the receiver is missing, but the test also requires that no message be recorded in any user's history on that failure, and the docstring never says so.
- missing: When the send fails because the sender or receiver is not in the chat, the method must leave every user's stored message list unchanged.

```python
def test_send_message_2(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.send_message('John', 'Tom', 'Hello'), False)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
```

**test_send_message_3**: `stated`
- reason: The docstring says that if the sender is not in the Chat the method returns False, and the test checks exactly that case, so a programmer following it would return False and leave the users dict untouched.

```python
def test_send_message_3(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.send_message('Amy', 'Mary', 'Hello'), False)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
```

**test_send_message_4**: `stated`
- reason: The docstring says that if the sender or receiver is not in the Chat, the method returns False, which is the behaviour this test checks, and a natural implementation would not alter the user dictionary on that path.

```python
def test_send_message_4(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.send_message('Amy', 'Tom', 'Hello'), False)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
```

**test_send_message_5**: `stated`
- reason: The docstring says send_message returns False when the sender or receiver is not in the Chat, and this test sends from and to an unregistered user and expects False, which a programmer following the docstring would produce.

```python
def test_send_message_5(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.send_message('Amy', 'Amy', 'Hello'), False)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
```

## Method `get_messages`

### Docstring

```python
def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        >>> chat = Chat()
        >>> chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]}
        >>> chat.get_messages('John')
        [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': '2023-01-01 00:00:00'}]
        >>> chat.get_messages('Mary')
        []

        """
```

### Reference code (`solution_code`)

```python
def get_messages(self, username):
        if username not in self.users:
            return []
        return self.users[username]
```

### Tests (`ChatTestGetMessages`)

**test_get_messages**: `stated`
- reason: The docstring says get_messages returns a user's messages as a list of dictionaries with the keys sender, receiver, message and timestamp, which is exactly what the test checks for user 'John' with one stored message.

```python
def test_get_messages(self):
    chat = Chat()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]}
    self.assertEqual(chat.get_messages('John'), [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}])
```

**test_get_messages_2**: `stated`
- reason: A programmer following the docstring would return the user's stored message list, which is empty here, so the test's expected `[]` matches the described behaviour.

```python
def test_get_messages_2(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.get_messages('John'), [])
```

**test_get_messages_3**: `stated`
- reason: The docstring's second example shows that asking for a user who has no entry in the chat returns an empty list, which is exactly what this test checks for an unknown user.

```python
def test_get_messages_3(self):
    chat = Chat()
    chat.users = {'John': [], 'Mary': []}
    self.assertEqual(chat.get_messages('Amy'), [])
```

**test_get_messages_4**: `stated`
- reason: The docstring's own example shows that asking for a user with no stored messages returns an empty list, which is exactly what this test checks.

```python
def test_get_messages_4(self):
    chat = Chat()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]}
    self.assertEqual(chat.get_messages('Mary'), [])
```

**test_get_messages_5**: `stated`
- reason: The docstring's own example shows that asking for a user with no messages (`'Mary'`) returns `[]`, so a programmer following it would return an empty list for the unknown user `'Amy'` and pass.

```python
def test_get_messages_5(self):
    chat = Chat()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat.users = {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]}
    self.assertEqual(chat.get_messages('Amy'), [])
```

## Tests in no method's test class

### `ChatTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    chat = Chat()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertEqual(chat.add_user('John'), True)
    self.assertEqual(chat.add_user('Mary'), True)
    self.assertEqual(chat.add_user('Amy'), True)
    self.assertEqual(chat.users, {'John': [], 'Mary': [], 'Amy': []})
    self.assertEqual(chat.remove_user('Amy'), True)
    self.assertEqual(chat.users, {'John': [], 'Mary': []})
    self.assertEqual(chat.send_message('John', 'Mary', 'Hello'), True)
    self.assertEqual(chat.send_message('John', 'Tom', 'Hello'), False)
    self.assertEqual(chat.users, {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}], 'Mary': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]})
    self.assertEqual(chat.get_messages('John'), [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}])
    self.assertEqual(chat.get_messages('Mary'), [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}])
```

**test_main_2**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main_2(self):
    chat = Chat()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertEqual(chat.remove_user('Amy'), False)
    self.assertEqual(chat.add_user('John'), True)
    self.assertEqual(chat.add_user('Mary'), True)
    self.assertEqual(chat.add_user('Amy'), True)
    self.assertEqual(chat.users, {'John': [], 'Mary': [], 'Amy': []})
    self.assertEqual(chat.send_message('John', 'Mary', 'Hello'), True)
    self.assertEqual(chat.send_message('John', 'Tom', 'Hello'), False)
    self.assertEqual(chat.remove_user('Amy'), True)
    self.assertEqual(chat.users, {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}], 'Mary': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]})
    self.assertEqual(chat.users, {'John': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}], 'Mary': [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}]})
    self.assertEqual(chat.get_messages('John'), [{'sender': 'John', 'receiver': 'Mary', 'message': 'Hello', 'timestamp': timestamp}])
```
