# ClassEval_31

## Skeleton (what the agent sees)

```python
import math

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """


    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data,list.
        :param data2: The second set of data,list.
        :return: The correlation coefficient, float.
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007

        """

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
        [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]

        """
```

## Method `correlation_coefficient`

### Docstring

```python
def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data,list.
        :param data2: The second set of data,list.
        :return: The correlation coefficient, float.
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """
```

### Reference code (`solution_code`)

```python
def correlation_coefficient(data1, data2):
        n = len(data1)
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n

        numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        denominator = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n))) * math.sqrt(sum((data2[i] - mean2) ** 2 for i in range(n)))

        return numerator / denominator if denominator != 0 else 0
```

### Tests (`DataStatistics4TestCorrelationCoefficient`)

**test_correlation_coefficient**: `stated`
- reason: The docstring's example gives the same input and the exact expected float (0.9999999999999998), so a programmer following it would match the test.

```python
def test_correlation_coefficient(self):
    self.assertEqual(DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6]), 0.9999999999999998)
```

**test_correlation_coefficient_2**: `unstated`
- reason: The docstring defines the correlation coefficient but says nothing about inputs with zero variance, where the formula divides by zero, so a programmer could raise an error or return NaN instead of the 0 the test expects.
- missing: The docstring should state what is returned when either input has zero variance (all values identical), for example that the function returns 0 instead of dividing by zero.

```python
def test_correlation_coefficient_2(self):
    self.assertEqual(DataStatistics4.correlation_coefficient([1, 1, 1], [2, 2, 2]), 0)
```

**test_correlation_coefficient_3**: `stated`
- reason: The docstring example gives the same floating-point result (0.9999999999999998) for another perfectly correlated pair, so a programmer using the standard Pearson formula would produce the value this test expects.

```python
def test_correlation_coefficient_3(self):
    self.assertEqual(DataStatistics4.correlation_coefficient([1, 2, 3], [1, 2, 3]), 0.9999999999999998)
```

**test_correlation_coefficient_4**: `stated`
- reason: The docstring asks for the correlation coefficient of two lists, which a programmer would implement as the standard Pearson coefficient, and that is exactly what this test checks for the given inputs.

```python
def test_correlation_coefficient_4(self):
    self.assertAlmostEqual(DataStatistics4.correlation_coefficient([1, 2, 3], [1, 2, 4]), 0.9819805060619659)
```

**test_correlation_coefficient_5**: `unstated`
- reason: The docstring names only the Pearson correlation, but this test's exact float expectation depends on the reference's specific arithmetic order, so a correct implementation that returns the mathematically exact value could fail the equality check.
- missing: The docstring should state the exact formula or rounding convention for float outputs (for example, whether results are rounded or computed in a particular order), so that exact-equality checks on float results are implementable from the docstring alone.

```python
def test_correlation_coefficient_5(self):
    self.assertEqual(DataStatistics4.correlation_coefficient([1, 2, 3], [1, 5, 3]), 0.4999999999999999)
```

## Method `skewness`

### Docstring

```python
@staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def skewness(data):
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std_deviation = math.sqrt(variance)

        skewness = sum((x - mean) ** 3 for x in data) * n / ((n - 1) * (n - 2) * std_deviation ** 3) if std_deviation != 0 else 0

        return skewness
```

### Tests (`DataStatistics4TestSkewness`)

**test_skewness**: `stated`
- reason: The docstring's example `skewness([1, 2, 5])` returns 2.3760224064818463, which is the exact value the test asserts, so a programmer matching the documented example would pass.

```python
def test_skewness(self):
    self.assertEqual(DataStatistics4.skewness([1, 2, 5]), 2.3760224064818463)
```

**test_skewness_2**: `unstated`
- reason: The test expects skewness of constant data (zero standard deviation, which makes the formula divide by zero) to return 0, and the docstring says nothing about this edge case, so a standard implementation could fail.
- missing: The docstring should say what to return when all values are equal (zero spread), since the skewness formula is otherwise undefined, for example that it returns 0 in that case.

```python
def test_skewness_2(self):
    self.assertEqual(DataStatistics4.skewness([1, 1, 1]), 0)
```

**test_skewness_3**: `stated`
- reason: The docstring asks for the skewness of the data, and any skewness formula yields 0 for the symmetric input [1, 2, 3] (deviations from the mean cancel), so a programmer following it would pass.

```python
def test_skewness_3(self):
    self.assertEqual(DataStatistics4.skewness([1, 2, 3]), 0)
```

**test_skewness_4**: `stated`
- reason: The docstring's example value for [1, 2, 5] pins down the adjusted Fisher-Pearson formula with the (n-1)(n-2) correction and population standard deviation, which is the same convention the test's expected value for [1, 2, 4] relies on.

```python
def test_skewness_4(self):
    self.assertEqual(DataStatistics4.skewness([1, 2, 4]), 1.7181079837227264)
```

**test_skewness_5**: `stated`
- reason: The docstring asks for the skewness of the data, and for symmetric data (mean 3, deviations -2, 2, 0) the cubed deviations sum to zero, so any correct skewness implementation returns 0.0.

```python
def test_skewness_5(self):
    self.assertEqual(DataStatistics4.skewness([1, 5, 3]), 0.0)
```

## Method `kurtosis`

### Docstring

