# ClassEval_94

## Skeleton (what the agent sees)

```python
class VendingMachine:
    """
    This is a class to simulate a vending machine, including adding products, inserting coins, purchasing products, viewing balance, replenishing product inventory, and displaying product information.
    """

    def __init__(self):
        """
        Initializes the vending machine's inventory and balance.
        """
        self.inventory = {}
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :param item_name: The name of the product to be added, str.
        :param price: The price of the product to be added, float.
        :param quantity: The quantity of the product to be added, int.
        :return: None
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.add_item('Coke', 1.25, 10)
        >>> vendingMachine.inventory
        {'Coke': {'price': 1.25, 'quantity': 10}}

        """

    def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted, float.
        :return: The balance of the vending machine after the coins are inserted, float.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.insert_coin(1.25)
        1.25

        """

    def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
        :param item_name: The name of the product to be purchased, str.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        >>> vendingMachine.balance = 1.25
        >>> vendingMachine.purchase_item('Coke')
        0.0
        >>> vendingMachine.purchase_item('Pizza')
        False

        """

    def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished, str.
        :param quantity: The quantity of the product to be replenished, int.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        >>> vendingMachine.restock_item('Coke', 10)
        True
        >>> vendingMachine.restock_item('Pizza', 10)
        False

        """

    def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.display_items()
        False
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10} }
        >>> vendingMachine.display_items()
        'Coke - $1.25 [10]'

        """
```

## Method `add_item`

### Docstring

```python
def add_item(self, item_name, price, quantity):
        """
        Adds a product to the vending machine's inventory.
        :param item_name: The name of the product to be added, str.
        :param price: The price of the product to be added, float.
        :param quantity: The quantity of the product to be added, int.
        :return: None
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.add_item('Coke', 1.25, 10)
        >>> vendingMachine.inventory
        {'Coke': {'price': 1.25, 'quantity': 10}}

        """
```

### Reference code (`solution_code`)

```python
def add_item(self, item_name, price, quantity):
        if not self.restock_item(item_name, quantity):
            self.inventory[item_name] = {'price': price, 'quantity': quantity}
```

### Tests (`VendingMachineTestAddItem`)

**test_add_item**: `stated`
- reason: The docstring's own example adds 'Coke' at 1.25 with quantity 10 to a fresh machine and shows the inventory as {'Coke': {'price': 1.25, 'quantity': 10}}, which is exactly what the test checks.

```python
def test_add_item(self):
    vendingMachine = VendingMachine()
    vendingMachine.add_item('Coke', 1.25, 10)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})
```

**test_add_item_2**: `unstated`
- reason: The docstring only says the method adds a product to the inventory, so a programmer could reasonably overwrite the existing entry when the same item is added again, and the test expects the quantity to accumulate instead.
- missing: When the item name already exists in the inventory, the new quantity must be added to the stored quantity and the stored price kept, rather than the entry being replaced.

```python
def test_add_item_2(self):
    vendingMachine = VendingMachine()
    vendingMachine.add_item('Coke', 1.25, 10)
    vendingMachine.add_item('Coke', 1.25, 10)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 20}})
```

**test_add_item_3**: `stated`
- reason: The docstring says add_item adds a product with its price and quantity to the inventory, so a programmer would store each new item and the test's two-item inventory would match.

```python
def test_add_item_3(self):
    vendingMachine = VendingMachine()
    vendingMachine.add_item('Coke', 1.25, 10)
    vendingMachine.add_item('Pizza', 1.25, 10)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 10}})
```

**test_add_item_4**: `unstated`
- reason: The docstring says only that the method adds a product to the inventory, so a programmer could reasonably overwrite an existing entry, while the test expects the quantity to accumulate when the same item is added again.
- missing: The docstring should say what happens when the item already exists in the inventory, for example whether its quantity is increased by the new amount or its price and quantity are replaced.

```python
def test_add_item_4(self):
    vendingMachine = VendingMachine()
    vendingMachine.add_item('Coke', 1.25, 10)
    vendingMachine.add_item('Pizza', 1.25, 10)
    vendingMachine.add_item('Pizza', 1.25, 10)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 20}})
```

