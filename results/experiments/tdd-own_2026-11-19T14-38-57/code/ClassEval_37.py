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
        key_shifts = [ord(k.lower()) - ord('a') for k in self.key if k.isalpha()]
        if not key_shifts:
            return plaintext
        result = []
        key_index = 0
        for ch in plaintext:
            if 'a' <= ch <= 'z':
                shift = key_shifts[key_index % len(key_shifts)]
                result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
                key_index += 1
            elif 'A' <= ch <= 'Z':
                shift = key_shifts[key_index % len(key_shifts)]
                result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
                key_index += 1
            else:
                result.append(ch)
        return ''.join(result)

    def rail_fence_cipher(self,plain_text, rails):
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
        cycle = 2 * (rails - 1)
        for i, ch in enumerate(plain_text):
            r = i % cycle
            if r >= rails:
                r = cycle - r
            fence[r].append(ch)
        return ''.join(''.join(rail) for rail in fence)