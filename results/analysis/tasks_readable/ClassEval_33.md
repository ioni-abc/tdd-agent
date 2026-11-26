# ClassEval_33

## Skeleton (what the agent sees)

```python
class DiscountStrategy:
    """
    This is a class that allows to use different discount strategy based on shopping credit or shopping cart in supermarket.
    """

    def __init__(self, customer, cart, promotion=None):
        """
        Initialize the DiscountStrategy with customer information, a cart of items, and an optional promotion.
        :param customer: dict, customer information
        :param cart: list of dicts, a cart of items with details
        :param promotion: function, optional promotion applied to the order
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)

        """
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.total()

    def total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart)
        >>> ds.total()
        329.0

        """


    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> ds.due()
        312.55

        """


    @staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45

        """


    @staticmethod
    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        >>> DiscountStrategy.BulkItemPromo(order)
        47.0

        """


    @staticmethod
    def LargeOrderPromo(order):
        """
        Calculate the discount based on the number of different products in the order.If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        >>> DiscountStrategy.LargeOrderPromo(order)
        0.0

        """
```

## Method `total`

### Docstring

```python
def total(self):
        """
        Calculate the total cost of items in the cart.
        :return: float, total cost of items
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart)
        >>> ds.total()
        329.0

        """
```

### Reference code (`solution_code`)

```python
def total(self):
        self.__total = sum(item['quantity'] * item['price'] for item in self.cart)
        return self.__total
```

### Tests (`DiscountStrategyTestTotal`)

**test_total_1**: `stated`
- reason: The docstring says total returns the sum of item costs in the cart, and the example shows quantity times price, so a programmer would compute 10×20.0 + 5×10.0 = 250.0 and pass.

```python
def test_total_1(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart)
    expected_total = 250.0
    actual_total = order.total()
    self.assertEqual(actual_total, expected_total)
```

**test_total_2**: `stated`
- reason: The docstring defines total as the cost of the cart's items, and the example shows quantity times price, so a programmer summing quantity × price across items would get the test's 150.0.

```python
def test_total_2(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 10.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart)
    expected_total = 150.0
    actual_total = order.total()
    self.assertEqual(actual_total, expected_total)
```

**test_total_3**: `stated`
- reason: The docstring says total returns the total cost of cart items, and a programmer would sum quantity times price across all items, which gives the 2050.0 this test expects.

```python
def test_total_3(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 200.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart)
    expected_total = 2050.0
    actual_total = order.total()
    self.assertEqual(actual_total, expected_total)
```

**test_total_4**: `stated`
- reason: The docstring says total returns the total cost of items in the cart, which a programmer would compute as the sum of quantity times price across all items, giving 70.0 for this two-item cart.

```python
def test_total_4(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 1, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart)
    expected_total = 70.0
    actual_total = order.total()
    self.assertEqual(actual_total, expected_total)
```

**test_total_5**: `stated`
- reason: The docstring defines the total as the sum of item costs over the cart, so an empty cart naturally gives 0, which is what the test expects, and assertEqual accepts 0 as equal to 0.0.

```python
def test_total_5(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = []
    order = DiscountStrategy(customer, cart)
    expected_total = 0
    actual_total = order.total()
    self.assertEqual(actual_total, expected_total)
```

## Method `due`

### Docstring

```python
def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> ds.due()
        312.55

        """
```

### Reference code (`solution_code`)

```python
def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.__total - discount
```

### Tests (`DiscountStrategyTestDue`)

**test_due_1**: `unstated`
- reason: The docstring only describes applying a discount and never says what `due` returns when no promotion is supplied, so a programmer could plausibly fail to return the undiscounted cart total that this test expects.
- missing: The docstring should state that when no discount strategy/promotion is set, `due` returns the full undiscounted total of all items (quantity times price summed over the cart).

```python
def test_due_1(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart)
    expected_due = 250.0
    actual_due = order.due()
    self.assertEqual(actual_due, expected_due)
```

**test_due_2**: `unstated`
- reason: The docstring's single example only hints at the fidelity promotion (a 5% discount for this customer), so a programmer would not reliably know the eligibility rule and percentage that the test's expected 237.5 depends on.
- missing: The docstring should state the discount rule that applies to each promotion, including the eligibility condition (such as a fidelity threshold) and the percentage or amount deducted from the total.

```python
def test_due_2(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    expected_due = 237.5
    actual_due = order.due()
    self.assertEqual(actual_due, expected_due)
```

**test_due_3**: `unstated`
- reason: The docstring only shows the fidelity promotion, so a programmer cannot infer how the bulk-item promotion used by this test computes its discount, and the expected 410.0 depends on that unstated rule.
- missing: The docstring should describe each promotion's discount rule, including which items qualify (for example, by quantity threshold), whether the discount is a percentage of that item's line subtotal or of the whole cart, and how multiple promotions or rounding are handled.

