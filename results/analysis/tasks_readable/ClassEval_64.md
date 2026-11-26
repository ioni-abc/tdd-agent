# ClassEval_64

## Skeleton (what the agent sees)

```python
class NumberConverter:
    """
    The class allows to convert  decimal to binary, octal and hexadecimal repectively and contrarily
    """

    @staticmethod
    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """

    @staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """


    @staticmethod
    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """

    @staticmethod
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """

    @staticmethod
    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """

    @staticmethod
    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """
```

## Method `decimal_to_binary`

### Docstring

```python
def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :param decimal_num: int, decimal number
        :return: str, the binary representation of an integer.
        >>> NumberConverter.decimal_to_binary(42423)
        '1010010110110111'
        """
```

### Reference code (`solution_code`)

```python
def decimal_to_binary(decimal_num):
        binary_num = bin(decimal_num)[2:]
        return binary_num
```

### Tests (`NumberConverterTestDecimalToBinary`)

**test_decimal_to_binary**: `stated`
- reason: The docstring says the method returns the binary representation of an integer as a string, so a programmer would produce the standard binary digits, which is what the test checks for 42423.

```python
def test_decimal_to_binary(self):
    self.assertEqual('1010010110110111', NumberConverter.decimal_to_binary(42423))
```

**test_decimal_to_binary_2**: `stated`
- reason: The docstring says the method returns the binary representation of an integer, and its example shows standard binary with no leading zeros, which is what the test checks for 21271.

```python
def test_decimal_to_binary_2(self):
    self.assertEqual('101001100010111', NumberConverter.decimal_to_binary(21271))
```

**test_decimal_to_binary_3**: `stated`
- reason: The docstring says the method returns the binary representation of an integer and gives an example, so a programmer would produce the standard binary string that the test expects for 42455.

```python
def test_decimal_to_binary_3(self):
    self.assertEqual('1010010111010111', NumberConverter.decimal_to_binary(42455))
```

**test_decimal_to_binary_4**: `stated`
- reason: The docstring asks for the binary representation of an integer as a str, and its example shows plain digits with no prefix, which is what the test expects for 84907 (I verified the expected string is correct).

```python
def test_decimal_to_binary_4(self):
    self.assertEqual('10100101110101011', NumberConverter.decimal_to_binary(84907))
```

**test_decimal_to_binary_5**: `stated`
- reason: The docstring asks for the binary representation of an integer as a str, and its example shows plain digits with no prefix, so a programmer would produce the same output the test expects for 169815.

```python
def test_decimal_to_binary_5(self):
    self.assertEqual('101001011101010111', NumberConverter.decimal_to_binary(169815))
```

## Method `binary_to_decimal`

### Docstring

```python
@staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :param binary_num: str, binary number
        :return: int, the decimal representation of binary number str.
        >>> NumberConverter.binary_to_decimal('1010010110110111')
        42423
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def binary_to_decimal(binary_num):
        decimal_num = int(binary_num, 2)
        return decimal_num
```

### Tests (`NumberConverterTestBinaryToDecimal`)

**test_binary_to_decimal**: `stated`
- reason: The docstring says to convert a binary string to its decimal integer, and the test checks exactly that for a 16-digit binary string, which a standard base-2 conversion satisfies.

```python
def test_binary_to_decimal(self):
    self.assertEqual(42423, NumberConverter.binary_to_decimal('1010010110110111'))
```

**test_binary_to_decimal_2**: `stated`
- reason: The docstring says the method converts a binary string to its decimal integer value, which is exactly what the test checks for a 14-digit input, so a standard base-2 conversion passes.

```python
def test_binary_to_decimal_2(self):
    self.assertEqual(10615, NumberConverter.binary_to_decimal('10100101110111'))
```

**test_binary_to_decimal_3**: `stated`
- reason: The docstring says the method returns the decimal value of a binary string, so a programmer would implement standard base-2 parsing, which gives 42455 for this input (I verified the bit sum).

```python
def test_binary_to_decimal_3(self):
    self.assertEqual(42455, NumberConverter.binary_to_decimal('1010010111010111'))
```

**test_binary_to_decimal_4**: `stated`
- reason: The docstring says the method converts a binary string to its decimal integer value, which is exactly what this test checks, and I verified the expected 169819 is the correct value for that input.

```python
def test_binary_to_decimal_4(self):
    self.assertEqual(169819, NumberConverter.binary_to_decimal('101001011101011011'))
```

**test_binary_to_decimal_5**: `stated`
- reason: The docstring says the method converts a binary string to its decimal integer value, which is exactly what the test checks (the 19-bit string maps to 339639), so a programmer following it would pass.

