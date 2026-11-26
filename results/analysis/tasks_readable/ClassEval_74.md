# ClassEval_74

## Skeleton (what the agent sees)

```python
class Server:
    """
    This is a class as a server, which handles a white list, message sending and receiving, and information display.
    """


    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}



    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :param addr: int, address to be deleted
        :return: new whitelist, return False if the address does not exist
        >>> server.add_white_list(88)
        >>> server.del_white_list(88)
        []
        """

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the infomation; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """

    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """

    def show(self, type):
        """
        Returns struct of the specified type
        :param type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: if type is equal to 'send' or 'receive', return the corresponding struct; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        >>> server.send({"addr":66,"content":"ABC"})
        >>> server.show("send")
        {"addr":66,"content":"ABC"}
        """
```

## Method `add_white_list`

### Docstring

```python
def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """
```

### Reference code (`solution_code`)

```python
def add_white_list(self, addr):
        if addr in self.white_list:
            return False
        else:
            self.white_list.append(addr)
            return self.white_list
```

### Tests (`ServerTestAddWhiteList`)

**test_add_white_list_1**: `stated`
- reason: The docstring says adding an address appends it to the whitelist and gives the example `add_white_list(88)` returning `[88]`, so a programmer following it would leave `white_list` equal to `[88]`, which is what the test checks.

```python
def test_add_white_list_1(self):
    server = Server()
    server.add_white_list(88)
    self.assertEqual(server.white_list, [88])
```

**test_add_white_list_2**: `stated`
- reason: The docstring says adding an existing address should return False, which is exactly what the test checks when 88 is added a second time.

```python
def test_add_white_list_2(self):
    server = Server()
    server.add_white_list(88)
    self.assertEqual(server.add_white_list(88), False)
```

**test_add_white_list_3**: `stated`
- reason: The docstring says the method should return False when the address already exists, which is exactly what the test checks when 11 is added a second time.

```python
def test_add_white_list_3(self):
    server = Server()
    server.add_white_list(88)
    server.add_white_list(11)
    self.assertEqual(server.add_white_list(11), False)
```

**test_add_white_list_4**: `stated`
- reason: The docstring says the address is added to the whitelist and the example shows the resulting list, so a programmer following it would produce `[11]` after adding 11 to an empty whitelist.

```python
def test_add_white_list_4(self):
    server = Server()
    server.add_white_list(11)
    self.assertEqual(server.white_list, [11])
```

**test_add_white_list_5**: `stated`
- reason: The docstring says adding an address that already exists returns False, which is exactly what the test checks when 22 is added a second time.

```python
def test_add_white_list_5(self):
    server = Server()
    server.add_white_list(88)
    server.add_white_list(11)
    server.add_white_list(22)
    self.assertEqual(server.add_white_list(22), False)
```

## Method `del_white_list`

### Docstring

```python
def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :param addr: int, address to be deleted
        :return: new whitelist, return False if the address does not exist
        >>> server.add_white_list(88)
        >>> server.del_white_list(88)
        []
        """
```

### Reference code (`solution_code`)

```python
def del_white_list(self, addr):
        if addr not in self.white_list:
            return False
        else:
            self.white_list.remove(addr)
            return self.white_list
```

### Tests (`ServerTestDelWhiteList`)

**test_del_white_list_1**: `stated`
- reason: The docstring says the address is removed from the whitelist, and its example shows the list empty afterward, so a programmer following it would leave `white_list` as an empty list, matching the test.

```python
def test_del_white_list_1(self):
    server = Server()
    server.add_white_list(88)
    server.del_white_list(88)
    self.assertEqual(server.white_list, [])
```

**test_del_white_list_2**: `stated`
- reason: The docstring says to return False when the address does not exist, and the test deletes an address from an empty whitelist and expects False, which a programmer following the docstring would produce.

```python
def test_del_white_list_2(self):
    server = Server()
    self.assertEqual(server.del_white_list(88), False)
```

**test_del_white_list_3**: `stated`
- reason: The docstring explicitly says that deleting an address that does not exist returns False, which is exactly what the test checks with an empty whitelist.

```python
def test_del_white_list_3(self):
    server = Server()
    self.assertEqual(server.del_white_list(11), False)
```

**test_del_white_list_4**: `stated`
- reason: The docstring says the method returns False when the address does not exist, which is exactly what the test checks when deleting from an empty whitelist.

```python
def test_del_white_list_4(self):
    server = Server()
    self.assertEqual(server.del_white_list(22), False)
```

**test_del_white_list_5**: `stated`
- reason: The docstring says deleting a non-existent address should return False, which is exactly what the test checks when it deletes an address absent from the whitelist.

