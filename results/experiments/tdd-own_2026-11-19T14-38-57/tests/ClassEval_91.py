import unittest


import unittest

import urllib.parse

class AgentTest_fix_path(unittest.TestCase):

    def test_fix_path_1(self):
        # Specification example: leading and trailing slashes are removed.
        self.assertEqual(UrlPath.fix_path('/foo/bar/'), 'foo/bar')

    def test_fix_path_2(self):
        # Only a leading slash is present; it should be removed.
        self.assertEqual(UrlPath.fix_path('/foo/bar'), 'foo/bar')

    def test_fix_path_3(self):
        # Only a trailing slash is present; it should be removed.
        self.assertEqual(UrlPath.fix_path('foo/bar/'), 'foo/bar')

    def test_fix_path_4(self):
        # No leading or trailing slashes; the path is returned unchanged.
        self.assertEqual(UrlPath.fix_path('foo/bar'), 'foo/bar')

    def test_fix_path_5(self):
        # Slashes between segments are not leading or trailing and must be kept.
        self.assertEqual(UrlPath.fix_path('/foo/bar/baz/'), 'foo/bar/baz')

import unittest

import urllib.parse

class AgentTest_add(unittest.TestCase):

    def test_add_1(self):
        # Adding a single segment to a new UrlPath appends it to the segments list.
        url_path = UrlPath()
        url_path.add('foo')
        self.assertEqual(url_path.segments, ['foo'])

    def test_add_2(self):
        # Specification example: adding 'foo' then 'bar' yields ['foo', 'bar'].
        url_path = UrlPath()
        url_path.add('foo')
        url_path.add('bar')
        self.assertEqual(url_path.segments, ['foo', 'bar'])

    def test_add_3(self):
        # Segments are kept in the order in which they were added.
        url_path = UrlPath()
        url_path.add('a')
        url_path.add('b')
        url_path.add('c')
        self.assertEqual(url_path.segments, ['a', 'b', 'c'])

    def test_add_4(self):
        # Adding the same segment twice appends it twice; add simply appends to the list.
        url_path = UrlPath()
        url_path.add('foo')
        url_path.add('foo')
        self.assertEqual(url_path.segments, ['foo', 'foo'])

    def test_add_5(self):
        # Each UrlPath instance has its own segments list, so adding to one
        # does not affect another.
        first = UrlPath()
        second = UrlPath()
        first.add('foo')
        self.assertEqual(first.segments, ['foo'])
        self.assertEqual(second.segments, [])

import unittest

class AgentTest_parse(unittest.TestCase):

    def test_parse_1(self):
        # Specification example: '/foo/bar/' parsed with 'utf-8' populates ['foo', 'bar'].
        url_path = UrlPath()
        url_path.parse('/foo/bar/', 'utf-8')
        self.assertEqual(url_path.segments, ['foo', 'bar'])

    def test_parse_2(self):
        # A leading slash without a trailing slash still yields the same segments.
        url_path = UrlPath()
        url_path.parse('/foo/bar', 'utf-8')
        self.assertEqual(url_path.segments, ['foo', 'bar'])

    def test_parse_3(self):
        # Segments are populated in the order they appear in the path string.
        url_path = UrlPath()
        url_path.parse('foo/bar/baz/', 'utf-8')
        self.assertEqual(url_path.segments, ['foo', 'bar', 'baz'])

    def test_parse_4(self):
        # A path with a single segment, surrounded by slashes, yields one segment.
        url_path = UrlPath()
        url_path.parse('/foo/', 'utf-8')
        self.assertEqual(url_path.segments, ['foo'])

    def test_parse_5(self):
        # For plain ASCII path text, the charset argument does not change the segments.
        utf8_path = UrlPath()
        utf8_path.parse('/foo/bar/', 'utf-8')
        latin1_path = UrlPath()
        latin1_path.parse('/foo/bar/', 'iso-8859-1')
        self.assertEqual(utf8_path.segments, ['foo', 'bar'])
        self.assertEqual(latin1_path.segments, ['foo', 'bar'])