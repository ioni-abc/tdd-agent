import unittest


class VendingMachineTestInsertCoin(unittest.TestCase):
    def test_insert_coin(self):
        vendingMachine = VendingMachine()
        self.assertEqual(vendingMachine.insert_coin(1.25), 1.25)

    def test_insert_coin_2(self):
        vendingMachine = VendingMachine()
        self.assertEqual(vendingMachine.insert_coin(2.5), 2.5)

    def test_insert_coin_3(self):
        vendingMachine = VendingMachine()
        vendingMachine.insert_coin(1.25)
        vendingMachine.insert_coin(1.25)
        self.assertEqual(vendingMachine.balance, 2.50)

import unittest

class AgentTest_insert_coin(unittest.TestCase):
    def test_insert_coin_1(self):
        vendingMachine = VendingMachine()
        vendingMachine.insert_coin(1.25)
        vendingMachine.insert_coin(0.5)
        returned = vendingMachine.insert_coin(0.25)
        self.assertEqual(returned, 2.0)
        self.assertEqual(vendingMachine.balance, 2.0)

    def test_insert_coin_2(self):
        vendingMachine = VendingMachine()
        vendingMachine.balance = 1.25
        returned = vendingMachine.insert_coin(1.25)
        self.assertEqual(returned, 2.5)
        self.assertEqual(vendingMachine.balance, 2.5)

class VendingMachineTestPurchaseItem(unittest.TestCase):
    def test_purchase_item(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vendingMachine.balance = 1.25
        self.assertEqual(vendingMachine.purchase_item('Coke'), 0.0)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 9}})

    def test_purchase_item_2(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vendingMachine.balance = 1.25
        self.assertEqual(vendingMachine.purchase_item('Pizza'), False)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})

    def test_purchase_item_3(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vendingMachine.balance = 0
        self.assertEqual(vendingMachine.purchase_item('Coke'), False)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})

class AgentTest_purchase_item(unittest.TestCase):
    def test_purchase_item_1(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        vendingMachine.balance = 5.0
        self.assertEqual(vendingMachine.purchase_item('Coke'), 3.75)
        self.assertEqual(vendingMachine.balance, 3.75)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 9}})

    def test_purchase_item_2(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
        vendingMachine.balance = 1.25
        self.assertEqual(vendingMachine.purchase_item('Coke'), False)
        self.assertEqual(vendingMachine.balance, 1.25)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 0}})

class VendingMachineTestRestockItem(unittest.TestCase):
    def test_restock_item(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        self.assertEqual(vendingMachine.restock_item('Coke', 10), True)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 20}})

    def test_restock_item_2(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        self.assertEqual(vendingMachine.restock_item('Pizza', 10), False)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})

    def test_restock_item_3(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
        self.assertEqual(vendingMachine.restock_item('Coke', 10), True)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})

class AgentTest_restock_item(unittest.TestCase):
    def test_restock_item_1(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {
            'Coke': {'price': 1.25, 'quantity': 10},
            'Chips': {'price': 0.75, 'quantity': 4},
        }
        self.assertEqual(vendingMachine.restock_item('Coke', 5), True)
        self.assertEqual(vendingMachine.inventory, {
            'Coke': {'price': 1.25, 'quantity': 15},
            'Chips': {'price': 0.75, 'quantity': 4},
        })

    def test_restock_item_2(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        self.assertEqual(vendingMachine.restock_item('Coke', 5), True)
        self.assertEqual(vendingMachine.restock_item('Coke', 3), True)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 18}})

class VendingMachineTestAddItem(unittest.TestCase):
    def test_add_item(self):
        vendingMachine = VendingMachine()
        vendingMachine.add_item('Coke', 1.25, 10)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})

    def test_add_item_2(self):
        vendingMachine = VendingMachine()
        vendingMachine.add_item('Coke', 1.25, 10)
        vendingMachine.add_item('Coke', 1.25, 10)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 20}})

    def test_add_item_3(self):
        vendingMachine = VendingMachine()
        vendingMachine.add_item('Coke', 1.25, 10)
        vendingMachine.add_item('Pizza', 1.25, 10)
        self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 10}})

import unittest

class AgentTest_add_item(unittest.TestCase):
    def test_add_item_1(self):
        vendingMachine = VendingMachine()
        self.assertIsNone(vendingMachine.add_item('Coke', 1.25, 10))

    def test_add_item_2(self):
        vendingMachine = VendingMachine()
        vendingMachine.add_item('Chips', 0.75, 0)
        self.assertEqual(vendingMachine.inventory, {'Chips': {'price': 0.75, 'quantity': 0}})

class VendingMachineTestDisplayItems(unittest.TestCase):
    def test_display_items(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        self.assertEqual(vendingMachine.display_items(), 'Coke - $1.25 [10]')

    def test_display_items_2(self):
        vendingMachine = VendingMachine()
        self.assertEqual(vendingMachine.display_items(), False)

    def test_display_items_3(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 10}}
        self.assertEqual(vendingMachine.display_items(),"Coke - $1.25 [10]\nPizza - $1.25 [10]")

import unittest

class AgentTest_display_items(unittest.TestCase):
    def test_display_items_1(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {'Chips': {'price': 0.75, 'quantity': 4}}
        self.assertEqual(vendingMachine.display_items(), 'Chips - $0.75 [4]')

    def test_display_items_2(self):
        vendingMachine = VendingMachine()
        vendingMachine.inventory = {
            'Coke': {'price': 1.25, 'quantity': 10},
            'Chips': {'price': 0.75, 'quantity': 4},
            'Pizza': {'price': 2.5, 'quantity': 3},
        }
        self.assertEqual(
            vendingMachine.display_items(),
            "Coke - $1.25 [10]\nChips - $0.75 [4]\nPizza - $2.50 [3]"
        )