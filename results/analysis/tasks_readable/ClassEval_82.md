# ClassEval_82

## Skeleton (what the agent sees)

```python
class StockPortfolioTracker:
    """
    This is a class as StockPortfolioTracker that allows to add stocks, remove stocks, buy stocks, sell stocks, calculate the total value of the portfolio, and obtain a summary of the portfolio.
    """

    def __init__(self, cash_balance):
        """
        Initialize the StockPortfolioTracker class with a cash balance and an empty portfolio.
        """
        self.portfolio = []
        self.cash_balance = cash_balance

    def add_stock(self, stock):
        """
        Add a stock to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

        """

    def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []

        """

    def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to buy,int.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

        """

    def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to sell,int.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []

        """

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.calculate_portfolio_value()
        11500.0

        """

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

        """

    def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
        1500.0

        """
```

## Method `add_stock`

### Docstring

```python
def add_stock(self, stock):
        """
        Add a stock to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

        """
```

### Reference code (`solution_code`)

```python
def add_stock(self, stock):
        for pf in self.portfolio:
            if pf['name'] == stock['name']:
                pf['quantity'] += stock['quantity']
                return

        self.portfolio.append(stock)
```

### Tests (`StockPortfolioTrackerTestAddStock`)

**test_add_stock**: `stated`
- reason: The docstring's own example adds one stock to an empty tracker and shows `tracker.portfolio` as a list containing that same dictionary, which is exactly what the test checks.

```python
def test_add_stock(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}])
```

**test_add_stock_2**: `unstated`
- reason: The docstring only shows adding a stock to an empty portfolio, so a programmer could reasonably append a duplicate entry, while the test expects the quantity to be merged into the existing AAPL entry.
- missing: When a stock with the same name is already in the portfolio, the method should add the new quantity to the existing entry's quantity instead of appending a second entry.

```python
def test_add_stock_2(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 20}])
```

**test_add_stock_3**: `stated`
- reason: The docstring says to add a stock to the portfolio, so a programmer would append a new, different-name stock as this test expects.

```python
def test_add_stock_3(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    tracker.add_stock({"name": "MSFT", "price": 150.0, "quantity": 10})
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
```

**test_add_stock_4**: `unstated`
- reason: The docstring only says the stock is added to the portfolio, so a programmer would likely append a new entry, but the test expects a stock whose name is already held to have its quantity increased instead.
- missing: When a stock with the same name is already in the portfolio, the method must add the new quantity to that existing entry rather than appending a duplicate entry.

```python
def test_add_stock_4(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    tracker.add_stock({"name": "MSFT", "price": 150.0, "quantity": 10})
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 20},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
```

**test_add_stock_5**: `unstated`
- reason: The docstring only says the method adds a stock to the portfolio, so a programmer would likely append a duplicate entry, while the test expects an existing holding of the same name to have its quantity increased.
- missing: When a stock with the same name is already in the portfolio, the method should add the new quantity to the existing entry instead of appending a second entry for that name.

```python
def test_add_stock_5(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    tracker.add_stock({"name": "MSFT", "price": 150.0, "quantity": 10})
    tracker.add_stock({"name": "MSFT", "price": 150.0, "quantity": 10})
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 20},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 20}])
```

## Method `remove_stock`

### Docstring

```python
def remove_stock(self, stock):
        """
        Remove a stock from the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []

        """
```

### Reference code (`solution_code`)

```python
def remove_stock(self, stock):
        for pf in self.portfolio:
            if pf['name'] == stock['name'] and pf['quantity'] >= stock['quantity']:
                pf['quantity'] -= stock['quantity']
                if pf['quantity'] == 0:
                    self.portfolio.remove(pf)
                return True
        return False
```

### Tests (`StockPortfolioTrackerTestRemoveStock`)

**test_remove_stock**: `stated`
- reason: The docstring's doctest shows that removing a holding with the full matching quantity returns True and leaves the portfolio empty, which is exactly what the test checks.

```python
def test_remove_stock(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [])
```

**test_remove_stock_2**: `stated`
- reason: The docstring says to remove the stock from the portfolio and its example shows `True` being returned with the matching entry removed, which is what the test checks for AAPL while leaving MSFT in place.

```python
def test_remove_stock_2(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
```

