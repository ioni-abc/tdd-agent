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

        def split_sign(s):
            s = s.strip()
            if s.startswith('-'):
                return True, s[1:]
            if s.startswith('+'):
                return False, s[1:]
            return False, s

        def strip_zeros(d):
            return d.lstrip('0') or '0'

        def compare_mag(a, b):
            if len(a) != len(b):
                return -1 if len(a) < len(b) else 1
            if a == b:
                return 0
            return -1 if a < b else 1

        def add_mag(a, b):
            i, j, carry = len(a) - 1, len(b) - 1, 0
            res = []
            while i >= 0 or j >= 0 or carry:
                s = carry
                if i >= 0:
                    s += int(a[i])
                    i -= 1
                if j >= 0:
                    s += int(b[j])
                    j -= 1
                res.append(str(s % 10))
                carry = s // 10
            return ''.join(reversed(res)) or '0'

        def sub_mag(a, b):
            # assumes a >= b (as magnitudes)
            i, j, borrow = len(a) - 1, len(b) - 1, 0
            res = []
            while i >= 0:
                d = int(a[i]) - borrow
                i -= 1
                if j >= 0:
                    d -= int(b[j])
                    j -= 1
                if d < 0:
                    d += 10
                    borrow = 1
                else:
                    borrow = 0
                res.append(str(d))
            return strip_zeros(''.join(reversed(res)))

        neg1, m1 = split_sign(num1)
        neg2, m2 = split_sign(num2)
        m1 = strip_zeros(m1)
        m2 = strip_zeros(m2)

        if neg1 == neg2:
            mag = add_mag(m1, m2)
            neg = neg1
        elif compare_mag(m1, m2) >= 0:
            mag = sub_mag(m1, m2)
            neg = neg1
        else:
            mag = sub_mag(m2, m1)
            neg = neg2

        if mag == '0':
            neg = False
        return ('-' if neg else '') + mag

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
        s = num2.strip()
        if s.startswith('-'):
            flipped = s[1:]
        elif s.startswith('+'):
            flipped = '-' + s[1:]
        else:
            flipped = '-' + s
        return BigNumCalculator.add(num1, flipped)

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

        def split_sign(s):
            s = s.strip()
            if s.startswith('-'):
                return True, s[1:]
            if s.startswith('+'):
                return False, s[1:]
            return False, s

        a_neg, a = split_sign(num1)
        b_neg, b = split_sign(num2)
        a = a.lstrip('0') or '0'
        b = b.lstrip('0') or '0'

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

        # Normalize any carry left in the highest position
        for k in range(la + lb - 1, 0, -1):
            if digits[k] >= 10:
                digits[k - 1] += digits[k] // 10
                digits[k] %= 10

        result = ''.join(str(d) for d in digits).lstrip('0') or '0'
        if a_neg != b_neg and result != '0':
            return '-' + result
        return result