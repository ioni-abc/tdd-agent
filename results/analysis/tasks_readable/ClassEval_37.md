# ClassEval_37

## Skeleton (what the agent sees)

```python
class EncryptionUtils:
    """
    This is a class that provides methods for encryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'

        """

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """

    def rail_fence_cipher(self,plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
```

## Method `caesar_cipher`

### Docstring

```python
def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'

        """
```

### Reference code (`solution_code`)

```python
def caesar_cipher(self, plaintext, shift):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.isupper():
                    ascii_offset = 65
                else:
                    ascii_offset = 97
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                ciphertext += shifted_char
            else:
                ciphertext += char
        return ciphertext
```

### Tests (`EncryptionUtilsTestCaesarCipher`)

**test_caesar_cipher**: `stated`
- reason: The docstring's own example, `caesar_cipher("abc", 1)` returning `'bcd'`, is exactly the case this test checks, so a programmer following the docstring would pass.

```python
def test_caesar_cipher(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.caesar_cipher("abc", 1), "bcd")
```

**test_caesar_cipher_2**: `unstated`
- reason: The docstring says only that shift is an int and does not say whether negative shifts are allowed or how letters wrap around the alphabet, so a correct implementation could still fail this test.
- missing: The docstring should state that negative shift values move letters backward, that letters wrap cyclically within their alphabet case, and that non-letter characters are left unchanged.

```python
def test_caesar_cipher_2(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.caesar_cipher("WORLD", -2), "UMPJB")
```

**test_caesar_cipher_3**: `stated`
- reason: The docstring says each character of the plaintext is shifted and the result returned, so a programmer's natural implementation of looping over characters would return an empty string for empty input.

```python
def test_caesar_cipher_3(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.caesar_cipher("", 4), "")
```

**test_caesar_cipher_4**: `unstated`
- reason: The docstring says each character is shifted but does not say that shifts wrap around the alphabet, so a programmer could implement a shift without wrap-around and fail the test's shift-by-26 expectation.
- missing: Letters should wrap around within their own case's alphabet (so shifting past the end continues from the start, with shifts taken modulo 26), while non-letter characters are left unchanged and letter case is preserved.

```python
def test_caesar_cipher_4(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.caesar_cipher("abcxyz", 26), "abcxyz")
```

**test_caesar_cipher_5**: `unstated`
- reason: The docstring does not say that letters wrap around the alphabet or that shifts larger than 26 are reduced modulo 26, which is what this test's expected output depends on.
- missing: The docstring should state that letters wrap around within their alphabet (so z shifted forward goes back to a) and that any shift amount is reduced modulo 26, with case preserved and non-letters left unchanged.

```python
def test_caesar_cipher_5(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.caesar_cipher("abcxyz", 27), "bcdyza")
```

