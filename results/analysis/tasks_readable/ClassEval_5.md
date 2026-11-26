# ClassEval_5

## Skeleton (what the agent sees)

```python
# This class is an automatic guitar simulator that can interpret and play based on the input guitar sheet music.

class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively. If the input is empty or contains only whitespace, an empty list is returned.
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

        """


    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
```

## Method `interpret`

### Docstring

```python
def interpret(self, display=False):
    """
    Interpret the music score to be played
    :param display:Bool, representing whether to print the interpreted score
    :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively. If the input is empty or contains only whitespace, an empty list is returned.
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> play_list = context.interpret(display = False)
    [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

    """
```

### Reference code (`solution_code`)

```python
def interpret(self, display=False):
    if not self.play_text.strip():
        return []
    else:
        play_list = []
        play_segs = self.play_text.split(" ")
        for play_seg in play_segs:
            pos = 0
            for ele in play_seg:
                if ele.isalpha():
                    pos += 1
                    continue
                break
            play_chord = play_seg[0:pos]
            play_value = play_seg[pos:]
            play_list.append({'Chord': play_chord, 'Tune': play_value})
            if display:
                self.display(play_chord, play_value)
        return play_list
```

### Tests (`AutomaticGuitarSimulatorTestInterpret`)

**test_interpret_1**: `stated`
- reason: The docstring says each entry pairs a letters Chord with a numeric Tune, and its example shows space-separated segments split into those fields, so a programmer would produce `[{'Chord': 'C', 'Tune': '53231323'}]` for this single-segment input.

```python
def test_interpret_1(self):
    context = AutomaticGuitarSimulator("C53231323")
    play_list = context.interpret()
    self.assertEqual(play_list, [{'Chord': 'C', 'Tune': '53231323'}])
```

**test_interpret_2**: `stated`
- reason: The docstring says each returned dict holds the letter part as Chord and the number part as Tune, and the test's single-chord input is just one instance of that split, so a programmer following it would produce the expected output.

```python
def test_interpret_2(self):
    context = AutomaticGuitarSimulator("F43231323")
    play_list = context.interpret()
    self.assertEqual(play_list, [{'Chord': 'F', 'Tune': '43231323'}])
```

**test_interpret_3**: `stated`
- reason: The docstring says the result is a list of dicts with letter-based Chord and numeric Tune fields, and its example already shows an Em chord split from its digits, so a programmer following it would produce this single-chord result.

```python
def test_interpret_3(self):
    context = AutomaticGuitarSimulator("Em43231323")
    play_list = context.interpret()
    self.assertEqual(play_list, [{'Chord': 'Em', 'Tune': '43231323'}])
```

**test_interpret_4**: `stated`
- reason: The docstring says each dict holds the leading letters as Chord and the numbers as Tune, so a programmer splitting "G63231323" would get the expected single-element list.

```python
def test_interpret_4(self):
    context = AutomaticGuitarSimulator("G63231323")
    play_list = context.interpret()
    self.assertEqual(play_list, [{'Chord': 'G', 'Tune': '63231323'}])
```

**test_interpret_5**: `stated`
- reason: The docstring's example and its description of Chord (letters) and Tune (numbers) make a programmer split the input on spaces and separate each segment's leading letters from its digits, which is exactly what this two-segment test checks.

```python
def test_interpret_5(self):
    context = AutomaticGuitarSimulator("F43231323 G63231323")
    play_list = context.interpret()
    self.assertEqual(play_list, [{'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}])
```

**test_interpret_6**: `stated`
- reason: The docstring explicitly says that if the input is empty or contains only whitespace, an empty list is returned, which is exactly what the test checks with a single-space input.

```python
def test_interpret_6(self):
    context = AutomaticGuitarSimulator(" ")
    play_list = context.interpret()
    self.assertEqual(play_list, [])
```

**test_interpret_7**: `stated`
- reason: The docstring says Chord is letters and Tune is numbers, and its example shows a multi-letter chord ("Em"), so a programmer would take the leading letter run as the chord and the rest as the tune, which gives "ABC" and "43231323" for this test.

