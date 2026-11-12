import re
import string
import gensim
from bs4 import BeautifulSoup, NavigableString, Comment


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
        return re.sub(r'\n+', '\n', text)

    def _render_node(self, node):
        """
        Recursively render the children of a node into plain text,
        replacing code blocks with the code mark.
        :param node: bs4 tag or soup object
        :return: string
        """
        parts = []
        for child in node.children:
            if isinstance(child, Comment):
                continue
            if isinstance(child, NavigableString):
                text = str(child)
                if text.strip() == '':
                    parts.append('\n')
                else:
                    parts.append(text)
                continue

            name = child.name
            if name == 'pre':
                parts.append(self.CODE_MARK)
            elif name == 'p':
                content = self._render_node(child).strip()
                if content:
                    if content[-1] not in '.!?':
                        content += '.'
                    parts.append(content)
            elif name == 'li':
                content = self._render_node(child).strip()
                if content:
                    if content[-1] not in '.!?':
                        content += '.'
                    parts.append('[-]' + content)
            else:
                parts.append(self._render_node(child))
        return ''.join(parts)

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
        soup = BeautifulSoup(html_text, 'html.parser')
        result = self._render_node(soup)
        return self.__format_line_feed(result)

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
        soup = BeautifulSoup(html_text, 'html.parser')
        return [pre.get_text() for pre in soup.find_all('pre')]