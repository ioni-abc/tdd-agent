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
            if string.startswith('&#', i):
                j = i + 2
                if j >= n:
                    break
                is_hex = string[j] in 'xX'
                if is_hex:
                    j += 1
                start = j
                if is_hex:
                    while j < n and self.is_hex_char(string[j]):
                        j += 1
                else:
                    while j < n and string[j] in '0123456789':
                        j += 1
                if j == start:
                    # Malformed reference
                    if j >= n or string[j].isalnum():
                        break
                    result.append('&#')
                    i += 2
                    continue
                code = int(string[start:j], 16 if is_hex else 10)
                try:
                    ch = chr(code)
                except (ValueError, OverflowError):
                    ch = string[i:j]
                result.append(ch)
                while j < n and string[j] == ';':
                    j += 1
                i = j
            else:
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