```python
def test_interpret_7(self):
    context = AutomaticGuitarSimulator("ABC43231323 DEF63231323")
    play_list = context.interpret()
    self.assertEqual(play_list, [{'Chord': 'ABC', 'Tune': '43231323'}, {'Chord': 'DEF', 'Tune': '63231323'}])
```

**test_interpret_8**: `stated`
- reason: The docstring says the return value is a list of dicts with Chord (letters) and Tune (numbers), so a programmer following it would return one dict for a single chord-and-tune string, which is what the test expects, and the display flag only controls printing.

```python
def test_interpret_8(self):
    context = AutomaticGuitarSimulator("C53231323")
    play_list = context.interpret(display=True)
    self.assertEqual(play_list, [{'Chord': 'C', 'Tune': '53231323'}])
```

**test_interpret_9**: `stated`
- reason: The docstring explicitly says an empty input returns an empty list, which is exactly what this test checks with an empty play text.

```python
def test_interpret_9(self):
    context = AutomaticGuitarSimulator("")
    play_list = context.interpret()
    self.assertEqual(play_list, [])
```

## Method `display`

### Docstring

```python
def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """
```

### Reference code (`solution_code`)

```python
def display(self, key, value):
        return "Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value)
```

### Tests (`AutomaticGuitarSimulatorTestDisplay`)

**test_display_1**: `stated`
- reason: The docstring gives the exact output format and an example with chord "C" and tune "53231323", which is the same format and input the test checks after parsing via interpret().

```python
def test_display_1(self):
    context = AutomaticGuitarSimulator("C53231323 Em43231323")
    play_list = context.interpret()
    str = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
    self.assertEqual(str, "Normal Guitar Playing -- Chord: C, Play Tune: 53231323")
```

**test_display_2**: `stated`
- reason: The docstring gives the exact output format "Normal Guitar Playing -- Chord: %s, Play Tune: %s", and the test only checks that display fills that format with the chord and tune it is given.

```python
def test_display_2(self):
    context = AutomaticGuitarSimulator("C53231323 Em43231323")
    play_list = context.interpret()
    str = context.display(play_list[1]['Chord'], play_list[1]['Tune'])
    self.assertEqual(str, "Normal Guitar Playing -- Chord: Em, Play Tune: 43231323")
```

**test_display_3**: `stated`
- reason: The docstring gives the exact output format "Normal Guitar Playing -- Chord: %s, Play Tune: %s" and the test checks only that format with a chord and tune, so a programmer following the docstring would pass.

```python
def test_display_3(self):
    context = AutomaticGuitarSimulator("F43231323 G63231323")
    play_list = context.interpret()
    str = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
    self.assertEqual(str, "Normal Guitar Playing -- Chord: F, Play Tune: 43231323")
```

**test_display_4**: `stated`
- reason: The docstring gives the exact output format "Normal Guitar Playing -- Chord: %s, Play Tune: %s" with the chord and tune substituted in, so a programmer following it would produce the expected string for chord G and tune 63231323.

```python
def test_display_4(self):
    context = AutomaticGuitarSimulator("F43231323 G63231323")
    play_list = context.interpret()
    str = context.display(play_list[1]['Chord'], play_list[1]['Tune'])
    self.assertEqual(str, "Normal Guitar Playing -- Chord: G, Play Tune: 63231323")
```

**test_display_5**: `stated`
- reason: The docstring gives the exact format string and says the key and value are substituted into it, so a programmer would produce "Chord: , Play Tune: " for empty inputs, matching the test.

```python
def test_display_5(self):
    context = AutomaticGuitarSimulator("")
    str = context.display('', '')
    self.assertEqual(str, "Normal Guitar Playing -- Chord: , Play Tune: ")
```

## Tests in no method's test class

### `AutomaticGuitarSimulatorTest`

**test_AutomaticGuitarSimulator**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_AutomaticGuitarSimulator(self):
    context = AutomaticGuitarSimulator("C53231323")
    play_list = context.interpret()
    self.assertEqual(play_list, [{'Chord': 'C', 'Tune': '53231323'}])

    context = AutomaticGuitarSimulator("C53231323 Em43231323")
    play_list = context.interpret()
    str = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
    self.assertEqual(str, "Normal Guitar Playing -- Chord: C, Play Tune: 53231323")
```
