import unittest


import unittest

class AgentTest_add_stock(unittest.TestCase):

    def test_add_stock_1(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertEqual(
            tracker.portfolio,
            [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        )

    def test_add_stock_2(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        tracker.add_stock({"name": "MSFT", "price": 300.0, "quantity": 5})
        self.assertEqual(
            tracker.portfolio,
            [
                {"name": "AAPL", "price": 150.0, "quantity": 10},
                {"name": "MSFT", "price": 300.0, "quantity": 5}
            ]
        )

    def test_add_stock_3(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        stored = tracker.portfolio[0]
        self.assertEqual(stored["name"], "AAPL")
        self.assertEqual(stored["price"], 150.0)
        self.assertEqual(stored["quantity"], 10)

    def test_add_stock_4(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "MSFT", "price": 300.0, "quantity": 5}]
        tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertEqual(len(tracker.portfolio), 2)
        self.assertIn({"name": "MSFT", "price": 300.0, "quantity": 5}, tracker.portfolio)
        self.assertIn({"name": "AAPL", "price": 150.0, "quantity": 10}, tracker.portfolio)

    def test_add_stock_5(self):
        tracker = StockPortfolioTracker(10000.0)
        self.assertEqual(tracker.portfolio, [])
        tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertEqual(len(tracker.portfolio), 1)
        self.assertEqual(tracker.portfolio[0]["name"], "AAPL")

import unittest

class AgentTest_remove_stock(unittest.TestCase):

    def test_remove_stock_1(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        result = tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertTrue(result)
        self.assertEqual(tracker.portfolio, [])

    def test_remove_stock_2(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [
            {"name": "AAPL", "price": 150.0, "quantity": 10},
            {"name": "MSFT", "price": 300.0, "quantity": 5}
        ]
        tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertEqual(
            tracker.portfolio,
            [{"name": "MSFT", "price": 300.0, "quantity": 5}]
        )

    def test_remove_stock_3(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [
            {"name": "AAPL", "price": 150.0, "quantity": 10},
            {"name": "MSFT", "price": 300.0, "quantity": 5},
            {"name": "GOOG", "price": 2800.0, "quantity": 2}
        ]
        tracker.remove_stock({"name": "MSFT", "price": 300.0, "quantity": 5})
        self.assertEqual(
            tracker.portfolio,
            [
                {"name": "AAPL", "price": 150.0, "quantity": 10},
                {"name": "GOOG", "price": 2800.0, "quantity": 2}
            ]
        )

    def test_remove_stock_4(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        result = tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertIs(result, True)

    def test_remove_stock_5(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [
            {"name": "AAPL", "price": 150.0, "quantity": 10},
            {"name": "MSFT", "price": 300.0, "quantity": 5},
            {"name": "GOOG", "price": 2800.0, "quantity": 2}
        ]
        self.assertEqual(len(tracker.portfolio), 3)
        tracker.remove_stock({"name": "GOOG", "price": 2800.0, "quantity": 2})
        self.assertEqual(len(tracker.portfolio), 2)
        names = [item["name"] for item in tracker.portfolio]
        self.assertNotIn("GOOG", names)
        self.assertIn("AAPL", names)
        self.assertIn("MSFT", names)

import unittest

class AgentTest_buy_stock(unittest.TestCase):

    def test_buy_stock_1(self):
        tracker = StockPortfolioTracker(10000.0)
        result = tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertIs(result, True)
        self.assertEqual(
            tracker.portfolio,
            [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        )

    def test_buy_stock_2(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        tracker.buy_stock({"name": "MSFT", "price": 300.0, "quantity": 5})
        self.assertEqual(
            tracker.portfolio,
            [
                {"name": "AAPL", "price": 150.0, "quantity": 10},
                {"name": "MSFT", "price": 300.0, "quantity": 5}
            ]
        )

    def test_buy_stock_3(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertEqual(tracker.cash_balance, 8500.0)

    def test_buy_stock_4(self):
        tracker = StockPortfolioTracker(1000.0)
        result = tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertIs(result, False)
        self.assertEqual(tracker.portfolio, [])

    def test_buy_stock_5(self):
        tracker = StockPortfolioTracker(1500.0)
        result = tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertIs(result, True)
        self.assertEqual(tracker.cash_balance, 0.0)
        self.assertEqual(
            tracker.portfolio,
            [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        )

class AgentTest_sell_stock(unittest.TestCase):

    def test_sell_stock_1(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        result = tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertIs(result, True)
        self.assertEqual(tracker.portfolio, [])

    def test_sell_stock_2(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertEqual(tracker.cash_balance, 11500.0)

    def test_sell_stock_3(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        result = tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 20})
        self.assertIs(result, False)
        self.assertEqual(
            tracker.portfolio,
            [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        )

    def test_sell_stock_4(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 20})
        self.assertEqual(tracker.cash_balance, 10000.0)

    def test_sell_stock_5(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [
            {"name": "AAPL", "price": 150.0, "quantity": 10},
            {"name": "MSFT", "price": 300.0, "quantity": 5}
        ]
        result = tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertIs(result, True)
        self.assertEqual(
            tracker.portfolio,
            [{"name": "MSFT", "price": 300.0, "quantity": 5}]
        )

import unittest

class AgentTest_calculate_portfolio_value(unittest.TestCase):

    def test_calculate_portfolio_value_1(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        self.assertEqual(tracker.calculate_portfolio_value(), 11500.0)

    def test_calculate_portfolio_value_2(self):
        tracker = StockPortfolioTracker(10000.0)
        self.assertEqual(tracker.calculate_portfolio_value(), 10000.0)

    def test_calculate_portfolio_value_3(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [
            {"name": "AAPL", "price": 150.0, "quantity": 10},
            {"name": "MSFT", "price": 300.0, "quantity": 5}
        ]
        self.assertEqual(tracker.calculate_portfolio_value(), 13000.0)

    def test_calculate_portfolio_value_4(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        result = tracker.calculate_portfolio_value()
        self.assertIsInstance(result, float)

    def test_calculate_portfolio_value_5(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        tracker.calculate_portfolio_value()
        self.assertEqual(tracker.cash_balance, 10000.0)
        self.assertEqual(
            tracker.portfolio,
            [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        )

import unittest

class AgentTest_get_stock_value(unittest.TestCase):

    def test_get_stock_value_1(self):
        tracker = StockPortfolioTracker(10000.0)
        self.assertEqual(
            tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10}),
            1500.0
        )

    def test_get_stock_value_2(self):
        tracker = StockPortfolioTracker(10000.0)
        result = tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
        self.assertIsInstance(result, float)

    def test_get_stock_value_3(self):
        tracker = StockPortfolioTracker(10000.0)
        self.assertEqual(
            tracker.get_stock_value({"name": "GOOG", "price": 2800.0, "quantity": 2}),
            5600.0
        )

    def test_get_stock_value_4(self):
        tracker = StockPortfolioTracker(10000.0)
        self.assertEqual(
            tracker.get_stock_value({"name": "XYZ", "price": 99.5, "quantity": 4}),
            398.0
        )

    def test_get_stock_value_5(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "MSFT", "price": 300.0, "quantity": 5}]
        self.assertEqual(
            tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10}),
            1500.0
        )
        self.assertEqual(
            tracker.portfolio,
            [{"name": "MSFT", "price": 300.0, "quantity": 5}]
        )

import unittest

class AgentTest_get_portfolio_summary(unittest.TestCase):

    def test_get_portfolio_summary_1(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        self.assertEqual(
            tracker.get_portfolio_summary(),
            (11500.0, [{"name": "AAPL", "value": 1500.0}])
        )

    def test_get_portfolio_summary_2(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [{"name": "AAPL", "price": 150.0, "quantity": 10}]
        result = tracker.get_portfolio_summary()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], float)
        self.assertIsInstance(result[1], list)

    def test_get_portfolio_summary_3(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [
            {"name": "GOOG", "price": 2800.0, "quantity": 2},
            {"name": "XYZ", "price": 99.5, "quantity": 4}
        ]
        total, summary = tracker.get_portfolio_summary()
        self.assertEqual(total, 15998.0)
        self.assertEqual(
            summary,
            [
                {"name": "GOOG", "value": 5600.0},
                {"name": "XYZ", "value": 398.0}
            ]
        )

    def test_get_portfolio_summary_4(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [
            {"name": "AAPL", "price": 150.0, "quantity": 10},
            {"name": "MSFT", "price": 300.0, "quantity": 5}
        ]
        _, summary = tracker.get_portfolio_summary()
        self.assertEqual(len(summary), 2)
        for entry in summary:
            self.assertEqual(set(entry.keys()), {"name", "value"})
        names = [entry["name"] for entry in summary]
        self.assertEqual(names, ["AAPL", "MSFT"])

    def test_get_portfolio_summary_5(self):
        tracker = StockPortfolioTracker(10000.0)
        tracker.portfolio = [
            {"name": "AAPL", "price": 150.0, "quantity": 10},
            {"name": "MSFT", "price": 300.0, "quantity": 5}
        ]
        first = tracker.get_portfolio_summary()
        second = tracker.get_portfolio_summary()
        self.assertEqual(first, second)
        self.assertEqual(tracker.cash_balance, 10000.0)
        self.assertEqual(
            tracker.portfolio,
            [
                {"name": "AAPL", "price": 150.0, "quantity": 10},
                {"name": "MSFT", "price": 300.0, "quantity": 5}
            ]
        )