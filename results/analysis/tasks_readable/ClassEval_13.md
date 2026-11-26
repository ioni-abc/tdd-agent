# ClassEval_13

## Skeleton (what the agent sees)

```python
class BookManagement:
    """
    This is a class as managing books system, which supports to add and remove books from the inventory dict, view the inventory, and check the quantity of a specific book.
    """

    def __init__(self):
        """
        Initialize the inventory of Book Manager.
        """
        self.inventory = {}

    def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """

    def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1}
        """

    def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.invenroty
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        0
        """
```

## Method `add_book`

### Docstring

```python
def add_book(self, title, quantity=1):
        """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
```

### Reference code (`solution_code`)

```python
def add_book(self, title, quantity=1):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity
```

### Tests (`BookManagementTestAddBook`)

**test_add_book_1**: `stated`
- reason: The docstring says quantity defaults to 1 and that books are added to the inventory keyed by title, so a programmer following it would produce `{"book1": 1}`.

```python
def test_add_book_1(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1")
    self.assertEqual({"book1": 1}, bookManagement.inventory)
```

**test_add_book_2**: `other_inconsistency`
- reason: The test never calls add_book; it only checks that a freshly constructed BookManagement has an empty inventory, which is constructor behaviour filed under the wrong method.

```python
def test_add_book_2(self):
    bookManagement = BookManagement()
    self.assertEqual({}, bookManagement.inventory)
```

**test_add_book_3**: `stated`
- reason: The docstring says add_book adds one or several books to the inventory with a quantity defaulting to 1, so a programmer would expect repeated calls to accumulate counts, which is what the test checks.

```python
def test_add_book_3(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1")
    bookManagement.add_book("book1", 2)
    self.assertEqual({"book1": 3}, bookManagement.inventory)
```

**test_add_book_4**: `unstated`
- reason: A programmer reading "add one or several books to inventory sorted by book title" would not know that the inventory must be a dict mapping each title to its count, so a correct implementation using another structure (such as a list of titles) would fail this test.
- missing: The docstring should state the type and layout of `self.inventory`, including that each key is a book title and its value is the number of copies, so that adding a quantity increases that count.

```python
def test_add_book_4(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    self.assertEqual({"book1": 2}, bookManagement.inventory)
```

**test_add_book_5**: `stated`
- reason: The docstring says add_book adds one or several books to the inventory with a default quantity of 1, so a programmer would accumulate the count when a title is added again, giving the expected 3.

```python
def test_add_book_5(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    bookManagement.add_book("book1")
    self.assertEqual({"book1": 3}, bookManagement.inventory)
```

## Method `remove_book`

### Docstring

```python
def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
```

### Reference code (`solution_code`)

```python
def remove_book(self, title, quantity):
        if title not in self.inventory or self.inventory[title] < quantity:
            raise False
        self.inventory[title] -= quantity
        if self.inventory[title] == 0:
            del (self.inventory[title])
```

### Tests (`BookManagementTestRemoveBook`)

setUp (runs before each test):

```python
def setUp(self) -> None:
    self.bookManagement = BookManagement()
    self.bookManagement.add_book("book1", 2)
    self.bookManagement.add_book("book2")
```

**test_remove_book_1**: `unstated`
- reason: The docstring says only that books are removed from inventory, so a programmer could leave a title in the inventory with a count of 0, whereas the test expects the title to be deleted once its count reaches zero.
- missing: The docstring should state that when a removal brings a title's count to zero, the title is deleted from the inventory entirely rather than kept with a zero count.

```python
def test_remove_book_1(self):
    self.bookManagement.remove_book("book1", 2)
    self.assertEqual(self.bookManagement.inventory, {"book2": 1})
```

**test_remove_book_2**: `stated`
- reason: The docstring says the method removes one or several books from the inventory, so a programmer would decrement the named title's count by the given quantity, which is what this test checks.

```python
def test_remove_book_2(self):
    self.bookManagement.remove_book("book1", 1)
    self.assertEqual(self.bookManagement.inventory, {"book1": 1, "book2": 1})
```

**test_remove_book_3**: `unstated`
- reason: The docstring only says to raise on "invalid input" without saying that a title absent from the inventory counts as invalid, so a correct implementation could silently do nothing and fail this test.
- missing: The docstring should say that removing a title that is not in the inventory (and removing more copies than are held) must raise an exception.

```python
def test_remove_book_3(self):
    with self.assertRaises(Exception):
        self.bookManagement.remove_book("book3", 1)
```

**test_remove_book_4**: `unstated`
- reason: The docstring only says to "raise false" on invalid input, which does not clearly say that asking to remove more copies than are in stock is invalid, so a programmer could reasonably let it succeed and fail the test.
- missing: The docstring should state that removing a title that is not in the inventory, or a quantity greater than the number of copies currently held, must raise an error and leave the inventory unchanged.

```python
def test_remove_book_4(self):
    with self.assertRaises(Exception):
        self.bookManagement.remove_book("book2", 2)
```

**test_remove_book_5**: `unstated`
- reason: The docstring says only "Raise false while get invalid input" without saying that asking to remove more copies than are in stock is invalid, so a correct implementation might not raise and fail this test.
- missing: The docstring should state that removing a quantity greater than the copies currently held for a title (including a title not in inventory) must raise an exception, and that removing exactly the held count removes the title entirely.

```python
def test_remove_book_5(self):
    with self.assertRaises(Exception):
        self.bookManagement.remove_book("book2", 5)
```

## Method `view_inventory`

### Docstring

