# ClassEval_90

## Skeleton (what the agent sees)

```python
class URLHandler:
    """
    The class supports to handle URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        self.url = url

    def get_scheme(self):
        """
        get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """


    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """


    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """


    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """


    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
```

## Method `get_scheme`

### Docstring

```python
def get_scheme(self):
        """
        get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """
```

### Reference code (`solution_code`)

```python
def get_scheme(self):
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            return self.url[:scheme_end]
        return None
```

### Tests (`URLHandlerTestGetScheme`)

**test_get_scheme_1**: `stated`
- reason: The docstring says get_scheme returns the scheme of the URL and gives the example "https" for an https URL, which matches the test's expected value "https".

```python
def test_get_scheme_1(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    temp = urlhandler.get_scheme()
    self.assertEqual(temp, "https")
```

**test_get_scheme_2**: `stated`
- reason: The docstring says get_scheme returns the scheme of the URL and its example gives "https" for an https URL, which is exactly what this test checks.

```python
def test_get_scheme_2(self):
    urlhandler = URLHandler(
        "https://www.bing.com/search?pglt=41&q=humaneval&cvid=4dc2da2bb4bc429eb498c85245ae5253&aqs=edge.0.0l7j69i61j69i60.10008j0j1&FORM=ANNTA1&PC=U531&mkt=zh-CN")
    temp = urlhandler.get_scheme()
    self.assertEqual(temp, "https")
```

**test_get_scheme_3**: `stated`
- reason: The docstring says get_scheme returns the scheme of the URL and gives an https example, so a programmer would return the text before "://", which is what this test expects.

```python
def test_get_scheme_3(self):
    urlhandler = URLHandler("https://github.com/openai/human-eval")
    temp = urlhandler.get_scheme()
    self.assertEqual(temp, "https")
```

**test_get_scheme_4**: `stated`
- reason: The docstring says get_scheme returns the scheme of the URL, and a programmer would take the text before "://" as the scheme, which gives "aaa" for this test's custom scheme.

```python
def test_get_scheme_4(self):
    urlhandler = URLHandler("aaa://github.com/openai/human-eval")
    temp = urlhandler.get_scheme()
    self.assertEqual(temp, "aaa")
```

**test_get_scheme_5**: `stated`
- reason: The docstring says get_scheme returns the scheme of the URL, and a programmer would take the text before "://", which gives "bbb" for this non-http scheme.

```python
def test_get_scheme_5(self):
    urlhandler = URLHandler("bbb://github.com/openai/human-eval")
    temp = urlhandler.get_scheme()
    self.assertEqual(temp, "bbb")
```

**test_get_scheme_6**: `unstated`
- reason: The docstring only says what happens "if successful" and never says what to return when the URL has no scheme, so a reasonable implementation could return an empty string or raise instead of None.
- missing: The docstring should state the return value when the URL has no scheme separator (for example, that it returns None when the input lacks the "://" delimiter).

```python
def test_get_scheme_6(self):
    urlhandler = URLHandler("abcdefg")
    temp = urlhandler.get_scheme()
    self.assertIsNone(temp)
```

## Method `get_host`

### Docstring

```python
def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
```

### Reference code (`solution_code`)

```python
def get_host(self):
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            url_without_scheme = self.url[scheme_end + 3:]
            host_end = url_without_scheme.find("/")
            if host_end != -1:
                return url_without_scheme[:host_end]
            return url_without_scheme
        return None
```

### Tests (`URLHandlerTestGetHost`)

**test_get_host_1**: `stated`
- reason: The docstring's example uses the same URL and expects "www.baidu.com" as the host domain name, so a programmer following it would return the same value the test checks.

```python
def test_get_host_1(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    temp = urlhandler.get_host()
    self.assertEqual(temp, "www.baidu.com")
```

**test_get_host_2**: `stated`
- reason: The docstring says get_host returns the host domain name of the URL, and its example shows a full URL with a path and query string yielding just the domain, so a programmer would extract the text between the scheme and the next slash, which is what this test expects.

```python
def test_get_host_2(self):
    urlhandler = URLHandler(
        "https://www.bing.com/search?pglt=41&q=humaneval&cvid=4dc2da2bb4bc429eb498c85245ae5253&aqs=edge.0.0l7j69i61j69i60.10008j0j1&FORM=ANNTA1&PC=U531&mkt=zh-CN")
    temp = urlhandler.get_host()
    self.assertEqual(temp, "www.bing.com")
```

