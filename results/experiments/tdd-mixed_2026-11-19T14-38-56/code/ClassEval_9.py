import unittest


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
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            d1 = int(num1[i]) if i >= 0 else 0
            d2 = int(num2[j]) if j >= 0 else 0
            total = d1 + d2 + carry
            result.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        s = ''.join(reversed(result)).lstrip('0')
        return s if s else '0'

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
        a = num1.lstrip('0') or '0'
        b = num2.lstrip('0') or '0'
        negative = False
        if (len(a), a) < (len(b), b):
            a, b = b, a
            negative = True
        i = len(a) - 1
        j = len(b) - 1
        borrow = 0
        result = []
        while i >= 0:
            d1 = int(a[i])
            d2 = int(b[j]) if j >= 0 else 0
            diff = d1 - d2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(diff))
            i -= 1
            j -= 1
        s = ''.join(reversed(result)).lstrip('0') or '0'
        if negative and s != '0':
            return '-' + s
        return s

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
        if not num1 or not num2:
            return '0'
        m, n = len(num1), len(num2)
        digits = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                total = d1 * d2 + digits[i + j + 1]
                digits[i + j + 1] = total % 10
                digits[i + j] += total // 10
        s = ''.join(str(d) for d in digits).lstrip('0')
        return s if s else '0'