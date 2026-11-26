# ClassEval_42

## Skeleton (what the agent sees)

```python
class Hotel:
    """
    This is a class as hotel management system, managing the booking, check-in, check-out, and availability of rooms in a hotel with different room types.
    """

    def __init__(self, name, rooms):
        """
        Initialize the three fields in Hotel System.
        name is the hotel name.
        available_rooms stores the remaining rooms in the hotel
        booked_rooms stores the rooms that have been booked and the person's name who booked rooms.
        >>> hotel.name
        'peace hotel'
        >>> hotel.available_rooms
        available_rooms = {'single': 5, 'double': 3}
        >>> hotel.booked_rooms
        {'single': {'guest 1': 2, 'guest 2':1}, 'double': {'guest1': 1}}
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        """
        Check if there are any rooms of the specified type available.
        if rooms are adequate, modify available_rooms and booked_rooms and finish booking, or fail to book otherwise.
        :param room_type: str
        :param room_number: int, the expected number of specified type rooms to be booked
        :param name: str, guest name
        :return: if number of rooms about to be booked doesn't exceed the remaining rooms, return str 'Success!'
                if exceeds but quantity of available rooms is not equal to zero, return int(the remaining quantity of this room type).
                if exceeds and quantity is zero or the room_type isn't in available_room, return False.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, 'guest 1')
        'Success!'
        >>> hotel.book_room('single', 5, 'guest 1')
        4
        >>> hotel.book_room('single', 4, 'guest 1')
        'Success!'
        >>> hotel.book_room('single', 1, 'guest 1')
        False
        >>> hotel.book_room('triple', 1, 'guest 1')
        False
        """
    
    def check_in(self, room_type, room_number, name):
        """
        Check if the room of the specified type and number is booked by the person named name.
        Remove this name when check in successfuly(room_number is equal to specific person's booked_rooms. When the actual check in quantity (room_number) is less than the booked quantity, number in booked_rooms will be booked quantity minus actual quantity
        :param room_type: str, check in room type
        :param room_number: int, check in room number
        :param name: str, person name
        :return False: only if the room_type is not in the booked_rooms or room_number is higher than quantity in booked rooms.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, 'guest 1')
        'Success!'
        >>> hotel.check_in('single', 2, 'guest 1')
        False
        >>> hotel.check_in('single', 1, 'guest 1')
        >>> hotel.booked_rooms
        {'single': {}}
        """

    def check_out(self, room_type, room_number):
        """
        Check out rooms, add number for specific type in available_rooms.
        If room_type is new, add new type in available_rooms.
        :param room_type: str, check out room type
        :param room_number: int, check out room number
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.check_out('single', 2)
        >>> hotel.available_rooms
        {'single': 7, 'double': 3}
        >>> hotel.check_out('triple', 2)
        >>> hotel.available_rooms
        {'single': 7, 'double': 3, 'triple': 2}
        """

    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.get_available_rooms('single')
        5
        """
```

## Method `book_room`

### Docstring

```python
def book_room(self, room_type, room_number, name):
        """
        Check if there are any rooms of the specified type available.
        if rooms are adequate, modify available_rooms and booked_rooms and finish booking, or fail to book otherwise.
        :param room_type: str
        :param room_number: int, the expected number of specified type rooms to be booked
        :param name: str, guest name
        :return: if number of rooms about to be booked doesn't exceed the remaining rooms, return str 'Success!'
                if exceeds but quantity of available rooms is not equal to zero, return int(the remaining quantity of this room type).
                if exceeds and quantity is zero or the room_type isn't in available_room, return False.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, 'guest 1')
        'Success!'
        >>> hotel.book_room('single', 5, 'guest 1')
        4
        >>> hotel.book_room('single', 4, 'guest 1')
        'Success!'
        >>> hotel.book_room('single', 1, 'guest 1')
        False
        >>> hotel.book_room('triple', 1, 'guest 1')
        False
        """
```

### Reference code (`solution_code`)

```python
def book_room(self, room_type, room_number, name):
        # Check if there are any rooms of the specified type available
        if room_type not in self.available_rooms.keys():
            return False

        if room_number <= self.available_rooms[room_type]:
            # Book the room by adding it to the booked_rooms dictionary
            if room_type not in self.booked_rooms.keys():
                self.booked_rooms[room_type] = {}
            self.booked_rooms[room_type][name] = room_number
            self.available_rooms[room_type] -= room_number
            return "Success!"
        elif self.available_rooms[room_type] != 0:
            return self.available_rooms[room_type]
        else:
            return False
```

### Tests (`HotelTestBookRoom`)

setUp (runs before each test):

```python
def setUp(self):
    self.hotel = Hotel('peace hotel', {'single': 3, 'double': 2})
```

