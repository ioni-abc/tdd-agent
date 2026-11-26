# ClassEval_36

## Skeleton (what the agent sees)

```python
from datetime import datetime

class EmailClient:
    """
    This is a class that serves as an email client, implementing functions such as checking emails, determining whether there is sufficient space, and cleaning up space
    """

    def __init__(self, addr, capacity) -> None:
        """
        Initializes the EmailClient class with the email address and the capacity of the email box.
        :param addr: The email address, str.
        :param capacity: The capacity of the email box, float.
        """
        self.addr = addr
        self.capacity = capacity
        self.inbox = []

    def send_to(self, recv, content, size):
        """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.send_to(receiver, 'Hello', 10)
        True
        >>> receiver.inbox
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}

        """

    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        >>> receiver.fetch()
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'read'}

        """

    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.is_full_with_one_more_email(10)
        False

        """

    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': datetime.now, 'state': 'unread'}]
        >>> sender.get_occupied_size()
        10

        """

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        >>> receiver.clear_inbox(30)
        >>> receiver.inbox
        [{'size': 15}]

        """
```

## Method `send_to`

### Docstring

```python
def send_to(self, recv, content, size):
        """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.send_to(receiver, 'Hello', 10)
        True
        >>> receiver.inbox
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}

        """
```

### Reference code (`solution_code`)

```python
def send_to(self, recv, content, size):
        if not recv.is_full_with_one_more_email(size):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            email = {
                "sender": self.addr,
                "receiver": recv.addr,
                "content": content,
                "size": size,
                "time": timestamp,
                "state": "unread"
            }
            recv.inbox.append(email)
            return True
        else:
            self.clear_inbox(size)
            return False
```

### Tests (`EmailClientTestSendTo`)

**test_send_to**: `stated`
- reason: The docstring says a successful send returns True and its example shows the inbox entry with sender, receiver, content, size, a timestamp, and state 'unread', which is what the test checks for a small email to a non-full inbox.

```python
def test_send_to(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertTrue(sender.send_to(receiver, 'Hello', 10))
    self.assertEqual(receiver.inbox[0], {"sender": 'sender@example.com','receiver': 'receiver@example.com','content': 'Hello','size': 10,'time': timestamp,'state': 'unread'})
```

**test_send_to_2**: `stated`
- reason: The docstring says send_to returns False when the receiver's mailbox is full, and this test sends a 10-unit email to a receiver with no capacity and expects False, which a programmer would implement as a full-mailbox check.

```python
def test_send_to_2(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 0)
    self.assertFalse(sender.send_to(receiver, 'Hello', 10))
```

**test_send_to_3**: `stated`
- reason: The docstring says send_to returns False when the receiver's mailbox is full, and a programmer following it would return False without adding the email, which is what this test checks.
- missing: The docstring should say whether a rejected send leaves the receiver's inbox unchanged and whether it has any side effect on the sender's inbox, since the reference clears the sender's inbox on rejection.

```python
def test_send_to_3(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 50, 'time': '2021-01-01 00:00:00', 'state': 'unread'}]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertFalse(sender.send_to(receiver, 'Hello', 10))
    self.assertEqual(receiver.inbox, [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 50, 'time': '2021-01-01 00:00:00', 'state': 'unread'}])
```

**test_send_to_4**: `stated`
- reason: The docstring says send_to returns True when the email is sent and shows the receiver's inbox gaining the email entry, which is exactly what this non-full case expects, and the timestamp follows the format shown in the example.

```python
def test_send_to_4(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 30)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertTrue(sender.send_to(receiver, 'Hello', 20))
    self.assertEqual(receiver.inbox, [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 20, 'time': timestamp, 'state': 'unread'}])
```

**test_send_to_5**: `stated`
- reason: A programmer following the docstring would send a 20-size email into an empty 30-capacity inbox, get True, and store the dict in the documented format, which is what the test checks.

```python
def test_send_to_5(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 30)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertTrue(sender.send_to(receiver, 'bye', 20))
    self.assertEqual(receiver.inbox, [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'bye', 'size': 20, 'time': timestamp, 'state': 'unread'}])
```

## Method `fetch`

### Docstring

```python
def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        >>> receiver.fetch()
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'read'}

        """
```

### Reference code (`solution_code`)

```python
def fetch(self):
        if len(self.inbox) == 0:
            return None
        for i in range(len(self.inbox)):
            if self.inbox[i]['state'] == "unread":
                self.inbox[i]['state'] = "read"
                return self.inbox[i]
        return None
```

### Tests (`EmailClientTestFetch`)

**test_fetch**: `stated`
- reason: The docstring says fetch returns the first unread email and marks it as read, which is exactly what the test checks with a single unread message.

```python
def test_fetch(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receiver.inbox = [
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
         'time': timestamp, 'state': 'unread'}]
    self.assertEqual(receiver.fetch(), {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time':timestamp, 'state': 'read'})
```

