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
            int_part, dec_part = s.split(".", 1)
        else:
            int_part, dec_part = s, ""

        int_part = int_part.strip() or "0"
        int_value = int(int_part)

        # Integer part: split into 3-digit groups from the right.
        int_words = ""
        if int_value == 0:
            int_words = "ZERO"
        else:
            groups = []
            group_index = 0
            digits = str(int_value)
            while digits:
                chunk = digits[-3:]
                digits = digits[:-3]
                chunk_value = int(chunk)
                if chunk_value != 0:
                    words = self.trans_three(chunk)
                    if group_index > 0:
                        words += " " + self.parse_more(group_index)
                    groups.append(words)
                group_index += 1
            int_words = " ".join(reversed(groups))

        dec_part = dec_part.strip()
        if dec_part:
            cents = (dec_part + "00")[:2]
            return int_words + " AND CENTS " + self.trans_two(cents) + " ONLY"
        return int_words + " ONLY"

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        s = str(s).strip().zfill(2)
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
        s = str(s).strip().zfill(3)
        hundreds = int(s[0])
        rest = s[1:]

        if hundreds == 0:
            return self.trans_two(rest)

        result = self.NUMBER[hundreds] + " HUNDRED"
        if int(rest) != 0:
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