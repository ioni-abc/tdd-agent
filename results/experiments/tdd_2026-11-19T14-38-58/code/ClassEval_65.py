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
            int_str, dec_str = s.split(".", 1)
        else:
            int_str, dec_str = s, ""

        int_value = int(int_str) if int_str else 0

        if int_value == 0:
            words = "ZERO"
        else:
            digits = str(int_value)
            padded = digits.zfill(((len(digits) + 2) // 3) * 3)
            chunks = [padded[i:i + 3] for i in range(0, len(padded), 3)]
            total = len(chunks)
            parts = []
            for k, chunk in enumerate(chunks):
                idx = total - 1 - k
                if int(chunk) == 0:
                    continue
                parts.append(self.trans_three(chunk))
                if idx:
                    parts.append(self.parse_more(idx))
            words = " ".join(p for p in parts if p)

        result = words
        if dec_str and int(dec_str) != 0:
            cents = dec_str.ljust(2, "0")[:2]
            result += " AND CENTS " + self.trans_two(cents)

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
        s = str(s).zfill(2)
        tens = int(s[0])
        ones = int(s[1])

        if tens == 1:
            return self.NUMBER_TEEN[ones]

        parts = []
        if tens >= 2:
            parts.append(self.NUMBER_TEN[tens - 1])
        if ones:
            parts.append(self.NUMBER[ones])
        return " ".join(parts)

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

        parts = []
        if hundreds:
            parts.append(self.NUMBER[hundreds])
            parts.append("HUNDRED")
            if rest_value:
                parts.append("AND")
        if rest_value:
            parts.append(self.trans_two(rest))
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