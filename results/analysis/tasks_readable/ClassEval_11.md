# ClassEval_11

## Skeleton (what the agent sees)

```python
class BitStatusUtil:
    """
    This is a utility class that provides methods for manipulating and checking status using bitwise operations.
    """

    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Status to be added,int.
        :return: The status after adding the status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2,4)
        6

        """

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: True if the current status contains the specified status,otherwise False,bool.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.has(6,2)
        True

        """

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after removing the specified status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.remove(6,2)
        4

        """

    @staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even,if not,raise ValueError.
        :param args: Parameters to be checked,list.
        :return: None.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: 3 not even
        """
```

## Method `add`

### Docstring

```python
def add(states, stat):
        """
        Add a status to the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Status to be added,int.
        :return: The status after adding the status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2,4)
        6

        """
```

### Reference code (`solution_code`)

```python
def add(states, stat):
        BitStatusUtil.check([states, stat])
        return states | stat
```

### Tests (`BitStatusUtilTestAdd`)

**test_add**: `stated`
- reason: The docstring's example `add(2,4)` returns `6`, which is exactly the value the test asserts, so a programmer following it would pass.

```python
def test_add(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.add(2, 4), 6)
```

**test_add_2**: `stated`
- reason: The docstring says add(states, stat) returns the combined status, and a programmer following the example (2 and 4 give 6) would return 2 when adding 0, which matches the test.

```python
def test_add_2(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.add(2, 0), 2)
```

**test_add_3**: `stated`
- reason: The docstring says to add the status to the current status, and for the zero-and-zero case both addition and bitwise OR give 0, so a programmer following it would pass.

```python
def test_add_3(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.add(0, 0), 0)
```

**test_add_4**: `stated`
- reason: The docstring says to add a status to the current status and gives add(2, 4) = 6, so a programmer would return 2 for add(0, 2), which is what the test expects.

```python
def test_add_4(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.add(0, 2), 2)
```

**test_add_5**: `unstated`
- reason: The docstring's only example (add(2,4) = 6) fits both arithmetic addition and bitwise OR, so a programmer could reasonably implement `states + stat`, which returns 4 for this test where the expected value is 2.
- missing: The docstring should say explicitly that combining statuses is a bitwise OR of the two integers, so that adding a flag already present leaves the value unchanged rather than summing it.

```python
def test_add_5(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.add(2, 2), 2)
```

## Method `has`

### Docstring

```python
@staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: True if the current status contains the specified status,otherwise False,bool.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.has(6,2)
        True

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def has(states, stat):
        BitStatusUtil.check([states, stat])
        return (states & stat) == stat
```

### Tests (`BitStatusUtilTestHas`)

**test_has**: `stated`
- reason: The docstring says `has` returns True when the current status contains the specified status, and its example `has(6,2)` returns True, which is exactly what the test asserts.

```python
def test_has(self):
    bit_status_util = BitStatusUtil()
    self.assertTrue(bit_status_util.has(6, 2))
```

**test_has_2**: `stated`
- reason: The docstring says `has` returns True only when the current status contains the specified status, so for 8 and 2 (no shared bit) a programmer would return False, which matches the test.

```python
def test_has_2(self):
    bit_status_util = BitStatusUtil()
    self.assertFalse(bit_status_util.has(8, 2))
```

**test_has_3**: `stated`
- reason: The docstring says `has` returns True when the current status contains the specified status, and 6 (binary 110) contains 4 (binary 100), so a programmer following it would return True.

```python
def test_has_3(self):
    bit_status_util = BitStatusUtil()
    self.assertTrue(bit_status_util.has(6, 4))
```

**test_has_4**: `stated`
- reason: The docstring defines `has` as returning True only when the current status contains all bits of the specified status and False otherwise, so a programmer would return False for 8 and 6, which share no bits.

```python
def test_has_4(self):
    bit_status_util = BitStatusUtil()
    self.assertFalse(bit_status_util.has(8, 6))
```

**test_has_5**: `stated`
- reason: The docstring says `has` returns True when the current status contains the specified status, and 6 contains 6, so a programmer following it would return True.

```python
def test_has_5(self):
    bit_status_util = BitStatusUtil()
    self.assertTrue(bit_status_util.has(6, 6))
```

## Method `remove`

### Docstring

