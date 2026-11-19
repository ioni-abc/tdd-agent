import unittest


import unittest

class AgentTest_add_item(unittest.TestCase):

    def test_add_item_1(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        self.assertEqual(cart.items, {"apple": {"price": 1, "quantity": 5}})

    def test_add_item_2(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1)
        self.assertEqual(cart.items, {"apple": {"price": 1, "quantity": 1}})

    def test_add_item_3(self):
        cart = ShoppingCart()
        result = cart.add_item("apple", 1, 5)
        self.assertIsNone(result)

    def test_add_item_4(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        cart.add_item("banana", 2, 3)
        self.assertEqual(
            cart.items,
            {
                "apple": {"price": 1, "quantity": 5},
                "banana": {"price": 2, "quantity": 3},
            },
        )

    def test_add_item_5(self):
        cart = ShoppingCart()
        cart.add_item("milk", 2.5, 2)
        self.assertEqual(cart.items["milk"]["price"], 2.5)
        self.assertEqual(cart.items["milk"]["quantity"], 2)

import unittest

class AgentTest_remove_item(unittest.TestCase):

    def test_remove_item_1(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        cart.remove_item("apple", 3)
        self.assertEqual(cart.items, {"apple": {"price": 1, "quantity": 2}})

    def test_remove_item_2(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        cart.remove_item("apple")
        self.assertEqual(cart.items["apple"]["quantity"], 4)

    def test_remove_item_3(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        result = cart.remove_item("apple", 3)
        self.assertIsNone(result)

    def test_remove_item_4(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        cart.add_item("banana", 2, 3)
        cart.remove_item("apple", 3)
        self.assertEqual(
            cart.items,
            {
                "apple": {"price": 1, "quantity": 2},
                "banana": {"price": 2, "quantity": 3},
            },
        )

    def test_remove_item_5(self):
        cart = ShoppingCart()
        cart.add_item("milk", 2.5, 6)
        cart.remove_item("milk", 1)
        cart.remove_item("milk", 2)
        self.assertEqual(cart.items["milk"]["price"], 2.5)
        self.assertEqual(cart.items["milk"]["quantity"], 3)

import unittest

class AgentTest_view_items(unittest.TestCase):

    def test_view_items_1(self):
        cart = ShoppingCart()
        result = cart.view_items()
        self.assertEqual(result, {})

    def test_view_items_2(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        result = cart.view_items()
        self.assertEqual(result, {"apple": {"price": 1, "quantity": 5}})

    def test_view_items_3(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        cart.remove_item("apple", 3)
        result = cart.view_items()
        self.assertEqual(result, {"apple": {"price": 1, "quantity": 2}})

    def test_view_items_4(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        cart.add_item("banana", 2, 3)
        result = cart.view_items()
        self.assertEqual(
            result,
            {
                "apple": {"price": 1, "quantity": 5},
                "banana": {"price": 2, "quantity": 3},
            },
        )

    def test_view_items_5(self):
        cart = ShoppingCart()
        cart.add_item("milk", 2.5, 2)
        result = cart.view_items()
        self.assertIsInstance(result, dict)
        self.assertEqual(result["milk"]["price"], 2.5)
        self.assertEqual(result["milk"]["quantity"], 2)

import unittest

class AgentTest_total_price(unittest.TestCase):

    def test_total_price_1(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        cart.add_item("banana", 2, 3)
        result = cart.total_price()
        self.assertEqual(result, 11.0)
        self.assertIsInstance(result, float)

    def test_total_price_2(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        self.assertEqual(cart.total_price(), 5.0)

    def test_total_price_3(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1)
        self.assertEqual(cart.total_price(), 1.0)

    def test_total_price_4(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1, 5)
        cart.remove_item("apple", 3)
        self.assertEqual(cart.total_price(), 2.0)

    def test_total_price_5(self):
        cart = ShoppingCart()
        cart.add_item("milk", 2.5, 2)
        cart.add_item("bread", 1.5, 4)
        self.assertAlmostEqual(cart.total_price(), 11.0)