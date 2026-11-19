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

        def parse(n):
            n = n.strip()
            negative = False
            if n.startswith('-'):
                negative = True
                n = n[1:]
            elif n.startswith('+'):
                n = n[1:]
            n = n.lstrip('0') or '0'
            return negative, n

        def add_abs(a, b):
            i, j = len(a) - 1, len(b) - 1
            carry = 0
            res = []
            while i >= 0 or j >= 0 or carry:
                d = carry
                if i >= 0:
                    d += int(a[i])
                    i -= 1
                if j >= 0:
                    d += int(b[j])
                    j -= 1
                res.append(str(d % 10))
                carry = d // 10
            return ''.join(reversed(res))

        def sub_abs(a, b):
            # assumes |a| >= |b|
            i, j = len(a) - 1, len(b) - 1
            borrow = 0
            res = []
            while i >= 0:
                d = int(a[i]) - borrow - (int(b[j]) if j >= 0 else 0)
                i -= 1
                j -= 1
                if d < 0:
                    d += 10
                    borrow = 1
                else:
                    borrow = 0
                res.append(str(d))
            return ''.join(reversed(res)).lstrip('0') or '0'

        def cmp_abs(a, b):
            if len(a) != len(b):
                return 1 if len(a) > len(b) else -1
            if a == b:
                return 0
            return 1 if a > b else -1

        neg1, a = parse(num1)
        neg2, b = parse(num2)

        if neg1 == neg2:
            s = add_abs(a, b)
            sign = neg1
        elif cmp_abs(a, b) >= 0:
            s = sub_abs(a, b)
            sign = neg1
        else:
            s = sub_abs(b, a)
            sign = neg2

        if s == '0':
            return '0'
        return ('-' if sign else '') + s

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
        n2 = num2.strip()
        if n2.startswith('-'):
            negated = n2[1:]
        elif n2.startswith('+'):
            negated = '-' + n2[1:]
        else:
            negated = '-' + n2
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

        def parse(n):
            n = n.strip()
            negative = False
            if n.startswith('-'):
                negative = True
                n = n[1:]
            elif n.startswith('+'):
                n = n[1:]
            n = n.lstrip('0') or '0'
            return negative, n

        neg1, a = parse(num1)
        neg2, b = parse(num2)

        if a == '0' or b == '0':
            return '0'

        la, lb = len(a), len(b)
        digits = [0] * (la + lb)
        for i in range(la - 1, -1, -1):
            da = ord(a[i]) - 48
            for j in range(lb - 1, -1, -1):
                db = ord(b[j]) - 48
                total = digits[i + j + 1] + da * db
                digits[i + j + 1] = total % 10
                digits[i + j] += total // 10

        s = ''.join(str(d) for d in digits).lstrip('0') or '0'
        if s == '0':
            return '0'
        return ('-' if neg1 != neg2 else '') + s