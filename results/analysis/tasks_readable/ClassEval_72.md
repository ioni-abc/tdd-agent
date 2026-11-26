# ClassEval_72

## Skeleton (what the agent sees)

```python
import re

class RegexUtils:
    """
    The class provides to match, find all occurrences, split, and substitute text using regular expressions. It also includes predefined patterns, validating phone numbers and extracting email addresses.
    """


    def match(self, pattern, text):
        """
        Check if the text matches the regular expression
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: True or False, representing whether the text matches the regular expression or not
        >>> ru = RegexUtils()
        >>> ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890")
        True
        """

    def findall(self, pattern, text):
        """
        Find all matching substrings and return a list of all matching substrings
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: list of string, List of all matching substrings
        >>> ru = RegexUtils()
        >>> ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        ['123-456-7890', '876-286-9876', '987-762-9767']
        """

    def split(self, pattern, text):
        """
        Split text based on regular expression patterns and return a list of substrings
        :param pattern: string, Regular expression pattern
        :param text: string, Text to be split
        :return: list of string, List of substrings after splitting
        >>> ru = RegexUtils()
        >>> ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        ['', ' abiguygusu ', ' kjgufwycs ', '']
        """

    def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string
        :param pattern: string, Regular expression pattern
        :param replacement: Text to replace with
        :param text: string, Text to be replaced
        :return: string, Text after replacement
        >>> ru = RegexUtils()
        >>> ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',  "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        'phone num abiguygusu phone num kjgufwycs phone num'
        """

    def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses
        :return: string, regular expression patterns that match email addresses
        >>> ru = RegexUtils()
        >>> ru.generate_email_pattern()
        '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        """

    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\b\d{3}-\d{3}-\d{4}\b'
        """

    def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the middle characters of two sentences
        :return: string, regular expression patterns that match the middle characters of two sentences
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
        '[.!?][\s]{1,2}(?=[A-Z])'
        """

    def split_sentences(self, text):
        """
        Split the text into a list of sentences without Punctuation except the last sentence
        :param text: Text to be split
        :return: Split Text List
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """

    def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid
        :param phone_number: Phone number to be verified
        :return: True or False, indicating whether the phone number is valid
        >>> ru = RegexUtils()
        >>> ru.validate_phone_number("123-456-7890")
        True
        """

    def extract_email(self, text):
        """
        Extract all email addresses from the text
        :param text: string, input text
        :return: list of string, All extracted email addresses
        >>> ru = RegexUtils()
        >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
        """
```

## Method `match`

### Docstring

```python
def match(self, pattern, text):
        """
        Check if the text matches the regular expression
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: True or False, representing whether the text matches the regular expression or not
        >>> ru = RegexUtils()
        >>> ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890")
        True
        """
```

### Reference code (`solution_code`)

```python
def match(self, pattern, text):
        ans = re.match(pattern, text)
        if ans:
            return True
        else:
            return False
```

### Tests (`RegexUtilsTestMatch`)

**test_match_1**: `stated`
- reason: The docstring says match returns True when the text matches the regular expression, and the test's phone-number string matches its pattern, so a programmer following the docstring would return True.

```python
def test_match_1(self):
    ru = RegexUtils()
    res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890")
    self.assertEqual(res, True)
```

**test_match_2**: `stated`
- reason: The docstring says the method returns whether the text matches the regular expression, so a programmer applying that pattern to a string lacking the required separators would correctly return False, which is what the test expects.

```python
def test_match_2(self):
    ru = RegexUtils()
    res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "1234567890")
    self.assertEqual(res, False)
```

**test_match_3**: `stated`
- reason: The docstring's example applies the same phone-number pattern to a matching string and expects True, so a programmer following it would return True for this similarly formatted input.

```python
def test_match_3(self):
    ru = RegexUtils()
    res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "111-111-1111")
    self.assertEqual(res, True)
```

**test_match_4**: `stated`
- reason: The docstring says the method returns True only when the text matches the regular expression and False otherwise, so a programmer would return False here because "123-456-789" lacks the required four-digit final group.

