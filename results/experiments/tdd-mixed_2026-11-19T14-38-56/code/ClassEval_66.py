class NumericEntityUnescaper:
    """
    This is a class that provides functionality to replace numeric entities with their corresponding characters in a given string.
    """

    def __init__(self):
        pass

    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'

        """
        result = []
        i = 0
        n = len(string)
        while i < n:
            if string.startswith("&#", i):
                i += 2
                hex_mode = False
                if i < n and string[i] in "xX":
                    hex_mode = True
                    i += 1
                digits = []
                while i < n:
                    ch = string[i]
                    if hex_mode:
                        if not self.is_hex_char(ch):
                            break
                    else:
                        if ch not in "0123456789":
                            break
                    digits.append(ch)
                    i += 1
                if i < n and string[i] == ";":
                    i += 1
                if digits:
                    code = int("".join(digits), 16 if hex_mode else 10)
                    if code <= 0x10FFFF:
                        try:
                            result.append(chr(code))
                        except (ValueError, OverflowError):
                            pass
            else:
                result.append(string[i])
                i += 1
        return "".join(result)

    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """
        return len(char) == 1 and char in "0123456789abcdefABCDEF"