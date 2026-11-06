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
        return self.format_string(str(x))

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
        if s.startswith("-"):
            negative = True
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        if "." in s:
            int_part, frac_part = s.split(".", 1)
        else:
            int_part, frac_part = s, ""

        if int_part == "":
            int_part = "0"
        int_value = int(int_part)

        # Integer part
        if int_value == 0:
            int_words = "ZERO"
        else:
            groups = []
            idx = 0
            n = int_value
            while n > 0:
                group = n % 1000
                if group:
                    words = self.trans_three(str(group))
                    suffix = self.parse_more(idx)
                    groups.append(words + (" " + suffix if suffix else ""))
                n //= 1000
                idx += 1
            int_words = " ".join(reversed(groups))

        result = int_words

        # Decimal part
        if frac_part and frac_part.strip("0"):
            digits = []
            for d in frac_part:
                if d.isdigit():
                    digits.append("ZERO" if d == "0" else self.NUMBER[int(d)])
            result += " POINT " + " ".join(digits)

        if negative:
            result = "MINUS " + result

        return result + " ONLY"

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
        tens, units = n // 10, n % 10
        result = self.NUMBER_TEN[tens - 1]
        if units:
            result += " " + self.NUMBER[units]
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
        hundreds = n // 100
        rest = n % 100
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
        if 0 <= i < len(self.NUMBER_MORE):
            return self.NUMBER_MORE[i]
        return ""