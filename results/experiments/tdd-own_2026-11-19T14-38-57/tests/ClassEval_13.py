import unittest


import unittest

class AgentTest_add_book(unittest.TestCase):

    def test_add_book_1(self):
        # Default quantity is 1 when none is given.
        bm = BookManagement()
        bm.add_book("book1")
        self.assertEqual(bm.view_inventory(), {"book1": 1})

    def test_add_book_2(self):
        # An explicit quantity is stored for the title.
        bm = BookManagement()
        bm.add_book("book1", 3)
        self.assertEqual(bm.view_inventory(), {"book1": 3})

    def test_add_book_3(self):
        # Several different titles are each added to the inventory.
        bm = BookManagement()
        bm.add_book("book1", 1)
        bm.add_book("book2", 1)
        self.assertEqual(bm.view_inventory(), {"book1": 1, "book2": 1})

    def test_add_book_4(self):
        # Adding an existing title again increases its quantity.
        bm = BookManagement()
        bm.add_book("book1", 1)
        bm.add_book("book1", 2)
        self.assertEqual(bm.view_inventory(), {"book1": 3})
        self.assertEqual(bm.view_book_quantity("book1"), 3)

    def test_add_book_5(self):
        # The inventory is kept sorted by book title.
        bm = BookManagement()
        bm.add_book("book2", 1)
        bm.add_book("book1", 1)
        bm.add_book("book3", 1)
        self.assertEqual(list(bm.view_inventory().keys()),
                         sorted(["book1", "book2", "book3"]))

import unittest

import unittest

class AgentTest_remove_book(unittest.TestCase):

    def test_remove_book_1(self):
        # Removing fewer copies than held reduces the stored quantity.
        bm = BookManagement()
        bm.add_book("book1", 3)
        bm.remove_book("book1", 1)
        self.assertEqual(bm.view_inventory(), {"book1": 2})
        self.assertEqual(bm.view_book_quantity("book1"), 2)

    def test_remove_book_2(self):
        # Removing all copies leaves the title with zero quantity.
        bm = BookManagement()
        bm.add_book("book1", 2)
        bm.remove_book("book1", 2)
        self.assertEqual(bm.view_book_quantity("book1"), 0)

    def test_remove_book_3(self):
        # Removing one title does not affect other titles in the inventory.
        bm = BookManagement()
        bm.add_book("book1", 1)
        bm.add_book("book2", 4)
        bm.remove_book("book1", 1)
        self.assertEqual(bm.view_inventory()["book2"], 4)
        self.assertEqual(bm.view_book_quantity("book2"), 4)

    def test_remove_book_4(self):
        # Removing a title that is not in the inventory is invalid input and raises.
        bm = BookManagement()
        bm.add_book("book1", 1)
        with self.assertRaises(Exception):
            bm.remove_book("book3", 1)
        self.assertEqual(bm.view_inventory(), {"book1": 1})

    def test_remove_book_5(self):
        # Removing more copies than are held is invalid input and raises,
        # leaving the inventory unchanged.
        bm = BookManagement()
        bm.add_book("book1", 2)
        with self.assertRaises(Exception):
            bm.remove_book("book1", 5)
        self.assertEqual(bm.view_inventory(), {"book1": 2})

import unittest

class AgentTest_view_inventory(unittest.TestCase):

    def test_view_inventory_1(self):
        # A newly created manager has an empty inventory.
        bm = BookManagement()
        self.assertEqual(bm.view_inventory(), {})

    def test_view_inventory_2(self):
        # Matches the docstring example: two titles added with quantity 1 each.
        bm = BookManagement()
        bm.add_book("book1", 1)
        bm.add_book("book2", 1)
        self.assertEqual(bm.view_inventory(), {"book1": 1, "book2": 1})

    def test_view_inventory_3(self):
        # Returned dictionary maps each title (str) to its quantity (int),
        # including default quantity and repeated additions of the same title.
        bm = BookManagement()
        bm.add_book("book1")
        bm.add_book("book2", 5)
        bm.add_book("book2", 2)
        inventory = bm.view_inventory()
        self.assertEqual(inventory, {"book1": 1, "book2": 7})
        self.assertIsInstance(inventory, dict)
        for title, quantity in inventory.items():
            self.assertIsInstance(title, str)
            self.assertIsInstance(quantity, int)

    def test_view_inventory_4(self):
        # The inventory is sorted by book title.
        bm = BookManagement()
        bm.add_book("book3", 1)
        bm.add_book("book1", 1)
        bm.add_book("book2", 1)
        self.assertEqual(list(bm.view_inventory().keys()),
                         sorted(["book1", "book2", "book3"]))

    def test_view_inventory_5(self):
        # The inventory reflects a partial removal of copies.
        bm = BookManagement()
        bm.add_book("book1", 3)
        bm.add_book("book2", 4)
        bm.remove_book("book1", 1)
        self.assertEqual(bm.view_inventory(), {"book1": 2, "book2": 4})

class AgentTest_view_book_quantity(unittest.TestCase):

    def test_view_book_quantity_1(self):
        # Docstring example: a title that was never added returns 0.
        bm = BookManagement()
        bm.add_book("book1", 1)
        self.assertEqual(bm.view_book_quantity("book3"), 0)

    def test_view_book_quantity_2(self):
        # A title added with the default quantity reports 1.
        bm = BookManagement()
        bm.add_book("book1")
        self.assertEqual(bm.view_book_quantity("book1"), 1)

    def test_view_book_quantity_3(self):
        # An explicit quantity is reported for that title.
        bm = BookManagement()
        bm.add_book("book1", 4)
        self.assertEqual(bm.view_book_quantity("book1"), 4)

    def test_view_book_quantity_4(self):
        # Repeated additions of the same title are reflected in the total quantity.
        bm = BookManagement()
        bm.add_book("book1", 1)
        bm.add_book("book1", 2)
        self.assertEqual(bm.view_book_quantity("book1"), 3)

    def test_view_book_quantity_5(self):
        # Quantities are reported per title and do not affect each other;
        # an empty manager returns 0 for any title.
        bm = BookManagement()
        self.assertEqual(bm.view_book_quantity("book1"), 0)
        bm.add_book("book1", 2)
        bm.add_book("book2", 5)
        self.assertEqual(bm.view_book_quantity("book1"), 2)
        self.assertEqual(bm.view_book_quantity("book2"), 5)