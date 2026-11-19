import unittest


import unittest

class AgentTest_convert(unittest.TestCase):

    def test_convert_1(self):
        # Docstring example: 64 CNY is 10.0 USD (6.40 CNY per USD)
        cc = CurrencyConverter()
        self.assertAlmostEqual(cc.convert(64, 'CNY', 'USD'), 10.0, places=6)

    def test_convert_2(self):
        # Converting from USD to another currency multiplies by that currency's rate
        cc = CurrencyConverter()
        self.assertAlmostEqual(cc.convert(100, 'USD', 'EUR'), 85.0, places=6)

    def test_convert_3(self):
        # Cross-currency conversion goes through USD: 85 EUR -> 100 USD -> 72 GBP
        cc = CurrencyConverter()
        self.assertAlmostEqual(cc.convert(85, 'EUR', 'GBP'), 72.0, places=6)

    def test_convert_4(self):
        # Converting a currency to itself returns the same amount
        cc = CurrencyConverter()
        self.assertAlmostEqual(cc.convert(50, 'AUD', 'AUD'), 50.0, places=6)

    def test_convert_5(self):
        # A zero amount converts to zero in any supported currency pair
        cc = CurrencyConverter()
        self.assertAlmostEqual(cc.convert(0, 'JPY', 'CAD'), 0.0, places=6)

import unittest

class AgentTest_get_supported_currencies(unittest.TestCase):

    def test_get_supported_currencies_1(self):
        # Docstring example: the default supported currencies, in this order
        cc = CurrencyConverter()
        self.assertEqual(
            cc.get_supported_currencies(),
            ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY']
        )

    def test_get_supported_currencies_2(self):
        # The specification says the method returns a list
        cc = CurrencyConverter()
        self.assertIsInstance(cc.get_supported_currencies(), list)

    def test_get_supported_currencies_3(self):
        # Every supported currency type is a string, and USD is among them
        cc = CurrencyConverter()
        currencies = cc.get_supported_currencies()
        self.assertEqual(len(currencies), 7)
        for currency in currencies:
            self.assertIsInstance(currency, str)
        self.assertIn('USD', currencies)

    def test_get_supported_currencies_4(self):
        # A currency added with add_currency_rate becomes a supported currency type
        cc = CurrencyConverter()
        cc.add_currency_rate('KRW', 1308.84)
        currencies = cc.get_supported_currencies()
        self.assertIn('KRW', currencies)
        self.assertEqual(
            currencies,
            ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY', 'KRW']
        )

    def test_get_supported_currencies_5(self):
        # Adding a currency that is already supported returns False and leaves the list unchanged
        cc = CurrencyConverter()
        result = cc.add_currency_rate('EUR', 0.90)
        self.assertFalse(result)
        self.assertEqual(
            cc.get_supported_currencies(),
            ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY']
        )

import unittest

class AgentTest_add_currency_rate(unittest.TestCase):

    def test_add_currency_rate_1(self):
        # Adding a new currency type succeeds and returns None
        cc = CurrencyConverter()
        result = cc.add_currency_rate('KRW', 1308.84)
        self.assertIsNone(result)

    def test_add_currency_rate_2(self):
        # Adding a currency type that is already supported returns False
        cc = CurrencyConverter()
        result = cc.add_currency_rate('USD', 1.0)
        self.assertFalse(result)

    def test_add_currency_rate_3(self):
        # A newly added currency appears in the supported currency types
        cc = CurrencyConverter()
        cc.add_currency_rate('KRW', 1308.84)
        self.assertIn('KRW', cc.get_supported_currencies())

    def test_add_currency_rate_4(self):
        # The rate given for a new currency is used in conversions (rate is units per USD)
        cc = CurrencyConverter()
        cc.add_currency_rate('KRW', 1308.84)
        self.assertAlmostEqual(cc.convert(100, 'USD', 'KRW'), 130884.0, places=6)

    def test_add_currency_rate_5(self):
        # Adding an already supported currency returns False and does not change its existing rate
        cc = CurrencyConverter()
        result = cc.add_currency_rate('CNY', 7.18)
        self.assertFalse(result)
        self.assertAlmostEqual(cc.convert(64, 'CNY', 'USD'), 10.0, places=6)

import unittest

class AgentTest_update_currency_rate(unittest.TestCase):

    def test_update_currency_rate_1(self):
        # Docstring example: updating CNY to 7.18 changes how CNY converts to USD
        cc = CurrencyConverter()
        cc.update_currency_rate('CNY', 7.18)
        self.assertAlmostEqual(cc.convert(64, 'CNY', 'USD'), 64 / 7.18, places=6)

    def test_update_currency_rate_2(self):
        # A successful update returns None
        cc = CurrencyConverter()
        result = cc.update_currency_rate('CNY', 7.18)
        self.assertIsNone(result)

    def test_update_currency_rate_3(self):
        # The new rate is units per USD, so converting USD to the updated currency uses it
        cc = CurrencyConverter()
        cc.update_currency_rate('CNY', 7.18)
        self.assertAlmostEqual(cc.convert(100, 'USD', 'CNY'), 718.0, places=6)

    def test_update_currency_rate_4(self):
        # Updating a currency that is not supported returns False
        cc = CurrencyConverter()
        result = cc.update_currency_rate('KRW', 1308.84)
        self.assertFalse(result)

    def test_update_currency_rate_5(self):
        # Updating one currency's rate does not change the rate of other currencies
        cc = CurrencyConverter()
        cc.update_currency_rate('CNY', 7.18)
        self.assertAlmostEqual(cc.convert(100, 'USD', 'EUR'), 85.0, places=6)