**test_add_item_5**: `unstated`
- reason: The docstring only says add_item adds a product, so a programmer would likely overwrite an existing entry, but the test expects the quantity to accumulate on re-adding an existing item.
- missing: The docstring should state what happens when the item name already exists: the quantity is added to the existing stock, and the stored price is left unchanged.

```python
def test_add_item_5(self):
    vendingMachine = VendingMachine()
    vendingMachine.add_item('Coke', 1.25, 10)
    vendingMachine.add_item('Pizza', 1.25, 10)
    vendingMachine.add_item('Pizza', 1.25, 10)
    vendingMachine.add_item('Coke', 1.25, 10)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 20}, 'Pizza': {'price': 1.25, 'quantity': 20}})
```

## Method `insert_coin`

### Docstring

```python
def insert_coin(self, amount):
        """
        Inserts coins into the vending machine.
        :param amount: The amount of coins to be inserted, float.
        :return: The balance of the vending machine after the coins are inserted, float.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.insert_coin(1.25)
        1.25

        """
```

### Reference code (`solution_code`)

```python
def insert_coin(self, amount):
        self.balance += amount
        return self.balance
```

### Tests (`VendingMachineTestInsertCoin`)

**test_insert_coin**: `stated`
- reason: The docstring says insert_coin returns the machine's balance after the coins are added, and its example shows a new machine returning 1.25 after inserting 1.25, which is exactly what the test checks.

```python
def test_insert_coin(self):
    vendingMachine = VendingMachine()
    self.assertEqual(vendingMachine.insert_coin(1.25), 1.25)
```

**test_insert_coin_2**: `stated`
- reason: The docstring says insert_coin adds the amount and returns the resulting balance, and its doctest shows a fresh machine returning the inserted amount, so a programmer would return 2.5 here.

```python
def test_insert_coin_2(self):
    vendingMachine = VendingMachine()
    self.assertEqual(vendingMachine.insert_coin(2.5), 2.5)
```

**test_insert_coin_3**: `stated`
- reason: The docstring says the method inserts coins and returns the machine's balance afterward, so a programmer would keep a running total that accumulates across calls, which is what the test checks after two insertions of 1.25.

```python
def test_insert_coin_3(self):
    vendingMachine = VendingMachine()
    vendingMachine.insert_coin(1.25)
    vendingMachine.insert_coin(1.25)
    self.assertEqual(vendingMachine.balance, 2.50)
```

**test_insert_coin_4**: `stated`
- reason: A programmer following the docstring would add the amount to the machine's existing balance and return the new total, which is what this test checks: three insertions onto a preset balance of 1.25 give 5.0.

```python
def test_insert_coin_4(self):
    vendingMachine = VendingMachine()
    vendingMachine.balance = 1.25
    vendingMachine.insert_coin(1.25)
    vendingMachine.insert_coin(1.25)
    vendingMachine.insert_coin(1.25)
    self.assertEqual(vendingMachine.balance, 5.0)
```

**test_insert_coin_5**: `stated`
- reason: The docstring says insert_coin adds the amount to the machine and returns the resulting balance, so a programmer would add each insertion to the existing balance and the test's cumulative 6.25 follows.

```python
def test_insert_coin_5(self):
    vendingMachine = VendingMachine()
    vendingMachine.balance = 1.25
    vendingMachine.insert_coin(1.25)
    vendingMachine.insert_coin(1.25)
    vendingMachine.insert_coin(1.25)
    vendingMachine.insert_coin(1.25)
    self.assertEqual(vendingMachine.balance, 6.25)
```

## Method `purchase_item`

### Docstring

```python
def purchase_item(self, item_name):
        """
        Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
        :param item_name: The name of the product to be purchased, str.
        :return: If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        >>> vendingMachine.balance = 1.25
        >>> vendingMachine.purchase_item('Coke')
        0.0
        >>> vendingMachine.purchase_item('Pizza')
        False

        """
```

### Reference code (`solution_code`)

```python
def purchase_item(self, item_name):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                return self.balance
            else:
                return False
        else:
            return False
```

### Tests (`VendingMachineTestPurchaseItem`)

