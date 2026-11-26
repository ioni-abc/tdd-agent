# ClassEval_44

## Skeleton (what the agent sees)

```python
import re
import string
import gensim
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    This is a class as util for html, supporting for formatting and extracting code from HTML text, including cleaning up the text and converting certain elements into specific marks.
    """

    def __init__(self):
        """
        Initialize a series of labels
        """
        self.SPACE_MARK = '-SPACE-'
        self.JSON_MARK = '-JSON-'
        self.MARKUP_LANGUAGE_MARK = '-MARKUP_LANGUAGE-'
        self.URL_MARK = '-URL-'
        self.NUMBER_MARK = '-NUMBER-'
        self.TRACE_MARK = '-TRACE-'
        self.COMMAND_MARK = '-COMMAND-'
        self.COMMENT_MARK = '-COMMENT-'
        self.CODE_MARK = '-CODE-'

    @staticmethod
    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """

    def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        Title
        This is a paragraph.
        -CODE-
        Another paragraph.
        -CODE-
        """

    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
        """
```

## Method `__format_line_feed`

### Docstring

```python
def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
```

### Reference code (`solution_code`)

```python
def __format_line_feed(text):
        return re.sub(re.compile(r'\n+'), '\n', text)
```

### Tests (`HtmlUtilTestFormatLineFeed`)

**test_format_line_feed_1**: `stated`
- reason: The docstring says consecutive line breaks are replaced with a single line break, which is exactly what the test checks: a run of three newlines becomes one.

```python
def test_format_line_feed_1(self):
    self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed('aaa\n\n\n'), 'aaa\n')
```

**test_format_line_feed_2**: `stated`
- reason: The docstring says consecutive line breaks are replaced with a single line break, so a programmer would collapse the run of trailing newlines into one, giving 'aaa\n' as the test expects.

```python
def test_format_line_feed_2(self):
    self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed('aaa\n\n\n\n'), 'aaa\n')
```

**test_format_line_feed_3**: `stated`
- reason: The docstring says consecutive line breaks are replaced with a single line break, which a programmer would implement as collapsing each run of newlines to one, producing the expected output here.

```python
def test_format_line_feed_3(self):
    self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed('aaa\n\n\nbbb\n\n'), 'aaa\nbbb\n')
```

**test_format_line_feed_4**: `stated`
- reason: The docstring says consecutive line breaks are replaced with a single line break, so collapsing the run of three newlines after 'ccc' to one newline gives the expected 'ccc\n'.

```python
def test_format_line_feed_4(self):
    self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed('ccc\n\n\n'), 'ccc\n')
```

**test_format_line_feed_5**: `stated`
- reason: A programmer implementing "replace consecutive line breaks with a single line break" would naturally leave an empty string unchanged and return '', which is what the test expects.

```python
def test_format_line_feed_5(self):
    self.assertEqual(HtmlUtil._HtmlUtil__format_line_feed(''), '')
```

## Method `format_line_html_text`

### Docstring

```python
def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        Title
        This is a paragraph.
        -CODE-
        Another paragraph.
        -CODE-
        """
```

### Reference code (`solution_code`)

```python
def format_line_html_text(self, html_text):
        if html_text is None or len(html_text) == 0:
            return ''
        soup = BeautifulSoup(html_text, 'lxml')

        code_tag = soup.find_all(name=['pre', 'blockquote'])
        for tag in code_tag:
            tag.string = self.CODE_MARK

        ul_ol_group = soup.find_all(name=['ul', 'ol'])
        for ul_ol_item in ul_ol_group:
            li_group = ul_ol_item.find_all('li')
            for li_item in li_group:
                li_item_text = li_item.get_text().strip()
                if len(li_item_text) == 0:
                    continue
                if li_item_text[-1] in string.punctuation:
                    li_item.string = '[{0}]{1}'.format('-', li_item_text)
                    continue
                li_item.string = '[{0}]{1}.'.format('-', li_item_text)

        p_group = soup.find_all(name=['p'])
        for p_item in p_group:
            p_item_text = p_item.get_text().strip()
            if p_item_text:
                if p_item_text[-1] in string.punctuation:
                    p_item.string = p_item_text
                    continue
                next_sibling = p_item.find_next_sibling()
                if next_sibling and self.CODE_MARK in next_sibling.get_text():
                    p_item.string = p_item_text + ':'
                    continue
                p_item.string = p_item_text + '.'

        clean_text = gensim.utils.decode_htmlentities(soup.get_text())
        return self.__format_line_feed(clean_text)
```

