import unittest


import unittest

class AgentTest_add_product(unittest.TestCase):

    def test_add_product_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product1', 'quantity': 3}})

    def test_add_product_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.add_product(1, "product1", 2)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product1', 'quantity': 5}})

    def test_add_product_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.add_product(2, "product2", 7)
        self.assertEqual(
            warehouse.inventory,
            {
                1: {'name': 'product1', 'quantity': 3},
                2: {'name': 'product2', 'quantity': 7},
            },
        )

    def test_add_product_4(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        self.assertEqual(warehouse.get_product_quantity(1), 3)

    def test_add_product_5(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.add_product(1, "product1", 4)
        self.assertEqual(len(warehouse.inventory), 1)
        self.assertIn(1, warehouse.inventory)

import unittest

class AgentTest_update_product_quantity(unittest.TestCase):

    def test_update_product_quantity_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.update_product_quantity(1, -1)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product1', 'quantity': 2}})

    def test_update_product_quantity_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.update_product_quantity(1, 5)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product1', 'quantity': 8}})

    def test_update_product_quantity_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.add_product(2, "product2", 7)
        warehouse.update_product_quantity(1, 4)
        self.assertEqual(
            warehouse.inventory,
            {
                1: {'name': 'product1', 'quantity': 7},
                2: {'name': 'product2', 'quantity': 7},
            },
        )

    def test_update_product_quantity_4(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.update_product_quantity(1, -3)
        self.assertEqual(warehouse.inventory[1]['quantity'], 0)
        self.assertEqual(warehouse.inventory[1]['name'], "product1")

    def test_update_product_quantity_5(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 10)
        warehouse.update_product_quantity(1, -2)
        warehouse.update_product_quantity(1, -3)
        warehouse.update_product_quantity(1, 1)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product1', 'quantity': 6}})

import unittest

class AgentTest_get_product_quantity(unittest.TestCase):

    def test_get_product_quantity_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        self.assertEqual(warehouse.get_product_quantity(1), 3)

    def test_get_product_quantity_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        self.assertEqual(warehouse.get_product_quantity(2), False)

    def test_get_product_quantity_3(self):
        warehouse = Warehouse()
        self.assertEqual(warehouse.get_product_quantity(1), False)

    def test_get_product_quantity_4(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.update_product_quantity(1, -1)
        self.assertEqual(warehouse.get_product_quantity(1), 2)

    def test_get_product_quantity_5(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.add_product(2, "product2", 7)
        self.assertEqual(warehouse.get_product_quantity(1), 3)
        self.assertEqual(warehouse.get_product_quantity(2), 7)

class AgentTest_create_order(unittest.TestCase):

    def test_create_order_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.create_order(1, 1, 2)
        self.assertEqual(
            warehouse.orders,
            {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}},
        )

    def test_create_order_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        result = warehouse.create_order(1, 2, 2)
        self.assertIs(result, False)
        self.assertNotIn(1, warehouse.orders)

    def test_create_order_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        result = warehouse.create_order(1, 1, 4)
        self.assertIs(result, False)
        self.assertNotIn(1, warehouse.orders)

    def test_create_order_4(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.add_product(2, "product2", 7)
        warehouse.create_order(1, 1, 2)
        warehouse.create_order(2, 2, 5)
        self.assertEqual(
            warehouse.orders,
            {
                1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'},
                2: {'product_id': 2, 'quantity': 5, 'status': 'Shipped'},
            },
        )

    def test_create_order_5(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        result = warehouse.create_order(1, 1, 3)
        self.assertNotIs(result, False) if hasattr(self, 'assertNotIs') else self.assertIsNot(result, False)
        self.assertEqual(
            warehouse.orders,
            {1: {'product_id': 1, 'quantity': 3, 'status': 'Shipped'}},
        )

class AgentTest_change_order_status(unittest.TestCase):

    def test_change_order_status_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.create_order(1, 1, 2)
        warehouse.change_order_status(1, "done")
        self.assertEqual(
            warehouse.orders,
            {1: {'product_id': 1, 'quantity': 2, 'status': 'done'}},
        )

    def test_change_order_status_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.create_order(1, 1, 2)
        result = warehouse.change_order_status(2, "done")
        self.assertIs(result, False)
        self.assertEqual(
            warehouse.orders,
            {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}},
        )

    def test_change_order_status_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.add_product(2, "product2", 7)
        warehouse.create_order(1, 1, 2)
        warehouse.create_order(2, 2, 5)
        warehouse.change_order_status(1, "done")
        self.assertEqual(
            warehouse.orders,
            {
                1: {'product_id': 1, 'quantity': 2, 'status': 'done'},
                2: {'product_id': 2, 'quantity': 5, 'status': 'Shipped'},
            },
        )

    def test_change_order_status_4(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.create_order(1, 1, 2)
        warehouse.change_order_status(1, "done")
        warehouse.change_order_status(1, "returned")
        self.assertEqual(warehouse.track_order(1), "returned")
        self.assertEqual(
            warehouse.orders,
            {1: {'product_id': 1, 'quantity': 2, 'status': 'returned'}},
        )

    def test_change_order_status_5(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.create_order(1, 1, 2)
        warehouse.change_order_status(1, "done")
        self.assertEqual(warehouse.orders[1]['product_id'], 1)
        self.assertEqual(warehouse.orders[1]['quantity'], 2)
        self.assertEqual(warehouse.orders[1]['status'], 'done')

import unittest

class AgentTest_track_order(unittest.TestCase):

    def test_track_order_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.create_order(1, 1, 2)
        self.assertEqual(warehouse.track_order(1), 'Shipped')

    def test_track_order_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.create_order(1, 1, 2)
        result = warehouse.track_order(2)
        self.assertIs(result, False)

    def test_track_order_3(self):
        warehouse = Warehouse()
        self.assertIs(warehouse.track_order(1), False)

    def test_track_order_4(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.create_order(1, 1, 2)
        warehouse.change_order_status(1, "done")
        self.assertEqual(warehouse.track_order(1), 'done')

    def test_track_order_5(self):
        warehouse = Warehouse()
        warehouse.add_product(1, "product1", 3)
        warehouse.add_product(2, "product2", 7)
        warehouse.create_order(1, 1, 2)
        warehouse.create_order(2, 2, 5)
        warehouse.change_order_status(1, "done")
        self.assertEqual(warehouse.track_order(1), 'done')
        self.assertEqual(warehouse.track_order(2), 'Shipped')