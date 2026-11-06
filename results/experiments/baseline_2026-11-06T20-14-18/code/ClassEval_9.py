def _parse_big(s):
    """Split a numeric string into (is_negative, digit_string without leading zeros)."""
    s = s.strip()
    neg = False
    if s and s[0] in '+-':
        neg = s[0] == '-'
        s = s[1:]
    if not s or any(c not in '0123456789' for c in s):
        raise ValueError("Invalid number: %r" % s)
    s = s.lstrip('0') or '0'
    return neg, s


def _cmp_abs(a, b):
    """Compare two normalized digit strings by magnitude."""
    if len(a) != len(b):
        return -1 if len(a) < len(b) else 1
    if a == b:
        return 0
    return -1 if a < b else 1


def _add_abs(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        d = carry
        if i >= 0:
            d += ord(a[i]) - 48
            i -= 1
        if j >= 0:
            d += ord(b[j]) - 48
            j -= 1
        res.append(chr(48 + d % 10))
        carry = d // 10
    return ''.join(reversed(res)).lstrip('0') or '0'


def _sub_abs(a, b):
    """Return |a| - |b|, assuming |a| >= |b|."""
    i, j = len(a) - 1, len(b) - 1
    borrow = 0
    res = []
    while i >= 0:
        d = ord(a[i]) - 48 - borrow
        i -= 1
        if j >= 0:
            d -= ord(b[j]) - 48
            j -= 1
        if d < 0:
            d += 10
            borrow = 1
        else:
            borrow = 0
        res.append(chr(48 + d))
    return ''.join(reversed(res)).lstrip('0') or '0'


def _mul_abs(a, b):
    if a == '0' or b == '0':
        return '0'
    arr = [0] * (len(a) + len(b))
    for i in range(len(a) - 1, -1, -1):
        da = ord(a[i]) - 48
        for j in range(len(b) - 1, -1, -1):
            db = ord(b[j]) - 48
            p = da * db + arr[i + j + 1]
            arr[i + j + 1] = p % 10
            arr[i + j] += p // 10
    return ''.join(chr(48 + d) for d in arr).lstrip('0') or '0'


def _format(neg, digits):
    if digits == '0':
        return '0'
    return ('-' if neg else '') + digits


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
        n1, d1 = _parse_big(num1)
        n2, d2 = _parse_big(num2)
        if n1 == n2:
            return _format(n1, _add_abs(d1, d2))
        if _cmp_abs(d1, d2) >= 0:
            return _format(n1, _sub_abs(d1, d2))
        return _format(n2, _sub_abs(d2, d1))

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
        n2, d2 = _parse_big(num2)
        neg2 = not n2
        if d2 == '0':
            neg2 = False
        return BigNumCalculator.add(num1, _format(neg2, d2))

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
        n1, d1 = _parse_big(num1)
        n2, d2 = _parse_big(num2)
        return _format(n1 != n2, _mul_abs(d1, d2))