```python
def test_del_white_list_5(self):
    server = Server()
    server.add_white_list(11)
    self.assertEqual(server.del_white_list(22), False)
```

## Method `recv`

### Docstring

```python
def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the infomation; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
```

### Reference code (`solution_code`)

```python
def recv(self, info):
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return -1
        addr = info["addr"]
        content = info["content"]
        if addr not in self.white_list:
            return False
        else:
            self.receive_struct = {"addr": addr, "content": content}
            return self.receive_struct["content"]
```

### Tests (`ServerTestRecv`)

**test_recv_1**: `unstated`
- reason: The docstring says recv returns the content for a whitelisted address, but the test checks that the method also saves the received address and content as instance state, which the docstring never mentions.
- missing: The docstring should say that when a message is accepted, its address and content are also saved on the object as state that a caller can inspect later, not only returned.

```python
def test_recv_1(self):
    server = Server()
    server.add_white_list(88)
    server.recv({"addr": 88, "content": "abc"})
    self.assertEqual(server.receive_struct, {"addr": 88, "content": "abc"})
```

**test_recv_2**: `unstated`
- reason: The docstring says a non-whitelisted address returns False and the content is not received, but it never says whether the stored `receive_struct` must stay in its initial empty state, which the test asserts.
- missing: When the address is not on the whitelist, the method must leave any internal record of received messages unchanged, so it stays at whatever its initial value was.

```python
def test_recv_2(self):
    server = Server()
    server.add_white_list(88)
    flag = server.recv({"addr": 66, "content": "abc"})
    self.assertEqual(server.receive_struct, {})
    self.assertEqual(flag, False)
```

**test_recv_3**: `unstated`
- reason: The docstring never mentions input validation, so a programmer following it could reasonably return False for a non-dict argument like a list, while the test expects -1 and an unchanged receive_struct.
- missing: The docstring should state what happens when the argument is not a dict or lacks the "addr" or "content" keys: the method returns -1 and leaves the stored receive state unchanged, rather than returning False.

```python
def test_recv_3(self):
    server = Server()
    flag = server.recv([88])
    self.assertEqual(server.receive_struct, {})
    self.assertEqual(flag, -1)
```

**test_recv_4**: `unstated`
- reason: The docstring only describes whitelisted versus non-whitelisted addresses, returning content or False, and says nothing about malformed input, so the test's expectation of -1 and an unchanged `receive_struct` for a message missing its content key is not specified.
- missing: The docstring should state that if the info is not a dict or lacks the "addr" or "content" key, the method returns -1 and leaves the stored receive state unchanged, regardless of whitelist membership.

```python
def test_recv_4(self):
    server = Server()
    flag = server.recv({"addr": 88})
    self.assertEqual(server.receive_struct, {})
    self.assertEqual(flag, -1)
```

**test_recv_5**: `unstated`
- reason: The docstring only describes whitelist acceptance and returning False for rejected addresses, so it never says that a dict missing the address key should return -1 and leave the stored state empty, which is what this test checks.
- missing: The docstring should state that if the input is not a dict or lacks the address or content key, the method returns -1 and does not change the stored receive record.

```python
def test_recv_5(self):
    server = Server()
    flag = server.recv({"content": "abc"})
    self.assertEqual(server.receive_struct, {})
    self.assertEqual(flag, -1)
```

## Method `send`

### Docstring

```python
def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
```

### Reference code (`solution_code`)

```python
def send(self, info):
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return "info structure is not correct"
        self.send_struct = {"addr": info["addr"], "content": info["content"]}
```

### Tests (`ServerTestSend`)

**test_send_1**: `stated`
- reason: The docstring says `send` takes a dict with address and content and gives the example that sets `self.send_struct` to that dict, which is exactly what this test checks with a valid input.

```python
def test_send_1(self):
    server = Server()
    server.send({"addr": 88, "content": "abc"})
    self.assertEqual(server.send_struct, {"addr": 88, "content": "abc"})
```

**test_send_2**: `unstated`
- reason: The docstring says an error string is returned when sending fails, but the test requires one exact message text for an input that lacks a required key, and the docstring does not give that text.
- missing: The docstring should state the exact error string to return when the input is not a dict or is missing any required key.

```python
def test_send_2(self):
    server = Server()
    flag = server.send({"addr": 88})
    self.assertEqual(flag, "info structure is not correct")
```

