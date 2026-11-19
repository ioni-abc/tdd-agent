import unittest


import unittest

class AgentTest_get_scheme(unittest.TestCase):

    def test_get_scheme_1(self):
        urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        self.assertEqual(urlhandler.get_scheme(), "https")

    def test_get_scheme_2(self):
        urlhandler = URLHandler("http://www.example.com/index.html")
        self.assertEqual(urlhandler.get_scheme(), "http")

    def test_get_scheme_3(self):
        urlhandler = URLHandler("ftp://files.example.org/pub/readme.txt")
        self.assertEqual(urlhandler.get_scheme(), "ftp")

    def test_get_scheme_4(self):
        urlhandler = URLHandler("https://localhost:8080/api/v1/users")
        result = urlhandler.get_scheme()
        self.assertIsInstance(result, str)
        self.assertEqual(result, "https")

    def test_get_scheme_5(self):
        urlhandler = URLHandler("file:///home/user/notes.txt")
        self.assertEqual(urlhandler.get_scheme(), "file")

import unittest

class AgentTest_get_host(unittest.TestCase):

    def test_get_host_1(self):
        urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        self.assertEqual(urlhandler.get_host(), "www.baidu.com")

    def test_get_host_2(self):
        urlhandler = URLHandler("http://www.example.com/index.html")
        self.assertEqual(urlhandler.get_host(), "www.example.com")

    def test_get_host_3(self):
        urlhandler = URLHandler("ftp://files.example.org/pub/readme.txt")
        self.assertEqual(urlhandler.get_host(), "files.example.org")

    def test_get_host_4(self):
        urlhandler = URLHandler("https://docs.python.org/3/library/unittest.html")
        result = urlhandler.get_host()
        self.assertIsInstance(result, str)
        self.assertEqual(result, "docs.python.org")

    def test_get_host_5(self):
        urlhandler = URLHandler("https://www.example.com")
        self.assertEqual(urlhandler.get_host(), "www.example.com")

import unittest

class AgentTest_get_path(unittest.TestCase):

    def test_get_path_1(self):
        urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        self.assertEqual(urlhandler.get_path(), "/s?wd=aaa&rsv_spt=1#page")

    def test_get_path_2(self):
        urlhandler = URLHandler("http://www.example.com/index.html")
        self.assertEqual(urlhandler.get_path(), "/index.html")

    def test_get_path_3(self):
        urlhandler = URLHandler("ftp://files.example.org/pub/readme.txt")
        self.assertEqual(urlhandler.get_path(), "/pub/readme.txt")

    def test_get_path_4(self):
        urlhandler = URLHandler("https://docs.python.org/3/library/unittest.html")
        result = urlhandler.get_path()
        self.assertIsInstance(result, str)
        self.assertEqual(result, "/3/library/unittest.html")

    def test_get_path_5(self):
        urlhandler = URLHandler("https://localhost:8080/api/v1/users")
        self.assertEqual(urlhandler.get_path(), "/api/v1/users")

import unittest

class AgentTest_get_query_params(unittest.TestCase):

    def test_get_query_params_1(self):
        urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        self.assertEqual(urlhandler.get_query_params(), {"wd": "aaa", "rsv_spt": "1"})

    def test_get_query_params_2(self):
        urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        result = urlhandler.get_query_params()
        self.assertIsInstance(result, dict)

    def test_get_query_params_3(self):
        urlhandler = URLHandler("http://www.example.com/search?q=python")
        self.assertEqual(urlhandler.get_query_params(), {"q": "python"})

    def test_get_query_params_4(self):
        urlhandler = URLHandler("http://www.example.com/index.html")
        self.assertEqual(urlhandler.get_query_params(), {})

    def test_get_query_params_5(self):
        urlhandler = URLHandler("https://www.example.com/page?a=1&b=2#section")
        self.assertEqual(urlhandler.get_query_params(), {"a": "1", "b": "2"})

import unittest

class AgentTest_get_fragment(unittest.TestCase):

    def test_get_fragment_1(self):
        urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        self.assertEqual(urlhandler.get_fragment(), "page")

    def test_get_fragment_2(self):
        urlhandler = URLHandler("https://www.example.com/page?a=1&b=2#section")
        self.assertEqual(urlhandler.get_fragment(), "section")

    def test_get_fragment_3(self):
        urlhandler = URLHandler("http://www.example.com/index.html#top")
        self.assertEqual(urlhandler.get_fragment(), "top")

    def test_get_fragment_4(self):
        urlhandler = URLHandler("https://docs.python.org/3/library/unittest.html#assertEqual")
        result = urlhandler.get_fragment()
        self.assertIsInstance(result, str)
        self.assertEqual(result, "assertEqual")

    def test_get_fragment_5(self):
        urlhandler = URLHandler("ftp://files.example.org/pub/readme.txt#section-2")
        self.assertEqual(urlhandler.get_fragment(), "section-2")