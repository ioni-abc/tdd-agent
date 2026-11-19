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


    def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
        words = textnum.lower().replace("-", " ").split()
        if not words:
            return "0"

        current = 0
        result = 0
        for word in words:
            if word not in self.numwords:
                raise ValueError(f"Unknown number word: {word!r}")
            scale, increment = self.numwords[word]
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
        if not isinstance(textnum, str):
            return False
        text = textnum.strip().lower()
        if not text:
            return False

        tokens = text.split()
        # A lone hyphenated compound such as "thirty-two" is not accepted on its own.
        if len(tokens) == 1 and "-" in tokens[0]:
            return False

        def is_valid_word(word):
            if not word:
                return False
            if word in self.numwords or word in self.ordinal_words:
                return True
            for ending, replacement in self.ordinal_endings:
                if word.endswith(ending):
                    base = word[: len(word) - len(ending)] + replacement
                    if base in self.numwords:
                        return True
            return False

        for token in tokens:
            for part in token.split("-"):
                if not is_valid_word(part):
                    return False
        return True