**test_book_room_1**: `unstated`
- reason: The docstring says booked_rooms is modified but never gives its structure, so a correct implementation could store bookings differently and fail the test's exact `{'single': {'guest 1': 2}}` assertion.
- missing: The docstring should specify the format of booked_rooms (e.g. a mapping from room type to a mapping from guest name to the number of rooms that guest booked) and that available_rooms for that type is reduced by the number booked.

```python
def test_book_room_1(self):
    result = self.hotel.book_room('single', 2, 'guest 1')
    self.assertEqual(result, 'Success!')
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}})
    self.assertEqual(self.hotel.available_rooms, {'single': 1, 'double': 2})
```

**test_book_room_2**: `stated`
- reason: The docstring explicitly says that returning False is the result when the room_type isn't in available_room, and failing to book implies no changes, so a programmer following it would return False and leave both dictionaries untouched.

```python
def test_book_room_2(self):
    result = self.hotel.book_room('triple', 2, 'guest 1')
    self.assertFalse(result)
    self.assertEqual(self.hotel.booked_rooms, {})
    self.assertEqual(self.hotel.available_rooms, {'single': 3, 'double': 2})
```

**test_book_room_3**: `unstated`
- reason: The return value of 1 matches the docstring's "exceeds but quantity not zero" rule, but the test also asserts the exact nested structure of `booked_rooms` (room type mapping to guest name to count), which the docstring never describes.
- missing: The docstring should specify the structure of `booked_rooms` (e.g., keyed first by room type, then by guest name, with the booked count as value) and state that a failed or partial booking leaves `booked_rooms` unchanged.

```python
def test_book_room_3(self):
    self.hotel.book_room('single', 2, 'guest 1')
    result = self.hotel.book_room('single', 2, 'guest 2')
    self.assertEqual(result, 1)
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}})
    self.assertEqual(self.hotel.available_rooms, {'single': 1, 'double': 2})
```

**test_book_room_4**: `unstated`
- reason: The docstring says the method returns 'Success!' and updates booked_rooms, but it never describes the structure of booked_rooms, which this test checks as a dict nested by room type and then by guest name.
- missing: The docstring should state the layout of booked_rooms and available_rooms, including that booked_rooms maps each room type to a dict of guest name to number of rooms booked, and that available_rooms maps each room type to its remaining count.

```python
def test_book_room_4(self):
    self.hotel.book_room('single', 2, 'guest 1')
    result = self.hotel.book_room('single', 1, 'guest 2')
    self.assertEqual(result, 'Success!')
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2, 'guest 2': 1}})
    self.assertEqual(self.hotel.available_rooms, {'double': 2, 'single': 0})
```

**test_book_room_5**: `unstated`
- reason: The docstring states the partial-availability return value (1 remaining), but it never says how `booked_rooms` should be structured, and this test asserts it is nested as room type → guest name → count.
- missing: The docstring should specify the layout of `booked_rooms` and `available_rooms` after a successful or partial booking, including whether booked entries are keyed by room type and then by guest name, and what value each holds.

```python
def test_book_room_5(self):
    self.hotel.book_room('single', 2, 'guest 1')
    result = self.hotel.book_room('single', 3, 'guest 2')
    self.assertEqual(result, 1)
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}})
    self.assertEqual(self.hotel.available_rooms, {'single': 1, 'double': 2})
```

**test_book_room_6**: `stated`
- reason: The docstring says that when the requested count exceeds the remaining rooms and the remaining quantity is zero, the method returns False, which is exactly what this test checks after all singles are booked.

```python
def test_book_room_6(self):
    self.hotel.book_room('single', 3, 'guest 1')
    result = self.hotel.book_room('single', 100, 'guest 1')
    self.assertFalse(result)
```

## Method `check_in`

### Docstring

```python
def check_in(self, room_type, room_number, name):
        """
        Check if the room of the specified type and number is booked by the person named name.
        Remove this name when check in successfuly(room_number is equal to specific person's booked_rooms. When the actual check in quantity (room_number) is less than the booked quantity, number in booked_rooms will be booked quantity minus actual quantity
        :param room_type: str, check in room type
        :param room_number: int, check in room number
        :param name: str, person name
        :return False: only if the room_type is not in the booked_rooms or room_number is higher than quantity in booked rooms.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.book_room('single', 1, 'guest 1')
        'Success!'
        >>> hotel.check_in('single', 2, 'guest 1')
        False
        >>> hotel.check_in('single', 1, 'guest 1')
        >>> hotel.booked_rooms
        {'single': {}}
        """
```

### Reference code (`solution_code`)

```python
def check_in(self, room_type, room_number, name):
        # Check if the room of the specified type and number is booked
        if room_type not in self.booked_rooms.keys():
            return False
        if name in self.booked_rooms[room_type]:
            if room_number > self.booked_rooms[room_type][name]:
                return False
            elif room_number == self.booked_rooms[room_type][name]:
                # Check in the room by removing it from the booked_rooms dictionary
                self.booked_rooms[room_type].pop(name)
            else:
                self.booked_rooms[room_type][name] -= room_number
```

