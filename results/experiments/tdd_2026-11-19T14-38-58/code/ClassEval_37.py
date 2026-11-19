import unittest


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
                base = ord('a')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
            elif 'A' <= ch <= 'Z':
                base = ord('A')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
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
        shifts = [ord(k.lower()) - ord('a') for k in self.key if k.isalpha()]
        if not shifts:
            return plaintext
        result = []
        index = 0
        for ch in plaintext:
            if 'a' <= ch <= 'z':
                base = ord('a')
            elif 'A' <= ch <= 'Z':
                base = ord('A')
            else:
                result.append(ch)
                continue
            shift = shifts[index % len(shifts)]
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            index += 1
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

        fence = [[] for _ in range(rails)]
        period = 2 * (rails - 1)
        for i, ch in enumerate(plain_text):
            r = i % period
            if r >= rails:
                r = period - r
            fence[r].append(ch)
        return ''.join(''.join(row) for row in fence)