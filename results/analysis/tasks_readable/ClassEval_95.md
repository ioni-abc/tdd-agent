# ClassEval_95

## Skeleton (what the agent sees)

```python
class Warehouse:
    """
    The class manages inventory and orders, including adding products, updating product quantities, retrieving product quantities, creating orders, changing order statuses, and tracking orders.
    """

    def __init__(self):
        """
        Initialize two fields.
        self.inventory is a dict that stores the products.
        self.inventory = {Product ID: Product}
        self.orders is a dict that stores the products in a order.
        self.orders = {Order ID: Order}
        """
        self.inventory = {}  # Product ID: Product
        self.orders = {}  # Order ID: Order

    def add_product(self, product_id, name, quantity):
        """
        Add product to inventory and plus the quantity if it has existed in inventory.
        Or just add new product to dict otherwise.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 3}}
        """

    def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.update_product_quantity(1, -1)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 2}}
        """

    def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :param product_id, int
        :return: if the product_id is in inventory then return the corresponding quantity,
                or False otherwise.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.get_product_quantity(1)
        3
        >>> warehouse.get_product_quantity(2)
        False
        """

    def create_order(self, order_id, product_id, quantity):
        """
        Create a order which includes the infomation of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: the quantity of product that be selected.
        :return False: only if product_id is not in inventory or the quantity is not adequate
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}
        >>> warehouse.create_order(1, 2, 2)
        False
        """

    def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state that is going to change to
        :return False: only if the order_id is not in self.orders
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.change_order_status(1, "done")
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'done'}}
        """

    def track_order(self, order_id):
        """
        Get the status of specific order.
        :param order_id: int
        :return False: only if the order_id is not in self.orders.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Shipped'
        """
```

## Method `add_product`

### Docstring

```python
def add_product(self, product_id, name, quantity):
        """
        Add product to inventory and plus the quantity if it has existed in inventory.
        Or just add new product to dict otherwise.
        :param product_id: int
        :param name: str, product name
        :param quantity: int, product quantity
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 3}}
        """
```

### Reference code (`solution_code`)

```python
def add_product(self, product_id, name, quantity):
        if product_id not in self.inventory:
            self.inventory[product_id] = {'name': name, 'quantity': quantity}
        else:
            self.inventory[product_id]['quantity'] += quantity
```

### Tests (`WarehouseTestAddProduct`)

**test_add_product_1**: `stated`
- reason: The docstring says a new product is added to the inventory dict with its name and quantity, and its example shows exactly that structure for an empty warehouse, so a programmer following it would pass this test.

```python
def test_add_product_1(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 10}})
```

**test_add_product_2**: `stated`
- reason: The docstring says a new product is added as a dict with its name and quantity when its id is not yet in the inventory, which is exactly what the test checks for two distinct product ids.

```python
def test_add_product_2(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    warehouse.add_product(2, 'product 2', 5)
    self.assertEqual(warehouse.inventory,
                     {1: {'name': 'product 1', 'quantity': 10}, 2: {'name': 'product 2', 'quantity': 5}})
```

**test_add_product_3**: `stated`
- reason: The docstring says adding a new product_id creates an entry with name and quantity in the inventory dict, which is exactly what this test checks after adding product 1 to an empty warehouse.

```python
def test_add_product_3(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 3', 10)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 3', 'quantity': 10}})
```

**test_add_product_4**: `stated`
- reason: The docstring says a new product is added to the inventory with its name and quantity, and its example shows exactly the expected dict for a first-time add, so a programmer following it would pass this test.

```python
def test_add_product_4(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 4', 10)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 4', 'quantity': 10}})
```

**test_add_product_5**: `stated`
- reason: The docstring says a new product is added to the inventory with its name and quantity, and its example shows exactly the dict structure the test checks for a fresh warehouse.

```python
def test_add_product_5(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 5', 10)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 5', 'quantity': 10}})
```

**test_add_product_6**: `stated`
- reason: The docstring says that adding an existing product increases its quantity rather than replacing the entry, which is exactly what the test checks by adding the same product twice and expecting a summed quantity.

```python
def test_add_product_6(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 5', 10)
    warehouse.add_product(1, 'product 5', 10)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 5', 'quantity': 20}})
```