**test_send_3**: `unstated`
- reason: The docstring says an error message is returned on failure but does not say that a missing key triggers it or give the exact message, so a programmer could reasonably return a different string or treat this input as valid.
- missing: The docstring should state exactly which inputs count as malformed (non-dict, or a dict lacking either required key) and the exact error string to return for them.

```python
def test_send_3(self):
    server = Server()
    flag = server.send({"content": "abc"})
    self.assertEqual(flag, "info structure is not correct")
```

**test_send_4**: `unstated`
- reason: The docstring says an error string is returned for bad input, but the test checks one exact wording, which a correct implementation could reasonably word differently.
- missing: The docstring should give the exact error message text returned when the input is not a dict or lacks the required keys.

```python
def test_send_4(self):
    server = Server()
    flag = server.send([])
    self.assertEqual(flag, "info structure is not correct")
```

**test_send_5**: `stated`
- reason: The docstring says send takes a dict with address and content and its example shows `self.send_struct` being set to that dict, which is exactly what the test checks with a valid input.

```python
def test_send_5(self):
    server = Server()
    server.send({"addr": 66, "content": "abc"})
    self.assertEqual(server.send_struct, {"addr": 66, "content": "abc"})
```

## Method `show`

### Docstring

```python
def show(self, type):
        """
        Returns struct of the specified type
        :param type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: if type is equal to 'send' or 'receive', return the corresponding struct; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        >>> server.send({"addr":66,"content":"ABC"})
        >>> server.show("send")
        {"addr":66,"content":"ABC"}
        """
```

### Reference code (`solution_code`)

```python
def show(self, type):
        if type == "send":
            return self.send_struct
        elif type == "receive":
            return self.receive_struct
        else:
            return False
```

### Tests (`ServerTestShow`)

**test_show_1**: `stated`
- reason: The docstring says `show("send")` returns the send struct, and the test sends one message, then receives another, and expects the send struct back, which is what a programmer would implement from that description.

```python
def test_show_1(self):
    server = Server()
    server.add_white_list(66)
    server.send({"addr": 88, "content": "abc"})
    server.recv({"addr": 66, "content": "ABC"})
    self.assertEqual(server.show("send"), {"addr": 88, "content": "abc"})
```

**test_show_2**: `stated`
- reason: The docstring says `show("receive")` returns the receive struct, and the test expects the struct from the most recent successful receive, which a programmer following the docstring would return.

```python
def test_show_2(self):
    server = Server()
    server.add_white_list(66)
    server.send({"addr": 88, "content": "abc"})
    server.recv({"addr": 66, "content": "ABC"})
    self.assertEqual(server.show("receive"), {"addr": 66, "content": "ABC"})
```

**test_show_3**: `stated`
- reason: The docstring says that any type other than 'send' or 'receive' returns False, and the test passes an unrecognised string and expects False.

```python
def test_show_3(self):
    server = Server()
    server.add_white_list(66)
    server.send({"addr": 88, "content": "abc"})
    server.recv({"addr": 66, "content": "ABC"})
    self.assertEqual(server.show("abcdefg"), False)
```

**test_show_4**: `stated`
- reason: The docstring says `show("send")` returns the struct of the send type, and the test sends one struct and then checks that `show("send")` returns it, which a programmer following the docstring would pass.

```python
def test_show_4(self):
    server = Server()
    server.add_white_list(66)
    server.send({"addr": 11, "content": "abc"})
    server.recv({"addr": 66, "content": "ABC"})
    self.assertEqual(server.show("send"), {"addr": 11, "content": "abc"})
```

**test_show_5**: `stated`
- reason: The docstring says `show("send")` returns the struct for send, and a programmer would return the most recently sent struct, which is what the test checks even though the address 22 is not on the whitelist.

```python
def test_show_5(self):
    server = Server()
    server.add_white_list(66)
    server.send({"addr": 22, "content": "abc"})
    server.recv({"addr": 66, "content": "ABC"})
    self.assertEqual(server.show("send"), {"addr": 22, "content": "abc"})
```

## Tests in no method's test class

### `ServerTest`

**test_server**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_server(self):
    server = Server()
    server.add_white_list(88)
    self.assertEqual(server.white_list, [88])
    server.del_white_list(88)
    self.assertEqual(server.white_list, [])
    server.add_white_list(88)
    server.recv({"addr": 88, "content": "abc"})
    self.assertEqual(server.receive_struct, {"addr": 88, "content": "abc"})
    server.send({"addr": 66, "content": "ABC"})
    self.assertEqual(server.send_struct, {"addr": 66, "content": "ABC"})
    server.recv({"addr": 88, "content": "abc"})
    self.assertEqual(server.show("receive"), {"addr": 88, "content": "abc"})
```
