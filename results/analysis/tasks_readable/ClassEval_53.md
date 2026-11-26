# ClassEval_53

## Skeleton (what the agent sees)

```python
import re
import string

class LongestWord:
    """
    This is a class allows to add words to a list and find the longest word in a given sentence by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of word.
        """
        self.word_list = []

    def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
```

## Method `add_word`

### Docstring

```python
def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """
```

### Reference code (`solution_code`)

```python
def add_word(self, word):
        self.word_list.append(word)
```

### Tests (`LongestWordTestAddWord`)

**test_add_word_1**: `stated`
- reason: The docstring says the input word is appended to self.word_list, which is exactly what the test checks (after adding "hello" to an empty list, the list equals ['hello']).

```python
def test_add_word_1(self):
    longestWord = LongestWord()
    longestWord.add_word("hello")
    self.assertEqual(['hello'], longestWord.word_list)
```

**test_add_word_2**: `stated`
- reason: The docstring says the method appends the input word to self.word_list, so a programmer would append each word in call order, which is what the test checks after two calls.

```python
def test_add_word_2(self):
    longestWord = LongestWord()
    longestWord.add_word("hello")
    longestWord.add_word("world")
    self.assertEqual(['hello', 'world'], longestWord.word_list)
```

**test_add_word_3**: `stated`
- reason: The docstring says add_word appends the input word to self.word_list, which is exactly what the test checks when it adds three words in sequence and expects them in insertion order.

```python
def test_add_word_3(self):
    longestWord = LongestWord()
    longestWord.add_word("hello")
    longestWord.add_word("world")
    longestWord.add_word("!")
    self.assertEqual(['hello', 'world', '!'], longestWord.word_list)
```

**test_add_word_4**: `stated`
- reason: The docstring says the input word is appended to self.word_list, and the test simply adds several words (including a duplicate) and checks that the list holds them all in insertion order, which a programmer following the docstring would pass.

```python
def test_add_word_4(self):
    longestWord = LongestWord()
    longestWord.add_word("hello")
    longestWord.add_word("world")
    longestWord.add_word("!")
    longestWord.add_word("!")
    self.assertEqual(['hello', 'world', '!', '!'], longestWord.word_list)
```

**test_add_word_5**: `stated`
- reason: The docstring says the method appends the input word to self.word_list, so a programmer following it would append each word in call order, keeping duplicates, which is what the test checks.

```python
def test_add_word_5(self):
    longestWord = LongestWord()
    longestWord.add_word("hello")
    longestWord.add_word("world")
    longestWord.add_word("!")
    longestWord.add_word("!")
    longestWord.add_word("!")
    self.assertEqual(['hello', 'world', '!', '!', '!'], longestWord.word_list)
```

## Method `find_longest_word`

### Docstring

```python
def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
```

### Reference code (`solution_code`)

```python
def find_longest_word(self, sentence):
        longest_word = ""
        sentence = sentence.lower()
        sentence = re.sub('[%s]' % re.escape(string.punctuation), '', sentence)
        sentence = re.split(' ', sentence)
        for word in sentence:
            if word in self.word_list and len(word) > len(longest_word):
                longest_word = word
        return longest_word
```

### Tests (`LongestWordTestFindLongestWord`)

**test_find_longest_word_1**: `stated`
- reason: The docstring says to strip punctuation, split the sentence into words, and return the longest one found in self.word_list, so a programmer would produce 'a' for this input, matching the test.

```python
def test_find_longest_word_1(self):
    longestWord = LongestWord()
    longestWord.add_word("a")
    sentence = 'I am a student.'
    self.assertEqual('a', longestWord.find_longest_word(sentence))
```

**test_find_longest_word_2**: `stated`
- reason: The docstring says the method returns '' when self.word_list is empty, and this test builds a fresh LongestWord with no words added and expects '', so a programmer following the docstring would pass.

```python
def test_find_longest_word_2(self):
    longestWord = LongestWord()
    sentence = 'I am a student.'
    self.assertEqual('', longestWord.find_longest_word(sentence))
```

**test_find_longest_word_3**: `stated`
- reason: The docstring says to strip punctuation, split the sentence into words, and return the longest word that is in the word list, so a programmer would produce 'student' from 'I am a student.' with "student" in the list.

```python
def test_find_longest_word_3(self):
    longestWord = LongestWord()
    longestWord.add_word("student")
    sentence = 'I am a student.'
    self.assertEqual('student', longestWord.find_longest_word(sentence))
```

**test_find_longest_word_4**: `contradicts`
- reason: The docstring says words are strictly case sensitive, so 'Apple' should not match 'apple', but the test and reference code lowercase the sentence and expect 'apple' to be returned.
- missing: The docstring should state that the sentence is lowercased before matching, so any capitalized word in a sentence matches a lowercase entry in the word list, and it should drop or qualify the claim that matching is strictly case sensitive.

```python
def test_find_longest_word_4(self):
    longestWord = LongestWord()
    longestWord.add_word("apple")
    sentence = 'Apple is red.'
    self.assertEqual('apple', longestWord.find_longest_word(sentence))
```

**test_find_longest_word_5**: `contradicts`
- reason: The docstring says matching is strictly case sensitive, so a capitalized sentence word like "Apple" should not match a lowercase list entry, but the test and reference code lowercase the sentence and expect that match.
- missing: The docstring should state whether the sentence is lowercased before matching, and that words in the sentence match list entries regardless of capitalization, since the stated case-sensitivity conflicts with the expected behaviour.

```python
def test_find_longest_word_5(self):
    longestWord = LongestWord()
    longestWord.add_word("apple")
    longestWord.add_word("red")
    sentence = 'Apple is red.'
    self.assertEqual('apple', longestWord.find_longest_word(sentence))
```
