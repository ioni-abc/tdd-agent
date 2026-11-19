import unittest


import unittest

class AgentTest_get_page(unittest.TestCase):

    def test_get_page_1(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        self.assertEqual(page_util.get_page(1), [1])

    def test_get_page_2(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        self.assertEqual(page_util.get_page(2), [2])
        self.assertEqual(page_util.get_page(3), [3])
        self.assertEqual(page_util.get_page(4), [4])

    def test_get_page_3(self):
        page_util = PageUtil([1, 2, 3, 4, 5], 2)
        self.assertEqual(page_util.get_page(1), [1, 2])
        self.assertEqual(page_util.get_page(2), [3, 4])
        self.assertEqual(page_util.get_page(3), [5])

    def test_get_page_4(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        result = page_util.get_page(1)
        self.assertIsInstance(result, list)

    def test_get_page_5(self):
        page_util = PageUtil([1, 2, 3], 10)
        self.assertEqual(page_util.get_page(1), [1, 2, 3])

import unittest

class AgentTest_get_page_info(unittest.TestCase):

    def test_get_page_info_1(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        expected = {
            "current_page": 1,
            "per_page": 1,
            "total_pages": 4,
            "total_items": 4,
            "has_previous": False,
            "has_next": True,
            "data": [1],
        }
        self.assertEqual(page_util.get_page_info(1), expected)

    def test_get_page_info_2(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        info = page_util.get_page_info(2)
        self.assertEqual(info["current_page"], 2)
        self.assertEqual(info["per_page"], 1)
        self.assertEqual(info["total_pages"], 4)
        self.assertEqual(info["total_items"], 4)
        self.assertTrue(info["has_previous"])
        self.assertTrue(info["has_next"])
        self.assertEqual(info["data"], [2])

    def test_get_page_info_3(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        info = page_util.get_page_info(4)
        self.assertEqual(info["current_page"], 4)
        self.assertTrue(info["has_previous"])
        self.assertFalse(info["has_next"])
        self.assertEqual(info["data"], [4])

    def test_get_page_info_4(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        info = page_util.get_page_info(1)
        self.assertIsInstance(info, dict)
        for key in ["current_page", "per_page", "total_pages", "total_items",
                    "has_previous", "has_next", "data"]:
            self.assertIn(key, info)

    def test_get_page_info_5(self):
        page_util = PageUtil([1, 2, 3, 4, 5], 2)
        info = page_util.get_page_info(3)
        self.assertEqual(info["current_page"], 3)
        self.assertEqual(info["per_page"], 2)
        self.assertEqual(info["total_pages"], 3)
        self.assertEqual(info["total_items"], 5)
        self.assertTrue(info["has_previous"])
        self.assertFalse(info["has_next"])
        self.assertEqual(info["data"], [5])

import unittest

class AgentTest_search(unittest.TestCase):

    def test_search_1(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        expected = {
            "keyword": "1",
            "total_results": 1,
            "total_pages": 1,
            "results": [1],
        }
        self.assertEqual(page_util.search("1"), expected)

    def test_search_2(self):
        page_util = PageUtil([1, 2, 3, 4], 1)
        info = page_util.search("9")
        self.assertIsInstance(info, dict)
        self.assertEqual(info["keyword"], "9")
        self.assertEqual(info["total_results"], 0)
        self.assertEqual(info["results"], [])

    def test_search_3(self):
        page_util = PageUtil(["apple", "banana", "cherry"], 2)
        info = page_util.search("an")
        self.assertEqual(info["keyword"], "an")
        self.assertEqual(info["total_results"], 1)
        self.assertEqual(info["results"], ["banana"])

    def test_search_4(self):
        page_util = PageUtil(["apple", "apricot", "banana", "cherry", "avocado"], 2)
        info = page_util.search("a")
        self.assertEqual(info["total_results"], 4)
        self.assertEqual(info["total_pages"], 2)
        self.assertEqual(info["results"], ["apple", "apricot", "banana", "avocado"])

    def test_search_5(self):
        page_util = PageUtil(["apple", "banana", "cherry"], 1)
        info = page_util.search("ch")
        for key in ["keyword", "total_results", "total_pages", "results"]:
            self.assertIn(key, info)
        self.assertEqual(info["keyword"], "ch")
        self.assertEqual(info["total_results"], 1)
        self.assertEqual(info["total_pages"], 1)
        self.assertEqual(info["results"], ["cherry"])