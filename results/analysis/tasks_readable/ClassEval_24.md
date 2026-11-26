# ClassEval_24

## Skeleton (what the agent sees)

```python
class ComplexCalculator:
    """
    This is a class that implements addition, subtraction, multiplication, and division operations for complex numbers.
    """


    def __init__(self):
        pass

    @staticmethod
    def add(c1, c2):
        """
        Adds two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The sum of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.add(1+2j, 3+4j)
        (4+6j)

        """

    @staticmethod
    def subtract(c1, c2):
        """
        Subtracts two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The difference of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.subtract(1+2j, 3+4j)
        (-2-2j)

        """

    @staticmethod
    def multiply(c1, c2):
        """
        Multiplies two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The product of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.multiply(1+2j, 3+4j)
        (-5+10j)

        """

    @staticmethod
    def divide(c1, c2):
        """
        Divides two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The quotient of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.divide(1+2j, 3+4j)
        (0.44+0.08j)

        """
```

## Method `add`

### Docstring

```python
def add(c1, c2):
        """
        Adds two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The sum of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.add(1+2j, 3+4j)
        (4+6j)

        """
```

### Reference code (`solution_code`)

```python
def add(c1, c2):
        real = c1.real + c2.real
        imaginary = c1.imag + c2.imag
        answer = complex(real, imaginary)
        return answer
```

### Tests (`ComplexCalculatorTestAdd`)

**test_add**: `stated`
- reason: The docstring says add returns the sum of the two complex numbers and gives the example 1+2j plus 3+4j equals (4+6j), which is exactly what the test checks.

```python
def test_add(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.add(1+2j, 3+4j), (4+6j))
```

**test_add_2**: `stated`
- reason: The docstring says add returns the sum of two complex numbers, and a programmer adding real and imaginary parts component-wise would get (-4-6j) for the negative-valued inputs, matching the test.

```python
def test_add_2(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.add(-1 - 2j, -3 - 4j), (-4 - 6j))
```

**test_add_3**: `stated`
- reason: The docstring says add returns the sum of two complex numbers, which is exactly what the test checks: (1-2j) + (3-4j) = 4-6j.

```python
def test_add_3(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.add(1-2j, 3-4j), (4-6j))
```

**test_add_4**: `stated`
- reason: The docstring says adding two complex numbers returns their component-wise sum, so a programmer would compute (-1+2j)+(-3+4j) = (-4+6j), which is what the test expects.

```python
def test_add_4(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.add(-1+2j, -3+4j), (-4+6j))
```

**test_add_5**: `stated`
- reason: The docstring says add returns the sum of two complex numbers, so a programmer would compute the componentwise sum, which for this input is zero and matches the expected value.

```python
def test_add_5(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.add(1+2j, -1-2j), (0+0j))
```

## Method `subtract`

### Docstring

```python
@staticmethod
    def subtract(c1, c2):
        """
        Subtracts two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The difference of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.subtract(1+2j, 3+4j)
        (-2-2j)

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def subtract(c1, c2):
        real = c1.real - c2.real
        imaginary = c1.imag - c2.imag
        return complex(real, imaginary)
```

### Tests (`ComplexCalculatorTestSubtract`)

**test_subtract**: `stated`
- reason: The docstring defines subtract as the difference of two complex numbers and its example gives (1+2j) - (3+4j) = (-2-2j), which matches the test's expected value exactly.

```python
def test_subtract(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.subtract(1+2j, 3+4j), (-2-2j))
```

**test_subtract_2**: `stated`
- reason: The docstring says subtract returns the difference of the two complex numbers, so a programmer would compute c1 minus c2, which gives 2+2j for these inputs, matching the test.

```python
def test_subtract_2(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.subtract(-1-2j, -3-4j), (2+2j))
```

**test_subtract_3**: `stated`
- reason: The docstring says subtract returns the difference of the two complex numbers, so a programmer computing c1 minus c2 gets -2+2j, matching the test.

```python
def test_subtract_3(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.subtract(1-2j, 3-4j), (-2+2j))
```

**test_subtract_4**: `stated`
- reason: The docstring says subtract returns the difference of the two complex numbers, so a programmer computing c1 minus c2 gets 2-2j, which matches the test's expected value.

```python
def test_subtract_4(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.subtract(-1+2j, -3+4j), (2-2j))
```

**test_subtract_5**: `stated`
- reason: The docstring says subtract returns the difference of the two complex numbers, so subtracting a number from itself should yield zero, which is what the test checks.