### Tests (`HtmlUtilTestFormatLineHtmlText`)

**test_format_line_html_text_1**: `stated`
- reason: The docstring says to return the text without code and put -CODE- where code blocks were, and the test's paragraphs and h1 text already end in periods, so the expected output follows directly from that description.

```python
    def test_format_line_html_text_1(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')
```

**test_format_line_html_text_2**: `unstated`
- reason: The docstring's example shows the general shape of the output, but it does not specify the exact whitespace and newline handling the test asserts, so a reasonable implementation could differ in leading or trailing line breaks.
- missing: The docstring should state how line breaks and blank lines are handled in the returned text (including leading and trailing newlines), and what punctuation is added to text blocks that lack ending punctuation, especially when they are followed by a code block.

```python
    def test_format_line_html_text_2(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title2</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title2
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')
```

**test_format_line_html_text_3**: `unstated`
- reason: The docstring says code blocks become -CODE- and other text is kept, but it doesn't specify the exact whitespace and line-break layout of the output, which is what this test checks.
- missing: The docstring should state how whitespace and line breaks in the source HTML map to the returned text (including leading and trailing newlines and how blank lines are handled), and how text in paragraphs and list items is punctuated or joined around code markers.

```python
    def test_format_line_html_text_3(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title3</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title3
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')
```

**test_format_line_html_text_4**: `unstated`
- reason: The docstring says code blocks become -CODE- and the other text is kept, but the test's exact expected string depends on line-feed and whitespace normalization that a correct implementation could get differently.
- missing: The docstring should specify how whitespace and line breaks in the output are formed, including leading or trailing newlines, indentation stripping, and whether each block element becomes its own line.

```python
    def test_format_line_html_text_4(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title4</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title4
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')
```

**test_format_line_html_text_5**: `unstated`
- reason: The docstring's example shows the right content (headings and paragraphs kept, each `<pre>` replaced by `-CODE-`), but it does not say how the surrounding blank lines and line breaks should look, and the test expects a leading and trailing newline that a programmer could easily produce differently.
- missing: The docstring should state the exact line-break and whitespace rules of the output, including whether leading and trailing newlines from the input are kept or stripped and how blank lines between blocks are handled.

```python
    def test_format_line_html_text_5(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title5</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title5
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')
```

**test_format_line_html_text_6**: `unstated`
- reason: The docstring gives no behaviour for an empty input string, so a correct implementation could return something other than the empty string the test expects.
- missing: The docstring should state what the method returns when the input HTML is empty or None, such as an empty string.

```python
def test_format_line_html_text_6(self):
    htmlutil = HtmlUtil()
    res = htmlutil.format_line_html_text('')
    self.assertEqual(res, '')
```

**test_format_line_html_text_7**: `unstated`
- reason: The docstring says nothing about list items, so a programmer following it would not know to prefix them with "[-]" or to leave the text unchanged when it already ends in punctuation, which is what this test expects.
- missing: The docstring should state that each list item (li inside ul or ol) is prefixed with "[-]", and that a period is appended to its text only when the text does not already end in punctuation.

```python
def test_format_line_html_text_7(self):
    htmlutil = HtmlUtil()
    res = htmlutil.format_line_html_text('''<ul><li>Item 1!</li></ul>''')
    self.assertEqual(res, '''[-]Item 1!''')
```

**test_format_line_html_text_8**: `unstated`
- reason: The docstring says nothing about how list items are rendered or how empty list items are handled, so a correct implementation that renders list items differently could return a non-empty string and fail this test.
- missing: The docstring should describe how list items are formatted (any prefix marker, whether a period is appended) and what output an empty list item or list with no text produces.

