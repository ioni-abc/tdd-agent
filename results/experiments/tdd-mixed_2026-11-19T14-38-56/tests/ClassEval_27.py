import unittest




class CurrencyConverterTestConvert(unittest.TestCase):
    def test_convert_1(self):
        cc = CurrencyConverter()
        res = cc.convert(64, 'CNY', 'USD')
        self.assertEqual(res, 10.0)

    def test_convert_2(self):
        cc = CurrencyConverter()
        res = cc.convert(64, 'USD', 'USD')
        self.assertEqual(res, 64)

    def test_convert_3(self):
        cc = CurrencyConverter()
        res = cc.convert(64, 'CNY', 'GBP')
        self.assertAlmostEqual(res, 7.1999999999999)

    def test_convert_4(self):
        cc = CurrencyConverter()
        res = cc.convert(64, 'USD', 'GBP')
        self.assertAlmostEqual(res, 46.08)

import unittest

class AgentTest_convert(unittest.TestCase):
    def test_convert_1(self):
        cc = CurrencyConverter()
        res = cc.convert(110.15, 'JPY', 'USD')
        self.assertAlmostEqual(res, 1.0)

    def test_convert_2(self):
        cc = CurrencyConverter()
        res = cc.convert(100, 'EUR', 'JPY')
        self.assertAlmostEqual(res, 100 / 0.85 * 110.15, places=6)

class CurrencyConverterTestGetSupportedCurrencies(unittest.TestCase):
    def test_get_supported_currencies_1(self):
        cc = CurrencyConverter()
        res = cc.get_supported_currencies()
        self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])

    def test_get_supported_currencies_2(self):
        cc = CurrencyConverter()
        res = cc.get_supported_currencies()
        self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])

    def test_get_supported_currencies_3(self):
        cc = CurrencyConverter()
        res = cc.get_supported_currencies()
        self.assertEqual(res, ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY'])

import unittest

class AgentTest_get_supported_currencies(unittest.TestCase):
    def test_get_supported_currencies_1(self):
        cc = CurrencyConverter()
        res = cc.get_supported_currencies()
        self.assertIsInstance(res, list)

    def test_get_supported_currencies_2(self):
        cc = CurrencyConverter()
        cc.add_currency_rate('KRW', 1308.84)
        res = cc.get_supported_currencies()
        self.assertIn('KRW', res)
        self.assertEqual(len(res), 8)
        for currency in ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY']:
            self.assertIn(currency, res)

class CurrencyConverterTestAddCurrencyRate(unittest.TestCase):
    def test_add_currency_rate_1(self):
        cc = CurrencyConverter()
        cc.add_currency_rate('KRW', 1308.84)
        self.assertEqual(cc.rates['KRW'], 1308.84)

    def test_add_currency_rate_2(self):
        cc = CurrencyConverter()
        cc.add_currency_rate('aaa', 1.0)
        self.assertEqual(cc.rates['aaa'], 1.0)

    def test_add_currency_rate_3(self):
        cc = CurrencyConverter()
        cc.add_currency_rate('bbb', 2.0)
        self.assertEqual(cc.rates['bbb'], 2.0)

    def test_add_currency_rate_4(self):
        cc = CurrencyConverter()
        cc.add_currency_rate('ccc', 3.0)
        self.assertEqual(cc.rates['ccc'], 3.0)

import unittest

class AgentTest_add_currency_rate(unittest.TestCase):
    def test_add_currency_rate_1(self):
        cc = CurrencyConverter()
        res = cc.add_currency_rate('EUR', 0.85)
        self.assertFalse(res)

    def test_add_currency_rate_2(self):
        cc = CurrencyConverter()
        res = cc.add_currency_rate('KRW', 1308.84)
        self.assertIsNone(res)

class CurrencyConverterTestUpdateCurrencyRate(unittest.TestCase):
    def test_update_currency_rate_1(self):
        cc = CurrencyConverter()
        cc.update_currency_rate('CNY', 7.18)
        self.assertEqual(cc.rates['CNY'], 7.18)

    def test_update_currency_rate_2(self):
        cc = CurrencyConverter()
        cc.update_currency_rate('CNY', 1.0)
        self.assertEqual(cc.rates['CNY'], 1.0)

    def test_update_currency_rate_3(self):
        cc = CurrencyConverter()
        cc.update_currency_rate('CNY', 2.0)
        self.assertEqual(cc.rates['CNY'], 2.0)

    def test_update_currency_rate_4(self):
        cc = CurrencyConverter()
        cc.update_currency_rate('CNY', 3.0)
        self.assertEqual(cc.rates['CNY'], 3.0)

class AgentTest_update_currency_rate(unittest.TestCase):
    def test_update_currency_rate_1(self):
        cc = CurrencyConverter()
        res = cc.update_currency_rate('CNY', 7.18)
        self.assertIsNone(res)

    def test_update_currency_rate_2(self):
        cc = CurrencyConverter()
        res = cc.update_currency_rate('XYZ', 1.5)
        self.assertFalse(res)