**test_purchase_item**: `unstated`
- reason: The docstring says the method returns the post-purchase balance but never says that the item's stock quantity is decremented, which the test asserts on the inventory after the call.
- missing: On a successful purchase, the method must deduct the item's price from the machine's balance and reduce that item's stored quantity by one.

```python
def test_purchase_item(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vendingMachine.balance = 1.25
    self.assertEqual(vendingMachine.purchase_item('Coke'), 0.0)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 9}})
```

**test_purchase_item_2**: `stated`
- reason: The docstring says the method returns False when the purchase cannot be made, and its example shows `purchase_item('Pizza')` returning False for an item not in the inventory, so a programmer following it would return False here and leave the inventory untouched.

```python
def test_purchase_item_2(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vendingMachine.balance = 1.25
    self.assertEqual(vendingMachine.purchase_item('Pizza'), False)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})
```

**test_purchase_item_3**: `stated`
- reason: The docstring says the method returns False when the purchase is not successful, and this test checks that a purchase with insufficient balance returns False, which a programmer following the docstring would produce.

```python
def test_purchase_item_3(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    vendingMachine.balance = 0
    self.assertEqual(vendingMachine.purchase_item('Coke'), False)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})
```

**test_purchase_item_4**: `stated`
- reason: The docstring says the method returns False when the product is out of stock, which is exactly the case this test checks (quantity 0 with enough balance), so a programmer following it would return False.

```python
def test_purchase_item_4(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
    vendingMachine.balance = 1.25
    self.assertEqual(vendingMachine.purchase_item('Coke'), False)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 0}})
```

**test_purchase_item_5**: `stated`
- reason: The docstring says a successful purchase returns the balance after the purchase, and the test's return value of 0.0 follows from that, while the inventory-quantity check is the natural reading of "purchases a product".

```python
def test_purchase_item_5(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 10}}
    vendingMachine.balance = 1.25
    self.assertEqual(vendingMachine.purchase_item('Pizza'), 0.0)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 9}})
```

## Method `restock_item`

### Docstring

```python
def restock_item(self, item_name, quantity):
        """
        Replenishes the inventory of a product already in the vending machine.
        :param item_name: The name of the product to be replenished, str.
        :param quantity: The quantity of the product to be replenished, int.
        :return: If the product is already in the vending machine, returns True, otherwise, returns False.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        >>> vendingMachine.restock_item('Coke', 10)
        True
        >>> vendingMachine.restock_item('Pizza', 10)
        False

        """
```

### Reference code (`solution_code`)

```python
def restock_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            return True
        else:
            return False
```

### Tests (`VendingMachineTestRestockItem`)

**test_restock_item**: `stated`
- reason: The docstring says restock_item replenishes an existing product and returns True when the product is present, so a programmer would add the quantity to the stock and return True, which is what the test checks.

```python
def test_restock_item(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    self.assertEqual(vendingMachine.restock_item('Coke', 10), True)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 20}})
```

**test_restock_item_2**: `stated`
- reason: The docstring says restock applies only to a product already in the machine and returns False otherwise, so a programmer would return False for an unknown item and leave the inventory untouched, which is what the test checks.

```python
def test_restock_item_2(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    self.assertEqual(vendingMachine.restock_item('Pizza', 10), False)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})
```

**test_restock_item_3**: `stated`
- reason: The docstring says restock_item replenishes an existing product's inventory and returns True when the product is present, which is exactly what this test checks: an existing item with quantity 0 is restocked by 10 and returns True.

```python
def test_restock_item_3(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
    self.assertEqual(vendingMachine.restock_item('Coke', 10), True)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})
```

**test_restock_item_4**: `stated`
- reason: The docstring says the method replenishes a product already in the machine and returns True in that case, so a programmer following it would add the quantity to the existing stock and return True, which is what the test checks.

```python
def test_restock_item_4(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 10}}
    self.assertEqual(vendingMachine.restock_item('Pizza', 10), True)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 20}})
```

**test_restock_item_5**: `stated`
- reason: The docstring says that restocking an existing product returns True and that the call otherwise behaves as a replenishment, so a programmer following it would add zero to the quantity, leave the inventory unchanged, and return True, which is what the test checks.

```python
def test_restock_item_5(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 10}}
    self.assertEqual(vendingMachine.restock_item('Pizza', 0), True)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 10}})
```