**test_get_host_3**: `stated`
- reason: The docstring says get_host returns the host domain name of the URL, so a programmer would extract the text between the scheme and the next slash, which yields "github.com" for this test's URL.

```python
def test_get_host_3(self):
    urlhandler = URLHandler("https://github.com/openai/human-eval")
    temp = urlhandler.get_host()
    self.assertEqual(temp, "github.com")
```

**test_get_host_4**: `stated`
- reason: A programmer following the docstring would extract the host domain between the scheme and the first path slash, which is what this test checks for an https URL with a path, and the docstring example shows the same pattern.

```python
def test_get_host_4(self):
    urlhandler = URLHandler("https://aaa.com/openai/human-eval")
    temp = urlhandler.get_host()
    self.assertEqual(temp, "aaa.com")
```

**test_get_host_5**: `stated`
- reason: A programmer reading "host domain name of the URL" with the example `https://www.baidu.com/...` would extract the text between `://` and the next `/`, which is what the test checks for `https://bbb.com/openai/human-eval`.

```python
def test_get_host_5(self):
    urlhandler = URLHandler("https://bbb.com/openai/human-eval")
    temp = urlhandler.get_host()
    self.assertEqual(temp, "bbb.com")
```

**test_get_host_6**: `unstated`
- reason: The docstring only describes the success case of returning the host, so a programmer could reasonably return the whole string, an empty value, or raise for a URL without a scheme, while the test expects None.
- missing: The docstring should say what the method returns when the URL has no "://" scheme separator, for example that it returns None in that case.

```python
def test_get_host_6(self):
    urlhandler = URLHandler("abcdefg")
    temp = urlhandler.get_host()
    self.assertIsNone(temp)
```

**test_get_host_7**: `stated`
- reason: The docstring says the method returns the host domain name of the URL, and for "https://bbb.com" a programmer would naturally return "bbb.com", which matches the test and the reference code.

```python
def test_get_host_7(self):
    urlhandler = URLHandler("https://bbb.com")
    temp = urlhandler.get_host()
    self.assertEqual(temp, "bbb.com")
```

**test_get_host_8**: `stated`
- reason: The docstring says get_host returns the host domain name of the URL, so a programmer would take the text between the scheme and the first slash and return "bbb.com" for this trailing-slash URL.

```python
def test_get_host_8(self):
    urlhandler = URLHandler("https://bbb.com/")
    temp = urlhandler.get_host()
    self.assertEqual(temp, "bbb.com")
```

## Method `get_path`

### Docstring

```python
def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
```

### Reference code (`solution_code`)

```python
def get_path(self):
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            url_without_scheme = self.url[scheme_end + 3:]
            host_end = url_without_scheme.find("/")
            if host_end != -1:
                return url_without_scheme[host_end:]
        return None
```

### Tests (`URLHandlerTestGetPath`)

**test_get_path_1**: `stated`
- reason: The docstring's own example uses the same URL and expects "/s?wd=aaa&rsv_spt=1#page", so a programmer following it would return the path with its query and fragment and pass this test.

```python
def test_get_path_1(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    temp = urlhandler.get_path()
    self.assertEqual(temp, "/s?wd=aaa&rsv_spt=1#page")
```

**test_get_path_2**: `stated`
- reason: The docstring's example shows the expected output for a URL with a query string as everything after the host, which is what this test checks, so a programmer following it would return the same path with query.

```python
def test_get_path_2(self):
    urlhandler = URLHandler(
        "https://www.bing.com/search?pglt=41&q=humaneval&cvid=4dc2da2bb4bc429eb498c85245ae5253&aqs=edge.0.0l7j69i61j69i60.10008j0j1&FORM=ANNTA1&PC=U531&mkt=zh-CN")
    temp = urlhandler.get_path()
    self.assertEqual(temp,
                     "/search?pglt=41&q=humaneval&cvid=4dc2da2bb4bc429eb498c85245ae5253&aqs=edge.0.0l7j69i61j69i60.10008j0j1&FORM=ANNTA1&PC=U531&mkt=zh-CN")
```

