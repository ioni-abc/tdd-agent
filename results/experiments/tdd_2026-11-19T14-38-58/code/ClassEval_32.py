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
        s = shift % 26
        result = []
        for ch in ciphertext:
            if 'a' <= ch <= 'z':
                result.append(chr((ord(ch) - ord('a') - s) % 26 + ord('a')))
            elif 'A' <= ch <= 'Z':
                result.append(chr((ord(ch) - ord('A') - s) % 26 + ord('A')))
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
        key_shifts = [ord(k.lower()) - ord('a') for k in self.key
                      if 'a' <= k.lower() <= 'z']
        if not key_shifts:
            return ciphertext

        result = []
        idx = 0
        for ch in ciphertext:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                base = ord('a') if ch.islower() else ord('A')
                s = key_shifts[idx % len(key_shifts)]
                result.append(chr((ord(ch) - base - s) % 26 + base))
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

        def rail_of(i):
            r = i % cycle
            if r >= rails:
                r = cycle - r
            return r

        # Positions of the plaintext, ordered as they were read off the rails
        order = sorted(range(n), key=lambda i: (rail_of(i), i))

        result = [''] * n
        for j, i in enumerate(order):
            result[i] = encrypted_text[j]
        return ''.join(result)