```python
def test_due_3(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 20, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
    expected_due = 410.0
    actual_due = order.due()
    self.assertEqual(actual_due, expected_due)
```

**test_due_4**: `unstated`
- reason: The docstring only illustrates the fidelity promotion, so a programmer following it cannot know the large-order promotion's threshold or discount rate that this test relies on.
- missing: The docstring should state each promotion's eligibility condition (for example, the item count or distinct-product count that triggers it) and the exact discount it applies (percentage or fixed amount, and whether it is computed on the total), so every promotion's behaviour can be implemented from the docstring alone.

```python
def test_due_4(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(15)]
    order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    expected_due = 139.5
    actual_due = order.due()
    self.assertEqual(actual_due, expected_due)
```

**test_due_5**: `unstated`
- reason: The docstring gives only one fidelity example (1200 points, 5% off), so a programmer cannot tell that a customer with 900 points gets no discount and the test's expected 250.0 is correct.
- missing: The docstring should state the eligibility rule for the loyalty promotion: the fidelity threshold at which the discount applies, and that customers below it receive no discount.

```python
def test_due_5(self):
    customer = {'name': 'John Doe', 'fidelity': 900}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    expected_due = 250.0
    actual_due = order.due()
    self.assertEqual(actual_due, expected_due)
```

## Method `FidelityPromo`

### Docstring

```python
@staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def FidelityPromo(order):
        return order.total() * 0.05 if order.customer['fidelity'] >= 1000 else 0
```

### Tests (`DiscountStrategyTestFidelityPromo`)

**test_fidelity_promo_1**: `contradicts`
- reason: The docstring says customers "with over 1000 points" get the discount, which excludes exactly 1000, but the test uses 1000 points and expects a 5% discount of 12.5, matching the reference's `>= 1000` check.
- missing: The docstring should state that the discount applies when the customer's points are at least the threshold (inclusive), and that the discount equals 5% of the order's total.

```python
def test_fidelity_promo_1(self):
    customer = {'name': 'John Doe', 'fidelity': 1000}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    expected_discount = 12.5
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_fidelity_promo_2**: `stated`
- reason: The docstring says only customers with more than 1000 points get a 5% discount, so a programmer would return 0 for a customer with 800 points, which is what the test expects.

```python
def test_fidelity_promo_2(self):
    customer = {'name': 'John Doe', 'fidelity': 800}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    expected_discount = 0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_fidelity_promo_3**: `stated`
- reason: The docstring says only customers with over 1000 points get a 5% discount, so a programmer would return 0 for a customer with 0 points, which is what the test expects.

```python
def test_fidelity_promo_3(self):
    customer = {'name': 'John Doe', 'fidelity': 0}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    expected_discount = 0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_fidelity_promo_4**: `stated`
- reason: The docstring says customers with over 1000 points get 5% off the entire order, and the test (10000 points, order total 250, expected 12.5) follows that rule directly.

```python
def test_fidelity_promo_4(self):
    customer = {'name': 'John Doe', 'fidelity': 10000}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    expected_discount = 12.5
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_fidelity_promo_5**: `stated`
- reason: The docstring says customers with over 1000 points get 5% off the entire order, and the test (1800 points, cart total 250, expected 12.5) matches that rule.

```python
def test_fidelity_promo_5(self):
    customer = {'name': 'John Doe', 'fidelity': 1800}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    expected_discount = 12.5
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

## Method `BulkItemPromo`

### Docstring

```python
@staticmethod
    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        >>> DiscountStrategy.BulkItemPromo(order)
        47.0

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def BulkItemPromo(order):
        discount = 0
        for item in order.cart:
            if item['quantity'] >= 20:
                discount += item['quantity'] * item['price'] * 0.1
        return discount