**test_get_path_3**: `stated`
- reason: The docstring says get_path returns everything after the host, starting at the first slash, and its example shows that convention, so a programmer following it would return "/openai/human-eval" for this input.

```python
def test_get_path_3(self):
    urlhandler = URLHandler("https://github.com/openai/human-eval")
    temp = urlhandler.get_path()
    self.assertEqual(temp, "/openai/human-eval")
```

**test_get_path_4**: `stated`
- reason: The docstring says get_path returns the resource address from the third part of the URL, and its example shows the leading slash and everything after the host, which is what this test expects for a plain URL with a path.

```python
def test_get_path_4(self):
    urlhandler = URLHandler("https://github.com/aaa/human-eval")
    temp = urlhandler.get_path()
    self.assertEqual(temp, "/aaa/human-eval")
```

**test_get_path_5**: `stated`
- reason: The docstring says get_path returns the resource address after the host, and its example shows the path starting at the first slash after the host, which is exactly what this test checks.

```python
def test_get_path_5(self):
    urlhandler = URLHandler("https://github.com/bbb/human-eval")
    temp = urlhandler.get_path()
    self.assertEqual(temp, "/bbb/human-eval")
```

**test_get_path_6**: `unstated`
- reason: The docstring says only "If successful, return the address," so a programmer would not know that a URL without a scheme separator should yield None, and a reasonable implementation could raise an error or return an empty string instead.
- missing: The docstring should say that the method returns None when the URL has no scheme separator or no path component after the host.

```python
def test_get_path_6(self):
    urlhandler = URLHandler("abcdefg")
    temp = urlhandler.get_path()
    self.assertIsNone(temp)
```

## Method `get_query_params`

### Docstring

```python
def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """
```

### Reference code (`solution_code`)

```python
def get_query_params(self):
        query_start = self.url.find("?")
        fragment_start = self.url.find("#")
        if query_start != -1:
            query_string = self.url[query_start + 1:fragment_start]
            params = {}
            if len(query_string) > 0:
                param_pairs = query_string.split("&")
                for pair in param_pairs:
                    key_value = pair.split("=")
                    if len(key_value) == 2:
                        key, value = key_value
                        params[key] = value
            return params
        return None
```

### Tests (`URLHandlerTestGetQueryParams`)

**test_get_query_params_1**: `stated`
- reason: The docstring's example uses the same URL shape (query string followed by a fragment) and shows the same expected dict, so a programmer following it would return the parsed key-value pairs and pass.

```python
def test_get_query_params_1(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    temp = urlhandler.get_query_params()
    self.assertEqual(temp, {"wd": "aaa", "rsv_spt": "1"})
```

**test_get_query_params_2**: `stated`
- reason: The docstring says the method returns the URL's request parameters as a dict, and the test checks that a plain query string with several key=value pairs and an empty trailing fragment is parsed into exactly those pairs, which a programmer would implement from that description.

```python
def test_get_query_params_2(self):
    urlhandler = URLHandler(
        "https://www.bing.com/search?pglt=41&q=humaneval&cvid=4dc2da2bb4bc429eb498c85245ae5253&aqs=edge.0.0l7j69i61j69i60.10008j0j1&FORM=ANNTA1&PC=U531#")
    temp = urlhandler.get_query_params()
    self.assertEqual(temp, {"pglt": "41", "q": "humaneval", "cvid": "4dc2da2bb4bc429eb498c85245ae5253",
                            "aqs": "edge.0.0l7j69i61j69i60.10008j0j1", "FORM": "ANNTA1", "PC": "U531"})
```

**test_get_query_params_3**: `unstated`
- reason: The docstring only describes the success case and says nothing about what to return when the URL has no query string, so a programmer could reasonably return an empty dict instead of None, which this test expects.
- missing: The docstring should state the return value when the URL has no "?" query part (for example, whether it returns None or an empty dict).

```python
def test_get_query_params_3(self):
    urlhandler = URLHandler("https://github.com/openai/human-eval")
    temp = urlhandler.get_query_params()
    self.assertEqual(temp, None)
```

**test_get_query_params_4**: `stated`
- reason: The docstring's example parses the query string `wd=aaa&rsv_spt=1` into a dict of key/value strings, which is the same behaviour this test checks with `bbb` in place of `aaa`.