```python
def test_format_line_html_text_8(self):
    htmlutil = HtmlUtil()
    res = htmlutil.format_line_html_text('''<ul><li></li></ul>''')
    self.assertEqual(res, '')
```

**test_format_line_html_text_9**: `unstated`
- reason: The docstring only says to return the text without code and insert the code marker, so it does not say how paragraph punctuation is handled, and the reference code's rules for adding a period or colon to paragraphs are not described.
- missing: The docstring should state how terminal punctuation on paragraph text is handled: whether a period is appended when a paragraph lacks trailing punctuation, when a colon is used instead before a code block, and when the text is left unchanged.

```python
def test_format_line_html_text_9(self):
    htmlutil = HtmlUtil()
    res = htmlutil.format_line_html_text('''<p>Some sentence here.</p>''')
    self.assertEqual(res, 'Some sentence here.')
```

**test_format_line_html_text_10**: `unstated`
- reason: The docstring never says that paragraph text lacking end punctuation gets a period appended, or that inline code outside a pre/blockquote is kept as plain text, so a faithful implementation could produce different output than this test expects.
- missing: The docstring should specify the normalization rules: a paragraph whose text does not end in punctuation gets a period (or a colon when the next sibling is a code block), only pre and blockquote elements are replaced by the code marker, and other inline tags are flattened to their text with no added separator.

```python
def test_format_line_html_text_10(self):
    htmlutil = HtmlUtil()
    res = htmlutil.format_line_html_text('''<p>Some paragraph here</p><code>Code block</code>''')
    self.assertEqual(res, '''Some paragraph here.Code block''')
```

**test_format_line_html_text_11**: `unstated`
- reason: The docstring does not say that paragraphs lacking terminal punctuation get a period appended, or how adjacent block text is joined, so a correct implementation could produce different output for this input.
- missing: The docstring should state that a paragraph whose text does not end in punctuation gets a period appended, unless the following sibling element contains the code marker, in which case a colon is appended, and it should specify how text from adjacent block elements is joined in the output.

```python
def test_format_line_html_text_11(self):
    htmlutil = HtmlUtil()
    res = htmlutil.format_line_html_text('''<p>Some paragraph here</p><div>Some text here</div>''')
    self.assertEqual(res, '''Some paragraph here.Some text here''')
```

**test_format_line_html_text_12**: `unstated`
- reason: The docstring only describes replacing code blocks with the CODE tag and never mentions how list items are rendered, so a correct implementation could output "Item 1" without the "[-]" prefix or the added period that the test expects.
- missing: The docstring should state that each list item (li inside ul or ol) is prefixed with "[-]" and gets a trailing period appended unless it already ends in punctuation, and that empty items are skipped.

```python
def test_format_line_html_text_12(self):
    htmlutil = HtmlUtil()
    res = htmlutil.format_line_html_text('''<ul><li>Item 1</li></ul>''')
    self.assertEqual(res, '''[-]Item 1.''')
```

## Method `extract_code_from_html_text`

### Docstring

```python
def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
        """
```

### Reference code (`solution_code`)

```python
def extract_code_from_html_text(self, html_text):
        text_with_code_tag = self.format_line_html_text(html_text)

        if self.CODE_MARK not in text_with_code_tag:
            return []

        code_index_start = 0
        soup = BeautifulSoup(html_text, 'lxml')
        code_tag = soup.find_all(name=['pre', 'blockquote'])
        code_count = text_with_code_tag.count(self.CODE_MARK)
        code_list = []
        for code_index in range(code_index_start, code_index_start + code_count):
            code = code_tag[code_index].get_text()
            if code:
                code_list.append(code)
        return code_list
```

### Tests (`HtmlUtilTestExtractCodeFromHtmlText`)

**test_extract_code_from_html_text_1**: `stated`
- reason: The docstring's example uses the same HTML structure and gives the same two extracted code strings, including the preserved indentation, so a programmer following it would produce the expected output.

```python
def test_extract_code_from_html_text_1(self):
    htmlutil = HtmlUtil()
    res = htmlutil.extract_code_from_html_text('''
            <html>
            <body>
            <h1>Title</h1>
            <p>This is a paragraph.</p>
            <pre>print('Hello, world!')</pre>
            <p>Another paragraph.</p>
            <pre><code>for i in range(5):
            print(i)</code></pre>
            </body>
            </html>
            ''')
    self.assertEqual(res, ["print('Hello, world!')", 'for i in range(5):\n                print(i)'])
```