```python
def test_match_4(self):
    ru = RegexUtils()
    res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-789")
    self.assertEqual(res, False)
```

**test_match_5**: `stated`
- reason: The docstring says the method returns True or False for whether the text matches the regular expression, so a programmer would return False for a phone-like string that has a non-digit where the final digit should be, and the test expects exactly that.

```python
def test_match_5(self):
    ru = RegexUtils()
    res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-789a")
    self.assertEqual(res, False)
```

## Method `findall`

### Docstring

```python
def findall(self, pattern, text):
        """
        Find all matching substrings and return a list of all matching substrings
        :param pattern: string, Regular expression pattern
        :param text: string, Text to match
        :return: list of string, List of all matching substrings
        >>> ru = RegexUtils()
        >>> ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        ['123-456-7890', '876-286-9876', '987-762-9767']
        """
```

### Reference code (`solution_code`)

```python
def findall(self, pattern, text):
        return re.findall(pattern, text)
```

### Tests (`RegexUtilsTestFindall`)

**test_findall_1**: `stated`
- reason: The docstring says findall returns a list of all matching substrings for a regex pattern, which is exactly what the test checks with a phone-number pattern over a text containing three matches.

```python
def test_findall_1(self):
    ru = RegexUtils()
    res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, ['123-456-7890', '876-286-9876', '987-762-9767'])
```

**test_findall_2**: `stated`
- reason: The docstring says findall returns a list of all matching substrings, so a programmer would return the single regex match in the text, which is what the test expects.

```python
def test_findall_2(self):
    ru = RegexUtils()
    res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "abiguygusu  kjgufwycs 987-762-9767")
    self.assertEqual(res, ['987-762-9767'])
```

**test_findall_3**: `stated`
- reason: The docstring says findall returns a list of all matching substrings, so when nothing matches a programmer would return an empty list, which is what the test expects.

```python
def test_findall_3(self):
    ru = RegexUtils()
    res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "abiguygusu  kjgufwycs ")
    self.assertEqual(res, [])
```

**test_findall_4**: `stated`
- reason: The docstring says findall returns a list of all matching substrings for a regex pattern, which is exactly what the test checks: two phone-number matches in a longer string, with the \b word-boundary pattern applied.

```python
def test_findall_4(self):
    ru = RegexUtils()
    res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "abiguygusu  111-111-1111 kjgufwycs 987-762-9767")
    self.assertEqual(res, ['111-111-1111', '987-762-9767'])
```

**test_findall_5**: `stated`
- reason: The docstring says findall returns all substrings matching the regex pattern, so a programmer using re.findall would return only the full-format phone number and skip the near-miss "111-111-111a", which has only three digits in the last group.

```python
def test_findall_5(self):
    ru = RegexUtils()
    res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "abiguygusu  111-111-111a kjgufwycs 987-762-9767")
    self.assertEqual(res, ['987-762-9767'])
```

## Method `split`

### Docstring

```python
def split(self, pattern, text):
        """
        Split text based on regular expression patterns and return a list of substrings
        :param pattern: string, Regular expression pattern
        :param text: string, Text to be split
        :return: list of string, List of substrings after splitting
        >>> ru = RegexUtils()
        >>> ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        ['', ' abiguygusu ', ' kjgufwycs ', '']
        """
```

### Reference code (`solution_code`)

```python
def split(self, pattern, text):
        return re.split(pattern, text)
```

### Tests (`RegexUtilsTestSplit`)

**test_split_1**: `stated`
- reason: The docstring's own example shows the same leading and trailing empty strings and the same middle substrings that the test expects, so a programmer implementing re.split would pass.

```python
def test_split_1(self):
    ru = RegexUtils()
    res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, ['', ' abiguygusu ', ' kjgufwycs ', ''])
```

