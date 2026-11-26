# ClassEval_52

## Skeleton (what the agent sees)

```python
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string


nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    """
    This is a class about Lemmatization, which utilizes the nltk library to perform lemmatization and part-of-speech tagging on sentences, as well as remove punctuation.
    """

    def __init__(self):
        """
        creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

        """

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """
```

## Method `lemmatize_sentence`

### Docstring

```python
def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """
```

### Reference code (`solution_code`)

```python
def lemmatize_sentence(self, sentence):
        lemmatized_words = []
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        for word, tag in tagged_words:
            if tag.startswith('V'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
            elif tag.startswith('J'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
            elif tag.startswith('R'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='r')
            else:
                lemmatized_word = self.lemmatizer.lemmatize(word)
            lemmatized_words.append(lemmatized_word)
        return lemmatized_words
```

### Tests (`LemmatizationTestLemmatizeSentence`)

**test_lemmatize_sentence_1**: `stated`
- reason: The docstring's doctest uses the same input and expected output as the test, so a programmer following the described punctuation removal, POS-based lemmatization, and example would produce the expected list.

```python
def test_lemmatize_sentence_1(self):
    lemmatization = Lemmatization()
    result = lemmatization.lemmatize_sentence("I am running in a race.")
    expected = ['I', 'be', 'run', 'in', 'a', 'race']
    self.assertEqual(result, expected)
```

**test_lemmatize_sentence_2**: `unstated`
- reason: The docstring says punctuation is removed but not whether removal joins the surrounding characters or leaves a gap, so a correct implementation that replaces the apostrophe with a space would produce different tokens than the test expects.
- missing: The docstring should say that punctuation characters are deleted without inserting a space, so that a word with an internal apostrophe or other punctuation stays as one token with the mark removed.

```python
def test_lemmatize_sentence_2(self):
    lemmatization = Lemmatization()
    result = lemmatization.lemmatize_sentence("Until the beating, Cantanco's eyesight had been weak, but adequate.")
    expected = ['Until', 'the', 'beating', 'Cantancos', 'eyesight', 'have', 'be', 'weak', 'but', 'adequate']
    self.assertEqual(result, expected)
```

**test_lammatize_sentence_3**: `stated`
- reason: The docstring says punctuation is removed before tokenizing and that words are lemmatized according to their part of speech, which is what the test's expected output ("dog's" becoming "dog", "barked" becoming "bark") relies on.

```python
def test_lammatize_sentence_3(self):
    lemmatization = Lemmatization()
    result = lemmatization.lemmatize_sentence("The dog's barked at the mailman.")
    expected = ['The', 'dog', 'bark', 'at', 'the', 'mailman']
    self.assertEqual(result, expected)
```

**test_lemmatize_sentence_4**: `stated`
- reason: The docstring's described behaviour (remove punctuation, POS-tag, lemmatize verbs to base form) and its example "am" → "be" lead a programmer to produce "was" → "be", "running" → "run", "eating" → "eat", and keep the other words, matching the test.

```python
def test_lemmatize_sentence_4(self):
    lemmatization = Lemmatization()
    result = lemmatization.lemmatize_sentence("He was running and eating at same time. ")
    expected = ['He', 'be', 'run', 'and', 'eat', 'at', 'same', 'time']
    self.assertEqual(result, expected)
```

**test_lemmatize_sentence_5**: `stated`
- reason: The docstring says the method removes punctuation, tokenizes, POS-tags, and lemmatizes verbs, adjectives and adverbs by part of speech, and its example shows "am" becoming "be" and "running" becoming "run", so a programmer following it would produce "be" for "was" and "take" for "taking".

```python
def test_lemmatize_sentence_5(self):
    lemmatization = Lemmatization()
    result = lemmatization.lemmatize_sentence("I was taking a ride in the car.")
    expected = ['I', 'be', 'take', 'a', 'ride', 'in', 'the', 'car']
    self.assertEqual(result, expected)
```

## Method `get_pos_tag`

### Docstring

```python
def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

        """
```

### Reference code (`solution_code`)

```python
def get_pos_tag(self, sentence):
        pos_tags = []
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        for tagged_word in tagged_words:
            pos_tags.append(tagged_word[1])
        return pos_tags
```

### Tests (`LemmatizationTestGetPosTag`)

**test_get_pos_tag_1**: `stated`
- reason: The docstring's own example uses the same sentence and gives the same expected tag list, so a programmer following it would pass this test.

```python
def test_get_pos_tag_1(self):
    lemmatization = Lemmatization()
    result = lemmatization.get_pos_tag("I am running in a race.")
    expected = ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
    self.assertEqual(result, expected)
```

**test_get_pos_tag_2**: `stated`
- reason: The docstring says punctuation is removed before tokenizing and tagging, so a programmer following it would strip the apostrophe and comma and return one tag per remaining word, which matches the expected seven tags.

```python
def test_get_pos_tag_2(self):
    lemmatization = Lemmatization()
    result = lemmatization.get_pos_tag("Cantanco's eyesight had been weak, but adequate.")
    expected = ['NNP', 'NN', 'VBD', 'VBN', 'JJ', 'CC', 'JJ']
    self.assertEqual(result, expected)
```

