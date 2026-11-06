class Words2Numbers:
    """
    The class provides a text-to-number conversion utility, allowing conversion of written numbers (in words) to their numerical representation.
    """

    def __init__(self):
        """
        Initialize the word lists and dictionaries required for conversion
        """
        self.numwords = {}
        self.units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        self.tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.scales = ["hundred", "thousand", "million", "billion", "trillion"]

        self.numwords["and"] = (1, 0)
        for idx, word in enumerate(self.units):
            self.numwords[word] = (1, idx)
        for idx, word in enumerate(self.tens):
            self.numwords[word] = (1, idx * 10)
        for idx, word in enumerate(self.scales):
            self.numwords[word] = (10 ** (idx * 3 or 2), 0)

        self.ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
        self.ordinal_endings = [('ieth', 'y'), ('th', '')]

    def _ordinal_to_cardinal(self, word):
        """
        Convert an ordinal word to its cardinal word equivalent.
        Returns the cardinal word, or None if the word is not a recognised ordinal.
        """
        if word in self.ordinal_words:
            number = self.ordinal_words[word]
            cardinal = {
                1: "one", 2: "two", 3: "three", 5: "five",
                8: "eight", 9: "nine", 12: "twelve",
            }
            return cardinal.get(number)
        for suffix, replacement in self.ordinal_endings:
            if word.endswith(suffix):
                stem = word[: -len(suffix)] + replacement
                if stem in self.numwords:
                    return stem
        return None

    def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
        text = textnum.lower().replace("-", " ")
        current = result = 0
        words = text.split()
        if not words:
            raise ValueError("Empty input")
        for word in words:
            if word in self.numwords:
                cardinal = word
            else:
                cardinal = self._ordinal_to_cardinal(word)
                if cardinal is None:
                    raise ValueError("Illegal word: " + word)
            scale, increment = self.numwords[cardinal]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
        return str(result + current)

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
        words = textnum.lower().split()
        if not words:
            return False
        for word in words:
            if word in self.numwords:
                continue
            if self._ordinal_to_cardinal(word) is None:
                return False
        return True