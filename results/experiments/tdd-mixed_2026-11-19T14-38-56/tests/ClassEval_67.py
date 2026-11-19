import unittest




class OrderTestAddDish(unittest.TestCase):
    def setUp(self):
        self.order = Order()

        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    def test_add_dish_1(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 4})
        self.assertTrue(result)

        # test the status of self.menu and self.selected_dishes
        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 3)
        self.assertEqual(self.order.selected_dishes, [{"dish": "dish3", "price": 15, "count": 4}])

    def test_add_dish_2(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 8})
        self.assertFalse(result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 7)
        self.assertEqual(self.order.selected_dishes, [])

    def test_add_dish_3(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 7})
        self.assertTrue(result)

        # test the status of self.menu and self.selected_dishes
        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 0)
        self.assertEqual(self.order.selected_dishes, [{"dish": "dish3", "price": 15, "count": 7}])

    def test_add_dish_4(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 6})
        self.assertTrue(result)

        # test the status of self.menu and self.selected_dishes
        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 1)
        self.assertEqual(self.order.selected_dishes, [{"dish": "dish3", "price": 15, "count": 6}])

import unittest

class AgentTest_add_dish(unittest.TestCase):
    def setUp(self):
        self.order = Order()

        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    def test_add_dish_1(self):
        # The menu count is reduced after each successful add, so a second add
        # of the same dish is validated against the remaining count.
        first = self.order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        self.assertTrue(first)

        second = self.order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        self.assertFalse(second)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 2)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 7)

    def test_add_dish_2(self):
        # A dish that is not on the menu cannot be added.
        result = self.order.add_dish({"dish": "dish4", "price": 12, "count": 1})
        self.assertFalse(result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 7)
        self.assertEqual(self.order.selected_dishes, [])

class OrderTestCalculateTotal(unittest.TestCase):
    def setUp(self):
        self.order = Order()
        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    def test_calculate_total_1(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 2})
        result = self.order.calculate_total()
        self.assertEqual(50, result)

    def test_calculate_total_2(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
        self.order.add_dish({"dish": "dish2", "price": 15, "count": 2})
        result = self.order.calculate_total()
        self.assertEqual(48, result)

    def test_calculate_total_3(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 1})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 1})
        result = self.order.calculate_total()
        self.assertEqual(25, result)

import unittest

class AgentTest_calculate_total(unittest.TestCase):
    def setUp(self):
        self.order = Order()
        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    def test_calculate_total_1(self):
        # Nothing has been ordered, so the total price is zero.
        result = self.order.calculate_total()
        self.assertEqual(0, result)

    def test_calculate_total_2(self):
        # A single dish with a fractional sale rate returns a float total
        # equal to count * price * sales.
        self.assertTrue(self.order.add_dish({"dish": "dish3", "price": 20, "count": 3}))
        result = self.order.calculate_total()
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(48.0, result)

class OrderTestCheckout(unittest.TestCase):
    def setUp(self):
        self.order = Order()
        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    def test_checkout_1(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 2})
        result = self.order.checkout()
        self.assertEqual(50, result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 5)
        self.assertEqual([], self.order.selected_dishes)

    def test_checkout_2(self):
        result = self.order.checkout()
        self.assertFalse(result)

    def test_checkout_3(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 1})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 1})
        result = self.order.checkout()
        self.assertEqual(25, result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 4)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 6)
        self.assertEqual([], self.order.selected_dishes)

import unittest

class AgentTest_checkout(unittest.TestCase):
    def setUp(self):
        self.order = Order()
        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    def test_checkout_1(self):
        # A single dish with a sale rate of 1 checks out as a float total
        # equal to count * price * sales, and the menu count is reduced.
        self.assertTrue(self.order.add_dish({"dish": "dish2", "price": 15, "count": 2}))
        result = self.order.checkout()
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(30.0, result)

        for menu_dish in self.order.menu:
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 1)
        self.assertEqual([], self.order.selected_dishes)

    def test_checkout_2(self):
        # After a successful checkout the selected dishes are cleared, so a
        # second checkout with nothing selected returns False.
        self.assertTrue(self.order.add_dish({"dish": "dish1", "price": 10, "count": 2}))
        first = self.order.checkout()
        self.assertAlmostEqual(18.0, first)

        second = self.order.checkout()
        self.assertFalse(second)
        self.assertEqual([], self.order.selected_dishes)