**test_split_2**: `stated`
- reason: The docstring defines split as regex splitting with the example showing re.split semantics (empty leading and trailing pieces kept), so a programmer would naturally return the whole text as a single element when the pattern never matches, which is what the test expects.

```python
def test_split_2(self):
    ru = RegexUtils()
    res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "1234567890 abiguygusu 8762869876 kjgufwycs 9877629767")
    self.assertEqual(res, ['1234567890 abiguygusu 8762869876 kjgufwycs 9877629767'])
```

**test_split_3**: `stated`
- reason: The docstring's own example splits on the same pattern and shows the empty strings at the start and end of the result, so a programmer implementing a regex split would produce the test's expected output.

```python
def test_split_3(self):
    ru = RegexUtils()
    res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "111-111-1111 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, ['', ' abiguygusu ', ' kjgufwycs ', ''])
```

**test_split_4**: `stated`
- reason: The docstring says split uses regex patterns to split text and return the substrings, which is exactly what re.split does, so a programmer following it would produce the expected list for this input.

```python
def test_split_4(self):
    ru = RegexUtils()
    res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, ['123456-7890 abiguygusu ', ' kjgufwycs ', ''])
```

**test_split_5**: `stated`
- reason: The docstring says to split text on the regex pattern and return the substrings, with an example showing empty leading and trailing pieces, so a programmer using standard regex splitting would produce this test's output, since the "789a" sequence fails the pattern's word-boundary and four-digit requirements.

```python
def test_split_5(self):
    ru = RegexUtils()
    res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-789a abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, ['123-456-789a abiguygusu ', ' kjgufwycs ', ''])
```

## Method `sub`

### Docstring

```python
def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string
        :param pattern: string, Regular expression pattern
        :param replacement: Text to replace with
        :param text: string, Text to be replaced
        :return: string, Text after replacement
        >>> ru = RegexUtils()
        >>> ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',  "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        'phone num abiguygusu phone num kjgufwycs phone num'
        """
```

### Reference code (`solution_code`)

```python
def sub(self, pattern, replacement, text):
        return re.sub(pattern, replacement, text)
```

### Tests (`RegexUtilsTestSub`)

**test_sub_1**: `stated`
- reason: The docstring says sub replaces regex-matched substrings with the replacement text and gives an example with the same phone-number pattern and expected output, so a programmer following it would pass this test.

```python
def test_sub_1(self):
    ru = RegexUtils()
    res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                 "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, 'phone num abiguygusu phone num kjgufwycs phone num')
```

**test_sub_2**: `stated`
- reason: The docstring says to replace whatever the regex matches, so a programmer would implement a plain regex substitution, which leaves the text unchanged when nothing matches, as this test expects.

```python
def test_sub_2(self):
    ru = RegexUtils()
    res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                 "1234567890 abiguygusu 8762869876 kjgufwycs 9877629767")
    self.assertEqual(res, "1234567890 abiguygusu 8762869876 kjgufwycs 9877629767")
```

**test_sub_3**: `stated`
- reason: The docstring says matches of the regex are replaced with the given string, so a programmer using standard regex substitution would leave the malformed "123456-7890" untouched and pass.

```python
def test_sub_3(self):
    ru = RegexUtils()
    res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                 "123456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, '123456-7890 abiguygusu phone num kjgufwycs phone num')
```

**test_sub_4**: `stated`
- reason: The docstring says the regex-matched substring is replaced with the given text, so a programmer using standard regex substitution would leave the non-matching "789a" sequence unchanged and produce the expected output.

```python
def test_sub_4(self):
    ru = RegexUtils()
    res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                 "123-456-789a abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, '123-456-789a abiguygusu phone num kjgufwycs phone num')
```

**test_sub_5**: `stated`
- reason: The docstring says sub replaces every substring matched by the regex pattern with the replacement text, so a programmer implementing that would leave the non-matching "123-456-780" untouched and replace the two valid phone numbers, which is what the test expects.

```python
def test_sub_5(self):
    ru = RegexUtils()
    res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                 "123-456-780 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, '123-456-780 abiguygusu phone num kjgufwycs phone num')
```