```python
@staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def kurtosis(data):

        n = len(data)
        mean = sum(data) / n
        std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / n)

        if std_dev == 0:
            return math.nan

        centered_data = [(x - mean) for x in data]
        fourth_moment = sum(x ** 4 for x in centered_data) / n

        kurtosis_value = (fourth_moment / std_dev ** 4) - 3

        return kurtosis_value
```

### Tests (`DataStatistics4TestKurtosis`)

**test_kurtosis**: `unstated`
- reason: The docstring's example fixes the convention only loosely, and the test's exact-equality check on a floating-point result depends on the specific computation order, which the docstring does not specify.
- missing: The docstring should state the exact formula used (for example, excess kurtosis with population moments, divided by n, minus 3) and the order of operations, so that an implementation following it reproduces the same floating-point value.

```python
def test_kurtosis(self):
    self.assertEqual(DataStatistics4.kurtosis([1, 2, 5]), -1.5000000000000002)
```

**test_kurtosis_2**: `unstated`
- reason: The docstring gives only the general kurtosis definition and a sample value, so a programmer would not know that a constant dataset (zero standard deviation) should return NaN rather than raising a division error.
- missing: The docstring should state what is returned when all values are identical (zero variance), for example that it returns NaN instead of raising a division-by-zero error.

```python
def test_kurtosis_2(self):
    self.assertTrue(math.isnan(DataStatistics4.kurtosis([1, 1, 1])))
```

**test_kurtosis_3**: `unstated`
- reason: The docstring's example pins down population excess kurtosis, but the test's exact float result depends on the order of floating-point operations, which the docstring does not specify, so a correct implementation could return a value that differs in the last digits and fail `assertEqual`.
- missing: The docstring should state the rounding or precision expected for float results, or that results are compared with a tolerance, so that any correct formula with different floating-point evaluation order is not rejected by exact equality.

```python
def test_kurtosis_3(self):
    self.assertEqual(DataStatistics4.kurtosis([1, 2, 3]), -1.5000000000000002)
```

**test_kurtosis_4**: `stated`
- reason: The docstring's example for [1, 20, 100] gives -1.5 under the population, excess-kurtosis formula that the test also uses, so a programmer following it would produce -1.5 for [1, 2, 4] up to floating-point rounding.

```python
def test_kurtosis_4(self):
    self.assertEqual(DataStatistics4.kurtosis([1, 2, 4]), -1.4999999999999996)
```

**test_kurtosis_5**: `stated`
- reason: The docstring's example for [1, 20, 100] returns about -1.5 using the same population excess-kurtosis formula as the reference, so a programmer following it would compute the same quantity this test checks.

```python
def test_kurtosis_5(self):
    self.assertEqual(DataStatistics4.kurtosis([1, 5, 3]), -1.5000000000000002)
```

## Method `pdf`

### Docstring

```python
@staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
        [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def pdf(data, mu, sigma):
        pdf_values = [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]
        return pdf_values
```

### Tests (`DataStatistics4TestPDF`)

**test_pdf**: `stated`
- reason: The docstring's doctest gives the exact expected output for `pdf([1, 2, 3], 1, 1)`, which is the same input and output the test checks, so a programmer following the normal density formula and matching the example would pass.

```python
def test_pdf(self):
    self.assertEqual(DataStatistics4.pdf([1, 2, 3], 1, 1),
                     [0.3989422804014327, 0.24197072451914337, 0.05399096651318806])
```

**test_pdf_2**: `stated`
- reason: The docstring gives the normal PDF and an example that fixes the formula, so a programmer would compute 1/(sigma*sqrt(2*pi)) at x equal to mu, which is exactly what the test expects.

```python
def test_pdf_2(self):
    self.assertEqual(DataStatistics4.pdf([1, 1, 1], 1, 1),
                     [0.3989422804014327, 0.3989422804014327, 0.3989422804014327])
```

**test_pdf_3**: `stated`
- reason: The docstring defines the output as the normal-distribution PDF evaluated at each data point, which is exactly what the test checks: mu=2 and sigma=1 give the symmetric values expected for inputs 1, 2, 3.

```python
def test_pdf_3(self):
    self.assertEqual(DataStatistics4.pdf([1, 2, 3], 2, 1),
                     [0.24197072451914337, 0.3989422804014327, 0.24197072451914337])
```

**test_pdf_4**: `stated`
- reason: The docstring defines the output as the normal PDF with mean mu and standard deviation sigma, so a programmer would implement the standard Gaussian density, which gives the expected values for sigma=2.

```python
def test_pdf_4(self):
    self.assertEqual(DataStatistics4.pdf([1, 2, 3], 1, 2),
                     [0.19947114020071635, 0.17603266338214976, 0.12098536225957168])
```

**test_pdf_5**: `stated`
- reason: The docstring defines the output as the normal-distribution PDF of each input value with the given mean and standard deviation, which is exactly what this test checks with mu=2 and sigma=2.

```python
def test_pdf_5(self):
    self.assertEqual(DataStatistics4.pdf([1, 2, 3], 2, 2),
                     [0.17603266338214976, 0.19947114020071635, 0.17603266338214976])
```

## Tests in no method's test class

### `DataStatistics4TestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    self.assertEqual(DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6]), 0.9999999999999998)
    self.assertEqual(DataStatistics4.skewness([1, 2, 5]), 2.3760224064818463)
    self.assertEqual(DataStatistics4.kurtosis([1, 2, 5]), -1.5000000000000002)
    self.assertEqual(DataStatistics4.pdf([1, 2, 3], 1, 1),
                     [0.3989422804014327, 0.24197072451914337, 0.05399096651318806])
```
