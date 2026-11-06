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
                hex_mode = False
                if j < n and string[j] in 'xX':
                    hex_mode = True
                    j += 1
                start = j
                if hex_mode:
                    while j < n and self.is_hex_char(string[j]):
                        j += 1
                else:
                    while j < n and string[j].isdigit() and string[j] in '0123456789':
                        j += 1
                digits = string[start:j]
                if digits:
                    try:
                        code = int(digits, 16) if hex_mode else int(digits, 10)
                    except ValueError:
                        code = None
                    if code is not None and 0 < code <= 0x10FFFF:
                        result.append(chr(code))
                        if j < n and string[j] == ';':
                            j += 1
                        i = j
                        continue
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