**test_fetch_2**: `unstated`
- reason: The docstring only describes returning the first unread email, so a programmer could reasonably return an empty dict or raise an error when the inbox is empty, and the test expects None.
- missing: The docstring should state what the method returns when no unread email exists, such as None or an empty value, and whether it raises an error.

```python
def test_fetch_2(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertEqual(receiver.fetch(),None)
```

**test_fetch_3**: `unstated`
- reason: The docstring only describes returning the first unread email, so it never says what to return when the inbox has no unread emails, which is the case this test checks (expects None).
- missing: The docstring should state the return value when no email is unread (for example, whether it returns None, an empty value, or raises an error), and when the inbox is empty.

```python
def test_fetch_3(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receiver.inbox = [
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
         'time': timestamp, 'state': 'read'}]
    self.assertEqual(receiver.fetch(), None)
```

**test_fetch_4**: `stated`
- reason: The docstring says fetch returns the first unread email and marks it read, and a programmer following that would return the first unread entry in the inbox, which is what the test expects.

```python
def test_fetch_4(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receiver.inbox = [
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
         'time':  '2021-01-01 00:00:00', 'state': 'unread'},
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
         'time': timestamp, 'state': 'unread'}]
    self.assertEqual(receiver.fetch(), {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
         'time':  '2021-01-01 00:00:00', 'state': 'read'})
```

**test_fetch_5**: `stated`
- reason: The docstring says fetch returns the first unread email and marks it as read, which is exactly what the test checks when an already-read email comes before the unread one.

```python
def test_fetch_5(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receiver.inbox = [
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
         'time': '2021-01-01 00:00:00', 'state': 'read'},
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
         'time': timestamp, 'state': 'unread'}]
    self.assertEqual(receiver.fetch(), {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10,
         'time': timestamp, 'state': 'read'})
```

## Method `is_full_with_one_more_email`

### Docstring

```python
def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.is_full_with_one_more_email(10)
        False

        """
```

### Reference code (`solution_code`)

```python
def is_full_with_one_more_email(self, size):
        occupied_size = self.get_occupied_size()
        return True if occupied_size + size > self.capacity else False
```

### Tests (`EmailClientTestIsFullWithOneMoreEmail`)

**test_is_full_with_one_more_email**: `stated`
- reason: The docstring says the method returns True only when the box would be full after adding the email, and the test checks a small email into a box with plenty of room, which a programmer following that description would return False for, matching the docstring example.

```python
def test_is_full_with_one_more_email(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    self.assertFalse(receiver.is_full_with_one_more_email(10))
```

**test_is_full_with_one_more_email_2**: `stated`
- reason: The docstring defines the result as whether the box is full after adding an email of the given size, so a programmer would compute occupied plus size against capacity, which returns True for an empty zero-capacity box and a 10-unit email.

```python
def test_is_full_with_one_more_email_2(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 0)
    self.assertTrue(receiver.is_full_with_one_more_email(10))
```

**test_is_full_with_one_more_email_3**: `unstated`
- reason: The test expects that adding an email that brings the box exactly to capacity returns False, but a programmer reading "full after adding" could reasonably treat an exactly-full box as full and return True.
- missing: The docstring should say whether a mailbox whose total size would exactly equal its capacity counts as full, or only when the total would exceed capacity.

```python
def test_is_full_with_one_more_email_3(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 10)
    self.assertFalse(receiver.is_full_with_one_more_email(10))
```

**test_is_full_with_one_more_email_4**: `stated`
- reason: The docstring says the method reports whether the box is full after adding an email of the given size, so a programmer would compare current occupied size plus the new size against capacity, and an oversized email into an empty box should return True.

```python
def test_is_full_with_one_more_email_4(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 10)
    self.assertTrue(receiver.is_full_with_one_more_email(20))
```

**test_is_full_with_one_more_email_5**: `unstated`
- reason: The test expects False when the incoming email brings the total exactly to capacity, but the docstring says only "full" without saying whether reaching capacity counts as full, so a programmer could reasonably return True.
- missing: The docstring should state whether a box whose occupied size plus the new email's size exactly equals its capacity counts as full or not full.

```python
def test_is_full_with_one_more_email_5(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 20)
    self.assertFalse(receiver.is_full_with_one_more_email(20))
```

## Method `get_occupied_size`

### Docstring

```python
def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': datetime.now, 'state': 'unread'}]
        >>> sender.get_occupied_size()
        10

        """
```

### Reference code (`solution_code`)

```python
def get_occupied_size(self):
        occupied_size = 0
        for email in self.inbox:
            occupied_size += email["size"]
        return occupied_size
```

### Tests (`EmailClientTestGetOccupiedSize`)

**test_get_occupied_size**: `stated`
- reason: The docstring says the method returns the total size of the emails in the inbox, so a programmer summing the `size` fields would get 10, which is what the test expects.

```python
def test_get_occupied_size(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': datetime.now, 'state': 'unread'}]
    self.assertEqual(sender.get_occupied_size(), 10)
```

**test_get_occupied_size_2**: `stated`
- reason: The docstring defines the result as the total size of all emails in the inbox, so an empty inbox naturally gives a total of 0, which is what the test expects.

