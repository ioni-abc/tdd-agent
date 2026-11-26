# ClassEval_29

## Skeleton (what the agent sees)

```python
from collections import Counter

class DataStatistics:
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
```

## Method `mean`

### Docstring

```python
def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
```

### Reference code (`solution_code`)

```python
def mean(self, data):
        return round(sum(data) / len(data), 2)
```

### Tests (`DataStatisticsTestMean`)

**test_mean_1**: `stated`
- reason: The docstring says the mean is computed and rounded to two decimal places, and its example gives 3.00 for [1, 2, 3, 4, 5], so a programmer following it would return 3.0 and pass the test.

```python
def test_mean_1(self):
    ds = DataStatistics()
    res = ds.mean([1, 2, 3, 4, 5])
    self.assertEqual(res, 3.00)
```

**test_mean_2**: `stated`
- reason: The docstring says the mean is the average rounded to two decimal places, so a programmer would compute sum/len rounded to 2 digits and get 3.5, matching the assertion.

```python
def test_mean_2(self):
    ds = DataStatistics()
    res = ds.mean([1, 2, 3, 4, 5, 6])
    self.assertEqual(res, 3.50)
```

**test_mean_3**: `stated`
- reason: A programmer reading "accurate to two digits after the Decimal separator" would compute the arithmetic mean and round it to two decimals, giving 4.17 for this input, which is what the test expects.

```python
def test_mean_3(self):
    ds = DataStatistics()
    res = ds.mean([1, 2, 4, 5, 6, 7])
    self.assertEqual(res, 4.17)
```

**test_mean_4**: `stated`
- reason: The docstring says the mean is accurate to two decimal places, so a programmer would compute 33/7 ≈ 4.714 and round it to 4.71, which is what the test expects.

```python
def test_mean_4(self):
    ds = DataStatistics()
    res = ds.mean([1, 2, 4, 5, 6, 7, 8])
    self.assertEqual(res, 4.71)
```

**test_mean_5**: `stated`
- reason: The docstring says the mean is rounded to two decimal places, and a programmer following it would compute 42/8 = 5.25, which matches the assertion.

```python
def test_mean_5(self):
    ds = DataStatistics()
    res = ds.mean([1, 2, 4, 5, 6, 7, 8, 9])
    self.assertEqual(res, 5.25)
```

## Method `median`

### Docstring

```python
def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
```

### Reference code (`solution_code`)

```python
def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            middle = n // 2
            return round((sorted_data[middle - 1] + sorted_data[middle]) / 2, 2)
        else:
            middle = n // 2
            return sorted_data[middle]
```

### Tests (`DataStatisticsTestMedian`)

**test_median_1**: `stated`
- reason: The docstring's own example is the same odd-length list with median 3, and it shows the result as 3.00, which equals the test's expected 3 under assertEqual.

```python
def test_median_1(self):
    ds = DataStatistics()
    res = ds.median([2, 5, 1, 3, 4])
    self.assertEqual(res, 3)
```

**test_median_2**: `stated`
- reason: The docstring asks for the median rounded to two decimal places, and the standard median of an even-length list is the mean of the two middle values, which is 3.5 here, so a programmer following it would pass.

```python
def test_median_2(self):
    ds = DataStatistics()
    res = ds.median([2, 5, 1, 3, 4, 6])
    self.assertEqual(res, 3.50)
```

**test_median_3**: `stated`
- reason: The docstring defines the median of a group of data, and a programmer applying the standard definition would average the two middle values for an even-length list, which is what the test expects (4.5 rounds to the same value as 4.50).

```python
def test_median_3(self):
    ds = DataStatistics()
    res = ds.median([2, 5, 1, 4, 6, 7])
    self.assertEqual(res, 4.5)
```

**test_median_4**: `stated`
- reason: The docstring defines the median of a group of data and gives an odd-length example returning 3.00, so a programmer would return 5.0 for this seven-element input, which equals the expected 5.

```python
def test_median_4(self):
    ds = DataStatistics()
    res = ds.median([2, 5, 1, 4, 6, 7, 8])
    self.assertEqual(res, 5)
```

**test_median_5**: `stated`
- reason: The docstring defines median and asks for a two-decimal result, and a programmer would take the standard median of an even-length list (the mean of the two middle values) to give 5.5, which is what the test expects.

```python
def test_median_5(self):
    ds = DataStatistics()
    res = ds.median([2, 5, 1, 4, 6, 7, 8, 9])
    self.assertEqual(res, 5.5)
```

## Method `mode`

### Docstring

```python
def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
```

### Reference code (`solution_code`)

```python
def mode(self, data):
        counter = Counter(data)
        mode_count = max(counter.values())
        mode = [x for x, count in counter.items() if count == mode_count]
        return mode
```

### Tests (`DataStatisticsTestMode`)

**test_mode_1**: `stated`
- reason: The docstring's example calls `mode([2, 2, 3, 3, 4])` and shows the output `[2, 3]`, which is exactly what the test asserts, so a programmer following the example would pass, even though the `:return:` line wrongly says float.

```python
def test_mode_1(self):
    ds = DataStatistics()
    res = ds.mode([2, 2, 3, 3, 4])
    self.assertEqual(res, [2, 3])
```

**test_mode_2**: `stated`
- reason: The docstring's example shows `mode` returning a list of all most-frequent values, so a programmer following it would return `[2]` for a single mode and pass, even though the `:return` line says float.

```python
def test_mode_2(self):
    ds = DataStatistics()
    res = ds.mode([2, 2, 2, 3, 3, 4])
    self.assertEqual(res, [2])
```

**test_mode_3**: `stated`
- reason: The docstring example shows that tied modes are returned together as a list (`[2, 3]`), so a programmer following it would return all values tied for the highest count and pass this test.

```python
def test_mode_3(self):
    ds = DataStatistics()
    res = ds.mode([2, 2, 3, 3, 4, 4])
    self.assertEqual(res, [2, 3, 4])
```

**test_mode_4**: `stated`
- reason: The docstring's example shows `mode` returning a list of all values tied for the highest count, so a programmer following it would return `[4]` for this input with a single most frequent value.

```python
def test_mode_4(self):
    ds = DataStatistics()
    res = ds.mode([2, 2, 3, 3, 4, 4, 4])
    self.assertEqual(res, [4])
```

**test_mode_5**: `stated`
- reason: The docstring's example returns a list of all values tied for the highest count, so a programmer following it would return `[4]` for this input, which is the single value with the highest count.

```python
def test_mode_5(self):
    ds = DataStatistics()
    res = ds.mode([2, 2, 3, 3, 4, 4, 4, 5])
    self.assertEqual(res, [4])
```

## Tests in no method's test class

### `DataStatisticsTest`

**test_datastatistics**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_datastatistics(self):
    ds = DataStatistics()
    res = ds.mean([1, 2, 3, 4, 5])
    self.assertEqual(res, 3.00)
    res = ds.median([2, 5, 1, 3, 4])
    self.assertEqual(res, 3.00)
    res = ds.mode([2, 2, 3, 3, 4])
    self.assertEqual(res, [2, 3])
```
