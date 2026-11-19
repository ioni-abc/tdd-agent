import unittest


class DecryptionUtils:
    """
    This is a class that provides methods for decryption, including the Caesar cipher, Vigenere cipher, and Rail Fence cipher.
    """

    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption,str.
        """
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        """
        Deciphers the given ciphertext using the Caesar cipher
        :param ciphertext: The ciphertext to decipher,str.
        :param shift: The shift to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'

        """
        result = []
        for ch in ciphertext:
            if 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
            elif 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
            else:
                result.append(ch)
        return ''.join(result)

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """
        shifts = [ord(c.lower()) - ord('a') for c in self.key if c.isalpha()]
        if not shifts:
            return ciphertext
        result = []
        idx = 0
        for ch in ciphertext:
            if 'a' <= ch <= 'z':
                s = shifts[idx % len(shifts)]
                result.append(chr((ord(ch) - ord('a') - s) % 26 + ord('a')))
                idx += 1
            elif 'A' <= ch <= 'Z':
                s = shifts[idx % len(shifts)]
                result.append(chr((ord(ch) - ord('A') - s) % 26 + ord('A')))
                idx += 1
            else:
                result.append(ch)
        return ''.join(result)

    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """
        n = len(encrypted_text)
        if rails <= 1 or n == 0:
            return encrypted_text
        cycle = 2 * (rails - 1)
        rows = [min(i % cycle, cycle - i % cycle) for i in range(n)]
        # Positions of the plaintext in the order they were read off the rails
        order = sorted(range(n), key=lambda i: (rows[i], i))
        result = [''] * n
        for k, pos in enumerate(order):
            result[pos] = encrypted_text[k]
        return ''.join(result)