## Method `generate_email_pattern`

### Docstring

```python
def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses
        :return: string, regular expression patterns that match email addresses
        >>> ru = RegexUtils()
        >>> ru.generate_email_pattern()
        '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        """
```

### Reference code (`solution_code`)

```python
def generate_email_pattern(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return pattern
```

### Tests (`RegexUtilsTestGenerateEmailPattern`)

**test_generate_email_pattern_1**: `stated`
- reason: The docstring says the method returns a regex pattern that matches email addresses, and the test checks that the returned pattern matches a valid email address.

```python
def test_generate_email_pattern_1(self):
    ru = RegexUtils()
    pat = ru.generate_email_pattern()
    res = ru.match(pat, 'iustd87t2euh@163.com')
    self.assertEqual(res, True)
```

**test_generate_email_pattern_2**: `stated`
- reason: The docstring says the pattern matches email addresses, so a programmer writing an email regex would expect a string with no "@" to fail to match, which is what this test checks.

```python
def test_generate_email_pattern_2(self):
    ru = RegexUtils()
    pat = ru.generate_email_pattern()
    res = ru.match(pat, 'iustd87t2euhifg.com')
    self.assertEqual(res, False)
```

**test_generate_email_pattern_3**: `stated`
- reason: The docstring says the pattern matches email addresses, so a programmer would write a standard email regex that rejects a malformed address like one with an empty domain label before the TLD, which is what the test expects.

```python
def test_generate_email_pattern_3(self):
    ru = RegexUtils()
    pat = ru.generate_email_pattern()
    res = ru.match(pat, 'iustd87t2euhifg@.com')
    self.assertEqual(res, False)
```

**test_generate_email_pattern_4**: `stated`
- reason: The docstring says the pattern should match email addresses, so a programmer writing a correct email regex would reject the input 'iustd87t2euhifg@.', which has no domain or top-level domain and so fails the test's expected False.

```python
def test_generate_email_pattern_4(self):
    ru = RegexUtils()
    pat = ru.generate_email_pattern()
    res = ru.match(pat, 'iustd87t2euhifg@.')
    self.assertEqual(res, False)
```

**test_generate_email_pattern_5**: `stated`
- reason: The docstring says the pattern should match email addresses, so a programmer would write the usual regex, which rejects "iustd87t2euhifg@com." because nothing follows the final dot to form a top-level domain.

```python
def test_generate_email_pattern_5(self):
    ru = RegexUtils()
    pat = ru.generate_email_pattern()
    res = ru.match(pat, 'iustd87t2euhifg@com.')
    self.assertEqual(res, False)
```

## Method `generate_phone_number_pattern`

### Docstring

```python
def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\b\d{3}-\d{3}-\d{4}\b'
        """
```

### Reference code (`solution_code`)

```python
def generate_phone_number_pattern(self):
        pattern = r'\b\d{3}-\d{3}-\d{4}\b'
        return pattern
```

### Tests (`RegexUtilsTestGeneratePhoneNumberPattern`)

**test_generate_phone_number_pattern_1**: `stated`
- reason: The docstring's example output gives the exact pattern `\b\d{3}-\d{3}-\d{4}\b`, which matches the 3-3-4 dashed format in the test input, so a programmer following it would pass.

```python
def test_generate_phone_number_pattern_1(self):
    ru = RegexUtils()
    pat = ru.generate_phone_number_pattern()
    res = ru.match(pat, '123-456-7890')
    self.assertEqual(res, True)
```

**test_generate_phone_number_pattern_2**: `unstated`
- reason: The test expects the pattern to reject an undelimited 10-digit string, which requires the hyphen-separated XXX-XXX-XXXX format, but the docstring only says the pattern matches "phone numbers" without naming that format.
- missing: The docstring should state the exact accepted phone number format, including whether separators such as hyphens are required between digit groups, so that undelimited digit strings are rejected.

