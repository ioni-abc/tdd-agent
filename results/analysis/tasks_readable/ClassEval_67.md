# ClassEval_67

## Skeleton (what the agent sees)

```python
class Order:
    """
    The class manages restaurant orders by allowing the addition of dishes, calculation of the total cost, and checkout.
    """


    def __init__(self):
        """
        Initialize the order management system
        self.menu stores the dishes of resturant inventory
        menu = [{"dish": dish name, "price": price, "count": count}, ...]
        self.selected_dishes stores the dished selected by customer
        selected_dish = {"dish": dish name, "count": count, price: price}
        self.sales stores the sales of each dish
        sales = {dish name: sales}
        """
        self.menu = []
        self.selected_dishes = []
        self.sales = {}


    def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        True
        """

    def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """

    def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.checkout()
        32.0
        """
```

## Method `add_dish`

### Docstring

```python
def add_dish(self, dish):
        """
        Check the self.menu and add into self.selected_dish if the dish count is valid.
        And if the dish has successfully been added, change the count in self.menu.
        :param dish: dict, the information of dish. dish = {"dish": dish name, "count": count, price: price}
        :return: True if successfully added, or False otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        True
        """
```

### Reference code (`solution_code`)

```python
def add_dish(self, dish):
        for menu_dish in self.menu:
            if dish["dish"] == menu_dish["dish"]:
                if menu_dish["count"] < dish["count"]:
                    return False
                else:
                    menu_dish["count"] -= dish["count"]
                    break
        self.selected_dishes.append(dish)
        return True
```

### Tests (`OrderTestAddDish`)

setUp (runs before each test):

```python
def setUp(self):
    self.order = Order()

    self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
    self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
    self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}
```

**test_add_dish_1**: `stated`
- reason: The docstring says a valid dish is added to the selected dishes, the menu count is decremented, and True is returned, which is what this test checks for an in-stock dish.

```python
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
```

**test_add_dish_2**: `stated`
- reason: The docstring says a dish is added only if its count is valid against self.menu and that the menu count changes only on success, so a programmer would return False and leave the menu and selected list untouched when the requested count exceeds the available count.

```python
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
```

**test_add_dish_3**: `stated`
- reason: The docstring says the dish is added only if its count is valid against the menu, the dish is then appended to selected dishes, and the menu count is decremented, which is what the test checks, including the exact-remaining-count boundary and the mismatched price being stored as passed.

```python
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
```

**test_add_dish_4**: `stated`
- reason: The docstring says a dish is added to `selected_dishes` when its count fits the menu, the menu count is then reduced, and the method returns True, which is exactly what the test checks.

```python
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
```

**test_add_dish_5**: `stated`
- reason: The docstring says a dish is added to the selected list when its count is available in the menu, and that the menu count is then reduced, which is what the test checks: dish3 with count 5 succeeds, menu count drops from 7 to 2, and the passed dict is appended.

```python
def test_add_dish_5(self):
    result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 5})
    self.assertTrue(result)

    # test the status of self.menu and self.selected_dishes
    menu = self.order.menu
    for menu_dish in menu:
        if menu_dish["dish"] == "dish1":
            self.assertEqual(menu_dish["count"], 5)
        if menu_dish["dish"] == "dish2":
            self.assertEqual(menu_dish["count"], 3)
        if menu_dish["dish"] == "dish3":
            self.assertEqual(menu_dish["count"], 2)
    self.assertEqual(self.order.selected_dishes, [{"dish": "dish3", "price": 15, "count": 5}])
```

**test_add_dish_6**: `unstated`
- reason: The docstring never says what happens when the requested dish is not on the menu, and the test expects a dish with no name or count (an empty dict) to be accepted with True, which a programmer reading "add if the dish count is valid" would likely reject.
- missing: The docstring should state whether a dish whose name does not match any menu entry (including one with missing fields) is accepted or rejected, and what result is returned in each case.

```python
def test_add_dish_6(self):
    self.order.menu = []
    result = self.order.add_dish({})
    self.assertTrue(result)
```

## Method `calculate_total`

### Docstring

```python
def calculate_total(self):
        """
        Calculate the total price of dishes that have been ordered. Multiply the count, price and sales.
        :return total: float, the final total price.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.calculate_total()
        32.0
        """
```

### Reference code (`solution_code`)

```python
def calculate_total(self):
        total = 0
        for dish in self.selected_dishes:
            total += dish["price"] * dish["count"] * self.sales[dish["dish"]]
        return total
```

### Tests (`OrderTestCalculateTotal`)

setUp (runs before each test):

```python
def setUp(self):
    self.order = Order()
    self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
    self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
    self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}
```

**test_calculate_total_1**: `stated`
- reason: The docstring says to total the ordered dishes by multiplying count, price and sales, which is exactly what the test checks, so a programmer following it would get 50.

```python
def test_calculate_total_1(self):
    self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
    self.order.add_dish({"dish": "dish3", "price": 20, "count": 2})
    result = self.order.calculate_total()
    self.assertEqual(50, result)
```

**test_calculate_total_2**: `stated`
- reason: The docstring says to multiply each dish's count, price and sales factor and total them, which gives 10×2×0.9 + 15×2×1 = 48 as the test expects.

```python
def test_calculate_total_2(self):
    self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
    self.order.add_dish({"dish": "dish2", "price": 15, "count": 2})
    result = self.order.calculate_total()
    self.assertEqual(48, result)
```