```python
def test_subtract_5(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.subtract(1+2j, 1+2j), (0+0j))
```

## Method `multiply`

### Docstring

```python
@staticmethod
    def multiply(c1, c2):
        """
        Multiplies two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The product of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.multiply(1+2j, 3+4j)
        (-5+10j)

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def multiply(c1, c2):
        real = c1.real * c2.real - c1.imag * c2.imag
        imaginary = c1.real * c2.imag + c1.imag * c2.real
        return complex(real, imaginary)
```

### Tests (`ComplexCalculatorTestMultiply`)

**test_multiply**: `stated`
- reason: The docstring says multiply should return the product of two complex numbers and gives the example (1+2j)*(3+4j) → (-5+10j), which is exactly the case the test checks.

```python
def test_multiply(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.multiply(1+2j, 3+4j), (-5+10j))
```

**test_multiply_2**: `stated`
- reason: The docstring defines multiply as the product of two complex numbers, which a programmer would implement as standard complex multiplication, and the test's negative-operand case yields the expected -5+10j under that rule.

```python
def test_multiply_2(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.multiply(-1-2j, -3-4j), (-5+10j))
```

**test_multiply_3**: `stated`
- reason: The docstring defines multiply as the product of two complex numbers, and a standard complex multiplication yields the test's expected -5-10j for these inputs.

```python
def test_multiply_3(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.multiply(1-2j, 3-4j), (-5-10j))
```

**test_multiply_4**: `stated`
- reason: The docstring defines multiply as the product of two complex numbers, and a programmer applying standard complex multiplication gets (-1+2j)(-3+4j) = -5-10j, which is what the test expects.

```python
def test_multiply_4(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.multiply(-1+2j, -3+4j), (-5-10j))
```

**test_multiply_5**: `stated`
- reason: The docstring says the method multiplies two complex numbers and returns their product, so standard complex multiplication yields 3-4j, which is what the test expects.

```python
def test_multiply_5(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.multiply(1+2j, -1-2j), (3-4j))
```

## Method `divide`

### Docstring

```python
@staticmethod
    def divide(c1, c2):
        """
        Divides two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The quotient of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.divide(1+2j, 3+4j)
        (0.44+0.08j)

        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def divide(c1, c2):
        denominator = c2.real**2 + c2.imag**2
        real = (c1.real * c2.real + c1.imag * c2.imag) / denominator
        imaginary = (c1.imag * c2.real - c1.real * c2.imag) / denominator
        return complex(real, imaginary)
```

### Tests (`ComplexCalculatorTestDivide`)

**test_divide**: `stated`
- reason: The docstring says divide returns the quotient of the two complex numbers and its example shows (0.44+0.08j) for the same inputs, which is exactly what the test checks.

```python
def test_divide(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.divide(1+2j, 3+4j), (0.44+0.08j))
```

**test_divide_2**: `stated`
- reason: The docstring describes standard complex division and gives the example (1+2j)/(3+4j) = 0.44+0.08j, which is the same mathematical rule and result the test checks with (-1-2j)/(-3-4j).

```python
def test_divide_2(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.divide(-1-2j, -3-4j), (0.44+0.08j))
```

**test_divide_3**: `stated`
- reason: The docstring defines divide as ordinary complex division and gives a worked example of that operation, so a programmer implementing standard complex division would produce 0.44-0.08j for this test's inputs.

```python
def test_divide_3(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.divide(1-2j, 3-4j), (0.44-0.08j))
```

**test_divide_4**: `stated`
- reason: The docstring defines divide as ordinary complex division, and a programmer applying standard complex division to (-1+2j)/(-3+4j) gets 0.44-0.08j, which is what the test expects.

```python
def test_divide_4(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.divide(-1+2j, -3+4j), (0.44-0.08j))
```

**test_divide_5**: `stated`
- reason: The docstring defines divide as the quotient of two complex numbers, so a programmer would compute standard complex division, which gives -1+0j for this test's inputs.

```python
def test_divide_5(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.divide(1+2j, -1-2j), (-1+0j))
```

## Tests in no method's test class

### `ComplexCalculatorTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    complexCalculator = ComplexCalculator()
    self.assertEqual(complexCalculator.add(1+2j, 3+4j), (4+6j))
    self.assertEqual(complexCalculator.subtract(1+2j, 3+4j), (-2-2j))
    self.assertEqual(complexCalculator.multiply(1+2j, 3+4j), (-5+10j))
    self.assertEqual(complexCalculator.divide(1+2j, 3+4j), (0.44+0.08j))
```
