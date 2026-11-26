# ClassEval_68

## Skeleton (what the agent sees)

```python
class PageUtil:
    """
    PageUtil class is a versatile utility for handling pagination and search functionalities in an efficient and convenient manner.
    """

    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object with the given data and page size.
        :param data: list, the data to be paginated
        :param page_size: int, the number of items per page
        """
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size

    def get_page(self, page_number):
        """
        Retrieve a specific page of data.
        :param page_number: int, the page number to fetch
        :return: list, the data on the specified page
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page(1)
        [1]

        """


    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to fetch information about
        :return: dict, containing page information such as current page number, total pages, etc.
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page_info(1)
        >>> {
        >>>     "current_page": 1,
        >>>     "per_page": 1,
        >>>     "total_pages": 4,
        >>>     "total_items": 4,
        >>>     "has_previous": False,
        >>>     "has_next": True,
        >>>     "data": [1]
        >>> }

        """


    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.search("1")
        >>> search_info = {
        >>>     "keyword": "1",
        >>>     "total_results": 1,
        >>>     "total_pages": 1,
        >>>     "results": [1]
        >>> }
        """
```

## Method `get_page`

### Docstring

```python
def get_page(self, page_number):
        """
        Retrieve a specific page of data.
        :param page_number: int, the page number to fetch
        :return: list, the data on the specified page
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page(1)
        [1]

        """
```

### Reference code (`solution_code`)

```python
def get_page(self, page_number):
        if page_number < 1 or page_number > self.total_pages:
            return []

        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]
```

### Tests (`PageUtilTestGetPage`)

setUp (runs before each test):

```python
def setUp(self):
    self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.page_size = 3
    self.page_util = PageUtil(self.data, self.page_size)
```

**test_get_page_1**: `stated`
- reason: A programmer reading the docstring and its example (page 1 of a list with page size 1 returns the first element) would naturally return the first page-sized slice, which is what this test checks with page size 3.

```python
def test_get_page_1(self):
    page_number = 1
    expected_page = [1, 2, 3]
    actual_page = self.page_util.get_page(page_number)
    self.assertEqual(actual_page, expected_page)
```

**test_get_page_2**: `stated`
- reason: The docstring says get_page returns a specific page of data, and its example with a page size of 1 shows 1-indexed pages of the constructor's page size, so a programmer would slice page 2 of size 3 to get [4, 5, 6].

```python
def test_get_page_2(self):
    page_number = 2
    expected_page = [4, 5, 6]
    actual_page = self.page_util.get_page(page_number)
    self.assertEqual(actual_page, expected_page)
```

**test_get_page_3**: `stated`
- reason: The docstring's example (page size 1 from the constructor, page 1 returns `[1]`) shows that pages are fixed-size slices of the data, so a programmer would compute page 3 of size 3 as `[7, 8, 9]`.

```python
def test_get_page_3(self):
    page_number = 3
    expected_page = [7, 8, 9]
    actual_page = self.page_util.get_page(page_number)
    self.assertEqual(actual_page, expected_page)
```

**test_get_page_4**: `stated`
- reason: The docstring says get_page returns the data on the specified page, so a programmer would slice the data by page size and naturally return the short remainder [10] for page 4.

```python
def test_get_page_4(self):
    page_number = 4
    expected_page = [10]
    actual_page = self.page_util.get_page(page_number)
    self.assertEqual(actual_page, expected_page)
```

**test_get_page_5**: `unstated`
- reason: The docstring describes fetching a page but says nothing about what happens for a page number below 1, so a programmer could reasonably return something other than an empty list (for example, a negative-index slice) and fail this test.
- missing: The docstring should state what is returned when the requested page number is out of range (less than 1 or beyond the last page), such as an empty list.

```python
def test_get_page_5(self):
    invalid_page_number = 0
    empty_page = []
    actual_page = self.page_util.get_page(invalid_page_number)
    self.assertEqual(actual_page, empty_page)
```

## Method `get_page_info`

### Docstring

```python
def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to fetch information about
        :return: dict, containing page information such as current page number, total pages, etc.
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page_info(1)
        >>> {
        >>>     "current_page": 1,
        >>>     "per_page": 1,
        >>>     "total_pages": 4,
        >>>     "total_items": 4,
        >>>     "has_previous": False,
        >>>     "has_next": True,
        >>>     "data": [1]
        >>> }

        """
```

### Reference code (`solution_code`)

```python
def get_page_info(self, page_number):
        if page_number < 1 or page_number > self.total_pages:
            return {}

        start_index = (page_number - 1) * self.page_size
        end_index = min(start_index + self.page_size, self.total_items)
        page_data = self.data[start_index:end_index]

        page_info = {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": page_number > 1,
            "has_next": page_number < self.total_pages,
            "data": page_data
        }
        return page_info
```

### Tests (`PageUtilTestGetPageInfo`)

setUp (runs before each test):

```python
def setUp(self):
    self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.page_size = 3
    self.page_util = PageUtil(self.data, self.page_size)
```

**test_get_page_info_1**: `stated`
- reason: The docstring's example shows the full key set and the meaning of each field (current page, per-page size, totals, has_previous/has_next, page data), so a programmer would produce the expected dict for page 2 of 10 items at 3 per page.

