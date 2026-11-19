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
        key_letters = [c for c in self.key if c.isalpha()]
        if not key_letters:
            return plaintext
        key_shifts = [ord(c.lower()) - ord('a') for c in key_letters]
        result = []
        j = 0
        for ch in plaintext:
            if ch.isalpha():
                shift = key_shifts[j % len(key_shifts)]
                base = ord('a') if ch.islower() else ord('A')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
                j += 1
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
        rail_list = [[] for _ in range(rails)]
        row = 0
        step = 1
        for ch in plain_text:
            rail_list[row].append(ch)
            if row == 0:
                step = 1
            elif row == rails - 1:
                step = -1
            row += step
        return ''.join(''.join(r) for r in rail_list)