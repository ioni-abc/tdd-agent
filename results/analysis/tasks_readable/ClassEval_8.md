# ClassEval_8

## Skeleton (what the agent sees)

```python
class BankAccount:
    """
    This is a class as a bank account system, which supports deposit money, withdraw money, view balance, and transfer money.
    """

    def __init__(self, balance=0):
        """
        Initializes a bank account object with an attribute balance, default value is 0.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a certain amount into the account, increasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        :param amount: int
        """

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").
        :param amount: int
        """

    def view_balance(self):
        """
        Return the account balance.
        """

    def transfer(self, other_account, amount):
        """
        Transfers a certain amount from the current account to another account.
        :param other_account: BankAccount
        :param amount: int
        >>> account1 = BankAccount()
        >>> account2 = BankAccount()
        >>> account1.deposit(1000)
        >>> account1.transfer(account2, 300)
        account1.balance = 700 account2.balance = 300
        """
```

## Method `deposit`

### Docstring

```python
def deposit(self, amount):
        """
        Deposits a certain amount into the account, increasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        :param amount: int
        """
```

### Reference code (`solution_code`)

```python
def deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance
```

### Tests (`BankAccountTestDeposit`)

**test_deposit**: `stated`
- reason: The docstring says deposit adds the amount to the balance and returns the current balance, so depositing 1000 into a fresh account should return 1000, which the test checks.

```python
def test_deposit(self):
    account1 = BankAccount()
    ret = account1.deposit(1000)
    self.assertEqual(ret, 1000)
```

**test_deposit_2**: `stated`
- reason: The docstring says deposit increases the balance and returns the current balance, so a programmer would return 3000 after depositing 1000 and then 2000, matching the test's assertion.

```python
def test_deposit_2(self):
    account1 = BankAccount()
    account1.deposit(1000)
    ret = account1.deposit(2000)
    self.assertEqual(ret, 3000)
```

**test_deposit_3**: `stated`
- reason: The docstring says a negative amount raises ValueError("Invalid amount"), which is exactly what the test checks by passing -1000 and comparing the exception message.

```python
def test_deposit_3(self):
    account1 = BankAccount()
    with self.assertRaises(ValueError) as context:
        account1.deposit(-1000)
    self.assertEqual(str(context.exception), "Invalid amount")
```

**test_deposit_4**: `stated`
- reason: The docstring says only negative amounts are rejected and that the current balance is returned, so a programmer would add 0 to a fresh account and return its balance of 0, which is what the test checks.

```python
def test_deposit_4(self):
    account1 = BankAccount()
    ret = account1.deposit(0)
    self.assertEqual(ret, 0)
```

**test_deposit_5**: `stated`
- reason: The docstring says deposit adds the amount to the balance and returns the current balance, so a programmer would return the running total of 2000 after two deposits of 1000.

```python
def test_deposit_5(self):
    account1 = BankAccount()
    account1.deposit(1000)
    ret = account1.deposit(1000)
    self.assertEqual(ret, 2000)
```

## Method `withdraw`

### Docstring

```python
def withdraw(self, amount):
        """
        Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").
        :param amount: int
        """
```

### Reference code (`solution_code`)

```python
def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance
```

### Tests (`BankAccountTestWithdraw`)

**test_withdraw**: `stated`
- reason: The docstring says withdraw decreases the balance and returns the current balance, so a programmer following it would return 800 for a balance of 1000 minus 200.

```python
def test_withdraw(self):
    account1 = BankAccount()
    account1.balance = 1000
    ret = account1.withdraw(200)
    self.assertEqual(ret, 800)
```

**test_withdraw_2**: `stated`
- reason: The docstring explicitly says withdrawing more than the balance raises ValueError("Insufficient balance."), which is exactly what the test checks, so a programmer following it would pass.

```python
def test_withdraw_2(self):
    account1 = BankAccount()
    account1.balance = 500
    with self.assertRaises(ValueError) as context:
        account1.withdraw(1000)
    self.assertEqual(str(context.exception), "Insufficient balance.")
```

**test_withdraw_3**: `stated`
- reason: The docstring explicitly says a negative amount raises ValueError("Invalid amount"), which is exactly what the test checks by passing -1000 and comparing the message.

```python
def test_withdraw_3(self):
    account1 = BankAccount()
    with self.assertRaises(ValueError) as context:
        account1.withdraw(-1000)
    self.assertEqual(str(context.exception), "Invalid amount")
```

**test_withdraw_4**: `stated`
- reason: The docstring says withdrawing a valid amount decreases the balance and returns the current balance, which is exactly what the test checks (1000 minus 500 returns 500).

```python
def test_withdraw_4(self):
    account1 = BankAccount()
    account1.balance = 1000
    ret = account1.withdraw(500)
    self.assertEqual(ret, 500)
```

**test_withdraw_5**: `stated`
- reason: The docstring says only amounts greater than the balance raise an error and that the current balance is returned, so a programmer would correctly return 0 when withdrawing the full balance.

```python
def test_withdraw_5(self):
    account1 = BankAccount()
    account1.balance = 1000
    ret = account1.withdraw(1000)
    self.assertEqual(ret, 0)
```

## Method `view_balance`

### Docstring

```python
def view_balance(self):
        """
        Return the account balance.
        """
```

### Reference code (`solution_code`)

```python
def view_balance(self):
        return self.balance
```

### Tests (`BankAccountTestViewBalance`)

**test_view_balance**: `unstated`
- reason: The docstring only says to return the account balance, so it does not say that a newly created account starts at zero, which is what the test expects.
- missing: The docstring should state the starting balance for a newly created account (and what a balance of a new account is when no initial amount is given), so that the expected initial value is specified.