## Method `update_product_quantity`

### Docstring

```python
def update_product_quantity(self, product_id, quantity):
        """
        According to product_id, add the quantity to the corresponding product in inventory.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.update_product_quantity(1, -1)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 2}}
        """
```

### Reference code (`solution_code`)

```python
def update_product_quantity(self, product_id, quantity):
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity
```

### Tests (`WarehouseTestUpdateProductQuantity`)

**test_update_product_quantity_1**: `stated`
- reason: The docstring says the quantity is added to the matching product's stock, so a programmer would produce 10 + 5 = 15, which is what the test expects.

```python
def test_update_product_quantity_1(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    warehouse.update_product_quantity(1, 5)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 15}})
```

**test_update_product_quantity_2**: `stated`
- reason: The docstring says to add the given quantity to the product's stock, and its example with a negative value (-1 taking 3 to 2) shows that negative amounts subtract, so a programmer following it would get 10 - 5 = 5.

```python
def test_update_product_quantity_2(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    warehouse.update_product_quantity(1, -5)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 5}})
```

**test_update_product_quantity_3**: `unstated`
- reason: The docstring only describes adding to an existing product, so a programmer could reasonably raise an error or create an entry for an unknown product_id, while the test expects the inventory to stay unchanged.
- missing: The docstring should say what happens when product_id is not in the inventory, for example that the call is silently ignored and no entry is created or error raised.

```python
def test_update_product_quantity_3(self):
    warehouse = Warehouse()
    warehouse.update_product_quantity(1, -5)
    self.assertEqual(warehouse.inventory, {})
```

**test_update_product_quantity_4**: `stated`
- reason: The docstring says to add the given quantity to the matching product's stock, and the test adds 1 to a quantity of 10 and expects 11, which a programmer following that description would produce.

```python
def test_update_product_quantity_4(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    warehouse.update_product_quantity(1, 1)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 11}})
```

**test_update_product_quantity_5**: `stated`
- reason: The docstring says to add the given quantity to the product's stock, and the example already shows a negative value reducing it, so a programmer would compute 10 + (-9) = 1 and pass the test.

```python
def test_update_product_quantity_5(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    warehouse.update_product_quantity(1, -9)
    self.assertEqual(warehouse.inventory, {1: {'name': 'product 1', 'quantity': 1}})
```

## Method `get_product_quantity`

### Docstring

```python
def get_product_quantity(self, product_id):
        """
        Get the quantity of specific product by product_id.
        :param product_id, int
        :return: if the product_id is in inventory then return the corresponding quantity,
                or False otherwise.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.get_product_quantity(1)
        3
        >>> warehouse.get_product_quantity(2)
        False
        """
```

### Reference code (`solution_code`)

```python
def get_product_quantity(self, product_id):
        if product_id in self.inventory:
            return self.inventory[product_id]['quantity']
        else:
            return False
```

### Tests (`WarehouseTestGetProductQuantity`)

**test_get_product_quantity_1**: `stated`
- reason: The docstring says that a product present in inventory returns its corresponding quantity, and the test adds product 1 with quantity 10 and expects get_product_quantity(1) to return 10, which a programmer following the docstring would implement.

```python
def test_get_product_quantity_1(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    self.assertEqual(warehouse.get_product_quantity(1), 10)
```

**test_get_product_quantity_2**: `stated`
- reason: The docstring says that an id absent from inventory returns False, and the test checks exactly that for an empty warehouse, so a programmer following the docstring would pass.

```python
def test_get_product_quantity_2(self):
    warehouse = Warehouse()
    self.assertEqual(warehouse.get_product_quantity(1), False)
```

**test_get_product_quantity_3**: `stated`
- reason: The docstring says that for a product_id in inventory the method returns its quantity, and the test adds product 1 with quantity 5 and expects 5 back, which a programmer following the docstring would pass.

```python
def test_get_product_quantity_3(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 5)
    self.assertEqual(warehouse.get_product_quantity(1), 5)
```

**test_get_product_quantity_4**: `stated`
- reason: The docstring says that a product in inventory returns its quantity, and the test checks exactly that for a product added with quantity 100, so a programmer following it would pass.