```python
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
```

**test_get_page_info_2**: `stated`
- reason: The docstring's example shows the same dict keys and semantics (per-page slice, has_previous/has_next, total_pages, total_items), so a programmer following it would reasonably produce the expected dict for page 1.

```python
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
```

**test_get_page_info_3**: `stated`
- reason: The docstring's example and its description of per-page information (current page, per-page size, total pages and items, has_previous/has_next flags, page data) let a programmer derive the expected dict for page 3 of 10 items at 3 per page, including the middle-page previous/next flags and the sliced data.

```python
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
```

**test_get_page_info_4**: `stated`
- reason: The docstring's example spells out the exact keys and their meanings (current page, per-page size, total pages and items, has_previous/has_next, and the data slice), so a programmer following it would produce this result for page 4 of 10 items with page size 3.

```python
def test_get_page_info_4(self):
    page_number = 4
    expected_info = {
        "current_page": 4,
        "per_page": 3,
        "total_pages": 4,
        "total_items": 10,
        "has_previous": True,
        "has_next": False,
        "data": [10]
    }
    actual_info = self.page_util.get_page_info(page_number)
    self.assertEqual(actual_info, expected_info)
```

**test_get_page_info_5**: `unstated`
- reason: The docstring only describes the return value for a valid page, so a programmer could reasonably return None, raise an error, or return a dict with empty data for an out-of-range page, while the test expects an empty dict.
- missing: The docstring should say what is returned when the requested page number is outside the valid range (below 1 or above the total number of pages), for example an empty dict.

```python
def test_get_page_info_5(self):
    invalid_page_number = 5
    empty_info = {}
    actual_info = self.page_util.get_page_info(invalid_page_number)
    self.assertEqual(actual_info, empty_info)
```

## Method `search`

### Docstring

```python
def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.search("1")
        >>> search_info = {
        >>>     "keyword": "1",
        >>>     "total_results": 1,
        >>>     "total_pages": 1,
        >>>     "results": [1]
        >>> }
        """
```

### Reference code (`solution_code`)

```python
def search(self, keyword):
        results = [item for item in self.data if keyword in str(item)]
        num_results = len(results)
        num_pages = (num_results + self.page_size - 1) // self.page_size

        search_info = {
            "keyword": keyword,
            "total_results": num_results,
            "total_pages": num_pages,
            "results": results
        }
        return search_info
```

### Tests (`PageUtilTestSearch`)

setUp (runs before each test):

```python
def setUp(self):
    self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.page_size = 3
    self.page_util = PageUtil(self.data, self.page_size)
```

**test_search_1**: `unstated`
- reason: The docstring says to return items that "contain" the keyword, which a programmer could read as exact equality, so an implementation matching only the item 1 would fail the test's expectation that 10 also matches.
- missing: The docstring should state that matching is a substring test on each item's string form (so a number matches when its digits contain the keyword), and that total_pages is the ceiling of matching results divided by the page size.

```python
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
```

**test_search_2**: `stated`
- reason: The docstring says search returns items containing the keyword, and its example with the string "1" matching the integer 1 shows the same str-based matching the test relies on for "2" matching 2.

```python
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
```

**test_search_3**: `stated`
- reason: The docstring says search returns items containing the keyword with total results and matching items, and its example shows string-based matching on integers, so a programmer would expect `[3]` with one result for "3".

```python
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
```

**test_search_4**: `stated`
- reason: The docstring says search returns items containing the keyword, with total results and matching items, and the example shows the dict keys, so a programmer would produce the same keyword, count, pages and results for "4".

```python
def test_search_4(self):
    keyword = "4"
    expected_results = {
        "keyword": "4",
        "total_results": 1,
        "total_pages": 1,
        "results": [4]
    }
    actual_results = self.page_util.search(keyword)
    self.assertEqual(actual_results, expected_results)
```

**test_search_5**: `unstated`
- reason: The docstring's example only covers a case with one matching result, so a programmer could reasonably give total_pages as 1 (or otherwise non-zero) when nothing matches, while the test expects 0.
- missing: The docstring should state how total_pages is computed when no items match the keyword, for example whether it is 0 or at least 1 and what results is in that case.

```python
def test_search_5(self):
    keyword = "11"
    expected_results = {
        "keyword": "11",
        "total_results": 0,
        "total_pages": 0,
        "results": []
    }
    actual_results = self.page_util.search(keyword)
    self.assertEqual(actual_results, expected_results)
```

## Tests in no method's test class

### `PageUtilTest`

setUp (runs before each test):

```python
def setUp(self):
    self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.page_size = 3
    self.page_util = PageUtil(self.data, self.page_size)
```

**test_pageutil**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_pageutil(self):
    page_number = 1
    expected_page = [1, 2, 3]
    actual_page = self.page_util.get_page(page_number)
    self.assertEqual(actual_page, expected_page)

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

    keyword = "4"
    expected_results = {
        "keyword": "4",
        "total_results": 1,
        "total_pages": 1,
        "results": [4]
    }
    actual_results = self.page_util.search(keyword)
    self.assertEqual(actual_results, expected_results)
```