```python
def test_binary_to_decimal_5(self):
    self.assertEqual(339639, NumberConverter.binary_to_decimal('1010010111010110111'))
```

## Method `decimal_to_octal`

### Docstring

```python
@staticmethod
    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :param decimal_num: int, decimal number
        :return: str, the octal representation of an integer.
        >>> NumberConverter.decimal_to_octal(42423)
        '122667'
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def decimal_to_octal(decimal_num):
        octal_num = oct(decimal_num)[2:]
        return octal_num
```

### Tests (`NumberConvertTestDecimalToOctal`)

**test_decimal_to_octal**: `stated`
- reason: The docstring asks for the octal representation as a str and its example shows '122667' for 42423, which is exactly what the test checks.

```python
def test_decimal_to_octal(self):
    self.assertEqual('122667', NumberConverter.decimal_to_octal(42423))
```

**test_decimal_to_octal_2**: `stated`
- reason: The docstring says the method returns the octal representation of an integer, and its example shows plain digits without a prefix, which is what the test checks (21271 is 51427 in octal).

```python
def test_decimal_to_octal_2(self):
    self.assertEqual('51427', NumberConverter.decimal_to_octal(21271))
```

**test_decimal_to_octal_3**: `stated`
- reason: The docstring says the method returns the octal representation of an integer as a string, and the test checks that 84907 converts to '245653', which is the correct octal form.

```python
def test_decimal_to_octal_3(self):
    self.assertEqual('245653', NumberConverter.decimal_to_octal(84907))
```

**test_decimal_to_octal_4**: `stated`
- reason: The docstring says the method returns the octal representation of an integer as a string, so a programmer would produce the standard base-8 digits, which is what this test checks.

```python
def test_decimal_to_octal_4(self):
    self.assertEqual('513527', NumberConverter.decimal_to_octal(169815))
```

**test_decimal_to_octal_5**: `stated`
- reason: The docstring says the method returns the octal representation of an integer as a string, and its example shows no "0o" prefix, so a programmer following it would produce the test's expected '1227256' for 339630.

```python
def test_decimal_to_octal_5(self):
    self.assertEqual('1227256', NumberConverter.decimal_to_octal(339630))
```

## Method `octal_to_decimal`

### Docstring

```python
@staticmethod
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :param octal_num: str, octal num
        :return: int, the decimal representation of octal number str.
        >>> NumberConverter.octal_to_decimal('122667')
        42423
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def octal_to_decimal(octal_num):
        decimal_num = int(octal_num, 8)
        return decimal_num
```

### Tests (`NumberConvertTestOctalToDecimal`)

**test_octal_to_decimal**: `stated`
- reason: The docstring says the method converts an octal string to its decimal integer, and its example matches the test's input and expected output, so a correct implementation would pass.

```python
def test_octal_to_decimal(self):
    self.assertEqual(42423, NumberConverter.octal_to_decimal('122667'))
```

**test_octal_to_decimal_2**: `stated`
- reason: The docstring says to convert an octal string to its decimal integer value, which is exactly what the test checks with '51427' expecting 21271, so a standard octal-to-decimal implementation passes.

```python
def test_octal_to_decimal_2(self):
    self.assertEqual(21271, NumberConverter.octal_to_decimal('51427'))
```

**test_octal_to_decimal_3**: `stated`
- reason: The docstring says the method takes an octal string and returns its decimal integer value, which is exactly what the test checks (245653 octal = 84907 decimal).

```python
def test_octal_to_decimal_3(self):
    self.assertEqual(84907, NumberConverter.octal_to_decimal('245653'))
```

**test_octal_to_decimal_4**: `stated`
- reason: The docstring says to convert an octal string to its decimal integer value, which is exactly what this test checks: '513527' should give 169815.

```python
def test_octal_to_decimal_4(self):
    self.assertEqual(169815, NumberConverter.octal_to_decimal('513527'))
```

**test_octal_to_decimal_5**: `stated`
- reason: The docstring says to convert an octal string to its decimal integer value, which is exactly what this test checks (octal 1227256 equals 339630 in decimal).

```python
def test_octal_to_decimal_5(self):
    self.assertEqual(339630, NumberConverter.octal_to_decimal('1227256'))
```

## Method `decimal_to_hex`

### Docstring

```python
@staticmethod
    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :param decimal_num: int, decimal number
        :return hex_num: str, the hex representation of an integer.
        >>> NumberConverter.decimal_to_hex(42423)
        'a5b7'
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def decimal_to_hex(decimal_num):
        hex_num = hex(decimal_num)[2:]
        return hex_num
```