```python
def test_get_product_quantity_4(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 100)
    self.assertEqual(warehouse.get_product_quantity(1), 100)
```

**test_get_product_quantity_5**: `stated`
- reason: The docstring says that a product id present in inventory returns its corresponding quantity, and the test adds product 5 with quantity 10 and expects 10 back, which a programmer following the docstring would produce.

```python
def test_get_product_quantity_5(self):
    warehouse = Warehouse()
    warehouse.add_product(5, 'product 1', 10)
    self.assertEqual(warehouse.get_product_quantity(5), 10)
```

## Method `create_order`

### Docstring

```python
def create_order(self, order_id, product_id, quantity):
        """
        Create a order which includes the infomation of product, like id and quantity.
        And put the new order into self.orders.
        The default value of status is 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: the quantity of product that be selected.
        :return False: only if product_id is not in inventory or the quantity is not adequate
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}
        >>> warehouse.create_order(1, 2, 2)
        False
        """
```

### Reference code (`solution_code`)

```python
def create_order(self, order_id, product_id, quantity):
        if self.get_product_quantity(product_id) >= quantity:
            self.update_product_quantity(product_id, -quantity)
            self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
        else:
            return False
```

### Tests (`WarehouseTestCreateOrder`)

**test_create_order_1**: `stated`
- reason: The docstring says create_order stores an order with product_id, quantity and a default status of 'Shipped' in self.orders when stock is sufficient, which is what this test checks.

```python
def test_create_order_1(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    warehouse.create_order(1, 1, 5)
    self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 5, 'status': 'Shipped'}})
```

**test_create_order_2**: `stated`
- reason: The docstring says create_order returns False when the requested quantity is not adequate, and the test orders 15 of a product with only 10 in stock and expects False, which a programmer following the docstring would pass.

```python
def test_create_order_2(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    result = warehouse.create_order(1, 1, 15)
    self.assertFalse(result)
```

**test_create_order_3**: `stated`
- reason: The docstring says an order is created and stored in `self.orders` with status 'Shipped' whenever the inventory holds enough quantity, and the test checks exactly that for an order that uses up the full stock.

```python
def test_create_order_3(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 1)
    warehouse.create_order(1, 1, 1)
    self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 1, 'status': 'Shipped'}})
```

**test_create_order_4**: `stated`
- reason: The docstring says an order is created and stored with product_id, quantity and status 'Shipped', and returns False only when stock is inadequate, so a programmer would create the order when the requested quantity equals the stock, which is what the test checks.

```python
def test_create_order_4(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 4', 5)
    warehouse.create_order(1, 1, 5)
    self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 5, 'status': 'Shipped'}})
```

**test_create_order_5**: `stated`
- reason: The docstring says create_order stores an order with product_id, quantity and status 'Shipped' in self.orders when stock is sufficient, which is exactly what this test checks with 50 of 100 units in stock.

```python
def test_create_order_5(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 5', 100)
    warehouse.create_order(1, 1, 50)
    self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 50, 'status': 'Shipped'}})
```

## Method `change_order_status`

### Docstring

```python
def change_order_status(self, order_id, status):
        """
        Change the status of order if the input order_id is in self.orders.
        :param order_id: int
        :param status: str, the state that is going to change to
        :return False: only if the order_id is not in self.orders
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.change_order_status(1, "done")
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'done'}}
        """
```

### Reference code (`solution_code`)

```python
def change_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False
```

### Tests (`WarehouseTestChangeOrderStatus`)

**test_change_order_status_1**: `stated`
- reason: The docstring says the order's status is changed to the given value when the order_id exists, and the test checks exactly that: an existing order's status becomes the passed string and the orders dict reflects it.

```python
def test_change_order_status_1(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    warehouse.create_order(1, 1, 5)
    warehouse.change_order_status(1, 'Delivered')
    self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 5, 'status': 'Delivered'}})
```

**test_change_order_status_2**: `stated`
- reason: The docstring says the method returns False when order_id is not in self.orders, and the test calls it on an empty warehouse and expects False, which a programmer following the docstring would produce.

```python
def test_change_order_status_2(self):
    warehouse = Warehouse()
    result = warehouse.change_order_status(1, 'Delivered')
    self.assertFalse(result)
```