```python
def test_generate_phone_number_pattern_2(self):
    ru = RegexUtils()
    pat = ru.generate_phone_number_pattern()
    res = ru.match(pat, '1234567890')
    self.assertEqual(res, False)
```

**test_generate_phone_number_pattern_3**: `unstated`
- reason: The docstring says only that the pattern matches "phone numbers" without giving the format, so a programmer could write a different phone pattern that accepts or rejects inputs differently from the expected 3-3-4 dashed format this test checks.
- missing: The docstring should state the exact digit-group lengths and separators the generated pattern must accept and reject, such as the number of digits in each group and which separator characters are required.

```python
def test_generate_phone_number_pattern_3(self):
    ru = RegexUtils()
    pat = ru.generate_phone_number_pattern()
    res = ru.match(pat, '123-456-789')
    self.assertEqual(res, False)
```

**test_generate_phone_number_pattern_4**: `unstated`
- reason: The docstring only says the method returns a pattern that matches phone numbers, so a programmer could pick a different format or boundary rule, and the test's expectation that a leading letter blocks the match depends on a specific format and word-boundary anchoring the docstring never gives.
- missing: The docstring should state the exact phone number format the pattern must match (digit groups and separators) and whether matches must be bounded so that digits directly preceded or followed by a letter or digit are rejected.

```python
def test_generate_phone_number_pattern_4(self):
    ru = RegexUtils()
    pat = ru.generate_phone_number_pattern()
    res = ru.match(pat, 'a23-456-7890')
    self.assertEqual(res, False)
```

**test_generate_phone_number_pattern_5**: `stated`
- reason: The docstring's example pattern `\b\d{3}-\d{3}-\d{4}\b` specifies a 3-3-4 digit format, so a programmer would produce a pattern that rejects the 4-2-4 string `'1234-56-7890'`, which is what the test expects.

```python
def test_generate_phone_number_pattern_5(self):
    ru = RegexUtils()
    pat = ru.generate_phone_number_pattern()
    res = ru.match(pat, '1234-56-7890')
    self.assertEqual(res, False)
```

## Method `generate_split_sentences_pattern`

### Docstring

```python
def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the middle characters of two sentences
        :return: string, regular expression patterns that match the middle characters of two sentences
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
        '[.!?][\s]{1,2}(?=[A-Z])'
        """
```

### Reference code (`solution_code`)

```python
def generate_split_sentences_pattern(self):
        pattern = r'[.!?][\s]{1,2}(?=[A-Z])'
        return pattern
```

### Tests (`RegexUtilsTestGenerateSplitSentencesPattern`)

**test_generate_split_sentences_pattern_1**: `stated`
- reason: A programmer reading that the pattern matches the middle of two sentences would write a sentence-boundary pattern (sentence-ending punctuation, whitespace, then an uppercase letter), which matches '? Y', so the test's expectation follows from the docstring.

```python
def test_generate_split_sentences_pattern_1(self):
    ru = RegexUtils()
    pat = ru.generate_split_sentences_pattern()
    res = ru.match(pat, '? Y')
    self.assertEqual(res, True)
```

**test_generate_split_sentences_pattern_2**: `unstated`
- reason: The docstring says only that the pattern matches "the middle characters of two sentences", so a correct implementation could leave out `!` as a sentence-ending mark or require a different amount of whitespace, and then fail on `'! Y'`.
- missing: The docstring should list exactly which sentence-ending punctuation marks count, how much whitespace may separate them from the next sentence, and that the next sentence must start with an uppercase letter.

```python
def test_generate_split_sentences_pattern_2(self):
    ru = RegexUtils()
    pat = ru.generate_split_sentences_pattern()
    res = ru.match(pat, '! Y')
    self.assertEqual(res, True)
```

**test_generate_split_sentences_pattern_3**: `stated`
- reason: The docstring's example output is the exact pattern `[.!?][\s]{1,2}(?=[A-Z])`, so a programmer following it would require an uppercase letter after the punctuation and whitespace, and the test's input with no following capital correctly fails to match.