```python
def test_view_balance(self):
    account1 = BankAccount()
    self.assertEqual(account1.view_balance(), 0)
```

**test_view_balance_2**: `stated`
- reason: The docstring says to return the account balance, and the test sets the balance to 1000 and expects view_balance to return 1000, which a programmer following the docstring would implement as returning the stored balance.

```python
def test_view_balance_2(self):
    account1 = BankAccount()
    account1.balance = 1000
    self.assertEqual(account1.view_balance(), 1000)
```

**test_view_balance_3**: `stated`
- reason: The docstring says the method returns the account balance, and the test sets the balance to 500 and checks that view_balance returns 500, which a programmer would implement by returning the stored balance.

```python
def test_view_balance_3(self):
    account1 = BankAccount()
    account1.balance = 500
    self.assertEqual(account1.view_balance(), 500)
```

**test_view_balance_4**: `stated`
- reason: The docstring says the method returns the account balance, and the test sets the balance to 1500 and checks that view_balance returns 1500, which a programmer would implement by returning self.balance.

```python
def test_view_balance_4(self):
    account1 = BankAccount()
    account1.balance = 1500
    self.assertEqual(account1.view_balance(), 1500)
```

**test_view_balance_5**: `stated`
- reason: The docstring says to return the account balance, and the test sets the balance to 2000 and expects view_balance to return 2000, which a programmer following the docstring would implement.

```python
def test_view_balance_5(self):
    account1 = BankAccount()
    account1.balance = 2000
    self.assertEqual(account1.view_balance(), 2000)
```

## Method `transfer`

### Docstring

```python
def transfer(self, other_account, amount):
        """
        Transfers a certain amount from the current account to another account.
        :param other_account: BankAccount
        :param amount: int
        >>> account1 = BankAccount()
        >>> account2 = BankAccount()
        >>> account1.deposit(1000)
        >>> account1.transfer(account2, 300)
        account1.balance = 700 account2.balance = 300
        """
```

### Reference code (`solution_code`)

```python
def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)
```

### Tests (`BankAccountTestTransfer`)

**test_transfer**: `stated`
- reason: The docstring says transfer moves an amount from the current account to the other account, so a programmer would withdraw from the sender and deposit to the receiver, which gives 500 and 1300 here.

```python
def test_transfer(self):
    account1 = BankAccount()
    account2 = BankAccount()
    account1.balance = 800
    account2.balance = 1000
    account1.transfer(account2, 300)
    self.assertEqual(account1.view_balance(), 500)
    self.assertEqual(account2.view_balance(), 1300)
```

**test_transfer_2**: `unstated`
- reason: The docstring only shows a successful transfer and never says that transferring more than the balance must raise a ValueError with the message "Insufficient balance.", which is what this test checks.
- missing: The docstring should state that if the amount exceeds the source account's balance, the method raises a ValueError with the message "Insufficient balance." and leaves both balances unchanged.

```python
def test_transfer_2(self):
    account1 = BankAccount()
    account2 = BankAccount()
    account1.balance = 500
    with self.assertRaises(ValueError) as context:
        account1.transfer(account2, 600)
    self.assertEqual(str(context.exception), "Insufficient balance.")
```

**test_transfer_3**: `unstated`
- reason: The docstring says nothing about invalid amounts, so a programmer following it would not know to raise an error for a negative transfer, while the test expects a ValueError with a specific message.
- missing: The docstring should state that any amount that is negative or otherwise invalid causes a ValueError with the message "Invalid amount", and that neither account's balance changes in that case.

```python
def test_transfer_3(self):
    account1 = BankAccount()
    account2 = BankAccount()
    account1.balance = 500
    account2.balance = 1000
    with self.assertRaises(ValueError) as context:
        account1.transfer(account2, -600)
    self.assertEqual(str(context.exception), "Invalid amount")
```

**test_transfer_4**: `stated`
- reason: The docstring says transfer moves a given amount from the current account to the other account, and a programmer would implement that as withdraw then deposit, which yields 0 and 1500 for this case.

```python
def test_transfer_4(self):
    account1 = BankAccount()
    account2 = BankAccount()
    account1.balance = 500
    account2.balance = 1000
    account1.transfer(account2, 500)
    self.assertEqual(account1.view_balance(), 0)
    self.assertEqual(account2.view_balance(), 1500)
```

**test_transfer_5**: `stated`
- reason: The docstring says the amount moves from the current account to the other account, so a programmer would subtract 200 from the 500 balance and add it to the 1000 balance, matching the test's 300 and 1200.

```python
def test_transfer_5(self):
    account1 = BankAccount()
    account2 = BankAccount()
    account1.balance = 500
    account2.balance = 1000
    account1.transfer(account2, 200)
    self.assertEqual(account1.view_balance(), 300)
    self.assertEqual(account2.view_balance(), 1200)
```

## Tests in no method's test class

### `BankAccountTest`

**test_all**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_all(self):
    account1 = BankAccount()
    account2 = BankAccount()
    account1.deposit(1000)
    account1.withdraw(200)
    account1.transfer(account2, 300)
    self.assertEqual(account1.view_balance(), 500)
    self.assertEqual(account2.view_balance(), 300)
```

**test_all2**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_all2(self):
    account1 = BankAccount()
    account2 = BankAccount()
    account1.deposit(1000)
    account1.withdraw(200)
    account1.transfer(account2, 300)
    account2.withdraw(100)
    self.assertEqual(account1.view_balance(), 500)
    self.assertEqual(account2.view_balance(), 200)
```
