# ClassEval_97

## Skeleton (what the agent sees)

```python
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

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
```

## Method `text2int`

### Docstring

```python
def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
```

### Reference code (`solution_code`)

```python
def text2int(self, textnum):
        textnum = textnum.replace('-', ' ')

        current = result = 0
        curstring = ""
        onnumber = False
        for word in textnum.split():
            if word in self.ordinal_words:
                scale, increment = (1, self.ordinal_words[word])
                current = current * scale + increment
                onnumber = True
            else:
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)

                if word not in self.numwords:
                    if onnumber:
                        curstring += repr(result + current) + " "
                    curstring += word + " "
                    result = current = 0
                    onnumber = False
                else:
                    scale, increment = self.numwords[word]
                    current = current * scale + increment
                    if scale > 100:
                        result += current
                        current = 0
                    onnumber = True

        if onnumber:
            curstring += repr(result + current)

        return curstring
```

### Tests (`Words2NumbersTestText2Int`)

**test_text2int**: `stated`
- reason: The docstring's own example, text2int("thirty-two") returning "32", is exactly the case the test checks, so a programmer following the docstring would produce the expected string.

```python
def test_text2int(self):
    w2n = Words2Numbers()
    self.assertEqual(w2n.text2int("thirty-two"), "32")
```

**test_text2int2**: `stated`
- reason: The docstring asks for converting a number written in words to its integer string, and a programmer would naturally produce "123" for "one hundred and twenty-three", with the hyphen in "twenty-three" handled as part of the number.

```python
def test_text2int2(self):
    w2n = Words2Numbers()
    self.assertEqual(w2n.text2int("one hundred and twenty-three"), "123")
```

**test_text2int3**: `unstated`
- reason: The docstring only shows a hyphenated example, so it doesn't say whether a connecting word inside a number phrase is absorbed into the number or breaks it into separate parts, which this test depends on.
- missing: The docstring should state how connecting words such as "and" that appear within a spelled-out number are treated, including whether they are ignored so the whole phrase yields one combined integer string.

```python
def test_text2int3(self):
    w2n = Words2Numbers()
    self.assertEqual(w2n.text2int("two thousand and nineteen"), "2019")
```

**test_text2int4**: `unstated`
- reason: The docstring only shows a hyphenated example ("thirty-two"), so it doesn't say how a conjunction like "and" inside a number phrase should be handled, and a correct implementation could reasonably produce a different string than "101".
- missing: The docstring should state how filler words such as "and" inside a number phrase are treated (ignored and folded into the number, or emitted as text), and what output a multi-part phrase with such a word should give.

```python
def test_text2int4(self):
    w2n = Words2Numbers()
    self.assertEqual(w2n.text2int("one hundred and one"), "101")
```

**test_text2int5**: `unstated`
- reason: The docstring gives only a hyphenated example ("thirty-two"), so a programmer would not know that a connector word like "and" inside a large number phrase is ignored, or that scale words like "million" combine with the words on both sides, which the test relies on.
- missing: The docstring should state how connector words (such as "and") within a number phrase are treated, and how scale words (such as thousand or million) combine with the number words before and after them, with examples that cover mixed-scale phrases.

```python
def test_text2int5(self):
    w2n = Words2Numbers()
    self.assertEqual(w2n.text2int("one million and eleven"), "1000011")
```

**test_text2int6**: `unstated`
- reason: The docstring only says to convert "the word string" to an integer string, so a programmer would not know that ordinal-form words such as "-th" endings are to be converted to their numeric values.
- missing: The docstring should state how ordinal-form number words (words with ordinal suffixes or ordinal forms like "first" or "-th" endings) are handled, including whether they are converted to their integer value and how they combine with the preceding cardinal words.

```python
def test_text2int6(self):
    w2n = Words2Numbers()
    self.assertEqual(w2n.text2int("one million one hundred sixty-ninth"), "1000169")
```

## Method `is_valid_input`

### Docstring

```python
def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
```

### Reference code (`solution_code`)

```python
def is_valid_input(self, textnum):

        textnum = textnum.replace('-', ' ')

        for word in textnum.split():
            if word in self.ordinal_words:
                continue
            else:
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)

                if word not in self.numwords:
                    return False

        return True
```

### Tests (`Words2NumbersTestIsValidInput`)

**test_is_valid_input**: `contradicts`
- reason: The docstring's own example says "thirty-two" returns False, but the test and reference code treat hyphenated number words like that as valid, so the test expects True.
- missing: The docstring should state that hyphens between number words are treated as separators, so a hyphenated compound number whose parts are all valid number words returns True, and its example should reflect that.

```python
def test_is_valid_input(self):
    w2n = Words2Numbers()
    self.assertTrue(w2n.is_valid_input("twenty-five thousand three hundred and forty-two"))
```

**test_is_valid_input2**: `unstated`
- reason: The docstring says valid words are those that "can be converted into numbers" but never says whether ordinal words or connecting words like "and" count as valid, so a programmer could reasonably reject the test's input.
- missing: The docstring should state which word forms are accepted, including whether ordinal forms and conjunction words are valid inputs, and how hyphens between words are treated.

```python
def test_is_valid_input2(self):
    w2n = Words2Numbers()
    self.assertTrue(w2n.is_valid_input("second hundred and third"))
```

**test_is_valid_input3**: `contradicts`
- reason: The docstring's own example says the hyphenated input "thirty-two" returns False, while this test and the reference code expect a hyphenated input containing "twenty-fifth" and "forty-second" to return True.
- missing: The docstring should state whether hyphenated compounds are split into separate words and checked individually, and whether ordinal forms (such as "fifth" or "second") count as valid words, and it should correct the example to match.

```python
def test_is_valid_input3(self):
    w2n = Words2Numbers()
    self.assertTrue(w2n.is_valid_input("twenty-fifth thousand three hundred and forty-second"))
```

**test_is_valid_input4**: `stated`
- reason: The docstring says the method returns False unless every word is a valid number word, and "eleventy" is not one, so a programmer following it would return False.

```python
def test_is_valid_input4(self):
    w2n = Words2Numbers()
    self.assertFalse(w2n.is_valid_input("eleventy thousand and five"))
```

**test_is_valid_input5**: `unstated`
- reason: The docstring says only that valid input contains words convertible to numbers, so a programmer could reasonably reject "and" or a bare "hundred" after "thousand", while the test expects True for such a phrase.
- missing: The docstring should state which connector words (such as "and") and multiplier words are accepted as valid input, and whether they are accepted in any position or only in certain grammatical forms.

```python
def test_is_valid_input5(self):
    w2n = Words2Numbers()
    self.assertTrue(w2n.is_valid_input("seventy two thousand and hundred eleven"))
```

**test_is_valid_input6**: `stated`
- reason: The docstring says valid words are those that can be converted into numbers, and "fifteenth" and "hundred" both convert to numbers, so a programmer would expect True, which matches the test.

```python
def test_is_valid_input6(self):
    w2n = Words2Numbers()
    self.assertTrue(w2n.is_valid_input("fifteenth hundred"))
```

## Tests in no method's test class

### `Words2NumbersTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    w2n = Words2Numbers()
    self.assertEqual(w2n.is_valid_input("seventy two thousand and hundred eleven"), True)
    self.assertEqual(w2n.text2int("seventy two thousand and hundred eleven"), "72011")
```