```python
def test_get_occupied_size_2(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    sender.inbox =[]
    self.assertEqual(sender.get_occupied_size(), 0)
```

**test_get_occupied_size_3**: `stated`
- reason: The docstring says the method returns the total size of the emails in the inbox, so summing the sizes of the single email (20) gives the expected result, and the test's int 20 equals a float 20.0 under assertEqual.

```python
def test_get_occupied_size_3(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    sender.inbox = [
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 20,
         'time': datetime.now, 'state': 'unread'}]
    self.assertEqual(sender.get_occupied_size(), 20)
```

**test_get_occupied_size_4**: `stated`
- reason: The docstring says the method returns the total size of all emails in the inbox, so a programmer would sum the sizes of every email, which gives the expected 50 for two emails of sizes 20 and 30.

```python
def test_get_occupied_size_4(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    sender.inbox = [
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 20,
         'time': datetime.now, 'state': 'unread'},
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 30,
         'time': datetime.now, 'state': 'unread'}]
    self.assertEqual(sender.get_occupied_size(), 50)
```

**test_get_occupied_size_5**: `stated`
- reason: The docstring says the method returns the total size of all emails in the inbox, so a programmer would sum the sizes of the emails, which gives the expected 80 for this test.

```python
def test_get_occupied_size_5(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    sender.inbox = [
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 20,
         'time': datetime.now, 'state': 'unread'},
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 60,
         'time': datetime.now, 'state': 'unread'}]
    self.assertEqual(sender.get_occupied_size(), 80)
```

## Method `clear_inbox`

### Docstring

```python
def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        >>> receiver.clear_inbox(30)
        >>> receiver.inbox
        [{'size': 15}]

        """
```

### Reference code (`solution_code`)

```python
def clear_inbox(self, size):
        if len(self.addr) == 0:
            return
        freed_space = 0
        while freed_space < size and self.inbox:
            email = self.inbox[0]
            freed_space += email['size']
            del self.inbox[0]
```

### Tests (`EmailClientTestClearInbox`)

**test_clear_inbox**: `stated`
- reason: The docstring example uses the same inbox and size (30) and shows the oldest emails removed until the freed space reaches the requested size, leaving the 15-size email, which is exactly what the test asserts.

```python
def test_clear_inbox(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
    receiver.clear_inbox(30)
    self.assertEqual(receiver.inbox, [{'size': 15}])
```

**test_clear_inbox_2**: `unstated`
- reason: The docstring says clear_inbox deletes the oldest emails to free space, so a programmer would delete them, but the test expects no change when the client's address is empty, which the docstring never mentions.
- missing: The docstring should state what happens when the email client has no address (for example, that it returns without removing any emails), since this edge case overrides the normal deletion behaviour.

```python
def test_clear_inbox_2(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('', 50)
    receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
    self.assertEqual(receiver.clear_inbox(30),None)
    self.assertEqual(receiver.inbox, [{'size': 10},{'size': 20},{'size': 15}])
```

**test_clear_inbox_3**: `stated`
- reason: The docstring says to delete the oldest emails until there is enough room for the given size, and a programmer following that would return None with no return value, which is what the test asserts.

```python
def test_clear_inbox_3(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    receiver.inbox = [{'size': 10}, {'size': 20}, {'size': 15}]
    self.assertEqual(receiver.clear_inbox(50), None)
```

**test_clear_inbox_4**: `stated`
- reason: The docstring says to delete the oldest emails until enough space is freed for the given size, so a programmer would remove all three emails (10+20+15 = 45) and leave the inbox empty, which is what the test expects.

```python
def test_clear_inbox_4(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    receiver.inbox = [{'size': 10}, {'size': 20}, {'size': 15}]
    receiver.clear_inbox(45)
    self.assertEqual(receiver.inbox, [])
```

**test_clear_inbox_5**: `stated`
- reason: The docstring says to delete the oldest emails until enough space is freed for the given size, which means removing the first email (size 10) and stopping once that meets the requested size, matching the test's expected remaining inbox.

```python
def test_clear_inbox_5(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    receiver.inbox = [{'size': 10}, {'size': 20}, {'size': 15}]
    receiver.clear_inbox(10)
    self.assertEqual(receiver.inbox, [{'size': 20}, {'size': 15}])
```

## Tests in no method's test class

### `EmailClientTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    sender = EmailClient('sender@example.com', 100)
    receiver = EmailClient('receiver@example.com', 50)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.assertTrue(sender.send_to(receiver, 'Hello', 10))
    self.assertEqual(receiver.inbox[0], {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': timestamp, 'state': 'unread'})
    self.assertEqual(receiver.fetch(), {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': timestamp, 'state': 'read'})
    self.assertFalse(receiver.is_full_with_one_more_email(10))
    self.assertEqual(receiver.get_occupied_size(), 10)
    receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
    receiver.clear_inbox(30)
    self.assertEqual(receiver.inbox, [{'size': 15}])
```
