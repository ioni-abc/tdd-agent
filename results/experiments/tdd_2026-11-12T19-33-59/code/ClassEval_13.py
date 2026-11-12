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
        self.inventory[title] = self.inventory.get(title, 0) + quantity
        self.inventory = dict(sorted(self.inventory.items()))

    def remove_book(self, title, quantity):
        """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("quantity must be a positive integer")
        if title not in self.inventory:
            raise KeyError(f"book '{title}' does not exist in inventory")
        current = self.inventory[title]
        if quantity > current:
            raise ValueError(
                f"cannot remove {quantity} copies of '{title}', only {current} available"
            )
        if quantity == current:
            del self.inventory[title]
        else:
            self.inventory[title] = current - quantity
        self.inventory = dict(sorted(self.inventory.items()))

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
        return self.inventory

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
        return self.inventory.get(title, 0)