**test_calculate_total_3**: `stated`
- reason: The docstring says to multiply count, price and sales and sum over the ordered dishes, which gives 10×1×0.9 + 20×1×0.8 = 25 for this test, matching the expected value.

```python
def test_calculate_total_3(self):
    self.order.add_dish({"dish": "dish1", "price": 10, "count": 1})
    self.order.add_dish({"dish": "dish3", "price": 20, "count": 1})
    result = self.order.calculate_total()
    self.assertEqual(25, result)
```

**test_calculate_total_4**: `stated`
- reason: The docstring says to multiply count, price and sales for each ordered dish and return the total, which a programmer would implement as a sum of price × count × sales over the selected dishes, giving 75 for this test's two dishes.

```python
def test_calculate_total_4(self):
    self.order.add_dish({"dish": "dish1", "price": 10, "count": 3})
    self.order.add_dish({"dish": "dish3", "price": 20, "count": 3})
    result = self.order.calculate_total()
    self.assertEqual(75, result)
```

**test_calculate_total_5**: `stated`
- reason: The docstring says to multiply count, price and sales for each ordered dish and total them, which gives 10×4×0.9 + 20×4×0.8 = 100, matching the test's expected value.

```python
def test_calculate_total_5(self):
    self.order.add_dish({"dish": "dish1", "price": 10, "count": 4})
    self.order.add_dish({"dish": "dish3", "price": 20, "count": 4})
    result = self.order.calculate_total()
    self.assertEqual(100, result)
```

## Method `checkout`

### Docstring

```python
def checkout(self):
        """
        Check out the dished ordered. IF the self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return Flase if the self.selected_dishes is empty, or total(return value of calculate_total) otherwise.
        >>> order = Order()
        >>> order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        >>> order.sales = {"dish1": 0.8}
        >>> order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        True
        >>> order.checkout()
        32.0
        """
```

### Reference code (`solution_code`)

```python
def checkout(self):
        if len(self.selected_dishes) == 0:
            return False
        total = self.calculate_total()
        self.selected_dishes = []
        return total
```

### Tests (`OrderTestCheckout`)

setUp (runs before each test):

```python
def setUp(self):
    self.order = Order()
    self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
    self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
    self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}
```

**test_checkout_1**: `unstated`
- reason: The test expects checkout to return the discounted total (50) and also to reduce the menu stock counts and clear the selected dishes, but the docstring mentions none of the side effects, so a correct implementation that leaves the order in place would fail the final assertions.
- missing: The docstring should state that after a successful checkout, the ordered quantity of each dish is subtracted from its menu count and the selected dishes list is emptied.

```python
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
```

**test_checkout_2**: `stated`
- reason: The docstring says checkout returns False when no dishes are selected, and this test checks that an order with no selected dishes gives a falsy result, so a programmer following it would pass.

```python
def test_checkout_2(self):
    result = self.order.checkout()
    self.assertFalse(result)
```

**test_checkout_3**: `unstated`
- reason: The test expects checkout to return the discounted total of 25 and also to decrement the menu counts and clear the selected dishes, but the docstring only describes the return value and never mentions these side effects.
- missing: The docstring should state that a successful checkout clears the selected dishes and subtracts each ordered quantity from that dish's count in the menu, and that the discount from the sales mapping is applied per dish when computing the total.

```python
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
```

**test_checkout_4**: `unstated`
- reason: The docstring covers only the returned total, but the test also expects checkout to decrement each ordered dish's menu count and empty `selected_dishes`, and a programmer following the docstring would not do either.
- missing: The docstring should state that checkout subtracts each selected dish's quantity from its count in the menu and clears the selected dishes list after a successful checkout.

```python
def test_checkout_4(self):
    self.order.add_dish({"dish": "dish1", "price": 10, "count": 3})
    self.order.add_dish({"dish": "dish3", "price": 20, "count": 3})
    result = self.order.checkout()
    self.assertEqual(75, result)

    menu = self.order.menu
    for menu_dish in menu:
        if menu_dish["dish"] == "dish1":
            self.assertEqual(menu_dish["count"], 2)
        if menu_dish["dish"] == "dish2":
            self.assertEqual(menu_dish["count"], 3)
        if menu_dish["dish"] == "dish3":
            self.assertEqual(menu_dish["count"], 4)
    self.assertEqual([], self.order.selected_dishes)
```

**test_checkout_5**: `unstated`
- reason: The test checks that a successful checkout reduces each dish's remaining menu count and empties the selected dishes, but the docstring only says it returns the total from calculate_total and never mentions these side effects.
- missing: After a successful checkout, the docstring should say that each ordered dish's menu count is reduced by the quantity ordered and that the selected dishes list is cleared afterward.

```python
def test_checkout_5(self):
    self.order.add_dish({"dish": "dish1", "price": 10, "count": 5})
    self.order.add_dish({"dish": "dish3", "price": 20, "count": 5})
    result = self.order.checkout()
    self.assertEqual(125, result)

    menu = self.order.menu
    for menu_dish in menu:
        if menu_dish["dish"] == "dish1":
            self.assertEqual(menu_dish["count"], 0)
        if menu_dish["dish"] == "dish2":
            self.assertEqual(menu_dish["count"], 3)
        if menu_dish["dish"] == "dish3":
            self.assertEqual(menu_dish["count"], 2)
    self.assertEqual([], self.order.selected_dishes)
```

## Tests in no method's test class

### `OrderTest`

setUp (runs before each test):

```python
def setUp(self):
    self.order = Order()

    self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
    self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
    self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
    self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}
```

**test_order**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_order(self):
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
```
