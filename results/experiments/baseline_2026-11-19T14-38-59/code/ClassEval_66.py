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
            if string[i] == '&' and i + 1 < n and string[i + 1] == '#':
                j = i + 2
                is_hex = False
                if j < n and string[j] in 'xX':
                    is_hex = True
                    j += 1
                start = j
                while j < n and (self.is_hex_char(string[j]) if is_hex else string[j].isdigit()):
                    j += 1
                digits = string[start:j]
                if digits and j < n and string[j] == ';':
                    try:
                        code_point = int(digits, 16) if is_hex else int(digits, 10)
                        if code_point <= 0x10FFFF:
                            result.append(chr(code_point))
                            i = j + 1
                            continue
                    except (ValueError, OverflowError):
                        pass
            result.append(string[i])
            i += 1
        return ''.join(result)

    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, the character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        >>> NumericEntityUnescaper.is_hex_char('a')
        True

        """
        return len(char) == 1 and char in '0123456789abcdefABCDEF'