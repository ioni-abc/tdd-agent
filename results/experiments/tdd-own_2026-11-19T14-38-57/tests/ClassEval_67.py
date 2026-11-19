import unittest


import unittest

class AgentTest_add_dish(unittest.TestCase):

    def test_add_dish_1(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        result = order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        self.assertTrue(result)
        self.assertEqual(len(order.selected_dishes), 1)
        self.assertEqual(order.selected_dishes[0]["dish"], "dish1")
        self.assertEqual(order.selected_dishes[0]["count"], 3)
        self.assertEqual(order.selected_dishes[0]["price"], 10)
        self.assertEqual(order.menu[0]["count"], 2)

    def test_add_dish_2(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        result = order.add_dish({"dish": "dish1", "price": 10, "count": 6})
        self.assertFalse(result)
        self.assertEqual(order.selected_dishes, [])
        self.assertEqual(order.menu[0]["count"], 5)

    def test_add_dish_3(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        result = order.add_dish({"dish": "dish2", "price": 12, "count": 1})
        self.assertFalse(result)
        self.assertEqual(order.selected_dishes, [])
        self.assertEqual(order.menu[0]["count"], 5)

    def test_add_dish_4(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 5}))
        self.assertEqual(order.menu[0]["count"], 0)
        self.assertFalse(order.add_dish({"dish": "dish1", "price": 10, "count": 1}))
        self.assertEqual(order.menu[0]["count"], 0)
        self.assertEqual(len(order.selected_dishes), 1)

    def test_add_dish_5(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.menu.append({"dish": "dish2", "price": 7, "count": 4})
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 2}))
        self.assertTrue(order.add_dish({"dish": "dish2", "price": 7, "count": 3}))
        self.assertEqual(len(order.selected_dishes), 2)
        self.assertEqual(order.menu[0]["count"], 3)
        self.assertEqual(order.menu[1]["count"], 1)

import unittest

class AgentTest_calculate_total(unittest.TestCase):

    def test_calculate_total_1(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.sales = {"dish1": 0.8}
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 4}))
        self.assertAlmostEqual(order.calculate_total(), 32.0)

    def test_calculate_total_2(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.menu.append({"dish": "dish2", "price": 7, "count": 4})
        order.sales = {"dish1": 1, "dish2": 0.5}
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 2}))
        self.assertTrue(order.add_dish({"dish": "dish2", "price": 7, "count": 3}))
        # 2 * 10 * 1 + 3 * 7 * 0.5 = 20 + 10.5
        self.assertAlmostEqual(order.calculate_total(), 30.5)

    def test_calculate_total_3(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 12.5, "count": 5})
        order.sales = {"dish1": 1}
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 12.5, "count": 2}))
        self.assertAlmostEqual(order.calculate_total(), 25.0)

    def test_calculate_total_4(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.sales = {"dish1": 0.8}
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 2}))
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 3}))
        # (2 + 3) * 10 * 0.8
        self.assertAlmostEqual(order.calculate_total(), 40.0)

    def test_calculate_total_5(self):
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.sales = {"dish1": 0.8}
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 4}))
        self.assertFalse(order.add_dish({"dish": "dish1", "price": 10, "count": 3}))
        # rejected dish must not contribute to the total
        self.assertAlmostEqual(order.calculate_total(), 32.0)

import unittest

class AgentTest_checkout(unittest.TestCase):

    def test_checkout_1(self):
        # Nothing has been selected, so checkout returns False
        order = Order()
        self.assertFalse(order.checkout())

    def test_checkout_2(self):
        # Menu has items but no dish has been selected, so checkout returns False
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.sales = {"dish1": 1}
        self.assertFalse(order.checkout())

    def test_checkout_3(self):
        # Docstring example: 4 * 10 * 0.8 = 32.0
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.sales = {"dish1": 0.8}
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 4}))
        self.assertAlmostEqual(order.checkout(), 32.0)

    def test_checkout_4(self):
        # Two dishes with different sales: 2 * 10 * 1 + 3 * 7 * 0.5 = 30.5
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.menu.append({"dish": "dish2", "price": 7, "count": 4})
        order.sales = {"dish1": 1, "dish2": 0.5}
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 2}))
        self.assertTrue(order.add_dish({"dish": "dish2", "price": 7, "count": 3}))
        self.assertAlmostEqual(order.checkout(), 30.5)

    def test_checkout_5(self):
        # Same dish added twice: (2 + 3) * 10 * 0.8 = 40.0
        order = Order()
        order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        order.sales = {"dish1": 0.8}
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 2}))
        self.assertTrue(order.add_dish({"dish": "dish1", "price": 10, "count": 3}))
        self.assertAlmostEqual(order.checkout(), 40.0)