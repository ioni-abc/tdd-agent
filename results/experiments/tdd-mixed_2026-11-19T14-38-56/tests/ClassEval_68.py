import unittest




class PageUtilTestGetPage(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.page_size = 3
        self.page_util = PageUtil(self.data, self.page_size)

    def test_get_page_1(self):
        page_number = 1
        expected_page = [1, 2, 3]
        actual_page = self.page_util.get_page(page_number)
        self.assertEqual(actual_page, expected_page)

    def test_get_page_2(self):
        page_number = 2
        expected_page = [4, 5, 6]
        actual_page = self.page_util.get_page(page_number)
        self.assertEqual(actual_page, expected_page)

    def test_get_page_3(self):
        page_number = 3
        expected_page = [7, 8, 9]
        actual_page = self.page_util.get_page(page_number)
        self.assertEqual(actual_page, expected_page)

import unittest

class AgentTest_get_page(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.page_size = 3
        self.page_util = PageUtil(self.data, self.page_size)

    def test_get_page_1(self):
        page_number = 4
        expected_page = [10]
        actual_page = self.page_util.get_page(page_number)
        self.assertEqual(actual_page, expected_page)

    def test_get_page_2(self):
        page_util = PageUtil([1, 2, 3, 4], 10)
        page_number = 1
        expected_page = [1, 2, 3, 4]
        actual_page = page_util.get_page(page_number)
        self.assertEqual(actual_page, expected_page)

class PageUtilTestGetPageInfo(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.page_size = 3
        self.page_util = PageUtil(self.data, self.page_size)

    def test_get_page_info_1(self):
        page_number = 2
        expected_info = {
            "current_page": 2,
            "per_page": 3,
            "total_pages": 4,
            "total_items": 10,
            "has_previous": True,
            "has_next": True,
            "data": [4, 5, 6]
        }
        actual_info = self.page_util.get_page_info(page_number)
        self.assertEqual(actual_info, expected_info)

    def test_get_page_info_2(self):
        page_number = 1
        expected_info = {
            "current_page": 1,
            "per_page": 3,
            "total_pages": 4,
            "total_items": 10,
            "has_previous": False,
            "has_next": True,
            "data": [1, 2, 3]
        }
        actual_info = self.page_util.get_page_info(page_number)
        self.assertEqual(actual_info, expected_info)

    def test_get_page_info_3(self):
        page_number = 3
        expected_info = {
            "current_page": 3,
            "per_page": 3,
            "total_pages": 4,
            "total_items": 10,
            "has_previous": True,
            "has_next": True,
            "data": [7, 8, 9]
        }
        actual_info = self.page_util.get_page_info(page_number)
        self.assertEqual(actual_info, expected_info)

import unittest

class AgentTest_get_page_info(unittest.TestCase):
    def test_get_page_info_1(self):
        page_util = PageUtil([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
        expected_info = {
            "current_page": 4,
            "per_page": 3,
            "total_pages": 4,
            "total_items": 10,
            "has_previous": True,
            "has_next": False,
            "data": [10]
        }
        actual_info = page_util.get_page_info(4)
        self.assertEqual(actual_info, expected_info)

    def test_get_page_info_2(self):
        page_util = PageUtil([1, 2, 3, 4], 10)
        expected_info = {
            "current_page": 1,
            "per_page": 10,
            "total_pages": 1,
            "total_items": 4,
            "has_previous": False,
            "has_next": False,
            "data": [1, 2, 3, 4]
        }
        actual_info = page_util.get_page_info(1)
        self.assertEqual(actual_info, expected_info)

class PageUtilTestSearch(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.page_size = 3
        self.page_util = PageUtil(self.data, self.page_size)

    def test_search_1(self):
        keyword = "1"
        expected_results = {
            "keyword": "1",
            "total_results": 2,
            "total_pages": 1,
            "results": [1, 10]
        }
        actual_results = self.page_util.search(keyword)
        self.assertEqual(actual_results, expected_results)

    def test_search_2(self):
        keyword = "2"
        expected_results = {
            "keyword": "2",
            "total_results": 1,
            "total_pages": 1,
            "results": [2]
        }
        actual_results = self.page_util.search(keyword)
        self.assertEqual(actual_results, expected_results)

    def test_search_3(self):
        keyword = "3"
        expected_results = {
            "keyword": "3",
            "total_results": 1,
            "total_pages": 1,
            "results": [3]
        }
        actual_results = self.page_util.search(keyword)
        self.assertEqual(actual_results, expected_results)

import unittest

class AgentTest_search(unittest.TestCase):
    def test_search_1(self):
        page_util = PageUtil([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
        keyword = "11"
        expected_results = {
            "keyword": "11",
            "total_results": 0,
            "total_pages": 0,
            "results": []
        }
        actual_results = page_util.search(keyword)
        self.assertEqual(actual_results, expected_results)

    def test_search_2(self):
        page_util = PageUtil(["apple", "banana", "cherry", "pineapple", "grape"], 2)
        keyword = "a"
        expected_results = {
            "keyword": "a",
            "total_results": 4,
            "total_pages": 2,
            "results": ["apple", "banana", "pineapple", "grape"]
        }
        actual_results = page_util.search(keyword)
        self.assertEqual(actual_results, expected_results)