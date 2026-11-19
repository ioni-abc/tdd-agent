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
        if center - diff == -1 or center + diff == len(string) or string[center + diff] != string[center - diff]:
            return 0
        return 1 + self.palindromic_length(center, diff + 1, string)

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

        # Build transformed string: letters at even indices, separators at odd indices.
        t = '|'.join(s)

        best_start = 0
        best_end = 0
        for center in range(len(t)):
            r = self.palindromic_length(center, 1, t)
            start = center - r
            end = center + r
            if end - start > best_end - best_start:
                best_start, best_end = start, end

        # Map transformed span back to original indices (letters live at even indices).
        if best_start % 2 == 1:
            best_start += 1
        if best_end % 2 == 1:
            best_end -= 1
        return s[best_start // 2: best_end // 2 + 1]