class Manacher:
    """
    his is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2

        """
        if center - diff < 0 or center + diff >= len(string):
            return 0
        if string[center - diff] == string[center + diff]:
            return 1 + self.palindromic_length(center, diff + 1, string)
        return 0

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        s = self.input_string
        if not s:
            return ''
        t = '|'.join(s)
        best = ''
        for i in range(len(t)):
            r = self.palindromic_length(i, 1, t)
            lo = i - r
            hi = i + r
            # letters live at even indices of t
            start = (lo + 1) // 2
            end = hi // 2
            if end >= start:
                length = end - start + 1
                if length > len(best):
                    best = s[start:end + 1]
        return best