**test_remove_stock_3**: `unstated`
- reason: The docstring never says what happens when the requested quantity exceeds the quantity held, so a programmer could reasonably remove the whole holding and return True, which fails this test expecting False with the portfolio unchanged.
- missing: The docstring should state the return value and the effect when the requested quantity is larger than the quantity held for that stock, or when no matching stock exists (e.g., return False and leave the portfolio unchanged), and whether a smaller quantity reduces the holding instead of removing it.

```python
def test_remove_stock_3(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.remove_stock({"name": "MSFT", "price": 150.0, "quantity": 20}), False)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
```

**test_remove_stock_4**: `unstated`
- reason: The docstring only shows the successful `True` return and never says what happens when the stock is absent from the portfolio, so the test's expected `False` and unchanged portfolio are not specified.
- missing: The docstring should state the return value and the effect on the portfolio when the requested stock is not held, including the case where the held quantity is insufficient to remove.

```python
def test_remove_stock_4(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.remove_stock({"name": "MSFT", "price": 150.0, "quantity": 10}), False)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}])
```

**test_remove_stock_5**: `stated`
- reason: The docstring says the method removes a stock from the portfolio, and its doctest shows it returns True and leaves the portfolio empty, so a programmer would remove the matching entry, return True, and keep the other holdings, as this test checks.

```python
def test_remove_stock_5(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.remove_stock({"name": "MSFT", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}])
```

## Method `buy_stock`

### Docstring

```python
def buy_stock(self, stock):
        """
        Buy a stock and add it to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to buy,int.
        :return: True if the stock was bought successfully, False if the cash balance is not enough.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

        """
```

### Reference code (`solution_code`)

```python
def buy_stock(self, stock):
        if stock['price'] * stock['quantity'] > self.cash_balance:
            return False
        else:
            self.add_stock(stock)
            self.cash_balance -= stock['price'] * stock['quantity']
            return True
```

### Tests (`StockPortfolioTrackerTestBuyStock`)

**test_buy_stock**: `unstated`
- reason: The docstring says a successful buy adds the stock to the portfolio but never says the cash balance is reduced, which the test checks after a purchase.
- missing: The docstring should state that a successful purchase deducts the total cost (price multiplied by quantity) from the cash balance, and that a failed purchase leaves the balance unchanged.

```python
def test_buy_stock(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.cash_balance, 8500.0)
```

**test_buy_stock_2**: `stated`
- reason: The docstring says buy_stock returns False when the cash balance is not enough, which is exactly the case this test checks (cost 1500 against 1000 cash), so a programmer following it would return False and leave the portfolio and cash unchanged.

```python
def test_buy_stock_2(self):
    tracker = StockPortfolioTracker(1000.0)
    self.assertEqual(tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), False)
    self.assertEqual(tracker.portfolio, [])
    self.assertEqual(tracker.cash_balance, 1000.0)
```

**test_buy_stock_3**: `unstated`
- reason: The docstring says only that the stock is added to the portfolio, so a programmer would reasonably append a new entry, while the test expects the existing holding's quantity to be increased to 20 and the cash balance to drop by the purchase cost.
- missing: The docstring should say what happens when the portfolio already holds a stock with the same name: whether the new quantity is merged into that existing entry (and how its price is kept) or a separate entry is appended, and that the cash balance is reduced by price times quantity on a successful purchase.

```python
def test_buy_stock_3(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 20}])
    self.assertEqual(tracker.cash_balance, 8500.0)
```

**test_buy_stock_4**: `unstated`
- reason: The test expects a second purchase of a stock already in the portfolio to merge into the existing entry with the combined quantity, but the docstring only says the stock is "added to the portfolio," so a correct implementation that appends a separate entry would fail.
- missing: The docstring should state that if a stock with the same name is already held, buying more increases that holding's quantity and does not create a second entry.

```python
def test_buy_stock_4(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.buy_stock({"name": "MSFT", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.buy_stock({"name": "MSFT", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 20}])
    self.assertEqual(tracker.cash_balance, 7000.0)
```

**test_buy_stock_5**: `unstated`
- reason: The docstring says only that the stock is added to the portfolio, so a programmer would likely append a second AAPL entry, whereas the test expects the purchase to merge into the existing AAPL entry with quantity 20.
- missing: The docstring should say that buying a stock whose name is already in the portfolio adds its quantity to the existing entry rather than creating a new one, and that cash is reduced by price times quantity.