### Tests (`NumberConvertTestDecimalToHex`)

**test_decimal_to_hex**: `stated`
- reason: The docstring's example `decimal_to_hex(42423)` returns `'a5b7'`, which is exactly the input and expected output this test checks, so a programmer following it would pass.

```python
def test_decimal_to_hex(self):
    self.assertEqual('a5b7', NumberConverter.decimal_to_hex(42423))
```

**test_decimal_to_hex_2**: `stated`
- reason: The docstring says to convert a decimal integer to its hex string, and a programmer following it (lowercase digits, no prefix, as in the example) would return '5317' for 21271.

```python
def test_decimal_to_hex_2(self):
    self.assertEqual('5317', NumberConverter.decimal_to_hex(21271))
```

**test_decimal_to_hex_3**: `stated`
- reason: The docstring's example `decimal_to_hex(42423)` returns `'a5b7'`, which shows the lowercase, unprefixed hex string the test expects for 84907 (`'14bab'`).

```python
def test_decimal_to_hex_3(self):
    self.assertEqual('14bab', NumberConverter.decimal_to_hex(84907))
```

**test_decimal_to_hex_4**: `stated`
- reason: The docstring's example shows the lowercase, unprefixed hex form that the test expects, and 169815 converts to '29757' under that convention, so a programmer following it would pass.

```python
def test_decimal_to_hex_4(self):
    self.assertEqual('29757', NumberConverter.decimal_to_hex(169815))
```

**test_decimal_to_hex_5**: `stated`
- reason: The docstring says to return the hex representation of an integer, and its example shows lowercase digits with no "0x" prefix, which is exactly what the test expects for 339639 (`52eb7`).

```python
def test_decimal_to_hex_5(self):
    self.assertEqual('52eb7', NumberConverter.decimal_to_hex(339639))
```

## Method `hex_to_decimal`

### Docstring

```python
@staticmethod
    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :param hex_num: str, hex num
        :return: int, the decimal representation of hex number str.
        >>> NumberConverter.hex_to_decimal('a5b7')
        42423
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def hex_to_decimal(hex_num):
        decimal_num = int(hex_num, 16)
        return decimal_num
```

### Tests (`NumberConvertTestHexToDecimal`)

**test_hex_to_decimal**: `stated`
- reason: The docstring says to convert a hex string to a decimal int and its example ('a5b7' → 42423) matches the test, so a programmer following it would pass.

```python
def test_hex_to_decimal(self):
    self.assertEqual(42423, NumberConverter.hex_to_decimal('a5b7'))
```

**test_hex_to_decimal_2**: `stated`
- reason: The docstring says the method converts a hex string to its decimal integer, and the test's input '52d7' should produce 21207 under that standard conversion, which a programmer would implement.

```python
def test_hex_to_decimal_2(self):
    self.assertEqual(21207, NumberConverter.hex_to_decimal('52d7'))
```

**test_hex_to_decimal_3**: `stated`
- reason: The docstring says to convert a hex string to its decimal integer, which is what the test checks with a five-digit mixed letter-and-digit hex string (0x14a93 = 84627), so a standard hex-to-int conversion passes.

```python
def test_hex_to_decimal_3(self):
    self.assertEqual(84627, NumberConverter.hex_to_decimal('14a93'))
```

**test_hex_to_decimal_4**: `stated`
- reason: The docstring says to convert a hex string to its decimal integer, which is exactly what the test checks for the input '29a77' (0x29a77 = 170615), so a programmer following it would pass.

```python
def test_hex_to_decimal_4(self):
    self.assertEqual(170615, NumberConverter.hex_to_decimal('29a77'))
```

**test_hex_to_decimal_5**: `stated`
- reason: The docstring says to convert a hex string to its decimal integer value, and a programmer following that would compute 0x53a77 = 342647, which is what the test expects.

```python
def test_hex_to_decimal_5(self):
    self.assertEqual(342647, NumberConverter.hex_to_decimal('53a77'))
```

## Tests in no method's test class

### `NumberConvertTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    self.assertEqual('1010010110110111', NumberConverter.decimal_to_binary(42423))
    self.assertEqual(42423, NumberConverter.binary_to_decimal('1010010110110111'))
    self.assertEqual('122667', NumberConverter.decimal_to_octal(42423))
    self.assertEqual('122667', NumberConverter.decimal_to_octal(42423))
    self.assertEqual('a5b7', NumberConverter.decimal_to_hex(42423))
    self.assertEqual(42423, NumberConverter.hex_to_decimal('a5b7'))
```
