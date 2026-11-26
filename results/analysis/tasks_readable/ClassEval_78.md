# ClassEval_78

## Skeleton (what the agent sees)

```python
import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """


    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
```

## Method `split_sentences`

### Docstring

```python
def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
```

### Reference code (`solution_code`)

```python
def split_sentences(self, sentences_string):
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', sentences_string)
        return sentences
```

### Tests (`SplitSentenceTestSplitSentences`)

**test_split_sentences_1**: `stated`
- reason: The docstring explicitly says sentences end with "." or "?" followed by a space, and its own example is the same input and expected output the test checks, so a programmer following it would pass.

```python
def test_split_sentences_1(self):
    ss = SplitSentence()
    lst = ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    self.assertEqual(lst, ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?'])
```

**test_split_sentences_2**: `stated`
- reason: The docstring says sentences end with "." or "?" followed by a space, and explicitly notes that "Mr." ends with a period but is not a sentence end, so a programmer would keep "Mr. Smith?" together and split after "?".

```python
def test_split_sentences_2(self):
    ss = SplitSentence()
    lst = ss.split_sentences("Who is Mr. Smith? He is a teacher.")
    self.assertEqual(lst, ['Who is Mr. Smith?', 'He is a teacher.'])
```

**test_split_sentences_3**: `stated`
- reason: The docstring says sentences end with "." or "?" followed by a space, so a programmer splitting there would produce ['Who is A.B.C.?', 'He is a teacher.'], which is what the test expects.

```python
def test_split_sentences_3(self):
    ss = SplitSentence()
    lst = ss.split_sentences("Who is A.B.C.? He is a teacher.")
    self.assertEqual(lst, ['Who is A.B.C.?', 'He is a teacher.'])
```

**test_split_sentences_4**: `stated`
- reason: The docstring says sentences end with "." or "?" followed by a space, and the test's first two sentences fit that rule, while the final sentence's trailing period is simply the end of the string, which a programmer splitting on those terminators would keep as the last element.

```python
def test_split_sentences_4(self):
    ss = SplitSentence()
    lst = ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc.")
    self.assertEqual(lst, ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.'])
```

**test_split_sentences_5**: `stated`
- reason: The docstring explicitly says sentences end with . or ? followed by a space, so splitting "aaa aaaa. bb bbbb bbb?" into ['aaa aaaa.', 'bb bbbb bbb?'] follows directly from the documented rule.

```python
def test_split_sentences_5(self):
    ss = SplitSentence()
    lst = ss.split_sentences("aaa aaaa. bb bbbb bbb?")
    self.assertEqual(lst, ['aaa aaaa.', 'bb bbbb bbb?'])
```

## Method `count_words`

### Docstring

```python
def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
```

### Reference code (`solution_code`)

```python
def count_words(self, sentence):
        sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)
        words = sentence.split()
        return len(words)
```

### Tests (`SplitSentenceTestCountWords`)

**test_count_words_1**: `stated`
- reason: The docstring defines words as space-separated tokens and gives the example `count_words("abc def")` returning 2, which is exactly what this test checks.

```python
def test_count_words_1(self):
    ss = SplitSentence()
    cnt = ss.count_words("abc def")
    self.assertEqual(cnt, 2)
```

**test_count_words_2**: `stated`
- reason: The docstring says numbers are not counted as words, so a programmer following it would count "abc" and "def" and skip "1", giving the expected 2.

```python
def test_count_words_2(self):
    ss = SplitSentence()
    cnt = ss.count_words("abc def 1")
    self.assertEqual(cnt, 2)
```

**test_count_words_3**: `stated`
- reason: The docstring says numbers are not counted as words, so a programmer would count only "abc" and get 1, matching the test.

```python
def test_count_words_3(self):
    ss = SplitSentence()
    cnt = ss.count_words("abc 1")
    self.assertEqual(cnt, 1)
```