### Tests (`HotelTestCheckIn`)

setUp (runs before each test):

```python
def setUp(self):
    self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2})
    self.hotel.booked_rooms = {'single': {'guest 1': 2}, 'double': {'guest 2': 1}}
```

**test_check_in_1**: `stated`
- reason: The docstring says that when the check-in quantity is less than the booked quantity, the remaining booked count becomes booked minus actual, which is exactly what this test checks (2 booked, 1 checked in, leaving 1).

```python
def test_check_in_1(self):
    self.hotel.check_in('single', 1, 'guest 1')
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 1}, 'double': {'guest 2': 1}})
```

**test_check_in_2**: `stated`
- reason: The docstring says check_in returns False when room_number exceeds the booked quantity, and the test checks exactly that case, so a programmer following it would return False.

```python
def test_check_in_2(self):
    self.assertFalse(self.hotel.check_in('single', 3, 'guest 1'))
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})
```

**test_check_in_3**: `unstated`
- reason: The docstring says the check is whether the named person booked the room, but its "False only if" clause lists just two failure cases, so it never says what happens when the type exists and the name has no booking under it. The test expects a falsy result with bookings unchanged, which the reference gives by returning None.
- missing: The docstring should state the outcome when the room type exists but the named person has no booking of that type: the return value (False or None) and that existing bookings stay unchanged.

```python
def test_check_in_3(self):
    self.assertFalse(self.hotel.check_in('double', 1, 'guest 1'))
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})
```

**test_check_in_4**: `stated`
- reason: The docstring says the guest's name is removed from booked_rooms when the check-in quantity equals the booked quantity, which is exactly what this test expects for the double room.

```python
def test_check_in_4(self):
    self.hotel.check_in('double', 1, 'guest 2')
    self.assertEqual(self.hotel.booked_rooms, {'double': {}, 'single': {'guest 1': 2}})
```

**test_check_in_5**: `stated`
- reason: The docstring says check_in returns False when room_number exceeds the booked quantity, and it only removes the name on a successful check-in, so a programmer would leave booked_rooms unchanged on this failed check-in, which is what the test asserts.

```python
def test_check_in_5(self):
    self.hotel.check_in('double', 2, 'guest 2')
    self.assertEqual(self.hotel.booked_rooms, {'double': {'guest 2': 1}, 'single': {'guest 1': 2}})
```

**test_check_in_6**: `stated`
- reason: The docstring says check_in returns False when the room_type is not in booked_rooms, which is exactly the case this test checks with an unknown room type.

```python
def test_check_in_6(self):
    res = self.hotel.check_in('abc', 1, 'guest 1')
    self.assertFalse(res)
```

## Method `check_out`

### Docstring

```python
def check_out(self, room_type, room_number):
        """
        Check out rooms, add number for specific type in available_rooms.
        If room_type is new, add new type in available_rooms.
        :param room_type: str, check out room type
        :param room_number: int, check out room number
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.check_out('single', 2)
        >>> hotel.available_rooms
        {'single': 7, 'double': 3}
        >>> hotel.check_out('triple', 2)
        >>> hotel.available_rooms
        {'single': 7, 'double': 3, 'triple': 2}
        """
```

### Reference code (`solution_code`)

```python
def check_out(self, room_type, room_number):
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number
```

### Tests (`HotelTestCheckOut`)

setUp (runs before each test):

```python
def setUp(self):
    self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2})
    self.hotel.booked_rooms = {'single': {'guest 1': 2}, 'double': {'guest 2': 1}}
```

**test_check_out_1**: `stated`
- reason: The docstring says check_out adds the given number to that room type's available count, which is what the test checks (3 single plus 1 gives 4), and a programmer would not touch booked_rooms since the docstring never mentions it.

```python
def test_check_out_1(self):
    self.hotel.check_out('single', 1)
    self.assertEqual(self.hotel.available_rooms, {'single': 4, 'double': 2})
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})
```

**test_check_out_2**: `unstated`
- reason: The docstring says check_out adds the count to available_rooms, which the test's available_rooms assertion matches, but it never says booked_rooms is left alone, which the test also asserts.
- missing: The docstring should state whether any other state (such as the per-guest booking records) is changed by a check-out, and that it is left unmodified when only the available count is updated.

```python
def test_check_out_2(self):
    self.hotel.check_out('single', 3)
    self.assertEqual(self.hotel.available_rooms, {'single': 6, 'double': 2})
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})
```

