import unittest




class UrlPathTestFixPath(unittest.TestCase):
    def test_fix_path_1(self):
        fixed_path = UrlPath.fix_path('/foo/bar/')
        self.assertEqual(fixed_path, 'foo/bar')

    def test_fix_path_2(self):
        fixed_path = UrlPath.fix_path('/aaa/bbb/')
        self.assertEqual(fixed_path, 'aaa/bbb')

    def test_fix_path_3(self):
        fixed_path = UrlPath.fix_path('/a/b/')
        self.assertEqual(fixed_path, 'a/b')

    def test_fix_path_4(self):
        fixed_path = UrlPath.fix_path('/111/222/')
        self.assertEqual(fixed_path, '111/222')

import unittest

class AgentTest_fix_path(unittest.TestCase):
    def test_fix_path_1(self):
        fixed_path = UrlPath.fix_path('/foo/bar')
        self.assertEqual(fixed_path, 'foo/bar')

    def test_fix_path_2(self):
        fixed_path = UrlPath.fix_path('foo/bar/')
        self.assertEqual(fixed_path, 'foo/bar')

class UrlPathTestAdd(unittest.TestCase):
    def test_add_1(self):
        url_path = UrlPath()
        url_path.add('foo')
        url_path.add('bar')
        self.assertEqual(url_path.segments, ['foo', 'bar'])

    def test_add_2(self):
        url_path = UrlPath()
        url_path.add('aaa')
        url_path.add('bbb')
        self.assertEqual(url_path.segments, ['aaa', 'bbb'])

    def test_add_3(self):
        url_path = UrlPath()
        url_path.add('123')
        self.assertEqual(url_path.segments, ['123'])

class AgentTest_add(unittest.TestCase):
    def test_add_1(self):
        url_path = UrlPath()
        url_path.add('hello world')
        url_path.add('%E3%81%82')
        self.assertEqual(url_path.segments, ['hello world', '%E3%81%82'])

    def test_add_2(self):
        first = UrlPath()
        second = UrlPath()
        first.add('foo')
        self.assertEqual(first.segments, ['foo'])
        self.assertEqual(second.segments, [])

class UrlPathTestParse(unittest.TestCase):
    def test_parse_1(self):
        url_path = UrlPath()
        url_path.parse('/foo/bar/', 'utf-8')
        self.assertEqual(url_path.segments, ['foo', 'bar'])
        self.assertEqual(url_path.with_end_tag, True)

    def test_parse_2(self):
        url_path = UrlPath()
        url_path.parse('aaa/bbb', 'utf-8')
        self.assertEqual(url_path.segments, ['aaa', 'bbb'])
        self.assertEqual(url_path.with_end_tag, False)

    def test_parse_3(self):
        url_path = UrlPath()
        url_path.parse('/123/456/', 'utf-8')
        self.assertEqual(url_path.segments, ['123', '456'])
        self.assertEqual(url_path.with_end_tag, True)

    def test_parse_4(self):
        url_path = UrlPath()
        url_path.parse('/123/456/789', 'utf-8')
        self.assertEqual(url_path.segments, ['123', '456', '789'])
        self.assertEqual(url_path.with_end_tag, False)

    def test_parse_5(self):
        url_path = UrlPath()
        url_path.parse('/foo/bar', 'utf-8')
        self.assertEqual(url_path.segments, ['foo', 'bar'])
        self.assertEqual(url_path.with_end_tag, False)

import unittest

class AgentTest_parse(unittest.TestCase):
    def test_parse_1(self):
        url_path = UrlPath()
        url_path.parse('/foo/', 'utf-8')
        self.assertEqual(url_path.segments, ['foo'])
        self.assertEqual(url_path.with_end_tag, True)

    def test_parse_2(self):
        url_path = UrlPath()
        url_path.parse('/あ/い/', 'utf-8')
        self.assertEqual(url_path.segments, ['あ', 'い'])
        self.assertEqual(url_path.with_end_tag, True)