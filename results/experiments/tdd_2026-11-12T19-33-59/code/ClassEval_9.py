class BigNumCalculator:
    """
    This is a class that implements big number calculations, including adding, subtracting and multiplying.
    """

    @staticmethod
    def _split_sign(num):
        """
        Splits a number string into its sign flag and its magnitude digits.
        :param num: The number as a string, optionally prefixed with '+' or '-'.
        :return: A tuple (is_negative, digits).
        """
        if num[:1] == '-':
            return True, num[1:]
        if num[:1] == '+':
            return False, num[1:]
        return False, num

    @staticmethod
    def _compare_magnitude(a, b):
        """
        Compares two unsigned digit strings.
        :return: 1 if a > b, -1 if a < b, 0 if equal.
        """
        a = a.lstrip('0') or '0'
        b = b.lstrip('0') or '0'
        if len(a) != len(b):
            return 1 if len(a) > len(b) else -1
        if a == b:
            return 0
        return 1 if a > b else -1

    @staticmethod
    def _add_magnitude(a, b):
        """
        Adds two unsigned digit strings digit by digit.
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            d = carry
            if i >= 0:
                d += int(a[i])
                i -= 1
            if j >= 0:
                d += int(b[j])
                j -= 1
            result.append(str(d % 10))
            carry = d // 10
        return ''.join(reversed(result))

    @staticmethod
    def _sub_magnitude(a, b):
        """
        Subtracts unsigned digit string b from a, assuming a >= b.
        """
        borrow = 0
        j = len(b) - 1
        result = []
        for i in range(len(a) - 1, -1, -1):
            d = int(a[i]) - borrow - (int(b[j]) if j >= 0 else 0)
            j -= 1
            if d < 0:
                d += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(d))
        return ''.join(reversed(result))

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
        neg1, m1 = BigNumCalculator._split_sign(num1)
        neg2, m2 = BigNumCalculator._split_sign(num2)

        if neg1 == neg2:
            mag = BigNumCalculator._add_magnitude(m1, m2)
            neg = neg1
        elif BigNumCalculator._compare_magnitude(m1, m2) >= 0:
            mag = BigNumCalculator._sub_magnitude(m1, m2)
            neg = neg1
        else:
            mag = BigNumCalculator._sub_magnitude(m2, m1)
            neg = neg2

        mag = mag.lstrip('0') or '0'
        if neg and mag != '0':
            return '-' + mag
        return mag

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
        if num2[:1] == '-':
            negated = num2[1:]
        elif num2[:1] == '+':
            negated = '-' + num2[1:]
        else:
            negated = '-' + num2
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
        neg1, m1 = BigNumCalculator._split_sign(num1)
        neg2, m2 = BigNumCalculator._split_sign(num2)

        m1 = m1.lstrip('0') or '0'
        m2 = m2.lstrip('0') or '0'

        if m1 == '0' or m2 == '0':
            return '0'

        result = [0] * (len(m1) + len(m2))
        for i in range(len(m1) - 1, -1, -1):
            x = int(m1[i])
            for j in range(len(m2) - 1, -1, -1):
                p = x * int(m2[j]) + result[i + j + 1]
                result[i + j + 1] = p % 10
                result[i + j] += p // 10

        # Normalize any remaining carries.
        carry = 0
        for k in range(len(result) - 1, -1, -1):
            d = result[k] + carry
            result[k] = d % 10
            carry = d // 10

        mag = ''.join(str(d) for d in result).lstrip('0') or '0'
        neg = neg1 != neg2
        if neg and mag != '0':
            return '-' + mag
        return mag