```python
def view_inventory(self):
        """
        Get the inventory of the Book Management.
        :return self.inventory: dictionary, {title(str): quantity(int), ...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1}
        """
```

### Reference code (`solution_code`)

```python
def view_inventory(self):
        return self.inventory
```

### Tests (`BookManagementTestViewInventory`)

**test_view_inventory_1**: `unstated`
- reason: The test relies on `add_book` using a quantity of 1 when the argument is omitted, but neither this docstring nor its example says what the default is, so a correct implementation could fail.
- missing: The docstring of the method that adds items should state the default quantity used when the caller omits the count argument, and what value it records in the inventory.

```python
def test_view_inventory_1(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    bookManagement.add_book("book2")
    expected = {"book1": 2, "book2": 1}
    self.assertEqual(expected, bookManagement.inventory)
```

**test_view_inventory_2**: `stated`
- reason: A programmer following the docstring would return the inventory dictionary of titles to quantities, and a freshly constructed manager with no books naturally has an empty one, so the test's expected `{}` is implied.

```python
def test_view_inventory_2(self):
    bookManagement = BookManagement()
    expected = {}
    self.assertEqual(expected, bookManagement.inventory)
```

**test_view_inventory_3**: `unstated`
- reason: The test relies on `add_book` defaulting the quantity to 1 when none is given, which the `view_inventory` docstring never mentions; its example always passes an explicit quantity.
- missing: The docstring should state that adding a book without a quantity records it with a quantity of 1, and that an explicit quantity overrides this default.

```python
def test_view_inventory_3(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    bookManagement.add_book("book2")
    expected = {"book1": 2, "book2": 1}
    self.assertEqual(expected, bookManagement.inventory)
```

**test_view_inventory_4**: `unstated`
- reason: The docstring only describes the inventory as a title-to-quantity dictionary, so a programmer could reasonably keep a title with quantity 0 after all copies are removed, while the test expects that title to be deleted.
- missing: The docstring should say that when removing copies brings a title's quantity to zero, that title is deleted from the inventory rather than kept with a count of 0.

```python
def test_view_inventory_4(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    bookManagement.add_book("book2")
    bookManagement.remove_book("book1", 2)
    expected = {"book2": 1}
    self.assertEqual(expected, bookManagement.inventory)
```

**test_view_inventory_5**: `unstated`
- reason: The docstring says the inventory maps titles to quantities but does not say whether a title whose copies are all removed stays in the dictionary with zero or is deleted, and the test expects it to be deleted.
- missing: The docstring should state that when removing copies brings a title's quantity to zero, that title is removed from the inventory entirely rather than kept with a count of 0.

```python
def test_view_inventory_5(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    bookManagement.add_book("book2", 1)
    bookManagement.remove_book("book1", 2)
    bookManagement.remove_book("book2",1)
    expected = {}
    self.assertEqual(expected, bookManagement.inventory)
```

## Method `view_book_quantity`

### Docstring

```python
def view_book_quantity(self, title):
        """
        Get the quantity of a book.
        :param title: str, the title of the book.
        :return quantity: the quantity of this book title. return 0 when the title does not exist in self.invenroty
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        0
        """
```

### Reference code (`solution_code`)

```python
def view_book_quantity(self, title):
        if title not in self.inventory:
            return 0
        return self.inventory[title]
```

### Tests (`BookManagementTestViewBookQuantity`)

**test_view_book_quantity_1**: `stated`
- reason: The docstring says the method returns the quantity of the given title, so a programmer would return the stored count for "book1", which is what the test checks (2).

```python
def test_view_book_quantity_1(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    self.assertEqual(2, bookManagement.view_book_quantity("book1"))
```

**test_view_book_quantity_2**: `stated`
- reason: The docstring says the method returns 0 when the title is not in the inventory, and the test queries a title on a fresh, empty manager, so a programmer following the docstring would return 0.

```python
def test_view_book_quantity_2(self):
    bookManagement = BookManagement()
    self.assertEqual(0, bookManagement.view_book_quantity("book1"))
```

**test_view_book_quantity_3**: `stated`
- reason: The docstring says the method returns the quantity of the given title, so a programmer would return the stored count of "book1", which is 2 after adding it with quantity 2.

```python
def test_view_book_quantity_3(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    self.assertEqual(2, bookManagement.view_book_quantity("book1"))
```

**test_view_book_quantity_4**: `stated`
- reason: The docstring says to return the book's quantity and to return 0 for an unknown title, so a programmer would return 0 for a title whose copies were all removed, whether the entry was deleted or kept at zero.

```python
def test_view_book_quantity_4(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    bookManagement.remove_book("book1", 2)
    self.assertEqual(0, bookManagement.view_book_quantity("book1"))
```

**test_view_book_quantity_5**: `stated`
- reason: A programmer following the docstring would return the current stored quantity for the title, which is 1 after adding 3 and removing 2.

```python
def test_view_book_quantity_5(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 3)
    bookManagement.remove_book("book1", 2)
    self.assertEqual(1, bookManagement.view_book_quantity("book1"))
```

## Tests in no method's test class

### `BookManagementTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    bookManagement = BookManagement()
    bookManagement.add_book("book1", 2)
    bookManagement.add_book("book2")
    self.assertEqual(bookManagement.view_inventory(), {"book1": 2, "book2": 1})

    bookManagement.remove_book("book2", 1)
    self.assertEqual(bookManagement.view_inventory(), {"book1": 2})
    self.assertEqual(0, bookManagement.view_book_quantity("book2"))
```
