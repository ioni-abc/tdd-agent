import unittest




class WarehouseTestAddProduct(unittest.TestCase):
    def test_add_product_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 10}})

    def test_add_product_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.add_product(2, 'product 2', 5)
        self.assertEqual(warehouse.inventory,
                         {1: {'name': 'product 1', 'quantity': 10}, 2: {'name': 'product 2', 'quantity': 5}})

    def test_add_product_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 3', 10)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 3', 'quantity': 10}})

    def test_add_product_4(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 4', 10)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 4', 'quantity': 10}})

import unittest

class AgentTest_add_product(unittest.TestCase):
    def test_add_product_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 3)
        warehouse.add_product(1, 'product 1', 2)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 5}})

    def test_add_product_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 3)
        warehouse.add_product(2, 'product 2', 6)
        warehouse.add_product(1, 'product 1', 4)
        self.assertEqual(warehouse.inventory,
                         {1: {'name': 'product 1', 'quantity': 7}, 2: {'name': 'product 2', 'quantity': 6}})

class WarehouseTestUpdateProductQuantity(unittest.TestCase):
    def test_update_product_quantity_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.update_product_quantity(1, 5)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 15}})

    def test_update_product_quantity_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.update_product_quantity(1, -5)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 5}})

    def test_update_product_quantity_3(self):
        warehouse = Warehouse()
        warehouse.update_product_quantity(1, -5)
        self.assertEqual(warehouse.inventory, {})

import unittest

class AgentTest_update_product_quantity(unittest.TestCase):
    def test_update_product_quantity_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.add_product(2, 'product 2', 7)
        warehouse.update_product_quantity(2, -3)
        self.assertEqual(warehouse.inventory,
                         {1: {'name': 'product 1', 'quantity': 10}, 2: {'name': 'product 2', 'quantity': 4}})

    def test_update_product_quantity_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.update_product_quantity(1, 0)
        self.assertEqual(warehouse.get_product_quantity(1), 10)
        self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 10}})

class WarehouseTestGetProductQuantity(unittest.TestCase):
    def test_get_product_quantity_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        self.assertEqual(warehouse.get_product_quantity(1), 10)

    def test_get_product_quantity_2(self):
        warehouse = Warehouse()
        self.assertEqual(warehouse.get_product_quantity(1), False)

    def test_get_product_quantity_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 5)
        self.assertEqual(warehouse.get_product_quantity(1), 5)

import unittest

class AgentTest_get_product_quantity(unittest.TestCase):
    def test_get_product_quantity_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.update_product_quantity(1, -4)
        self.assertEqual(warehouse.get_product_quantity(1), 6)

    def test_get_product_quantity_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 3)
        warehouse.update_product_quantity(1, -3)
        result = warehouse.get_product_quantity(1)
        self.assertEqual(result, 0)
        self.assertIsNot(result, False)

class WarehouseTestCreateOrder(unittest.TestCase):
    def test_create_order_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.create_order(1, 1, 5)
        self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 5, 'status': 'Shipped'}})

    def test_create_order_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        result = warehouse.create_order(1, 1, 15)
        self.assertFalse(result)

    def test_create_order_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 1)
        warehouse.create_order(1, 1, 1)
        self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 1, 'status': 'Shipped'}})

import unittest

class AgentTest_create_order(unittest.TestCase):
    def test_create_order_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 3)
        result = warehouse.create_order(2, 2, 1)
        self.assertFalse(result)
        self.assertEqual(warehouse.orders, {})

    def test_create_order_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.add_product(2, 'product 2', 4)
        warehouse.create_order(1, 1, 2)
        warehouse.create_order(2, 2, 3)
        self.assertEqual(warehouse.orders,
                         {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'},
                          2: {'product_id': 2, 'quantity': 3, 'status': 'Shipped'}})

class WarehouseTestChangeOrderStatus(unittest.TestCase):
    def test_change_order_status_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.create_order(1, 1, 5)
        warehouse.change_order_status(1, 'Delivered')
        self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 5, 'status': 'Delivered'}})

    def test_change_order_status_2(self):
        warehouse = Warehouse()
        result = warehouse.change_order_status(1, 'Delivered')
        self.assertFalse(result)

    def test_change_order_status_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 3', 5)
        warehouse.create_order(1, 1, 5)
        warehouse.change_order_status(1, 'Delivered')
        self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 5, 'status': 'Delivered'}})

class AgentTest_change_order_status(unittest.TestCase):
    def test_change_order_status_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.add_product(2, 'product 2', 8)
        warehouse.create_order(1, 1, 2)
        warehouse.create_order(2, 2, 3)
        warehouse.change_order_status(2, 'done')
        self.assertEqual(warehouse.orders,
                         {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'},
                          2: {'product_id': 2, 'quantity': 3, 'status': 'done'}})

    def test_change_order_status_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.create_order(1, 1, 4)
        warehouse.change_order_status(1, 'done')
        warehouse.change_order_status(1, 'Returned')
        self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 4, 'status': 'Returned'}})
        self.assertEqual(warehouse.track_order(1), 'Returned')

class WarehouseTestTrackOrder(unittest.TestCase):
    def test_track_order_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.create_order(1, 1, 5)
        self.assertEqual(warehouse.track_order(1), 'Shipped')

    def test_track_order_2(self):
        warehouse = Warehouse()
        result = warehouse.track_order(1)
        self.assertFalse(result)

    def test_track_order_3(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 3', 10)
        warehouse.create_order(1, 1, 1)
        self.assertEqual(warehouse.track_order(1), 'Shipped')

import unittest

class AgentTest_track_order(unittest.TestCase):
    def test_track_order_1(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 3)
        warehouse.create_order(1, 1, 2)
        warehouse.change_order_status(1, 'done')
        self.assertEqual(warehouse.track_order(1), 'done')

    def test_track_order_2(self):
        warehouse = Warehouse()
        warehouse.add_product(1, 'product 1', 10)
        warehouse.create_order(1, 1, 4)
        warehouse.create_order(2, 1, 3)
        result = warehouse.track_order(3)
        self.assertFalse(result)
        self.assertEqual(warehouse.track_order(2), 'Shipped')