**test_count_words_4**: `unstated`
- reason: The docstring says numbers are not counted as words, but it does not say whether a space-separated token that mixes letters and digits (like "bbb1") counts, so a correct implementation could go either way and fail this test.
- missing: The docstring should state how a space-separated token that mixes letters and digits is handled, for example whether its letters are kept as a word with the digits stripped or the whole token is dropped.

```python
def test_count_words_4(self):
    ss = SplitSentence()
    cnt = ss.count_words("abc def bbb1")
    self.assertEqual(cnt, 3)
```

**test_count_words_5**: `stated`
- reason: The docstring says numbers are not counted as words, so a programmer would count "abc" and "def" and skip "111", giving 2 as the test expects.

```python
def test_count_words_5(self):
    ss = SplitSentence()
    cnt = ss.count_words("abc def 111")
    self.assertEqual(cnt, 2)
```

## Method `process_text_file`

### Docstring

```python
def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
```

### Reference code (`solution_code`)

```python
def process_text_file(self, sentences_string):
        sentences = self.split_sentences(sentences_string)
        max_count = 0
        for sentence in sentences:
            count = self.count_words(sentence)
            if count > max_count:
                max_count = count

        return max_count
```

### Tests (`SplitSentenceTestProcessTextFile`)

**test_process_text_file_1**: `stated`
- reason: The docstring's own example uses the same input (sentences ending in "." and "?") and expects 4, so a programmer following it would return the word count of the longest sentence and pass this test.

```python
def test_process_text_file_1(self):
    ss = SplitSentence()
    cnt = ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
    self.assertEqual(cnt, 4)
```

**test_process_text_file_2**: `unstated`
- reason: The test expects 5 because "Mr." does not end a sentence, but the docstring never says how abbreviations or periods inside a sentence are handled, so a natural sentence split at every period would give 4 instead.
- missing: The docstring should state that a period is a sentence terminator only when it does not belong to an abbreviation or title (such as a name prefix followed by a capitalised word), so that such periods do not split the sentence.

```python
def test_process_text_file_2(self):
    ss = SplitSentence()
    cnt = ss.process_text_file("Mr. Smith is a teacher. Yes.")
    self.assertEqual(cnt, 5)
```

**test_process_text_file_3**: `unstated`
- reason: The docstring does not say whether numeric tokens count as words or whether an abbreviation period like "Mr." ends a sentence, so a reasonable implementation could produce a different maximum than the expected 5.
- missing: The docstring should specify what counts as a word (for example, whether pure-number tokens are included) and how sentence boundaries are detected when a period follows an abbreviation or appears inside a token.

```python
def test_process_text_file_3(self):
    ss = SplitSentence()
    cnt = ss.process_text_file("Mr. Smith is a teacher. Yes 1 2 3 4 5 6.")
    self.assertEqual(cnt, 5)
```

**test_process_text_file_4**: `stated`
- reason: The docstring says to return the word count of the longest sentence, and this test's input has sentences of 2, 3 and 4 words, so a programmer following it would return 4.

```python
def test_process_text_file_4(self):
    ss = SplitSentence()
    cnt = ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc.")
    self.assertEqual(cnt, 4)
```

**test_process_text_file_5**: `stated`
- reason: The docstring says to return the word count of the longest sentence, and the test's two sentences (2 and 3 words) give the expected 3 under that rule, matching the reference code.

```python
def test_process_text_file_5(self):
    ss = SplitSentence()
    cnt = ss.process_text_file("aaa aaaa. bb bbbb bbb?")
    self.assertEqual(cnt, 3)
```

## Tests in no method's test class

### `SplitSentenceTest`

**test_SplitSentence**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_SplitSentence(self):
    ss = SplitSentence()
    lst = ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    self.assertEqual(lst, ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?'])

    cnt = ss.count_words("abc def")
    self.assertEqual(cnt, 2)

    cnt = ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
    self.assertEqual(cnt, 4)
```
