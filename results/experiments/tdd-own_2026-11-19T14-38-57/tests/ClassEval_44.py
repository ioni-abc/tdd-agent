import unittest


import unittest

class AgentTest___format_line_feed(unittest.TestCase):

    def test___format_line_feed_1(self):
        # Two consecutive line breaks collapse into a single line break.
        result = HtmlUtil._HtmlUtil__format_line_feed("a\n\nb")
        self.assertEqual(result, "a\nb")

    def test___format_line_feed_2(self):
        # A run of several consecutive line breaks collapses into a single line break.
        result = HtmlUtil._HtmlUtil__format_line_feed("a\n\n\n\nb")
        self.assertEqual(result, "a\nb")

    def test___format_line_feed_3(self):
        # Text that already has a single line break between lines is left unchanged.
        result = HtmlUtil._HtmlUtil__format_line_feed("a\nb\nc")
        self.assertEqual(result, "a\nb\nc")

    def test___format_line_feed_4(self):
        # Every run of consecutive line breaks in the text is replaced, not just the first.
        result = HtmlUtil._HtmlUtil__format_line_feed("line1\n\nline2\n\n\nline3")
        self.assertEqual(result, "line1\nline2\nline3")

    def test___format_line_feed_5(self):
        # Mixed content, as produced by format_line_html_text: consecutive breaks become one,
        # and the surrounding text is preserved.
        text = "Title\n\nThis is a paragraph.\n\n\n-CODE-\n\nAnother paragraph.\n-CODE-"
        result = HtmlUtil._HtmlUtil__format_line_feed(text)
        self.assertEqual(
            result,
            "Title\nThis is a paragraph.\n-CODE-\nAnother paragraph.\n-CODE-"
        )

import unittest

import re

import string

import gensim

from bs4 import BeautifulSoup

class AgentTest_format_line_html_text(unittest.TestCase):

    def _non_empty_lines(self, text):
        return [line.strip() for line in text.split("\n") if line.strip()]

    def test_format_line_html_text_1(self):
        # The docstring example: headings and paragraphs are kept as text lines,
        # and each <pre> block is replaced by the -CODE- mark at its position.
        html_text = (
            "<html>\n"
            " <body>\n"
            "    <h1>Title</h1>\n"
            "    <p>This is a paragraph.</p>\n"
            "    <pre>print('Hello, world!')</pre>\n"
            "    <p>Another paragraph.</p>\n"
            "    <pre><code>for i in range(5):\n"
            "    print(i)</code></pre>\n"
            "    </body>\n"
            "    </html>"
        )
        htmlutil = HtmlUtil()
        result = htmlutil.format_line_html_text(html_text)
        self.assertEqual(
            self._non_empty_lines(result),
            ["Title", "This is a paragraph.", "-CODE-", "Another paragraph.", "-CODE-"]
        )

    def test_format_line_html_text_2(self):
        # The code itself is removed from the output and replaced by the mark.
        html_text = (
            "<html><body>"
            "<p>Run this:</p>"
            "<pre>print('Hello, world!')</pre>"
            "</body></html>"
        )
        htmlutil = HtmlUtil()
        result = htmlutil.format_line_html_text(html_text)
        self.assertNotIn("print('Hello, world!')", result)
        self.assertIn("-CODE-", result)
        self.assertIn("Run this:", result)

    def test_format_line_html_text_3(self):
        # HTML without any <pre> block keeps its text and contains no -CODE- mark.
        html_text = (
            "<html><body>"
            "<h1>Heading</h1>"
            "<p>Some text.</p>"
            "</body></html>"
        )
        htmlutil = HtmlUtil()
        result = htmlutil.format_line_html_text(html_text)
        self.assertNotIn("-CODE-", result)
        self.assertEqual(self._non_empty_lines(result), ["Heading", "Some text."])

    def test_format_line_html_text_4(self):
        # A single code block between two paragraphs becomes one -CODE- line in place.
        html_text = (
            "<html><body>"
            "<p>Before</p>"
            "<pre>x = 1</pre>"
            "<p>After</p>"
            "</body></html>"
        )
        htmlutil = HtmlUtil()
        result = htmlutil.format_line_html_text(html_text)
        self.assertEqual(self._non_empty_lines(result), ["Before", "-CODE-", "After"])

    def test_format_line_html_text_5(self):
        # Multiple code blocks, including one wrapped in a nested <code> tag,
        # are each replaced by a -CODE- mark and their code text is removed.
        html_text = (
            "<html><body>"
            "<p>Intro</p>"
            "<pre>a=1</pre>"
            "<p>Middle</p>"
            "<pre><code>b=2</code></pre>"
            "</body></html>"
        )
        htmlutil = HtmlUtil()
        result = htmlutil.format_line_html_text(html_text)
        self.assertEqual(
            self._non_empty_lines(result),
            ["Intro", "-CODE-", "Middle", "-CODE-"]
        )
        self.assertNotIn("a=1", result)
        self.assertNotIn("b=2", result)