```python
def test_generate_split_sentences_pattern_3(self):
    ru = RegexUtils()
    pat = ru.generate_split_sentences_pattern()
    res = ru.match(pat, '? ')
    self.assertEqual(res, False)
```

**test_generate_split_sentences_pattern_4**: `stated`
- reason: The docstring's example gives the exact regex, which requires punctuation, then 1–2 whitespace characters, then an uppercase letter, so a string with no whitespace after the punctuation should not match.

```python
def test_generate_split_sentences_pattern_4(self):
    ru = RegexUtils()
    pat = ru.generate_split_sentences_pattern()
    res = ru.match(pat, '?Y')
    self.assertEqual(res, False)
```

**test_generate_split_sentences_pattern_5**: `unstated`
- reason: The docstring only describes the pattern as matching the middle of two sentences, so a programmer could reasonably allow zero whitespace between the punctuation and the capital letter and wrongly match `.Y`, and the test would fail.
- missing: The docstring should state that a sentence boundary requires between one and two whitespace characters between the terminal punctuation mark (., !, or ?) and the following uppercase letter, so a bare punctuation mark directly followed by a letter does not count.

```python
def test_generate_split_sentences_pattern_5(self):
    ru = RegexUtils()
    pat = ru.generate_split_sentences_pattern()
    res = ru.match(pat, '.Y')
    self.assertEqual(res, False)
```

## Method `split_sentences`

### Docstring

```python
def split_sentences(self, text):
        """
        Split the text into a list of sentences without Punctuation except the last sentence
        :param text: Text to be split
        :return: Split Text List
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """
```

### Reference code (`solution_code`)

```python
def split_sentences(self, text):
        pattern = self.generate_split_sentences_pattern()
        return self.split(pattern, text)
```

### Tests (`RegexUtilsTestSplitSentences`)

**test_split_sentences_1**: `stated`
- reason: The docstring's example input "Aaa. Bbbb? Ccc!" yields ['Aaa', 'Bbbb', 'Ccc!'], which is exactly the case the test checks, so a programmer following the docstring would pass.

```python
def test_split_sentences_1(self):
    ru = RegexUtils()
    res = ru.split_sentences("Aaa. Bbbb? Ccc!")
    self.assertEqual(res, ['Aaa', 'Bbbb', 'Ccc!'])
```

**test_split_sentences_2**: `unstated`
- reason: The docstring says to split on sentence punctuation, so a programmer would likely split at the period in "Aaa.Bbbb", but the test expects no split there, which only happens if a boundary requires whitespace after the punctuation.
- missing: The docstring should say that a sentence-ending mark (. ? !) only ends a sentence when it is followed by whitespace or the end of the text, so a mark directly followed by a letter does not split.

```python
def test_split_sentences_2(self):
    ru = RegexUtils()
    res = ru.split_sentences("Aaa.Bbbb? Ccc!")
    self.assertEqual(res, ['Aaa.Bbbb', 'Ccc!'])
```

**test_split_sentences_3**: `unstated`
- reason: A programmer reading the docstring would split at every sentence-ending punctuation mark, giving ['Aaa', 'bbbb', 'Ccc!'], but the test expects no split where a period is followed by a lowercase word, which the docstring never mentions.
- missing: The docstring should say when a sentence-ending mark counts as a boundary, such as only when the next word starts with an uppercase letter, and that a mark followed by a lowercase word does not end a sentence.

```python
def test_split_sentences_3(self):
    ru = RegexUtils()
    res = ru.split_sentences("Aaa. bbbb? Ccc!")
    self.assertEqual(res, ['Aaa. bbbb', 'Ccc!'])
```

**test_split_sentences_4**: `unstated`
- reason: The docstring says to split on sentence punctuation, so a programmer would split "Aaa. bbbb, Ccc!" after "Aaa", but the test expects no split because the next word is lowercase.
- missing: The docstring should say whether a sentence boundary is recognised only when the following text starts with an uppercase letter, and what happens to punctuation-separated text that does not meet that condition.