## Method `display_items`

### Docstring

```python
def display_items(self):
        """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.display_items()
        False
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10} }
        >>> vendingMachine.display_items()
        'Coke - $1.25 [10]'

        """
```

### Reference code (`solution_code`)

```python
def display_items(self):
        if not self.inventory:
            return False
        else:
            items = []
            for item_name, item_info in self.inventory.items():
                items.append(f"{item_name} - ${item_info['price']} [{item_info['quantity']}]")
            return "\n".join(items)
```

### Tests (`VendingMachineTestDisplayItems`)

**test_display_items**: `stated`
- reason: The docstring's second doctest shows the exact single-item output the test expects, 'Coke - $1.25 [10]', so a programmer following it would pass.

```python
def test_display_items(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    self.assertEqual(vendingMachine.display_items(), 'Coke - $1.25 [10]')
```

**test_display_items_2**: `stated`
- reason: The docstring says an empty vending machine makes display_items return False, which is exactly what the test checks on a fresh VendingMachine.

```python
def test_display_items_2(self):
    vendingMachine = VendingMachine()
    self.assertEqual(vendingMachine.display_items(), False)
```

**test_display_items_3**: `unstated`
- reason: The docstring shows only a single-product output, so a programmer could reasonably join multiple products with a comma, semicolon, or other separator, and the test's newline separator is not specified.
- missing: The docstring should state how multiple products are separated in the returned string (for example, that each product goes on its own line, joined by newline characters).

```python
def test_display_items_3(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}, 'Pizza': {'price': 1.25, 'quantity': 10}}
    self.assertEqual(vendingMachine.display_items(),"Coke - $1.25 [10]\nPizza - $1.25 [10]")
```

**test_display_items_4**: `unstated`
- reason: The docstring says products are listed when the machine is non-empty, but it does not say whether a product with zero stock is still shown, so a programmer could reasonably filter it out and fail this test.
- missing: The docstring should state whether products whose quantity is zero (sold out) are still listed, and in what form their quantity appears.

```python
def test_display_items_4(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 0}}
    self.assertEqual(vendingMachine.display_items(), 'Coke - $1.25 [0]')
```

**test_display_items_5**: `unstated`
- reason: The docstring never says how multiple products are joined into the returned string, so a correct implementation could choose a different separator and fail this test, which expects one item per line joined by newlines.
- missing: The docstring should state that when there are several products, each product's line is separated from the next by a newline character, in the order they appear in the inventory.

```python
def test_display_items_5(self):
    vendingMachine = VendingMachine()
    vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 0}, 'Pizza': {'price': 1.25, 'quantity': 10}}
    self.assertEqual(vendingMachine.display_items(), 'Coke - $1.25 [0]\nPizza - $1.25 [10]')
```

## Tests in no method's test class

### `VendingMachineTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    vendingMachine = VendingMachine()
    self.assertEqual(vendingMachine.display_items(), False)
    vendingMachine.add_item('Coke', 1.25, 10)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})
    self.assertEqual(vendingMachine.insert_coin(1.25), 1.25)
    self.assertEqual(vendingMachine.purchase_item('Coke'), 0.0)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 9}})
    self.assertEqual(vendingMachine.purchase_item('Pizza'), False)
    self.assertEqual(vendingMachine.restock_item('Coke', 10), True)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 19}})
    self.assertEqual(vendingMachine.restock_item('Pizza', 10), False)
    self.assertEqual(vendingMachine.display_items(), 'Coke - $1.25 [19]')
```

**test_main_2**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main_2(self):
    vendingMachine = VendingMachine()
    self.assertEqual(vendingMachine.purchase_item('Coke'), False)
    vendingMachine.add_item('Coke', 1.25, 10)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})
    self.assertEqual(vendingMachine.restock_item('Pizza', 10), False)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 10}})
    self.assertEqual(vendingMachine.insert_coin(1.25), 1.25)
    self.assertEqual(vendingMachine.purchase_item('Coke'), 0.0)
    self.assertEqual(vendingMachine.inventory, {'Coke': {'price': 1.25, 'quantity': 9}})
    self.assertEqual(vendingMachine.display_items(), 'Coke - $1.25 [9]')
```
