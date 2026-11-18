import unittest


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
        if x is None:
            return ""
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
        if "." in s:
            int_part, frac_part = s.split(".", 1)
        else:
            int_part, frac_part = s, ""

        if int_part == "":
            int_part = "0"
        if not int_part.isdigit() or (frac_part and not frac_part.isdigit()):
            raise ValueError("Invalid number string: %r" % x)

        # Integer part
        int_value = int(int_part)
        if int_value == 0:
            words = "ZERO"
        else:
            groups = []
            digits = str(int_value)
            while digits:
                groups.append(digits[-3:])
                digits = digits[:-3]
            if len(groups) > len(self.NUMBER_MORE):
                raise ValueError("Number too large: %r" % x)

            parts = []
            for i in range(len(groups) - 1, -1, -1):
                group = groups[i]
                if int(group) == 0:
                    continue
                part = self.trans_three(group)
                if self.parse_more(i):
                    part += " " + self.parse_more(i)
                parts.append(part)
            words = " ".join(parts)

        # Decimal part (cents)
        if frac_part:
            cents = int((frac_part + "00")[:2])
            if cents:
                words += " AND CENTS " + self.trans_two(cents)

        return words + " ONLY"

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        s = str(s).zfill(2)
        tens = int(s[0])
        ones = int(s[1])

        if tens == 0:
            return self.NUMBER[ones]
        if tens == 1:
            return self.NUMBER_TEEN[ones]

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
        s = str(s).zfill(3)
        hundreds = int(s[0])
        rest = s[1:]
        rest_value = int(rest)

        if hundreds == 0:
            return self.trans_two(rest)

        result = self.NUMBER[hundreds] + " HUNDRED"
        if rest_value:
            result += " AND " + self.trans_two(rest)
        return result

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