```python
def test_split_sentences_4(self):
    ru = RegexUtils()
    res = ru.split_sentences("Aaa. bbbb, Ccc!")
    self.assertEqual(res, ['Aaa. bbbb, Ccc!'])
```

**test_split_sentences_5**: `stated`
- reason: The docstring says sentences are split with their terminal punctuation removed except on the last sentence, which is exactly what this test checks: the `?` is dropped, the final `!` is kept, and the comma stays inside the first sentence.

```python
def test_split_sentences_5(self):
    ru = RegexUtils()
    res = ru.split_sentences("Aaa, Bbbb? Ccc!")
    self.assertEqual(res, ['Aaa, Bbbb', 'Ccc!'])
```

## Method `validate_phone_number`

### Docstring

```python
def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid
        :param phone_number: Phone number to be verified
        :return: True or False, indicating whether the phone number is valid
        >>> ru = RegexUtils()
        >>> ru.validate_phone_number("123-456-7890")
        True
        """
```

### Reference code (`solution_code`)

```python
def validate_phone_number(self, phone_number):
        pattern = self.generate_phone_number_pattern()
        return self.match(pattern, phone_number)
```

### Tests (`RegexUtilsTestValidatePhoneNumber`)

**test_validate_phone_number_1**: `stated`
- reason: The docstring's own example passes "123-456-7890" and shows the expected result True, which is exactly what this test checks.

```python
def test_validate_phone_number_1(self):
    ru = RegexUtils()
    res = ru.validate_phone_number("123-456-7890")
    self.assertEqual(res, True)
```

**test_validate_phone_number_2**: `unstated`
- reason: The docstring gives only "123-456-7890" as a valid example, so a programmer would not know whether a ten-digit string without dashes must be rejected, and the test expects False for exactly that input.
- missing: The docstring should state the exact accepted phone number format, including whether separators such as dashes are required or optional and which digit groupings are valid.

```python
def test_validate_phone_number_2(self):
    ru = RegexUtils()
    res = ru.validate_phone_number("1234567890")
    self.assertEqual(res, False)
```

**test_validate_phone_number_3**: `stated`
- reason: A programmer reading "Verify if the phone number is valid" with the digits-and-dashes example would reject "a23-456-7890" because it contains a letter, so the expected False follows from the docstring.

```python
def test_validate_phone_number_3(self):
    ru = RegexUtils()
    res = ru.validate_phone_number("a23-456-7890")
    self.assertEqual(res, False)
```

**test_validate_phone_number_4**: `unstated`
- reason: The docstring only says "verify if the phone number is valid" with one passing example, so a programmer could reasonably accept a 9-digit number with dashes, while the test expects it to be rejected.
- missing: The docstring should state the exact accepted phone number format, including the required number of digits and the allowed separators, and that any input deviating from it (such as too few digits) returns False.

```python
def test_validate_phone_number_4(self):
    ru = RegexUtils()
    res = ru.validate_phone_number("123-456-789")
    self.assertEqual(res, False)
```

**test_validate_phone_number_5**: `unstated`
- reason: The docstring gives only one valid example ("123-456-7890") and never says which digit grouping is required, so a programmer could reasonably accept "1234-56-789" as valid, and the test's expected False depends on a format the docstring does not state.
- missing: The docstring should specify the exact accepted phone number format (number of digits in each group, allowed separators, and whether other characters or lengths are rejected), so that any input not matching that format is known to return False.

```python
def test_validate_phone_number_5(self):
    ru = RegexUtils()
    res = ru.validate_phone_number("1234-56-789")
    self.assertEqual(res, False)
```

## Method `extract_email`

### Docstring

```python
def extract_email(self, text):
        """
        Extract all email addresses from the text
        :param text: string, input text
        :return: list of string, All extracted email addresses
        >>> ru = RegexUtils()
        >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
        """
```

### Reference code (`solution_code`)

