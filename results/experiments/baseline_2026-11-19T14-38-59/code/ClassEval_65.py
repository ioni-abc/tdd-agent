class NumberWordFormatter:
    """
    This is a class that provides to convert numbers into their corresponding English word representation, including handling the conversion of both the integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN",
                            "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        """
        Converts a number into words format
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        s = str(x)
        if 'e' in s.lower():
            s = format(float(x), '.15f').rstrip('0')
            if s.endswith('.'):
                s = s[:-1]
        return self.format_string(s)

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        s = str(x).strip()
        negative = False
        if s.startswith('-'):
            negative = True
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]

        if '.' in s:
            int_part, dec_part = s.split('.', 1)
        else:
            int_part, dec_part = s, ''

        if int_part == '':
            int_part = '0'
        if not int_part.isdigit() or (dec_part and not dec_part.isdigit()):
            raise ValueError("Invalid number string: %r" % x)

        words = []
        if negative:
            words.append("MINUS")

        int_words = self._trans_integer(int_part)
        words.append(int_words)

        if dec_part:
            words.append("POINT")
            digit_words = [self.NUMBER[int(d)] if d != '0' else "ZERO" for d in dec_part]
            words.append(" ".join(digit_words))

        words.append("ONLY")
        return " ".join(w for w in words if w)

    def _trans_integer(self, int_part):
        """
        Converts a string of digits (integer part) into words, grouped by thousands.
        """
        n = int(int_part)
        if n == 0:
            return "ZERO"
        groups = []
        idx = 0
        while n > 0:
            group = n % 1000
            if group:
                if idx >= len(self.NUMBER_MORE):
                    raise ValueError("Number too large to convert")
                text = self.trans_three(str(group))
                suffix = self.parse_more(idx)
                groups.append(text + (" " + suffix if suffix else ""))
            n //= 1000
            idx += 1
        return " ".join(reversed(groups))

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        n = int(s)
        if n < 10:
            return self.NUMBER[n]
        if n < 20:
            return self.NUMBER_TEEN[n - 10]
        tens, ones = divmod(n, 10)
        result = self.NUMBER_TEN[tens - 1]
        if ones:
            result += " " + self.NUMBER[ones]
        return result

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        n = int(s)
        hundreds, rest = divmod(n, 100)
        parts = []
        if hundreds:
            parts.append(self.NUMBER[hundreds] + " HUNDRED")
        if rest:
            if hundreds:
                parts.append("AND " + self.trans_two(str(rest)))
            else:
                parts.append(self.trans_two(str(rest)))
        return " ".join(parts)

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        return self.NUMBER_MORE[i]