import unittest




class ShoppingCartTestAddItem(unittest.TestCase):
    def test_add_item_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 5}})

    def test_add_item_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1)
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 1}})

    def test_add_item_3(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("aaa", 1)
        self.assertEqual(shoppingcart.items, {"aaa": {"price": 1, "quantity": 1}})

    def test_add_item_4(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("bbb", 1)
        self.assertEqual(shoppingcart.items, {"bbb": {"price": 1, "quantity": 1}})

import unittest

class AgentTest_add_item(unittest.TestCase):
    def test_add_item_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("milk", 2.5, 3)
        self.assertEqual(shoppingcart.items, {"milk": {"price": 2.5, "quantity": 3}})

    def test_add_item_2(self):
        shoppingcart = ShoppingCart()
        result = shoppingcart.add_item("apple", 1, 5)
        self.assertIsNone(result)

class ShoppingCartTestRemoveItem(unittest.TestCase):
    def test_remove_item_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.remove_item("apple", 3)
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 2}})

    def test_remove_item_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.remove_item("apple")
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 4}})

    def test_remove_item_3(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.remove_item("apple", 1)
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 4}})

    def test_remove_item_4(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.remove_item("apple", 2)
        self.assertEqual(shoppingcart.items, {"apple": {"price": 1, "quantity": 3}})

import unittest

class AgentTest_remove_item(unittest.TestCase):
    def test_remove_item_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.add_item("banana", 2, 3)
        shoppingcart.remove_item("apple", 2)
        self.assertEqual(
            shoppingcart.items,
            {"apple": {"price": 1, "quantity": 3}, "banana": {"price": 2, "quantity": 3}},
        )

    def test_remove_item_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        result = shoppingcart.remove_item("apple", 3)
        self.assertIsNone(result)

class ShoppingCartTestViewItems(unittest.TestCase):
    def test_view_items_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        self.assertEqual(shoppingcart.view_items(), {"apple": {"price": 1, "quantity": 5}})

    def test_view_items_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 4)
        self.assertEqual(shoppingcart.view_items(), {"apple": {"price": 1, "quantity": 4}})

    def test_view_items_3(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 3)
        self.assertEqual(shoppingcart.view_items(), {"apple": {"price": 1, "quantity": 3}})

import unittest

class AgentTest_view_items(unittest.TestCase):
    def test_view_items_1(self):
        shoppingcart = ShoppingCart()
        self.assertEqual(shoppingcart.view_items(), {})

    def test_view_items_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.add_item("banana", 2, 3)
        shoppingcart.remove_item("apple", 3)
        self.assertEqual(
            shoppingcart.view_items(),
            {"apple": {"price": 1, "quantity": 2}, "banana": {"price": 2, "quantity": 3}},
        )

class ShoppingCartTestTotalPrice(unittest.TestCase):
    def test_total_price_1(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.add_item("banana", 2, 3)
        self.assertEqual(shoppingcart.total_price(), 11.0)

    def test_total_price_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 5)
        shoppingcart.add_item("banana", 2, 3)
        shoppingcart.remove_item("apple", 3)
        self.assertEqual(shoppingcart.total_price(), 8.0)

    def test_total_price_3(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("apple", 1, 1)
        shoppingcart.add_item("banana", 2, 1)
        self.assertEqual(shoppingcart.total_price(), 3.0)

import unittest

class AgentTest_total_price(unittest.TestCase):
    def test_total_price_1(self):
        shoppingcart = ShoppingCart()
        self.assertEqual(shoppingcart.total_price(), 0.0)

    def test_total_price_2(self):
        shoppingcart = ShoppingCart()
        shoppingcart.add_item("milk", 2.5, 3)
        self.assertEqual(shoppingcart.total_price(), 7.5)