```python
def extract_email(self, text):
        pattern = self.generate_email_pattern()
        return self.findall(pattern, text)
```

### Tests (`RegexUtilsTestExtractEmail`)

**test_extract_email_1**: `stated`
- reason: The docstring says to extract all email addresses from the text and return them as a list, which is exactly what the test checks with three space-separated addresses.

```python
def test_extract_email_1(self):
    ru = RegexUtils()
    res = ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
    self.assertEqual(res, ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com'])
```

**test_extract_email_2**: `unstated`
- reason: The docstring says "all email addresses" without defining what counts as one, so a programmer could not know that an address with an empty domain label (like the one in the input) must be excluded.
- missing: The docstring should define the valid email format, stating that each address needs a non-empty local part and a non-empty domain name before the top-level suffix, and that malformed strings lacking these parts are not returned.

```python
def test_extract_email_2(self):
    ru = RegexUtils()
    res = ru.extract_email("abcdefg@.com ygusyfysy@126.com wljduyuv@qq.com")
    self.assertEqual(res, ['ygusyfysy@126.com', 'wljduyuv@qq.com'])
```

**test_extract_email_3**: `stated`
- reason: The docstring says to extract all email addresses from the text, so a programmer would naturally skip the non-email token "abcdefgiscom" and return only the two valid addresses, as the test expects.

```python
def test_extract_email_3(self):
    ru = RegexUtils()
    res = ru.extract_email("abcdefgiscom ygusyfysy@126.com wljduyuv@qq.com")
    self.assertEqual(res, ['ygusyfysy@126.com', 'wljduyuv@qq.com'])
```

**test_extract_email_4**: `stated`
- reason: The docstring asks for all email addresses in the text, so a programmer would reasonably return only the well-formed address and skip the strings that lack an "@" and a proper structure, which is what the test expects.

```python
def test_extract_email_4(self):
    ru = RegexUtils()
    res = ru.extract_email("abcdefgiscom ygusyfysy126.com wljduyuv@qq.com")
    self.assertEqual(res, ['wljduyuv@qq.com'])
```

**test_extract_email_5**: `unstated`
- reason: The docstring says to extract "all email addresses" but does not define what counts as one, so a programmer could reasonably accept or reject the malformed tokens "abcdefgiscom" (no @) and "ygusyfysy@.com" (empty domain label) that this test expects to be skipped.
- missing: The docstring should state the validity rule for an email address, such as requiring a non-empty local part, an @ sign, and a non-empty domain made of labels separated by dots, with anything not meeting that rule excluded from the result.

```python
def test_extract_email_5(self):
    ru = RegexUtils()
    res = ru.extract_email("abcdefgiscom ygusyfysy@.com wljduyuv@qq.com")
    self.assertEqual(res, ['wljduyuv@qq.com'])
```

## Tests in no method's test class

### `RegexUtilsTest`

**test_regexutils**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_regexutils(self):
    ru = RegexUtils()
    res = ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890")
    self.assertEqual(res, True)

    res = ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, ['123-456-7890', '876-286-9876', '987-762-9767'])

    res = ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, ['', ' abiguygusu ', ' kjgufwycs ', ''])

    res = ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',
                 "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    self.assertEqual(res, 'phone num abiguygusu phone num kjgufwycs phone num')

    pat = ru.generate_email_pattern()
    res = ru.match(pat, 'iustd87t2euh@163.com')
    self.assertEqual(res, True)

    pat = ru.generate_phone_number_pattern()
    res = ru.match(pat, '123-456-7890')
    self.assertEqual(res, True)

    pat = ru.generate_split_sentences_pattern()
    res = ru.match(pat, '? Y')
    self.assertEqual(res, True)

    res = ru.split_sentences("Aaa. Bbbb? Ccc!")
    self.assertEqual(res, ['Aaa', 'Bbbb', 'Ccc!'])

    res = ru.validate_phone_number("123-456-7890")
    self.assertEqual(res, True)

    res = ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
    self.assertEqual(res, ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com'])
```
