import unittest


import unittest

class AgentTest_total(unittest.TestCase):

    def setUp(self):
        self.customer = {'name': 'John Doe', 'fidelity': 1200}

    def test_total_1(self):
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        ds = DiscountStrategy(self.customer, cart)
        self.assertEqual(ds.total(), 329.0)

    def test_total_2(self):
        cart = [
            {'product': 'apple', 'quantity': 2, 'price': 10.0},
            {'product': 'bread', 'quantity': 3, 'price': 5.5},
        ]
        ds = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(ds.total(), 36.5)

    def test_total_3(self):
        cart = [{'product': 'pen', 'quantity': 3, 'price': 0.1}]
        ds = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(ds.total(), 0.3)

    def test_total_4(self):
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        ds = DiscountStrategy(self.customer, cart, DiscountStrategy.FidelityPromo)
        self.assertEqual(ds.total(), 329.0)

    def test_total_5(self):
        cart = []
        ds = DiscountStrategy(self.customer, cart)
        self.assertEqual(ds.total(), 0)

import unittest

class AgentTest_due(unittest.TestCase):

    def setUp(self):
        self.customer = {'name': 'John Doe', 'fidelity': 1200}

    def test_due_1(self):
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        ds = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(ds.due(), 329.0)

    def test_due_2(self):
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        ds = DiscountStrategy(self.customer, cart, DiscountStrategy.FidelityPromo)
        self.assertAlmostEqual(ds.due(), 312.55)

    def test_due_3(self):
        customer = {'name': 'Jane Doe', 'fidelity': 500}
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        self.assertAlmostEqual(ds.due(), 329.0)

    def test_due_4(self):
        cart = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
        ds = DiscountStrategy(self.customer, cart, DiscountStrategy.BulkItemPromo)
        self.assertAlmostEqual(ds.due(), 423.0)

    def test_due_5(self):
        cart = [{'product': 'item' + str(i), 'quantity': 1, 'price': 10.0}
                for i in range(10)]
        ds = DiscountStrategy(self.customer, cart, DiscountStrategy.LargeOrderPromo)
        self.assertAlmostEqual(ds.due(), 93.0)

import unittest

class AgentTest_FidelityPromo(unittest.TestCase):

    def setUp(self):
        self.customer = {'name': 'John Doe', 'fidelity': 1200}

    def test_FidelityPromo_1(self):
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.FidelityPromo(order), 16.45)

    def test_FidelityPromo_2(self):
        customer = {'name': 'Jane Doe', 'fidelity': 500}
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        order = DiscountStrategy(customer, cart)
        self.assertAlmostEqual(DiscountStrategy.FidelityPromo(order), 0.0)

    def test_FidelityPromo_3(self):
        customer = {'name': 'Edge Case', 'fidelity': 1000}
        cart = [{'product': 'product', 'quantity': 4, 'price': 25.0}]
        order = DiscountStrategy(customer, cart)
        self.assertAlmostEqual(DiscountStrategy.FidelityPromo(order), 0.0)

    def test_FidelityPromo_4(self):
        customer = {'name': 'Just Over', 'fidelity': 1001}
        cart = [{'product': 'product', 'quantity': 4, 'price': 25.0}]
        order = DiscountStrategy(customer, cart)
        self.assertAlmostEqual(DiscountStrategy.FidelityPromo(order), 5.0)

    def test_FidelityPromo_5(self):
        cart = [
            {'product': 'apple', 'quantity': 2, 'price': 10.0},
            {'product': 'bread', 'quantity': 3, 'price': 5.5},
        ]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.FidelityPromo(order), 1.825)

import unittest

class AgentTest_BulkItemPromo(unittest.TestCase):

    def setUp(self):
        self.customer = {'name': 'John Doe', 'fidelity': 1200}

    def test_BulkItemPromo_1(self):
        cart = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.BulkItemPromo(order), 47.0)

    def test_BulkItemPromo_2(self):
        cart = [{'product': 'product', 'quantity': 19, 'price': 23.5}]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.BulkItemPromo(order), 0.0)

    def test_BulkItemPromo_3(self):
        cart = [{'product': 'product', 'quantity': 40, 'price': 10.0}]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.BulkItemPromo(order), 40.0)

    def test_BulkItemPromo_4(self):
        cart = [
            {'product': 'apple', 'quantity': 25, 'price': 4.0},
            {'product': 'bread', 'quantity': 5, 'price': 100.0},
        ]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.BulkItemPromo(order), 10.0)

    def test_BulkItemPromo_5(self):
        cart = [
            {'product': 'pen', 'quantity': 20, 'price': 10.0},
            {'product': 'pencil', 'quantity': 30, 'price': 2.5},
        ]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.BulkItemPromo(order), 27.5)

import unittest

class AgentTest_LargeOrderPromo(unittest.TestCase):

    def setUp(self):
        self.customer = {'name': 'John Doe', 'fidelity': 1200}

    def test_LargeOrderPromo_1(self):
        cart = [{'product': 'item' + str(i), 'quantity': 1, 'price': 10.0}
                for i in range(10)]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.LargeOrderPromo(order), 7.0)

    def test_LargeOrderPromo_2(self):
        cart = [{'product': 'item' + str(i), 'quantity': 1, 'price': 10.0}
                for i in range(9)]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.LargeOrderPromo(order), 0.0)

    def test_LargeOrderPromo_3(self):
        cart = [{'product': 'item' + str(i), 'quantity': 3, 'price': 2.5}
                for i in range(10)]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.LargeOrderPromo(order), 5.25)

    def test_LargeOrderPromo_4(self):
        cart = [{'product': 'item' + str(i), 'quantity': 1, 'price': float(i + 1)}
                for i in range(12)]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.LargeOrderPromo(order), 5.46)

    def test_LargeOrderPromo_5(self):
        cart = [{'product': 'product' + str(i), 'quantity': 14, 'price': 23.5}
                for i in range(9)]
        order = DiscountStrategy(self.customer, cart)
        self.assertAlmostEqual(DiscountStrategy.LargeOrderPromo(order), 0.0)