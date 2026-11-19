import unittest




class DiscountStrategyTestTotal(unittest.TestCase):
    def test_total_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart)
        expected_total = 250.0
        actual_total = order.total()
        self.assertEqual(actual_total, expected_total)

    def test_total_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 10.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart)
        expected_total = 150.0
        actual_total = order.total()
        self.assertEqual(actual_total, expected_total)

    def test_total_3(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 200.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart)
        expected_total = 2050.0
        actual_total = order.total()
        self.assertEqual(actual_total, expected_total)

import unittest

class AgentTest_total(unittest.TestCase):
    def test_total_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        order = DiscountStrategy(customer, cart)
        expected_total = 329.0
        actual_total = order.total()
        self.assertEqual(actual_total, expected_total)

    def test_total_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 3, 'price': 1.99},
                {'product': 'product2', 'quantity': 2, 'price': 0.5}]
        order = DiscountStrategy(customer, cart)
        expected_total = 6.97
        actual_total = order.total()
        self.assertAlmostEqual(actual_total, expected_total, places=2)

class DiscountStrategyTestDue(unittest.TestCase):
    def test_due_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart)
        expected_due = 250.0
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

    def test_due_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_due = 237.5
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

    def test_due_3(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 20, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        expected_due = 410.0
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

import unittest

class AgentTest_due(unittest.TestCase):
    def test_due_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product' + str(i), 'quantity': 1, 'price': 10.0}
                for i in range(10)]
        order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        expected_due = 93.0
        actual_due = order.due()
        self.assertAlmostEqual(actual_due, expected_due, places=2)

    def test_due_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1000}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_due = 250.0
        actual_due = order.due()
        self.assertEqual(actual_due, expected_due)

class DiscountStrategyTestFidelityPromo(unittest.TestCase):
    def test_fidelity_promo_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1000}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 12.5
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_fidelity_promo_2(self):
        customer = {'name': 'John Doe', 'fidelity': 800}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 0
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_fidelity_promo_3(self):
        customer = {'name': 'John Doe', 'fidelity': 0}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 0
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

import unittest

class AgentTest_FidelityPromo(unittest.TestCase):
    def test_FidelityPromo_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 16.45
        actual_discount = DiscountStrategy.FidelityPromo(order)
        self.assertAlmostEqual(actual_discount, expected_discount, places=2)

    def test_FidelityPromo_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1001}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 12.5
        actual_discount = DiscountStrategy.FidelityPromo(order)
        self.assertAlmostEqual(actual_discount, expected_discount, places=2)

class DiscountStrategyTestBulkItemPromo(unittest.TestCase):
    def test_bulk_item_promo_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 20, 'price': 10.0},
                {'product': 'product2', 'quantity': 5, 'price': 5.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        expected_discount = 20.0
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_bulk_item_promo_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 10.0},
                {'product': 'product2', 'quantity': 5, 'price': 5.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        expected_discount = 0
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_bulk_item_promo_3(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 100, 'price': 10.0},
                {'product': 'product2', 'quantity': 5, 'price': 5.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        expected_discount = 100.0
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

class AgentTest_BulkItemPromo(unittest.TestCase):
    def test_BulkItemPromo_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 19, 'price': 10.0},
                {'product': 'product2', 'quantity': 25, 'price': 4.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        expected_discount = 10.0
        actual_discount = DiscountStrategy.BulkItemPromo(order)
        self.assertAlmostEqual(actual_discount, expected_discount, places=2)

    def test_BulkItemPromo_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': 'product1', 'quantity': 21, 'price': 23.5}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        expected_discount = 49.35
        actual_discount = DiscountStrategy.BulkItemPromo(order)
        self.assertAlmostEqual(actual_discount, expected_discount, places=2)

class DiscountStrategyTestLargeOrderPromo(unittest.TestCase):
    def test_large_order_promo_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(10)]
        order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        expected_discount = 7.0
        actual_discount = order.promotion(order)
        self.assertAlmostEqual(actual_discount, expected_discount)

    def test_large_order_promo_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(5)]
        order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        expected_discount = 0
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_large_order_promo_3(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(100)]
        order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        expected_discount = 70.0
        actual_discount = order.promotion(order)
        self.assertAlmostEqual(actual_discount, expected_discount)

import unittest

class AgentTest_LargeOrderPromo(unittest.TestCase):
    def test_LargeOrderPromo_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': f'product{i}', 'quantity': 3, 'price': 10.0} for i in range(9)]
        order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        expected_discount = 0.0
        actual_discount = DiscountStrategy.LargeOrderPromo(order)
        self.assertAlmostEqual(actual_discount, expected_discount, places=2)

    def test_LargeOrderPromo_2(self):
        customer = {'name': 'John Doe', 'fidelity': 1200}
        cart = [{'product': f'product{i}', 'quantity': 2, 'price': float(i)} for i in range(1, 11)]
        order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        expected_discount = 7.7
        actual_discount = DiscountStrategy.LargeOrderPromo(order)
        self.assertAlmostEqual(actual_discount, expected_discount, places=2)