**test_extract_code_from_html_text_2**: `stated`
- reason: The docstring's example shows the method returning the text of each `<pre>` block (including a nested `<code>` block) in order, which is exactly what this test checks, so a programmer following it would pass.

```python
def test_extract_code_from_html_text_2(self):
    htmlutil = HtmlUtil()
    res = htmlutil.extract_code_from_html_text('''
            <html>
            <body>
            <h1>Title</h1>
            <p>This is a paragraph.</p>
            <pre>print('Hello, world!')</pre>
            <p>Another paragraph.</p>
            <pre><code>for i in range(4):
            print(i)</code></pre>
            </body>
            </html>
            ''')
    self.assertEqual(res, ["print('Hello, world!')", 'for i in range(4):\n                print(i)'])
```

**test_extract_code_from_html_text_3**: `stated`
- reason: The docstring's example shows the same behaviour the test checks: text inside `<pre>` tags (including `<code>` nested in `<pre>`) is returned as a list of code strings, with whitespace preserved.

```python
def test_extract_code_from_html_text_3(self):
    htmlutil = HtmlUtil()
    res = htmlutil.extract_code_from_html_text('''
            <html>
            <body>
            <h1>Title</h1>
            <p>This is a paragraph.</p>
            <pre>print('Hello, world!')</pre>
            <p>Another paragraph.</p>
            <pre><code>for i in range(3):
            print(i)</code></pre>
            </body>
            </html>
            ''')
    self.assertEqual(res, ["print('Hello, world!')", 'for i in range(3):\n                print(i)'])
```

**test_extract_code_from_html_text_4**: `stated`
- reason: The docstring's example uses the same structure (a plain `<pre>` and a `<pre><code>` block, with the inner text's indentation preserved), so a programmer following it would return the same two strings this test expects.

```python
def test_extract_code_from_html_text_4(self):
    htmlutil = HtmlUtil()
    res = htmlutil.extract_code_from_html_text('''
            <html>
            <body>
            <h1>Title</h1>
            <p>This is a paragraph.</p>
            <pre>print('Hello, world!')</pre>
            <p>Another paragraph.</p>
            <pre><code>for i in range(2):
            print(i)</code></pre>
            </body>
            </html>
            ''')
    self.assertEqual(res, ["print('Hello, world!')", 'for i in range(2):\n                print(i)'])
```

**test_extract_code_from_html_text_5**: `stated`
- reason: The docstring says the method returns the list of code found in the HTML, so a programmer would naturally return an empty list when the input contains no code, which is what this empty-input test expects.

```python
def test_extract_code_from_html_text_5(self):
    htmlutil = HtmlUtil()
    htmlutil.CODE_MARK = 'abcdefg'
    res = htmlutil.extract_code_from_html_text("")
    self.assertEqual(res, [])
```

## Tests in no method's test class

### `HtmlUtilTest`

**test_htmlutil**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
    def test_htmlutil(self):
        htmlutil = HtmlUtil()
        res = htmlutil.format_line_html_text('''
        <html>
        <body>
        <h1>Title</h1>
        <p>This is a paragraph.</p>
        <pre>print('Hello, world!')</pre>
        <p>Another paragraph.</p>
        <pre><code>for i in range(5):
        print(i)</code></pre>
        </body>
        </html>
        ''')
        self.assertEqual(res, '''
Title
This is a paragraph.
-CODE-
Another paragraph.
-CODE-
''')
        res = htmlutil.extract_code_from_html_text('''
                <html>
                <body>
                <h1>Title</h1>
                <p>This is a paragraph.</p>
                <pre>print('Hello, world!')</pre>
                <p>Another paragraph.</p>
                <pre><code>for i in range(5):
                print(i)</code></pre>
                </body>
                </html>
                ''')
        self.assertEqual(res, ["print('Hello, world!')", 'for i in range(5):\n                print(i)'])
```
