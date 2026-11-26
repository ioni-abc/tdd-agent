# ClassEval_9

## Skeleton (what the agent sees)

```python
class BigNumCalculator:
    """
    This is a class that implements big number calculations, including adding, subtracting and multiplying.
    """

    @staticmethod
    def add(num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add,str.
        :param num2: The second number to add,str.
        :return: The sum of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'

        """

    @staticmethod
    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract,str.
        :param num2: The second number to subtract,str.
        :return: The difference of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
        '-86419753208641975320'

        """

    @staticmethod
    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'

        """
```

## Method `add`

### Docstring

```python
def add(num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add,str.
        :param num2: The second number to add,str.
        :return: The sum of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'

        """
```

### Reference code (`solution_code`)

```python
def add(num1, num2):
        max_length = max(len(num1), len(num2))
        num1 = num1.zfill(max_length)
        num2 = num2.zfill(max_length)

        carry = 0
        result = []
        for i in range(max_length - 1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            carry = digit_sum // 10
            digit = digit_sum % 10
            result.insert(0, str(digit))

        if carry > 0:
            result.insert(0, str(carry))

        return ''.join(result)
```

### Tests (`BigNumCalculatorTestAdd`)

**test_add**: `stated`
- reason: The docstring specifies adding two decimal digit strings and returning the sum as a string, and its example is the same input and expected output the test checks, so a correct implementation would pass.

```python
def test_add(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.add("12345678901234567890", "98765432109876543210"), "111111111011111111100")
```

**test_add_2**: `stated`
- reason: The docstring says add returns the decimal sum of two big numbers passed and returned as strings, so a programmer would implement arbitrary-length string addition, which is what this test checks with operands of different lengths.

```python
def test_add_2(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.add("123456789012345678922", "98765432109876543210"), "222222221122222222132")
```

**test_add_3**: `stated`
- reason: The docstring says add takes two numeric strings and returns their sum as a string, which is exactly what this test checks, including the case where the first number has one more digit than the second.

```python
def test_add_3(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.add("123456789012345678934", "98765432109876543210"), "222222221122222222144")
```

**test_add_4**: `stated`
- reason: The docstring says the method adds two big numbers given and returned as decimal strings, which is what the test checks: ordinary decimal addition of two inputs with different lengths.

```python
def test_add_4(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.add("123456789012345678946", "98765432109876543210"), "222222221122222222156")
```

**test_add_5**: `stated`
- reason: The docstring says the method adds two big numbers given as strings and returns the sum as a string, so a programmer would implement arbitrary-length decimal addition with carry, which is what the test checks.

```python
def test_add_5(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.add("123456789012345678958", "98765432109876543210"), "222222221122222222168")
```

## Method `subtract`

### Docstring

```python
@staticmethod
    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract,str.
        :param num2: The second number to subtract,str.
        :return: The difference of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
        '-86419753208641975320'

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def subtract(num1, num2):

        if len(num1) < len(num2):
            num1, num2 = num2, num1
            negative = True
        elif len(num1) > len(num2):
            negative = False
        else:
            if num1 < num2:
                num1, num2 = num2, num1
                negative = True
            else:
                negative = False

        max_length = max(len(num1), len(num2))
        num1 = num1.zfill(max_length)
        num2 = num2.zfill(max_length)

        borrow = 0
        result = []
        for i in range(max_length - 1, -1, -1):
            digit_diff = int(num1[i]) - int(num2[i]) - borrow

            if digit_diff < 0:
                digit_diff += 10
                borrow = 1
            else:
                borrow = 0

            result.insert(0, str(digit_diff))

        while len(result) > 1 and result[0] == '0':
            result.pop(0)

        if negative:
            result.insert(0, '-')

        return ''.join(result)
```

### Tests (`BigNumCalculatorTestSubtract`)

**test_subtract**: `stated`
- reason: The docstring's doctest uses the same inputs and the same expected string "-86419753208641975320", so a programmer following it would produce the tested result.

