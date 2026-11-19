import unittest



class BankAccountTestDeposit(unittest.TestCase):

    def test_deposit(self):
        account1 = BankAccount()
        ret = account1.deposit(1000)
        self.assertEqual(ret, 1000)

    def test_deposit_2(self):
        account1 = BankAccount()
        account1.deposit(1000)
        ret = account1.deposit(2000)
        self.assertEqual(ret, 3000)

    def test_deposit_3(self):
        account1 = BankAccount()
        with self.assertRaises(ValueError) as context:
            account1.deposit(-1000)
        self.assertEqual(str(context.exception), "Invalid amount")

class AgentTest_deposit(unittest.TestCase):

    def test_deposit_1(self):
        account1 = BankAccount(500)
        ret = account1.deposit(1000)
        self.assertEqual(ret, 1500)
        self.assertEqual(account1.balance, 1500)

    def test_deposit_2(self):
        account1 = BankAccount(700)
        ret = account1.deposit(0)
        self.assertEqual(ret, 700)
        self.assertEqual(account1.view_balance(), 700)

class BankAccountTestWithdraw(unittest.TestCase):

    def test_withdraw(self):
        account1 = BankAccount()
        account1.balance = 1000
        ret = account1.withdraw(200)
        self.assertEqual(ret, 800)

    def test_withdraw_2(self):
        account1 = BankAccount()
        account1.balance = 500
        with self.assertRaises(ValueError) as context:
            account1.withdraw(1000)
        self.assertEqual(str(context.exception), "Insufficient balance.")

    def test_withdraw_3(self):
        account1 = BankAccount()
        with self.assertRaises(ValueError) as context:
            account1.withdraw(-1000)
        self.assertEqual(str(context.exception), "Invalid amount")

import unittest

class AgentTest_withdraw(unittest.TestCase):

    def test_withdraw_1(self):
        account1 = BankAccount(500)
        ret = account1.withdraw(500)
        self.assertEqual(ret, 0)
        self.assertEqual(account1.view_balance(), 0)

    def test_withdraw_2(self):
        account1 = BankAccount(1000)
        ret1 = account1.withdraw(300)
        self.assertEqual(ret1, 700)
        ret2 = account1.withdraw(200)
        self.assertEqual(ret2, 500)
        self.assertEqual(account1.balance, 500)
        self.assertEqual(account1.view_balance(), 500)

class BankAccountTestViewBalance(unittest.TestCase):

    def test_view_balance(self):
        account1 = BankAccount()
        self.assertEqual(account1.view_balance(), 0)

    def test_view_balance_2(self):
        account1 = BankAccount()
        account1.balance = 1000
        self.assertEqual(account1.view_balance(), 1000)

    def test_view_balance_3(self):
        account1 = BankAccount()
        account1.balance = 500
        self.assertEqual(account1.view_balance(), 500)

import unittest

class AgentTest_view_balance(unittest.TestCase):

    def test_view_balance_1(self):
        account1 = BankAccount(750)
        self.assertEqual(account1.view_balance(), 750)

    def test_view_balance_2(self):
        account1 = BankAccount(300)
        first = account1.view_balance()
        second = account1.view_balance()
        self.assertEqual(first, 300)
        self.assertEqual(second, 300)
        self.assertEqual(account1.balance, 300)

class BankAccountTestTransfer(unittest.TestCase):

    def test_transfer(self):
        account1 = BankAccount()
        account2 = BankAccount()
        account1.balance = 800
        account2.balance = 1000
        account1.transfer(account2, 300)
        self.assertEqual(account1.view_balance(), 500)
        self.assertEqual(account2.view_balance(), 1300)

    def test_transfer_2(self):
        account1 = BankAccount()
        account2 = BankAccount()
        account1.balance = 500
        with self.assertRaises(ValueError) as context:
            account1.transfer(account2, 600)
        self.assertEqual(str(context.exception), "Insufficient balance.")

    def test_transfer_3(self):
        account1 = BankAccount()
        account2 = BankAccount()
        account1.balance = 500
        account2.balance = 1000
        with self.assertRaises(ValueError) as context:
            account1.transfer(account2, -600)
        self.assertEqual(str(context.exception), "Invalid amount")

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
        account2 = BankAccount(200)
        account1.transfer(account2, 500)
        self.assertEqual(account1.view_balance(), 0)
        self.assertEqual(account2.view_balance(), 700)