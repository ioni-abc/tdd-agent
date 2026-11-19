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
        j = 0
        for ch in ciphertext:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                base = ord('a') if ch.islower() else ord('A')
                s = shifts[j % len(shifts)]
                result.append(chr((ord(ch) - base - s) % 26 + base))
                j += 1
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
        rail_of = []
        r = 0
        step = 1
        for _ in range(n):
            rail_of.append(r)
            if r == 0:
                step = 1
            elif r == rails - 1:
                step = -1
            r += step
        order = sorted(range(n), key=lambda i: (rail_of[i], i))
        result = [''] * n
        for k, idx in enumerate(order):
            result[idx] = encrypted_text[k]
        return ''.join(result)