import unittest


import unittest

class AgentTest_insert_coin(unittest.TestCase):

    def test_insert_coin_1(self):
        vending_machine = VendingMachine()
        result = vending_machine.insert_coin(1.25)
        self.assertEqual(result, 1.25)

    def test_insert_coin_2(self):
        vending_machine = VendingMachine()
        result = vending_machine.insert_coin(1.25)
        self.assertEqual(result, vending_machine.balance)

    def test_insert_coin_3(self):
        vending_machine = VendingMachine()
        vending_machine.insert_coin(1.25)
        result = vending_machine.insert_coin(0.75)
        self.assertAlmostEqual(result, 2.0)
        self.assertAlmostEqual(vending_machine.balance, 2.0)

    def test_insert_coin_4(self):
        vending_machine = VendingMachine()
        result = vending_machine.insert_coin(0.5)
        self.assertIsInstance(result, float)

    def test_insert_coin_5(self):
        vending_machine = VendingMachine()
        vending_machine.balance = 3.0
        result = vending_machine.insert_coin(0.5)
        self.assertAlmostEqual(result, 3.5)
        self.assertAlmostEqual(vending_machine.balance, 3.5)

import unittest

class AgentTest_purchase_item(unittest.TestCase):

    def test_purchase_item_1(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vending_machine.balance = 1.25
        result = vending_machine.purchase_item('Coke')
        self.assertAlmostEqual(result, 0.0)

    def test_purchase_item_2(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vending_machine.balance = 1.25
        result = vending_machine.purchase_item('Pizza')
        self.assertFalse(result)
        self.assertIs(result, False)

    def test_purchase_item_3(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vending_machine.balance = 2.5
        result = vending_machine.purchase_item('Coke')
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 1.25)

    def test_purchase_item_4(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
        vending_machine.balance = 5.0
        result = vending_machine.purchase_item('Coke')
        self.assertIs(result, False)

    def test_purchase_item_5(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vending_machine.balance = 3.0
        result = vending_machine.purchase_item('Coke')
        self.assertAlmostEqual(result, 1.75)
        self.assertAlmostEqual(vending_machine.balance, 1.75)

import unittest

class AgentTest_restock_item(unittest.TestCase):

    def test_restock_item_1(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        result = vending_machine.restock_item('Coke', 10)
        self.assertIs(result, True)

    def test_restock_item_2(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        result = vending_machine.restock_item('Pizza', 10)
        self.assertIs(result, False)

    def test_restock_item_3(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vending_machine.restock_item('Coke', 10)
        self.assertEqual(vending_machine.inventory['Coke']['quantity'], 20)

    def test_restock_item_4(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vending_machine.restock_item('Pizza', 10)
        self.assertNotIn('Pizza', vending_machine.inventory)
        self.assertEqual(vending_machine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})

    def test_restock_item_5(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
        result = vending_machine.restock_item('Coke', 5)
        self.assertIs(result, True)
        self.assertEqual(vending_machine.inventory['Coke']['quantity'], 5)
        self.assertAlmostEqual(vending_machine.inventory['Coke']['price'], 1.25)

import unittest

class AgentTest_add_item(unittest.TestCase):

    def test_add_item_1(self):
        vending_machine = VendingMachine()
        vending_machine.add_item('Coke', 1.25, 10)
        self.assertEqual(vending_machine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})

    def test_add_item_2(self):
        vending_machine = VendingMachine()
        result = vending_machine.add_item('Coke', 1.25, 10)
        self.assertIsNone(result)

    def test_add_item_3(self):
        vending_machine = VendingMachine()
        vending_machine.add_item('Coke', 1.25, 10)
        vending_machine.add_item('Chips', 0.75, 5)
        self.assertEqual(vending_machine.inventory['Coke'], {'price': 1.25, 'quantity': 10})
        self.assertEqual(vending_machine.inventory['Chips'], {'price': 0.75, 'quantity': 5})
        self.assertEqual(len(vending_machine.inventory), 2)

    def test_add_item_4(self):
        vending_machine = VendingMachine()
        vending_machine.add_item('Water', 2.5, 3)
        self.assertIn('Water', vending_machine.inventory)
        self.assertAlmostEqual(vending_machine.inventory['Water']['price'], 2.5)
        self.assertEqual(vending_machine.inventory['Water']['quantity'], 3)

    def test_add_item_5(self):
        vending_machine = VendingMachine()
        self.assertEqual(vending_machine.inventory, {})
        vending_machine.add_item('Candy', 0.5, 0)
        self.assertEqual(list(vending_machine.inventory.keys()), ['Candy'])
        self.assertEqual(vending_machine.inventory['Candy'], {'price': 0.5, 'quantity': 0})

import unittest

class AgentTest_display_items(unittest.TestCase):

    def test_display_items_1(self):
        vending_machine = VendingMachine()
        result = vending_machine.display_items()
        self.assertIs(result, False)

    def test_display_items_2(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        result = vending_machine.display_items()
        self.assertEqual(result, 'Coke - $1.25 [10]')

    def test_display_items_3(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {
            'Coke': {'price': 1.25, 'quantity': 10},
            'Chips': {'price': 0.75, 'quantity': 5},
        }
        result = vending_machine.display_items()
        self.assertIsNot(result, False)
        self.assertIn('Coke - $1.25 [10]', result)
        self.assertIn('Chips - $0.75 [5]', result)

    def test_display_items_4(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Water': {'price': 2.5, 'quantity': 3}}
        result = vending_machine.display_items()
        self.assertIn('Water', result)
        self.assertIn('$2.50', result)
        self.assertIn('[3]', result)

    def test_display_items_5(self):
        vending_machine = VendingMachine()
        vending_machine.inventory = {'Candy': {'price': 0.5, 'quantity': 0}}
        result = vending_machine.display_items()
        self.assertIsNot(result, False)
        self.assertIn('Candy', result)
        self.assertIn('[0]', result)