**test_get_pos_tag_3**: `unstated`
- reason: The test expects the possessive apostrophe in "dog's" to be removed so the word becomes "dogs" (tagged NNS), but the docstring only says "remove punctuations" without saying whether apostrophes count or how they are removed.
- missing: The docstring should state which punctuation characters are removed, including apostrophes in possessives and contractions, and whether the removed character joins the surrounding letters into one word or splits them into separate tokens.

```python
def test_get_pos_tag_3(self):
    lemmatization = Lemmatization()
    result = lemmatization.get_pos_tag("The dog's barked at the mailman.")
    expected = ['DT', 'NNS', 'VBD', 'IN', 'DT', 'NN']
    self.assertEqual(result, expected)
```

**test_get_pos_tag_4**: `stated`
- reason: The docstring says to remove punctuation, tokenize, and return the part-of-speech tag of each word, which is what the test checks for this sentence.

```python
def test_get_pos_tag_4(self):
    lemmatization = Lemmatization()
    result = lemmatization.get_pos_tag("He was running and eating at same time. ")
    expected = ['PRP', 'VBD', 'VBG', 'CC', 'VBG', 'IN', 'JJ', 'NN']
    self.assertEqual(result, expected)
```

**test_get_pos_tag_5**: `stated`
- reason: The docstring says to remove punctuation, tokenize, and return the part-of-speech tag of each word, and the example shows the Penn Treebank-style output, so a programmer following it would produce the same tag list the test expects.

```python
def test_get_pos_tag_5(self):
    lemmatization = Lemmatization()
    result = lemmatization.get_pos_tag("I was taking a ride in the car.")
    expected = ['PRP', 'VBD', 'VBG', 'DT', 'NN', 'IN', 'DT', 'NN']
    self.assertEqual(result, expected)
```

## Method `remove_punctuation`

### Docstring

```python
def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """
```

### Reference code (`solution_code`)

```python
def remove_punctuation(self, sentence):
        return sentence.translate(str.maketrans('', '', string.punctuation))
```

### Tests (`LemmatizationTestRemovePunctuation`)

**test_remove_punctuation_1**: `stated`
- reason: The docstring says the method removes punctuation and gives an example where the trailing period is dropped, which is exactly what the test checks.

```python
def test_remove_punctuation_1(self):
    lemmatization = Lemmatization()
    result = lemmatization.remove_punctuation("I am running in a race.")
    expected = "I am running in a race"
    self.assertEqual(result, expected)
```

**test_remove_punctuation_2**: `stated`
- reason: The docstring says the output has "without any punctuation", so a programmer would strip the apostrophe in "Cantanco's" along with the commas and period, which is what the test expects.

```python
def test_remove_punctuation_2(self):
    lemmatization = Lemmatization()
    result = lemmatization.remove_punctuation("Until the beating, Cantanco's eyesight had been weak, but adequate.")
    expected = 'Until the beating Cantancos eyesight had been weak but adequate'
    self.assertEqual(result, expected)
```

**test_remove_punctuation_3**: `stated`
- reason: The docstring says the method removes punctuation and returns the sentence "without any punctuation," so a programmer would strip the apostrophe in "dog's" and the exclamation marks, which is what the test expects.

```python
def test_remove_punctuation_3(self):
    lemmatization = Lemmatization()
    result = lemmatization.remove_punctuation("The dog's barked at the mailman!!!")
    expected = 'The dogs barked at the mailman'
    self.assertEqual(result, expected)
```

**test_remove_punctuation_4**: `stated`
- reason: The docstring says to remove any punctuation from the text, and a programmer would delete the ellipsis dots and leave the other characters, including the trailing space, unchanged, which matches the expected output.

```python
def test_remove_punctuation_4(self):
    lemmatization = Lemmatization()
    result = lemmatization.remove_punctuation("He was running and eating at same time... ")
    expected = 'He was running and eating at same time '
    self.assertEqual(result, expected)
```

**test_remove_punctuation_5**: `stated`
- reason: The docstring says the output should be the sentence "without any punctuation", so a programmer would strip every punctuation mark, including the question mark and the repeated periods this test uses.

```python
def test_remove_punctuation_5(self):
    lemmatization = Lemmatization()
    result = lemmatization.remove_punctuation("Is this a test? I hope it is...")
    expected = 'Is this a test I hope it is'
    self.assertEqual(result, expected)
```

## Tests in no method's test class

### `LemmatizationTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    lemmatization = Lemmatization()
    result = lemmatization.lemmatize_sentence("Until the beating, Cantanco's eyesight had been weak, but adequate.")
    expected = ['Until', 'the', 'beating', 'Cantancos', 'eyesight', 'have', 'be', 'weak', 'but', 'adequate']
    self.assertEqual(result, expected)

    result = lemmatization.get_pos_tag("Cantanco's eyesight had been weak, but adequate.")
    expected = ['NNP', 'NN', 'VBD', 'VBN', 'JJ', 'CC', 'JJ']
    self.assertEqual(result, expected)
```
