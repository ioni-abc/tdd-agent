# ClassEval_27

## Skeleton (what the agent sees)

```python
class CurrencyConverter:
    """
    This is a class for currency conversion, which supports to convert amounts between different currencies, retrieve supported currencies, add new currency rates, and update existing currency rates.
    """

    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies
        """
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.15,
            'CAD': 1.23,
            'AUD': 1.34,
            'CNY': 6.40,
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        >>> cc = CurrencyConverter()
        >>> cc.convert(64, 'CNY','USD')
        10.0
        """


    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """


    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :param currency:string, currency type to be added
        :param rate:float, exchange rate for this type of currency
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.add_currency_rate('KRW', 1308.84)
        self.rates['KRW'] = 1308.84
        """


    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency:string
        :param new_rate:float
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.update_currency_rate('CNY', 7.18)
        self.rates['CNY'] = 7.18
        """
```

## Method `convert`

### Docstring

```python
def convert(self, amount, from_currency, to_currency):
        """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        >>> cc = CurrencyConverter()
        >>> cc.convert(64, 'CNY','USD')
        10.0
        """
```

### Reference code (`solution_code`)

```python
def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount

        if from_currency not in self.rates or to_currency not in self.rates:
            return False

        from_rate = self.rates[from_currency]
        to_rate = self.rates[to_currency]

        converted_amount = (amount / from_rate) * to_rate
        return converted_amount
```

### Tests (`CurrencyConverterTestConvert`)

**test_convert_1**: `stated`
- reason: The docstring's doctest gives the exact call `convert(64, 'CNY', 'USD')` returning `10.0`, which is the same case and expected value the test checks.

```python
def test_convert_1(self):
    cc = CurrencyConverter()
    res = cc.convert(64, 'CNY', 'USD')
    self.assertEqual(res, 10.0)
```

**test_convert_2**: `unstated`
- reason: The docstring only covers converting between currencies, so a programmer could reasonably check that both currencies are known before comparing them, and would then fail this same-currency case, which the test expects to return the amount unchanged.
- missing: The docstring should state what happens when the source and target currencies are identical, namely that the amount is returned unchanged, and whether this check happens before or regardless of validating the currency codes.

```python
def test_convert_2(self):
    cc = CurrencyConverter()
    res = cc.convert(64, 'USD', 'USD')
    self.assertEqual(res, 64)
```

**test_convert_3**: `unstated`
- reason: The test expects 64 CNY to convert to 7.2 GBP, which depends on the GBP and CNY rates stored in the class, and the docstring only gives a single CNY-to-USD example, so a programmer cannot derive the GBP result.
- missing: The docstring should state the exchange rates used (or the rate table and its base currency) so that the converted value for any currency pair can be computed, not just the one example given.

```python
def test_convert_3(self):
    cc = CurrencyConverter()
    res = cc.convert(64, 'CNY', 'GBP')
    self.assertAlmostEqual(res, 7.1999999999999)
```

