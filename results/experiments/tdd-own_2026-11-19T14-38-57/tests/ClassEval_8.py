import unittest


import unittest

class AgentTest_deposit(unittest.TestCase):

    def test_deposit_1(self):
        account = BankAccount()
        result = account.deposit(500)
        self.assertEqual(result, 500)

    def test_deposit_2(self):
        account = BankAccount(100)
        account.deposit(50)
        self.assertEqual(account.balance, 150)

    def test_deposit_3(self):
        account = BankAccount(1000)
        result = account.deposit(250)
        self.assertEqual(result, 1250)
        self.assertEqual(account.balance, 1250)

    def test_deposit_4(self):
        account = BankAccount(200)
        account.deposit(100)
        result = account.deposit(300)
        self.assertEqual(result, 600)
        self.assertEqual(account.balance, 600)

    def test_deposit_5(self):
        account = BankAccount(300)
        with self.assertRaises(ValueError) as cm:
            account.deposit(-50)
        self.assertEqual(str(cm.exception), "Invalid amount")
        self.assertEqual(account.balance, 300)

import unittest

class AgentTest_withdraw(unittest.TestCase):

    def test_withdraw_1(self):
        account = BankAccount(500)
        result = account.withdraw(200)
        self.assertEqual(result, 300)

    def test_withdraw_2(self):
        account = BankAccount(100)
        account.withdraw(30)
        self.assertEqual(account.balance, 70)

    def test_withdraw_3(self):
        account = BankAccount(250)
        result = account.withdraw(250)
        self.assertEqual(result, 0)
        self.assertEqual(account.balance, 0)

    def test_withdraw_4(self):
        account = BankAccount(300)
        with self.assertRaises(ValueError) as cm:
            account.withdraw(-50)
        self.assertEqual(str(cm.exception), "Invalid amount")

    def test_withdraw_5(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError) as cm:
            account.withdraw(150)
        self.assertEqual(str(cm.exception), "Insufficient balance.")

class AgentTest_view_balance(unittest.TestCase):

    def test_view_balance_1(self):
        account = BankAccount()
        result = account.view_balance()
        self.assertEqual(result, 0)

    def test_view_balance_2(self):
        account = BankAccount(750)
        result = account.view_balance()
        self.assertEqual(result, 750)

    def test_view_balance_3(self):
        account = BankAccount(100)
        account.deposit(50)
        result = account.view_balance()
        self.assertEqual(result, 150)

    def test_view_balance_4(self):
        account = BankAccount(500)
        account.withdraw(200)
        result = account.view_balance()
        self.assertEqual(result, 300)

    def test_view_balance_5(self):
        account1 = BankAccount()
        account2 = BankAccount()
        account1.deposit(1000)
        account1.transfer(account2, 300)
        self.assertEqual(account1.view_balance(), 700)
        self.assertEqual(account2.view_balance(), 300)

import unittest

class AgentTest_transfer(unittest.TestCase):

    def test_transfer_1(self):
        account1 = BankAccount()
        account2 = BankAccount()
        account1.deposit(1000)
        account1.transfer(account2, 300)
        self.assertEqual(account1.view_balance(), 700)
        self.assertEqual(account2.view_balance(), 300)

    def test_transfer_2(self):
        account1 = BankAccount(500)
        account2 = BankAccount()
        account1.transfer(account2, 500)
        self.assertEqual(account1.view_balance(), 0)
        self.assertEqual(account2.view_balance(), 500)

    def test_transfer_3(self):
        account1 = BankAccount(200)
        account2 = BankAccount(100)
        account1.transfer(account2, 50)
        self.assertEqual(account1.view_balance(), 150)
        self.assertEqual(account2.view_balance(), 150)

    def test_transfer_4(self):
        account1 = BankAccount(400)
        account2 = BankAccount(250)
        account1.transfer(account2, 0)
        self.assertEqual(account1.view_balance(), 400)
        self.assertEqual(account2.view_balance(), 250)

    def test_transfer_5(self):
        account1 = BankAccount(1000)
        account2 = BankAccount(300)
        total_before = account1.view_balance() + account2.view_balance()
        account1.transfer(account2, 125)
        account2.transfer(account1, 75)
        total_after = account1.view_balance() + account2.view_balance()
        self.assertEqual(total_after, total_before)
        self.assertEqual(account1.view_balance(), 950)
        self.assertEqual(account2.view_balance(), 350)