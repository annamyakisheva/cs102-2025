def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char.lower()) - ord('a')
            start = ord('A') if char.isupper() else ord('a')
            next_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += next_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char.lower()) - ord('a')
            start = ord('A') if char.isupper() else ord('a')
            next_char = chr((ord(char) - start - shift) % 26 + start)
            plaintext += next_char
        else:
            plaintext += char
    return plaintext