```python
def test_subtract(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.subtract("12345678901234567890", "98765432109876543210"), "-86419753208641975320")
```

**test_subtract_2**: `stated`
- reason: The docstring says to subtract the second number from the first and return the difference, so a programmer would compute 123456789012345678922 - 98765432109876543210 and get the expected positive result.

```python
def test_subtract_2(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.subtract("123456789012345678922", "98765432109876543210"), "24691356902469135712")
```

**test_subtract_3**: `stated`
- reason: The docstring defines subtract as the difference num1 - num2 returned as a string, so a programmer would produce the same positive result the test expects for this case.

```python
def test_subtract_3(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.subtract("123456789012345678934", "98765432109876543"), "123358023580235802391")
```

**test_subtract_4**: `stated`
- reason: The docstring's example shows the same behaviour the test checks, a negative result returned with a leading '-' when the second number is larger, so a programmer following it would produce the test's expected output.

```python
def test_subtract_4(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.subtract("12345678901234567", "98765432109876543210"), "-98753086430975308643")
```

**test_subtract_5**: `stated`
- reason: The docstring says the method subtracts two big numeric strings and returns the difference, so a programmer would produce the ordinary positive difference of 923456789 minus 187654321, which matches the expected "735802468".

```python
def test_subtract_5(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.subtract("923456789", "187654321"), "735802468")
```

## Method `multiply`

### Docstring

```python
@staticmethod
    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def multiply(num1, num2):
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]

                result[p1] += total // 10
                result[p2] = total % 10

        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))
```

### Tests (`BigNumCalculatorTestMultiply`)

**test_multiply**: `stated`
- reason: The docstring says it multiplies two big numbers passed as strings and returns the product as a string, and its example is this exact input and output, so a programmer following it would pass.

```python
def test_multiply(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.multiply("12345678901234567890", "98765432109876543210"), "1219326311370217952237463801111263526900")
```

**test_multiply_2**: `stated`
- reason: The docstring says it multiplies two big numbers given as strings and returns the product as a string, which is exactly what this test checks with ordinary large-number multiplication.

```python
def test_multiply_2(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.multiply("123456789012345678922", "98765432109876543210"), "12193263113702179524547477517529919219620")
```

**test_multiply_3**: `stated`
- reason: The docstring says it multiplies two big numbers given as strings and returns the product as a string, so a programmer would implement exact arbitrary-precision multiplication, which is what this test checks.

```python
def test_multiply_3(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.multiply("123456789012345678934", "98765432109876543"), "12193263113702179499806737010255845162")
```

**test_multiply_4**: `stated`
- reason: The docstring says the method multiplies two big numbers given as strings and returns the product as a string, which is exactly what this test checks for a large-number multiplication.

```python
def test_multiply_4(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.multiply("12345678901234567", "98765432109876543210"), "1219326311370217864336229223321140070")
```

**test_multiply_5**: `stated`
- reason: The docstring says the method multiplies two numeric strings and returns the product as a string, which is exactly what this test checks with no special convention needed.

```python
def test_multiply_5(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.multiply("923456789", "187654321"), "173290656712635269")
```

**test_multiply_6**: `unstated`
- reason: The docstring says only that the product is returned as a string, so a correct implementation could return the padded or leading-zero form of the product, while the test expects the canonical form "1" for zero-padded inputs.
- missing: The docstring should state whether the result must have leading zeros removed (and that zero is returned as a single "0"), and whether inputs with leading zeros are accepted.

```python
def test_multiply_6(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.multiply("000000001", "000000001"), "1")
```

## Tests in no method's test class

### `BigNumCalculatorTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    bigNum = BigNumCalculator()
    self.assertEqual(bigNum.add("12345678901234567890", "98765432109876543210"), "111111111011111111100")
    self.assertEqual(bigNum.subtract("12345678901234567890", "98765432109876543210"), "-86419753208641975320")
    self.assertEqual(bigNum.multiply("12345678901234567890", "98765432109876543210"), "1219326311370217952237463801111263526900")
```
