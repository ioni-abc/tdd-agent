def _parse_big(s):
    """Split a numeric string into (is_negative, digit_string without leading zeros)."""
    s = s.strip()
    negative = False
    if s and s[0] in '+-':
        negative = s[0] == '-'
        s = s[1:]
    if not s.isdigit():
        raise ValueError(f"Invalid number: {s!r}")
    digits = s.lstrip('0') or '0'
    return negative, digits


def _format_big(negative, digits):
    """Build the output string, avoiding a '-' sign for zero."""
    if digits == '0':
        return '0'
    return ('-' if negative else '') + digits


def _cmp_abs(a, b):
    """Compare two digit strings without leading zeros. Returns -1, 0 or 1."""
    if len(a) != len(b):
        return -1 if len(a) < len(b) else 1
    if a == b:
        return 0
    return -1 if a < b else 1


def _add_abs(a, b):
    """Add two non-negative digit strings."""
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        da = int(a[i]) if i >= 0 else 0
        db = int(b[j]) if j >= 0 else 0
        total = da + db + carry
        result.append(str(total % 10))
        carry = total // 10
        i -= 1
        j -= 1
    return ''.join(reversed(result)).lstrip('0') or '0'


def _sub_abs(a, b):
    """Subtract b from a, where |a| >= |b| (digit strings, non-negative)."""
    i, j = len(a) - 1, len(b) - 1
    borrow = 0
    result = []
    while i >= 0:
        da = int(a[i]) - borrow
        db = int(b[j]) if j >= 0 else 0
        if da < db:
            da += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(da - db))
        i -= 1
        j -= 1
    return ''.join(reversed(result)).lstrip('0') or '0'


def _mul_abs(a, b):
    """Multiply two non-negative digit strings (schoolbook algorithm)."""
    if a == '0' or b == '0':
        return '0'
    n, m = len(a), len(b)
    res = [0] * (n + m)
    for i in range(n - 1, -1, -1):
        da = int(a[i])
        for j in range(m - 1, -1, -1):
            res[i + j + 1] += da * int(b[j])
    carry = 0
    for k in range(n + m - 1, -1, -1):
        total = res[k] + carry
        res[k] = total % 10
        carry = total // 10
    return ''.join(map(str, res)).lstrip('0') or '0'


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
        neg1, d1 = _parse_big(num1)
        neg2, d2 = _parse_big(num2)
        if neg1 == neg2:
            return _format_big(neg1, _add_abs(d1, d2))
        cmp = _cmp_abs(d1, d2)
        if cmp == 0:
            return '0'
        if cmp > 0:
            return _format_big(neg1, _sub_abs(d1, d2))
        return _format_big(neg2, _sub_abs(d2, d1))

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
        neg2, d2 = _parse_big(num2)
        negated = ('+' if neg2 else '-') + d2
        return BigNumCalculator.add(num1, negated)

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
        neg1, d1 = _parse_big(num1)
        neg2, d2 = _parse_big(num2)
        product = _mul_abs(d1, d2)
        return _format_big(neg1 != neg2, product)