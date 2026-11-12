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
        result = []
        for ch in plaintext:
            if 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
            elif 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(ch)
        return ''.join(result)

    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        key_letters = [c.lower() for c in self.key if c.isalpha()]
        if not key_letters:
            return plaintext

        result = []
        key_index = 0
        for ch in plaintext:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                shift = ord(key_letters[key_index % len(key_letters)]) - ord('a')
                if 'a' <= ch <= 'z':
                    base = ord('a')
                else:
                    base = ord('A')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
                key_index += 1
            else:
                result.append(ch)
        return ''.join(result)

    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
        if rails <= 1 or len(plain_text) <= 1:
            return plain_text

        period = 2 * (rails - 1)
        fence = [[] for _ in range(rails)]
        for i, ch in enumerate(plain_text):
            pos = i % period
            row = pos if pos < rails else period - pos
            fence[row].append(ch)
        return ''.join(''.join(row) for row in fence)