**test_convert_4**: `unstated`
- reason: The test expects 64 USD to convert to 46.08 GBP, which depends on the class's hidden USD and GBP rates, and the docstring gives no rates beyond the single CNY-to-USD example.
- missing: The docstring should list the exchange rate for each supported currency (or state the base currency and each currency's rate relative to it) so that any conversion between two supported currencies can be computed.

```python
def test_convert_4(self):
    cc = CurrencyConverter()
    res = cc.convert(64, 'USD', 'GBP')
    self.assertAlmostEqual(res, 46.08)
```

**test_convert_5**: `unstated`
- reason: The test expects 64 USD to convert to 78.72 CAD, which depends on the exchange rates hard-coded in the class, and the docstring gives no rates or supported currencies beyond the CNY-to-USD example.
- missing: The docstring should list the supported currencies and the exchange rate used between each pair (or the base currency and each currency's rate against it), and state what happens for unsupported currencies.

```python
def test_convert_5(self):
    cc = CurrencyConverter()
    res = cc.convert(64, 'USD', 'CAD')
    self.assertAlmostEqual(res, 78.72)
```

**test_convert_6**: `unstated`
- reason: The docstring only describes a successful conversion and says nothing about an unrecognised currency code, yet the test expects the call to return a falsy value rather than raising an error or returning a number.
- missing: The docstring should state what the method returns or raises when either currency code is not a supported currency, including the exact falsy value (such as False) it should return.

```python
def test_convert_6(self):
    cc = CurrencyConverter()
    res = cc.convert(64, '???', 'USD')
    self.assertFalse(res)
```

## Method `get_supported_currencies`

### Docstring

```python
def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """
```

### Reference code (`solution_code`)

```python
def get_supported_currencies(self):
        return list(self.rates.keys())
```

### Tests (`CurrencyConverterTestGetSupportedCurrencies`)

**test_get_supported_currencies_1**: `stated`
- reason: The docstring's example shows the exact list and order `['USD','EUR','GBP','JPY','CAD','AUD','CNY']` for a default `CurrencyConverter`, which is what the test asserts.

```python
def test_get_supported_currencies_1(self):
    cc = CurrencyConverter()
    res = cc.get_supported_currencies()
    self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])
```

**test_get_supported_currencies_2**: `stated`
- reason: The docstring's example shows that a fresh `CurrencyConverter` returns exactly `['USD','EUR','GBP','JPY','CAD','AUD','CNY']`, which is the same list and order the test asserts.

```python
def test_get_supported_currencies_2(self):
    cc = CurrencyConverter()
    res = cc.get_supported_currencies()
    self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])
```

**test_get_supported_currencies_3**: `stated`
- reason: The docstring's doctest shows that a fresh `CurrencyConverter()` returns exactly `['USD','EUR','GBP','JPY','CAD','AUD','CNY']` in that order, which is what the test asserts.

```python
def test_get_supported_currencies_3(self):
    cc = CurrencyConverter()
    res = cc.get_supported_currencies()
    self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])
```

**test_get_supported_currencies_4**: `stated`
- reason: The docstring's example output is exactly the list the test asserts, including the order, so a programmer following it would return that same list.

```python
def test_get_supported_currencies_4(self):
    cc = CurrencyConverter()
    res = cc.get_supported_currencies()
    self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])
```

**test_get_supported_currencies_5**: `stated`
- reason: The docstring's example call returns exactly the seven currencies in the same order the test asserts, so a programmer following it would return that list and pass.

```python
def test_get_supported_currencies_5(self):
    cc = CurrencyConverter()
    res = cc.get_supported_currencies()
    self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])
```

## Method `add_currency_rate`

### Docstring

```python
def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :param currency:string, currency type to be added
        :param rate:float, exchange rate for this type of currency
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.add_currency_rate('KRW', 1308.84)
        self.rates['KRW'] = 1308.84
        """
```

### Reference code (`solution_code`)

```python
def add_currency_rate(self, currency, rate):
        if currency in self.rates:
            return False
        self.rates[currency] = rate
```

### Tests (`CurrencyConverterTestAddCurrencyRate`)

**test_add_currency_rate_1**: `stated`
- reason: The docstring says adding a new currency stores its exchange rate, and the example shows `self.rates['KRW'] = 1308.84`, so a programmer following it would pass this test.

```python
def test_add_currency_rate_1(self):
    cc = CurrencyConverter()
    cc.add_currency_rate('KRW', 1308.84)
    self.assertEqual(cc.rates['KRW'], 1308.84)
```

**test_add_currency_rate_2**: `stated`
- reason: The docstring says a new currency with its exchange rate is added to the supported list, and its example shows the rate stored in `self.rates`, so a programmer following it would store `'aaa'` with rate 1.0 and pass the test.

```python
def test_add_currency_rate_2(self):
    cc = CurrencyConverter()
    cc.add_currency_rate('aaa', 1.0)
    self.assertEqual(cc.rates['aaa'], 1.0)
```

**test_add_currency_rate_3**: `stated`
- reason: The docstring says to add a new supported currency with its exchange rate, and its example shows the rate being stored in `self.rates`, so a programmer following it would store `'bbb'` with rate 2.0 and pass.

```python
def test_add_currency_rate_3(self):
    cc = CurrencyConverter()
    cc.add_currency_rate('bbb', 2.0)
    self.assertEqual(cc.rates['bbb'], 2.0)
```

**test_add_currency_rate_4**: `stated`
- reason: The docstring says adding a new currency stores its exchange rate, and its example shows `self.rates['KRW'] = 1308.84`, so a programmer following it would store `'ccc'` with rate 3.0 in `rates` and pass the test.

```python
def test_add_currency_rate_4(self):
    cc = CurrencyConverter()
    cc.add_currency_rate('ccc', 3.0)
    self.assertEqual(cc.rates['ccc'], 3.0)
```

**test_add_currency_rate_5**: `stated`
- reason: The docstring says adding a new currency stores its exchange rate, and its example shows `self.rates['KRW'] = 1308.84`, so a programmer would store the new rate under that key and the test's check on `cc.rates['ddd']` would pass.

```python
def test_add_currency_rate_5(self):
    cc = CurrencyConverter()
    cc.add_currency_rate('ddd', 4.0)
    self.assertEqual(cc.rates['ddd'], 4.0)
```

**test_add_currency_rate_6**: `stated`
- reason: The docstring says to return False when the currency is already in the support list, and the test adds USD, which the default converter already supports, so a programmer following the docstring would return False and pass.

```python
def test_add_currency_rate_6(self):
    cc = CurrencyConverter()
    res = cc.add_currency_rate('USD', 1.0)
    self.assertFalse(res)
```

## Method `update_currency_rate`

### Docstring

```python
def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency:string
        :param new_rate:float
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.update_currency_rate('CNY', 7.18)
        self.rates['CNY'] = 7.18
        """
```

### Reference code (`solution_code`)

```python
def update_currency_rate(self, currency, new_rate):
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate
```

### Tests (`CurrencyConverterTestUpdateCurrencyRate`)

**test_update_currency_rate_1**: `stated`
- reason: The docstring says the method updates the exchange rate for the given currency, and its example shows `self.rates['CNY'] = 7.18`, so a programmer following it would store the new rate and pass this test.

```python
def test_update_currency_rate_1(self):
    cc = CurrencyConverter()
    cc.update_currency_rate('CNY', 7.18)
    self.assertEqual(cc.rates['CNY'], 7.18)
```

**test_update_currency_rate_2**: `stated`
- reason: The docstring says the method updates the exchange rate for a given currency, and its example shows `rates['CNY']` being set to the new value, so a programmer following it would store 1.0 for CNY and pass the test.

```python
def test_update_currency_rate_2(self):
    cc = CurrencyConverter()
    cc.update_currency_rate('CNY', 1.0)
    self.assertEqual(cc.rates['CNY'], 1.0)
```

**test_update_currency_rate_3**: `stated`
- reason: The docstring says the method updates the rate for the given currency, and its example shows `self.rates['CNY']` being set to the new value, so a programmer following it would store the new rate and pass this test.

```python
def test_update_currency_rate_3(self):
    cc = CurrencyConverter()
    cc.update_currency_rate('CNY', 2.0)
    self.assertEqual(cc.rates['CNY'], 2.0)
```

**test_update_currency_rate_4**: `stated`
- reason: The docstring says the method updates the exchange rate for a currency and gives an example that sets `rates['CNY']` to 7.18, so a programmer would implement a direct assignment that the test's check of `rates['CNY'] == 3.0` confirms.

```python
def test_update_currency_rate_4(self):
    cc = CurrencyConverter()
    cc.update_currency_rate('CNY', 3.0)
    self.assertEqual(cc.rates['CNY'], 3.0)
```

**test_update_currency_rate_5**: `stated`
- reason: The docstring's example shows `update_currency_rate('CNY', 7.18)` setting `self.rates['CNY']` to the new value, which is exactly what this test checks with 4.0.

```python
def test_update_currency_rate_5(self):
    cc = CurrencyConverter()
    cc.update_currency_rate('CNY', 4.0)
    self.assertEqual(cc.rates['CNY'], 4.0)
```

**test_update_currency_rate_6**: `stated`
- reason: The docstring says the method returns False when the update is unsuccessful, and a programmer would reasonably treat an unknown currency code as an unsuccessful update, so the test's `assertFalse` matches the documented behaviour.

```python
def test_update_currency_rate_6(self):
    cc = CurrencyConverter()
    res = cc.update_currency_rate('???', 7.18)
    self.assertFalse(res)
```

## Tests in no method's test class

### `CurrencyConverterTest`

**test_currencyconverter**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_currencyconverter(self):
    cc = CurrencyConverter()
    res = cc.convert(64, 'CNY', 'USD')
    self.assertEqual(res, 10.0)
    res = cc.get_supported_currencies()
    self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])
    cc.add_currency_rate('KRW', 1308.84)
    self.assertEqual(cc.rates['KRW'], 1308.84)
    cc.update_currency_rate('CNY', 7.18)
    self.assertEqual(cc.rates['CNY'], 7.18)
```