import unittest

class AgentTest_extract_code_from_html_text(unittest.TestCase):

    def test_extract_code_from_html_text_1(self):
        # The docstring example: two <pre> blocks give two code strings, in document order.
        # The second block's indentation is not pinned, only its content.
        html_text = (
            "<html>\n"
            " <body>\n"
            "    <h1>Title</h1>\n"
            "    <p>This is a paragraph.</p>\n"
            "    <pre>print('Hello, world!')</pre>\n"
            "    <p>Another paragraph.</p>\n"
            "    <pre><code>for i in range(5):\n"
            "    print(i)</code></pre>\n"
            "    </body>\n"
            "    </html>"
        )
        htmlutil = HtmlUtil()
        result = htmlutil.extract_code_from_html_text(html_text)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "print('Hello, world!')")
        self.assertIn("for i in range(5):", result[1])
        self.assertIn("print(i)", result[1])

    def test_extract_code_from_html_text_2(self):
        # HTML with no <pre> block contains no code, so the result is an empty list.
        html_text = (
            "<html><body>"
            "<h1>Heading</h1>"
            "<p>Some text.</p>"
            "</body></html>"
        )
        htmlutil = HtmlUtil()
        result = htmlutil.extract_code_from_html_text(html_text)
        self.assertEqual(result, [])

    def test_extract_code_from_html_text_3(self):
        # A single <pre> block with plain text yields exactly that text as the only code item.
        html_text = "<html><body><pre>x = 1</pre></body></html>"
        htmlutil = HtmlUtil()
        result = htmlutil.extract_code_from_html_text(html_text)
        self.assertEqual(result, ["x = 1"])

    def test_extract_code_from_html_text_4(self):
        # Code wrapped in a nested <code> tag inside <pre> is returned as its text,
        # without the surrounding tags.
        html_text = "<html><body><pre><code>b=2</code></pre></body></html>"
        htmlutil = HtmlUtil()
        result = htmlutil.extract_code_from_html_text(html_text)
        self.assertEqual(result, ["b=2"])
        self.assertNotIn("<code>", result[0])

    def test_extract_code_from_html_text_5(self):
        # Several code blocks interleaved with paragraphs are returned in document order,
        # and the paragraph text is not included in the code list.
        html_text = (
            "<html><body>"
            "<p>Intro</p>"
            "<pre>a=1</pre>"
            "<p>Middle</p>"
            "<pre><code>b=2</code></pre>"
            "<p>End</p>"
            "<pre>c=3</pre>"
            "</body></html>"
        )
        htmlutil = HtmlUtil()
        result = htmlutil.extract_code_from_html_text(html_text)
        self.assertEqual(result, ["a=1", "b=2", "c=3"])
        for item in result:
            self.assertNotIn("Intro", item)
            self.assertNotIn("Middle", item)
            self.assertNotIn("End", item)