```python
def test_buy_stock_5(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.buy_stock({"name": "MSFT", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 20},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.cash_balance, 7000.0)
```

## Method `sell_stock`

### Docstring

```python
def sell_stock(self, stock):
        """
        Sell a stock and remove it from the portfolio and add the cash to the cash balance.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :param quantity: the quantity of the stock to sell,int.
        :return: True if the stock was sold successfully, False if the quantity of the stock is not enough.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []

        """
```

### Reference code (`solution_code`)

```python
def sell_stock(self, stock):
        if self.remove_stock(stock) == False:
            return False
        self.cash_balance += stock['price'] * stock['quantity']
        return True
```

### Tests (`StockPortfolioTrackerTestSellStock`)

**test_sell_stock**: `contradicts`
- reason: The docstring says the stock is removed from the portfolio, which implies the whole holding goes, but the test sells 9 of 10 shares and expects 1 share to remain with the cash credited for 9 shares.
- missing: The docstring should state that selling a quantity less than the holding reduces that holding's quantity by the amount sold, and removes the entry only when the full quantity is sold.

```python
def test_sell_stock(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 9}), True)
    self.assertEqual(tracker.portfolio, [{"name": "AAPL", "price": 150.0, "quantity": 1}])
    self.assertEqual(tracker.cash_balance, 11350.0)
```

**test_sell_stock_2**: `stated`
- reason: The docstring says sell_stock returns False when the held quantity is not enough, and a programmer would naturally leave both the portfolio and cash untouched in that case, which is what the test checks.

```python
def test_sell_stock_2(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 20}), False)
    self.assertEqual(tracker.portfolio, [{"name": "AAPL", "price": 150.0, "quantity": 10}])
    self.assertEqual(tracker.cash_balance, 10000.0)
```

**test_sell_stock_3**: `stated`
- reason: The docstring says sell_stock returns False when the quantity of the stock is not enough, and selling a stock that is not held in the portfolio is a case of insufficient quantity, so a programmer following it would return False and leave the portfolio and cash unchanged.

```python
def test_sell_stock_3(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), False)
    self.assertEqual(tracker.portfolio, [])
    self.assertEqual(tracker.cash_balance, 10000.0)
```

**test_sell_stock_4**: `stated`
- reason: The docstring says selling removes the stock from the portfolio, adds the cash to the balance, and returns True on success, which covers everything this test checks (True return, empty portfolio, balance rising by 150 × 20).

```python
def test_sell_stock_4(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 20}]
    self.assertEqual(tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 20}), True)
    self.assertEqual(tracker.portfolio, [])
    self.assertEqual(tracker.cash_balance, 13000.0)
```

**test_sell_stock_5**: `stated`
- reason: The docstring says selling removes the stock from the portfolio and adds its cash value to the balance, which is what this test checks: the AAPL entry is removed, the MSFT holding remains, and cash rises by price times quantity.

```python
def test_sell_stock_5(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 20},
                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 20}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.cash_balance, 13000.0)
```

## Method `calculate_portfolio_value`

### Docstring

```python
def calculate_portfolio_value(self):
        """
        Calculate the total value of the portfolio.
        :return: the total value of the portfolio, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.calculate_portfolio_value()
        11500.0

        """
```

### Reference code (`solution_code`)

```python
def calculate_portfolio_value(self):
        total_value = self.cash_balance
        for stock in self.portfolio:
            total_value += stock['price'] * stock['quantity']
        return total_value
```

### Tests (`StockPortfolioTrackerTestCalculatePortfolioValue`)

**test_calculate_portfolio_value**: `stated`
- reason: The docstring's doctest uses the same setup (10000.0 starting cash, one AAPL holding of 10 at 150.0) and the same expected value 11500.0, so a programmer following it would pass this test.

```python
def test_calculate_portfolio_value(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.calculate_portfolio_value(), 11500.0)
```

**test_calculate_portfolio_value_2**: `stated`
- reason: The docstring says the method returns the total value of the portfolio, and its example (cash of 10000 plus one holding of 1500 giving 11500) shows that value is cash plus the sum of price times quantity, so a programmer would compute 13000 for two 1500 holdings.