```python
def test_get_query_params_4(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=bbb&rsv_spt=1#page")
    temp = urlhandler.get_query_params()
    self.assertEqual(temp, {"wd": "bbb", "rsv_spt": "1"})
```

**test_get_query_params_5**: `stated`
- reason: The docstring's example parses the query string after "?" and before "#" into a dict of string key/value pairs, which is exactly what this test checks with different values.

```python
def test_get_query_params_5(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=ccc&rsv_spt=1#page")
    temp = urlhandler.get_query_params()
    self.assertEqual(temp, {"wd": "ccc", "rsv_spt": "1"})
```

**test_get_query_params_6**: `unstated`
- reason: The test expects an empty dict for a query string containing only an empty `&` separator, but the docstring never says how empty or malformed `&`-separated segments are handled, so a reasonable implementation might produce an entry like `{"": ""}` instead.
- missing: The docstring should say that query segments lacking a `key=value` form (such as empty segments between `&` separators or segments with no `=`) are skipped, and that an empty query string yields an empty dict.

```python
def test_get_query_params_6(self):
    urlhandler = URLHandler("https://www.baidu.com/s?&#page")
    temp = urlhandler.get_query_params()
    self.assertEqual(temp, {})
```

## Method `get_fragment`

### Docstring

```python
def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
```

### Reference code (`solution_code`)

```python
def get_fragment(self):
        fragment_start = self.url.find("#")
        if fragment_start != -1:
            return self.url[fragment_start + 1:]
        return None
```

### Tests (`URLHandlerTestGetFragment`)

**test_get_fragment_1**: `stated`
- reason: The docstring says the method returns the part after '#' in the URL, and the test checks that a URL ending in "#page" yields "page", which a programmer would implement directly.

```python
def test_get_fragment_1(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    temp = urlhandler.get_fragment()
    self.assertEqual(temp, "page")
```

**test_get_fragment_2**: `unstated`
- reason: The docstring only describes the success case (returning the text after '#'), so a programmer would not know that a URL with no '#' should return None; returning an empty string or raising an error would be equally plausible.
- missing: The docstring should say what is returned when the URL contains no '#' character, for example that it returns None in that case.

```python
def test_get_fragment_2(self):
    urlhandler = URLHandler(
        "https://www.bing.com/search?pglt=41&q=humaneval&cvid=4dc2da2bb4bc429eb498c85245ae5253&aqs=edge.0.0l7j69i61j69i60.10008j0j1&FORM=ANNTA1&PC=U531&mkt=zh-CN")
    temp = urlhandler.get_fragment()
    self.assertEqual(temp, None)
```

**test_get_fragment_3**: `stated`
- reason: The docstring says get_fragment returns the text after '#' in the URL, and the test checks a URL with fragment "aaa" expecting "aaa", which a programmer following the docstring would produce.

```python
def test_get_fragment_3(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#aaa")
    temp = urlhandler.get_fragment()
    self.assertEqual(temp, "aaa")
```

**test_get_fragment_4**: `stated`
- reason: The docstring says get_fragment returns the text after '#' in the URL, and the test checks a URL with "#bbb" expecting "bbb", which a programmer following the docstring would produce.

```python
def test_get_fragment_4(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#bbb")
    temp = urlhandler.get_fragment()
    self.assertEqual(temp, "bbb")
```

**test_get_fragment_5**: `stated`
- reason: The docstring says the method returns the part of the URL after '#', which is exactly what the test checks when the URL ends in "#ccc" and expects "ccc".

```python
def test_get_fragment_5(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#ccc")
    temp = urlhandler.get_fragment()
    self.assertEqual(temp, "ccc")
```

## Tests in no method's test class

### `URLHandlerTest`

**test_urlhandler**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_urlhandler(self):
    urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
    temp = urlhandler.get_scheme()
    self.assertEqual(temp, "https")
    temp = urlhandler.get_host()
    self.assertEqual(temp, "www.baidu.com")
    temp = urlhandler.get_path()
    self.assertEqual(temp, "/s?wd=aaa&rsv_spt=1#page")
    temp = urlhandler.get_query_params()
    self.assertEqual(temp, {"wd": "aaa", "rsv_spt": "1"})
    temp = urlhandler.get_fragment()
    self.assertEqual(temp, "page")
```
