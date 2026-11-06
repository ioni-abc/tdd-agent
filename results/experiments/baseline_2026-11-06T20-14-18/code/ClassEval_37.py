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
            raise ValueError("Vigenere cipher requires a key containing letters")
        result = []
        k = 0
        for ch in plaintext:
            if ch.isalpha():
                shift = ord(key_letters[k % len(key_letters)]) - ord('a')
                if ch.islower():
                    result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
                else:
                    result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
                k += 1
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
        cycle = 2 * (rails - 1)
        rail_of = []
        for i in range(len(plain_text)):
            r = i % cycle
            if r >= rails:
                r = cycle - r
            rail_of.append(r)
        order = sorted(range(len(plain_text)), key=lambda i: (rail_of[i], i))
        return ''.join(plain_text[i] for i in order)