```python
def test_calculate_portfolio_value_2(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.calculate_portfolio_value(), 13000.0)
```

**test_calculate_portfolio_value_3**: `stated`
- reason: The docstring example (cash of 10000.0 plus one holding worth 1500.0 gives 11500.0) shows that the total includes the cash balance, so with no holdings a programmer would return the cash balance, which is what the test expects.

```python
def test_calculate_portfolio_value_3(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.calculate_portfolio_value(), 10000.0)
```

**test_calculate_portfolio_value_4**: `stated`
- reason: The docstring example (10000 cash plus 10 shares at 150 giving 11500) shows that the total is cash plus the sum of price times quantity, so a zero-quantity holding adds nothing and the result is just the cash balance.

```python
def test_calculate_portfolio_value_4(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 0}]
    self.assertEqual(tracker.calculate_portfolio_value(), 10000.0)
```

**test_calculate_portfolio_value_5**: `stated`
- reason: The docstring's example shows the total is the starting cash plus the sum of price times quantity, so a zero-price holding adds nothing and the test's expected 10000.0 follows directly from that rule.

```python
def test_calculate_portfolio_value_5(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 0.0, 'quantity': 10}]
    self.assertEqual(tracker.calculate_portfolio_value(), 10000.0)
```

## Method `get_portfolio_summary`

### Docstring

```python
def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

        """
```

### Reference code (`solution_code`)

```python
def get_portfolio_summary(self):
        summary = []
        for stock in self.portfolio:
            value = self.get_stock_value(stock)
            summary.append({"name": stock["name"], "value": value})
        portfolio_value = self.calculate_portfolio_value()
        return portfolio_value, summary
```

### Tests (`StockPortfolioTrackerTestGetPortfolioSummary`)

**test_get_portfolio_summary**: `stated`
- reason: The docstring's own example uses the same setup (a 10000.0 starting balance, one AAPL holding at 150.0 × 10) and shows the same return value, (11500.0, [{'name': 'AAPL', 'value': 1500.0}]), so a programmer following it would pass.

```python
def test_get_portfolio_summary(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.get_portfolio_summary(), (11500.0, [{'name': 'AAPL', 'value': 1500.0}]))
```

**test_get_portfolio_summary_2**: `stated`
- reason: The docstring example (cash of 10000 plus one 1500 holding giving a total of 11500) shows that the total includes the starting cash, so a programmer applying that rule to two 1500 holdings would get 13000 and the per-stock list as the test expects.

```python
def test_get_portfolio_summary_2(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.get_portfolio_summary(),
                     (13000.0, [{'name': 'AAPL', 'value': 1500.0}, {'name': 'MSFT', 'value': 1500.0}]))
```

**test_get_portfolio_summary_3**: `stated`
- reason: The docstring example shows the total as 11500, which is the 10000 starting cash plus the 1500 stock value, so a programmer would return the cash balance alone with an empty list for an empty portfolio, which is what the test expects.

```python
def test_get_portfolio_summary_3(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.get_portfolio_summary(), (10000.0, []))
```

**test_get_portfolio_summary_4**: `stated`
- reason: A programmer following the docstring would compute each holding's value as price times quantity, giving 0.0 for zero shares, and the example's total (10000 cash plus 1500 holdings) implies the total is cash plus holdings, so this test's expectations follow.

```python
def test_get_portfolio_summary_4(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 0}]
    self.assertEqual(tracker.get_portfolio_summary(), (10000.0, [{'name': 'AAPL', 'value': 0.0}]))
```

**test_get_portfolio_summary_5**: `stated`
- reason: The docstring example shows the total as cash plus holdings value (10000 + 1500 = 11500), so a zero-priced holding should yield a value of 0.0 and a total equal to the starting cash, which is what the test expects.

```python
def test_get_portfolio_summary_5(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 0.0, 'quantity': 10}]
    self.assertEqual(tracker.get_portfolio_summary(), (10000.0, [{'name': 'AAPL', 'value': 0.0}]))
```

## Method `get_stock_value`

### Docstring

```python
def get_stock_value(self, stock):
        """
        Get the value of a stock.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        :return: the value of the stock, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
        1500.0

        """
```

### Reference code (`solution_code`)