```

### Tests (`DiscountStrategyTestBulkItemPromo`)

**test_bulk_item_promo_1**: `stated`
- reason: The docstring says items with a quantity of 20 or more get a 10% discount, so a programmer would compute 10% of quantity times price for those items and skip the rest, which yields the expected 20.0.

```python
def test_bulk_item_promo_1(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 20, 'price': 10.0},
            {'product': 'product2', 'quantity': 5, 'price': 5.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
    expected_discount = 20.0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_bulk_item_promo_2**: `stated`
- reason: The docstring says the 10% discount applies only when an item's quantity reaches 20 or more, so a programmer following it would return 0 when both items are below that threshold, matching the test's expected 0.

```python
def test_bulk_item_promo_2(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 10.0},
            {'product': 'product2', 'quantity': 5, 'price': 5.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
    expected_discount = 0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_bulk_item_promo_3**: `stated`
- reason: The docstring says each item with quantity of at least 20 gets a 10% discount and items below that get none, so a programmer would compute 10% of 100 × 10.0 = 100.0 for the qualifying item and ignore the 5-unit item, matching the expected value.

```python
def test_bulk_item_promo_3(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 100, 'price': 10.0},
            {'product': 'product2', 'quantity': 5, 'price': 5.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
    expected_discount = 100.0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_bulk_item_promo_4**: `stated`
- reason: The docstring says a 10% discount applies only when an item's quantity reaches 20 or more, so a cart with all quantities below 20 should yield a discount of 0, which is what the test expects.

```python
def test_bulk_item_promo_4(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 1, 'price': 10.0},
            {'product': 'product2', 'quantity': 5, 'price': 5.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
    expected_discount = 0.0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_bulk_item_promo_5**: `stated`
- reason: The docstring says items with quantity 20 or more get a 10% discount, so a programmer would discount only the qualifying item (30 × 10.0 × 0.1 = 30.0) and exclude the item with quantity 5, which is what the test expects.

```python
def test_bulk_item_promo_5(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 30, 'price': 10.0},
            {'product': 'product2', 'quantity': 5, 'price': 5.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
    expected_discount = 30.0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

## Method `LargeOrderPromo`

### Docstring

```python
@staticmethod
    def LargeOrderPromo(order):
        """
        Calculate the discount based on the number of different products in the order.If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        >>> DiscountStrategy.LargeOrderPromo(order)
        0.0

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def LargeOrderPromo(order):
        return order.total() * 0.07 if len({item['product'] for item in order.cart}) >= 10 else 0
```

### Tests (`DiscountStrategyTestLargeOrderPromo`)

**test_large_order_promo_1**: `stated`
- reason: The docstring says that 10 or more distinct products earns a 7% discount on the entire order, so a programmer would return 7% of the order total, which gives 7.0 for ten products at 10.0 each.

```python
def test_large_order_promo_1(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(10)]
    order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    expected_discount = 7.0
    actual_discount = order.promotion(order)
    self.assertAlmostEqual(actual_discount, expected_discount)
```

**test_large_order_promo_2**: `stated`
- reason: The docstring says the 7% discount applies only when the order has 10 or more different products, so a programmer would return 0 for an order with only 5 distinct products, which is what the test expects.

```python
def test_large_order_promo_2(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(5)]
    order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    expected_discount = 0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)
```

**test_large_order_promo_3**: `stated`
- reason: The docstring says a 7% discount applies to the whole order once there are 10 or more different products, which is exactly what this test checks: 100 distinct products totalling 1000 should give 70.0.

```python
def test_large_order_promo_3(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(100)]
    order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    expected_discount = 70.0
    actual_discount = order.promotion(order)
    self.assertAlmostEqual(actual_discount, expected_discount)
```

**test_large_order_promo_4**: `stated`
- reason: The docstring states that an order with 10 or more distinct products gets a 7% discount on the whole order, and the test's 1000 distinct products with a total of 10000 should yield 700, which a programmer following the docstring would produce.

```python
def test_large_order_promo_4(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(1000)]
    order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    expected_discount = 700.0
    actual_discount = order.promotion(order)
    self.assertAlmostEqual(actual_discount, expected_discount)
```

**test_large_order_promo_5**: `stated`
- reason: The docstring says the 7% discount applies only when the order has 10 or more different products, so a programmer would return 0 for a single-product order, which matches the test's expected 0.0.

```python
def test_large_order_promo_5(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(1)]
    order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    expected_discount = 0.0
    actual_discount = order.promotion(order)
    self.assertAlmostEqual(actual_discount, expected_discount)
```

## Tests in no method's test class

### `DiscountStrategyTest`

**test_DiscountStrategy**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_DiscountStrategy(self):
    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart)
    expected_total = 250.0
    actual_total = order.total()
    self.assertEqual(actual_total, expected_total)

    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart)
    expected_due = 250.0
    actual_due = order.due()
    self.assertEqual(actual_due, expected_due)

    customer = {'name': 'John Doe', 'fidelity': 1000}
    cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
            {'product': 'product2', 'quantity': 5, 'price': 10.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    expected_discount = 12.5
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)

    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': 'product1', 'quantity': 20, 'price': 10.0},
            {'product': 'product2', 'quantity': 5, 'price': 5.0}]
    order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
    expected_discount = 20.0
    actual_discount = order.promotion(order)
    self.assertEqual(actual_discount, expected_discount)

    customer = {'name': 'John Doe', 'fidelity': 1200}
    cart = [{'product': f'product{i}', 'quantity': 1, 'price': 10.0} for i in range(10)]
    order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    expected_discount = 7.0
    actual_discount = order.promotion(order)
    self.assertAlmostEqual(actual_discount, expected_discount)
```
