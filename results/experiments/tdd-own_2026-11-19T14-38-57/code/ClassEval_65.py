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
        integer_part = int(x)
        return self.format_string(str(integer_part))


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
        if not s.isdigit():
            raise ValueError("format_string expects a string of digits: %r" % x)

        s = s.lstrip("0")
        if not s:
            return "ZERO ONLY"

        # Split into groups of three digits, from the least significant end.
        groups = []
        while s:
            groups.append(s[-3:])
            s = s[:-3]
        groups.reverse()

        words = []
        total = len(groups)
        for idx, group in enumerate(groups):
            if int(group) == 0:
                continue
            magnitude = total - 1 - idx
            if magnitude >= len(self.NUMBER_MORE):
                raise ValueError("number too large to convert")
            part = self.trans_three(group)
            suffix = self.parse_more(magnitude)
            if suffix:
                part += " " + suffix
            words.append(part)

        return " ".join(words) + " ONLY"


    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        s = str(s).strip()
        if len(s) == 1:
            s = "0" + s
        tens = int(s[0])
        units = int(s[1])

        if tens == 0:
            return self.NUMBER[units]
        if tens == 1:
            return self.NUMBER_TEEN[units]

        word = self.NUMBER_TEN[tens - 1]
        if units:
            word += " " + self.NUMBER[units]
        return word


    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        s = str(s).strip().zfill(3)
        hundreds = int(s[0])
        rest = int(s[1:])

        if hundreds == 0:
            return self.trans_two(str(rest))

        word = self.NUMBER[hundreds] + " HUNDRED"
        if rest:
            word += " AND " + self.trans_two(str(rest))
        return word

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