**test_caesar_cipher_6**: `unstated`
- reason: The docstring says each character is shifted but never says that non-letter characters are left unchanged, so a programmer could shift digits too and fail this test.
- missing: The docstring should say that only alphabetic characters are shifted (wrapping within their own case's alphabet), while all other characters such as digits, spaces and punctuation are copied through unchanged.

```python
def test_caesar_cipher_6(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.caesar_cipher("123", 27), "123")
```

## Method `vigenere_cipher`

### Docstring

```python
def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
```

### Reference code (`solution_code`)

```python
def vigenere_cipher(self, plain_text):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)].lower()) - ord('a')
                encrypted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
                encrypted_text += encrypted_char.upper() if char.isupper() else encrypted_char
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text
```

### Tests (`EncryptionUtilsTestVigenereCipher`)

**test_vigenere_cipher**: `stated`
- reason: The docstring's own example, a key of "key" encrypting "abc" to 'kfa', is exactly the case this test checks, and the standard Vigenere rule (shift each letter by the key letter, cycling the key) produces that result.

```python
def test_vigenere_cipher(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.vigenere_cipher("abc"), "kfa")
```

**test_vigenere_cipher_2**: `stated`
- reason: The docstring describes a standard Vigenere encryption with the key set in the constructor, and the test's input is all lowercase letters, so a programmer implementing that cipher would produce the expected output.

```python
def test_vigenere_cipher_2(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.vigenere_cipher("hello"), "rijvs")
```

**test_vigenere_cipher_3**: `unstated`
- reason: The docstring gives only a lowercase example, so a programmer could reasonably lowercase the output, whereas this test expects the case of each input letter to be preserved (A→L, b→p).
- missing: The docstring should say that each letter keeps its original case in the output, and that non-letter characters pass through unchanged without consuming a key letter.

```python
def test_vigenere_cipher_3(self):
    encryption_utils = EncryptionUtils("longkey")
    self.assertEqual(encryption_utils.vigenere_cipher("AbCdEfG"), "LpPjOjE")
```

**test_vigenere_cipher_4**: `unstated`
- reason: The test expects non-letter characters to pass through unchanged without consuming a key letter, and the docstring says nothing about how punctuation, digits, or spaces are handled, so a plausible implementation (e.g., advancing the key on every character) would fail.
- missing: The docstring should say that non-alphabetic characters are copied to the output unchanged and do not advance the position in the key, and that the case of each letter is preserved.

```python
def test_vigenere_cipher_4(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.vigenere_cipher("Hello, World! 123"), "Rijvs, Uyvjn! 123")
```

**test_vigenere_cipher_5**: `stated`
- reason: The docstring says the method encrypts the plaintext and returns the ciphertext, so an empty plaintext should produce an empty ciphertext, which is what the test expects.

```python
def test_vigenere_cipher_5(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.vigenere_cipher(""), "")
```

## Method `rail_fence_cipher`

### Docstring

```python
def rail_fence_cipher(self,plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
```

### Reference code (`solution_code`)

```python
def rail_fence_cipher(self, plain_text, rails):
        fence = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
        direction = -1
        row, col = 0, 0

        for char in plain_text:
            if row == 0 or row == rails-1:
                direction = -direction

            fence[row][col] = char
            col += 1
            row += direction

        encrypted_text = ''
        for i in range(rails):
            for j in range(len(plain_text)):
                if fence[i][j] != '\n':
                    encrypted_text += fence[i][j]

        return encrypted_text
```

### Tests (`EncryptionUtilsTestRailFenceCipher`)

**test_rail_fence_cipher**: `stated`
- reason: The docstring's own example, rail_fence_cipher("abc", 2) returning 'acb', is the same case the test checks, and a standard zigzag rail-fence implementation produces that output.

```python
def test_rail_fence_cipher(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.rail_fence_cipher("abc", 2), "acb")
```

**test_rail_fence_cipher_2**: `stated`
- reason: The docstring names the Rail Fence cipher and its example ("abc", 2 rails gives "acb") pins down the standard zigzag convention, which a programmer would apply to give "hloel" for the test input.

```python
def test_rail_fence_cipher_2(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.rail_fence_cipher("hello", 2), "hloel")
```

**test_rail_fence_cipher_3**: `stated`
- reason: The docstring names the Rail Fence cipher and its example ("abc", 2 gives 'acb') shows the zigzag-then-read-by-rail convention, so a programmer would produce "ACEGbdf" for this input with two rails.

```python
def test_rail_fence_cipher_3(self):
    encryption_utils = EncryptionUtils("longkey")
    self.assertEqual(encryption_utils.rail_fence_cipher("AbCdEfG", 2), "ACEGbdf")
```

**test_rail_fence_cipher_4**: `stated`
- reason: The docstring names the standard Rail Fence cipher and its example (`"abc"`, 2 rails → `'acb'`) shows the zigzag-then-read-rail-by-rail convention, so a programmer implementing the standard cipher would produce this test's expected output.

```python
def test_rail_fence_cipher_4(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.rail_fence_cipher("Hello, World! 123", 2), "Hlo ol!13el,Wrd 2")
```

**test_rail_fence_cipher_5**: `stated`
- reason: The docstring says the function encrypts the given plaintext and returns the ciphertext, so a programmer would naturally return an empty string for empty input, which is what the test expects.

```python
def test_rail_fence_cipher_5(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.rail_fence_cipher("", 2), "")
```

**test_rail_fence_cipher_6**: `stated`
- reason: The docstring names the standard Rail Fence cipher, whose zigzag-then-read-by-rail behaviour a programmer would implement, and the test's 3-rail output matches that standard pattern.

```python
def test_rail_fence_cipher_6(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.rail_fence_cipher("abcdefg", 3), "aebdfcg")
```

## Tests in no method's test class

### `EncryptionUtilsTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    encryption_utils = EncryptionUtils("key")
    self.assertEqual(encryption_utils.caesar_cipher("abc", 1), "bcd")
    self.assertEqual(encryption_utils.vigenere_cipher("abc"), "kfa")
    self.assertEqual(encryption_utils.rail_fence_cipher("abc", 2), "acb")
```