```python
@staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Specified status,int.
        :return: The status after removing the specified status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.remove(6,2)
        4

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def remove(states, stat):
        BitStatusUtil.check([states, stat])
        if BitStatusUtil.has(states, stat):
            return states ^ stat
        return states
```

### Tests (`BitStatusUtilTestRemove`)

**test_remove**: `stated`
- reason: The docstring says remove should take the specified status out of the current status, and its example `remove(6,2)` returns `4`, which is exactly what the test asserts.

```python
def test_remove(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.remove(6, 2), 4)
```

**test_remove_2**: `unstated`
- reason: The docstring says to remove the specified status from the current status but never says what happens when that status is not currently set, which is the case this test checks (expects the input unchanged), so a naive XOR would return a different value.
- missing: If the specified status bit is not set in the current status, the method must return the current status unchanged instead of toggling that bit.

```python
def test_remove_2(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.remove(8, 2), 8)
```

**test_remove_3**: `stated`
- reason: The docstring says to remove the specified status bit from the current status, so a programmer would clear bit 4 from 6 (binary 110) to get 2, which is what the test expects, and the docstring example (6, 2) → 4 confirms the bit-clearing behaviour.

```python
def test_remove_3(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.remove(6, 4), 2)
```

**test_remove_4**: `unstated`
- reason: The docstring says to remove the specified status but never says what happens when that status is not currently set, so a programmer could reasonably toggle it or otherwise alter the value, while the test expects the input returned unchanged.
- missing: The docstring should state that if the status to remove is not already set in the current status, the function returns the current status unchanged.

```python
def test_remove_4(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.remove(8, 6), 8)
```

**test_remove_5**: `stated`
- reason: The docstring says to remove the specified status from the current status, so removing a status that is fully present (6 from 6) should leave 0, which is what the test expects.

```python
def test_remove_5(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.remove(6, 6), 0)
```

## Method `check`

### Docstring

```python
@staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even,if not,raise ValueError.
        :param args: Parameters to be checked,list.
        :return: None.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: 3 not even
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def check(args):
        for arg in args:
            if arg < 0:
                raise ValueError(f"{arg} must be greater than or equal to 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")
```

### Tests (`BitStatusUtilTestCheck`)

**test_check**: `stated`
- reason: The docstring says every argument must be non-negative and even and that a ValueError is raised otherwise, so a programmer would implement a check that returns silently for the valid input [2], which is what the test asserts.

```python
def test_check(self):
    bit_status_util = BitStatusUtil()
    bit_status_util.check([2])
```

**test_check_2**: `stated`
- reason: The docstring says `check` must raise ValueError when an argument is not even, and 3 is odd, so the test's expected ValueError follows directly from the documented behaviour.

```python
def test_check_2(self):
    bit_status_util = BitStatusUtil()
    with self.assertRaises(ValueError):
        bit_status_util.check([3])
```

**test_check_3**: `stated`
- reason: The docstring says that arguments must be greater than or equal to 0 and even, and otherwise a ValueError is raised, so a programmer following it would raise for the negative input in this test.

```python
def test_check_3(self):
    bit_status_util = BitStatusUtil()
    with self.assertRaises(ValueError):
        bit_status_util.check([-1])
```

**test_check_4**: `stated`
- reason: The docstring says that a non-even argument raises ValueError, and the test passes [2, 3, 4], where 3 is odd, so a programmer following the docstring would raise ValueError and pass.

```python
def test_check_4(self):
    bit_status_util = BitStatusUtil()
    with self.assertRaises(ValueError):
        bit_status_util.check([2, 3, 4])
```

**test_check_5**: `stated`
- reason: The docstring says that non-even arguments must raise ValueError, and the test passes a list containing odd values, so a correct implementation would raise.

```python
def test_check_5(self):
    bit_status_util = BitStatusUtil()
    with self.assertRaises(ValueError):
        bit_status_util.check([2, 3, 4, 5])
```

## Tests in no method's test class

### `BitStatusUtilTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    bit_status_util = BitStatusUtil()
    self.assertEqual(bit_status_util.add(2, 4), 6)
    self.assertTrue(bit_status_util.has(6, 2))
    self.assertEqual(bit_status_util.remove(6, 2), 4)
    with self.assertRaises(ValueError):
        bit_status_util.check([2, 3, 4])
```