```python
def get_stock_value(self, stock):
        return stock['price'] * stock['quantity']
```

### Tests (`StockPortfolioTrackerTestGetStockValue`)

**test_get_stock_value**: `stated`
- reason: The docstring says the value is price times quantity returned as a float, and the example with price 150.0 and quantity 10 giving 1500.0 matches the test exactly, so a programmer following it would pass.

```python
def test_get_stock_value(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10}), 1500.0)
```

**test_get_stock_value_2**: `stated`
- reason: The docstring defines the stock's value as price times quantity (shown by the 150.0 × 10 = 1500.0 example), so a programmer would compute 150.0 × 0 = 0.0 and pass.

```python
def test_get_stock_value_2(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 0}), 0.0)
```

**test_get_stock_value_3**: `stated`
- reason: A programmer following the docstring would multiply price by quantity, which the example confirms, so a zero price gives 0.0 and the test passes.

```python
def test_get_stock_value_3(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.get_stock_value({"name": "AAPL", "price": 0.0, "quantity": 10}), 0.0)
```

**test_get_stock_value_4**: `stated`
- reason: The docstring says the stock value is computed from its price and quantity, so a programmer would multiply them and get 0.0 for zero price and zero quantity, matching the test.

```python
def test_get_stock_value_4(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.get_stock_value({"name": "AAPL", "price": 0.0, "quantity": 0}), 0.0)
```

**test_get_stock_value_5**: `stated`
- reason: The docstring says the value is price times quantity (the example shows 150.0 × 10 = 1500.0), so the test's 150.0 × 2 = 300.0 is what a programmer following it would compute.

```python
def test_get_stock_value_5(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.get_stock_value({"name": "MSFL", "price": 150.0, "quantity": 2}), 300.0)
```

## Tests in no method's test class

### `StockPortfolioTrackerTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    tracker = StockPortfolioTracker(10000.0)
    self.assertEqual(tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), None)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.buy_stock({"name": "MSFT", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.cash_balance, 8500.0)
    self.assertEqual(tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 9}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 1},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.cash_balance, 9850.0)
    self.assertEqual(tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 1}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.calculate_portfolio_value(), 11350.0)
    self.assertEqual(tracker.get_portfolio_summary(), (11350.0, [{'name': 'MSFT', 'value': 1500.0}]))
    self.assertEqual(tracker.get_stock_value({"name": "MSFT", "price": 150.0, "quantity": 10}), 1500.0)
```

**test_main_2**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main_2(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.add_stock({"name": "MSFT", "price": 150.0, "quantity": 10}), None)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.calculate_portfolio_value(), 11500.0)
    self.assertEqual(tracker.get_portfolio_summary(), (11500.0, [{'name': 'MSFT', 'value': 1500.0}]))
    self.assertEqual(tracker.get_stock_value({"name": "MSFT", "price": 150.0, "quantity": 10}), 1500.0)
    self.assertEqual(tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'MSFT', 'price': 150.0, 'quantity': 10},
                                         {'name': 'AAPL', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.cash_balance, 8500.0)
```

**test_main_3**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main_3(self):
    tracker = StockPortfolioTracker(10000.0)
    tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}]
    self.assertEqual(tracker.get_stock_value({"name": "MSFT", "price": 150.0, "quantity": 10}), 1500.0)
    self.assertEqual(tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 20},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.cash_balance, 8500.0)
    self.assertEqual(tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'AAPL', 'price': 150.0, 'quantity': 10},
                                         {'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.cash_balance, 10000.0)
    self.assertEqual(tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), True)
    self.assertEqual(tracker.portfolio, [{'name': 'MSFT', 'price': 150.0, 'quantity': 10}])
    self.assertEqual(tracker.calculate_portfolio_value(), 11500.0)
    self.assertEqual(tracker.get_portfolio_summary(), (11500.0, [{'name': 'MSFT', 'value': 1500.0}]))
    self.assertEqual(tracker.get_stock_value({"name": "MSFT", "price": 150.0, "quantity": 10}), 1500.0)
    self.assertEqual(tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10}), None)
    self.assertEqual(tracker.portfolio, [{'name': 'MSFT', 'price': 150.0, 'quantity': 10},
                                         {'name': 'AAPL', 'price': 150.0, 'quantity': 10}])
```