**test_change_order_status_3**: `stated`
- reason: The docstring says the status changes when the order exists, and the test checks that an existing order's status is updated to the given string, which a programmer following the docstring would implement.

```python
def test_change_order_status_3(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 3', 5)
    warehouse.create_order(1, 1, 5)
    warehouse.change_order_status(1, 'Delivered')
    self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 5, 'status': 'Delivered'}})
```

**test_change_order_status_4**: `stated`
- reason: The docstring says the status of an existing order is changed to the given value, and its example shows the orders dict updated with the new status, which is exactly what this test checks.

```python
def test_change_order_status_4(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 4', 100)
    warehouse.create_order(1, 1, 50)
    warehouse.change_order_status(1, 'Delivered')
    self.assertEqual(warehouse.orders, {1: {'product_id': 1, 'quantity': 50, 'status': 'Delivered'}})
```

**test_change_order_status_5**: `stated`
- reason: The docstring says the method returns False when order_id is not in self.orders, and the test calls it with a non-existent order on an empty warehouse and expects False.

```python
def test_change_order_status_5(self):
    warehouse = Warehouse()
    result = warehouse.change_order_status(2, 'Delivered')
    self.assertFalse(result)
```

## Method `track_order`

### Docstring

```python
def track_order(self, order_id):
        """
        Get the status of specific order.
        :param order_id: int
        :return False: only if the order_id is not in self.orders.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Shipped'
        """
```

### Reference code (`solution_code`)

```python
def track_order(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]['status']
        else:
            return False
```

### Tests (`WarehouseTestTrackOrder`)

**test_track_order_1**: `stated`
- reason: The docstring's example does the same flow (add product, create order, track it) and shows `'Shipped'` as the returned status, so a programmer following it would return that status for this test.

```python
def test_track_order_1(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    warehouse.create_order(1, 1, 5)
    self.assertEqual(warehouse.track_order(1), 'Shipped')
```

**test_track_order_2**: `stated`
- reason: The docstring says track_order returns False when the order_id is not in self.orders, and the test queries an empty warehouse for an absent id and expects False, which a programmer following the docstring would produce.

```python
def test_track_order_2(self):
    warehouse = Warehouse()
    result = warehouse.track_order(1)
    self.assertFalse(result)
```

**test_track_order_3**: `stated`
- reason: The docstring example shows that tracking an order just created with create_order returns 'Shipped', which is the behaviour this test checks.

```python
def test_track_order_3(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 3', 10)
    warehouse.create_order(1, 1, 1)
    self.assertEqual(warehouse.track_order(1), 'Shipped')
```

**test_track_order_4**: `stated`
- reason: The docstring's example shows that tracking an order right after creating it returns 'Shipped', which is exactly what this test checks.

```python
def test_track_order_4(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 4', 100)
    warehouse.create_order(1, 1, 50)
    self.assertEqual(warehouse.track_order(1), 'Shipped')
```

**test_track_order_5**: `stated`
- reason: The docstring's example shows that after adding a product and creating an order, `track_order` on that order id returns `'Shipped'`, which is exactly what this test checks.

```python
def test_track_order_5(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 5', 100)
    warehouse.create_order(1, 1, 10)
    self.assertEqual(warehouse.track_order(1), 'Shipped')
```

## Tests in no method's test class

### `WarehouseTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    warehouse = Warehouse()
    warehouse.add_product(1, 'product 1', 10)
    self.assertEqual({1: {'name': 'product 1', 'quantity': 10}}, warehouse.inventory)

    warehouse.update_product_quantity(1, -5)
    self.assertEqual({1: {'name': 'product 1', 'quantity': 5}}, warehouse.inventory)

    self.assertEqual(warehouse.get_product_quantity(1), 5)

    warehouse.create_order(1, 1, 3)
    self.assertEqual({1: {'product_id': 1, 'quantity': 3, 'status': 'Shipped'}}, warehouse.orders)

    warehouse.change_order_status(1, 'Delivered')
    self.assertEqual({1: {'product_id': 1, 'quantity': 3, 'status': 'Delivered'}}, warehouse.orders)

    self.assertEqual('Delivered', warehouse.track_order(1))
```