**test_check_out_3**: `stated`
- reason: The docstring says check_out adds the room number to available_rooms and creates a new room type entry when the type is new, which is what the test's available_rooms assertion checks, and it names no other state to change, so an implementation following it would leave booked_rooms alone and pass.

```python
def test_check_out_3(self):
    self.hotel.check_out('triple', 2)
    self.assertEqual(self.hotel.available_rooms, {'single': 3, 'double': 2, 'triple': 2})
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})
```

**test_check_out_4**: `unstated`
- reason: The docstring says check_out adds the room number to available_rooms, but it never says whether booked_rooms should change, and the test asserts booked_rooms stays exactly the same, so a programmer who also updates booked_rooms would fail.
- missing: The docstring should state whether the method touches any other state, such as the booked_rooms record, and if it does not, that only available_rooms is changed.

```python
def test_check_out_4(self):
    self.hotel.check_out('double', 1)
    self.assertEqual(self.hotel.available_rooms, {'single': 3, 'double': 3})
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})
```

**test_check_out_5**: `stated`
- reason: The docstring says check_out adds the returned room count to the existing available_rooms entry for that type, which is what the test's 2 + 2 = 4 expects, and it implies nothing else should change, so booked_rooms staying the same follows naturally.

```python
def test_check_out_5(self):
    self.hotel.check_out('double', 2)
    self.assertEqual(self.hotel.available_rooms, {'single': 3, 'double': 4})
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}, 'double': {'guest 2': 1}})
```

## Method `get_available_rooms`

### Docstring

```python
def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        >>> hotel = Hotel('peace hotel', {'single': 5, 'double': 3})
        >>> hotel.get_available_rooms('single')
        5
        """
```

### Reference code (`solution_code`)

```python
def get_available_rooms(self, room_type):
        return self.available_rooms[room_type]
```

### Tests (`HotelTestAvailableRooms`)

setUp (runs before each test):

```python
def setUp(self):
    self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2, 'triple': 2})
```

**test_get_available_rooms**: `stated`
- reason: The docstring says the method returns the remaining count for the given room type, and the test checks that a lookup of 'single' on a hotel initialised with 3 singles returns 3, which a programmer following the docstring would produce.

```python
def test_get_available_rooms(self):
    result = self.hotel.get_available_rooms('single')
    self.assertEqual(result, 3)
```

**test_get_available_rooms_2**: `stated`
- reason: The docstring says the method returns "the remaining number of this type rooms", so a programmer would subtract booked rooms from the initial count and return 1 after two of three singles are booked.

```python
def test_get_available_rooms_2(self):
    self.hotel.book_room('single', 2, 'guest 1')
    result = self.hotel.get_available_rooms('single')
    self.assertEqual(result, 1)
```

**test_get_available_rooms_3**: `stated`
- reason: The docstring says it returns the remaining number of rooms of a type, so a programmer would expect booking rooms to reduce that count, which is what this test checks (3 singles booked leaves 0).

```python
def test_get_available_rooms_3(self):
    self.hotel.book_room('single', 3, 'guest 1')
    result = self.hotel.get_available_rooms('single')
    self.assertEqual(result, 0)
```

**test_get_available_rooms_4**: `stated`
- reason: The docstring says the method returns the remaining count for the requested room type, so a programmer tracking per-type availability would return 2 for doubles after singles are booked.

```python
def test_get_available_rooms_4(self):
    self.hotel.book_room('single', 3, 'guest 1')
    result = self.hotel.get_available_rooms('double')
    self.assertEqual(result, 2)
```

**test_get_available_rooms_5**: `stated`
- reason: The docstring says the method returns the remaining count for the requested room type, so a programmer would return the untouched triple count (2) regardless of bookings of other types, which is what the test checks.

```python
def test_get_available_rooms_5(self):
    self.hotel.book_room('single', 3, 'guest 1')
    result = self.hotel.get_available_rooms('triple')
    self.assertEqual(result, 2)
```

## Tests in no method's test class

### `HotelTestMain`

setUp (runs before each test):

```python
def setUp(self) -> None:
    self.hotel = Hotel('Test Hotel', {'single': 3, 'double': 2})
```

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    result = self.hotel.book_room('single', 2, 'guest 1')
    self.assertEqual(result, 'Success!')
    self.assertEqual(self.hotel.booked_rooms, {'single': {'guest 1': 2}})
    self.assertEqual(self.hotel.available_rooms, {'single': 1, 'double': 2})

    self.hotel.check_in('single', 2, 'guest 1')
    self.assertEqual(self.hotel.booked_rooms, {'single': {}})
    self.assertEqual(self.hotel.available_rooms, {'single': 1, 'double': 2})

    self.hotel.check_out('single', 2)
    self.assertEqual(self.hotel.available_rooms, {'single': 3, 'double': 2})

    self.assertEqual(self.hotel.get_available_rooms('single'), 3)
```
