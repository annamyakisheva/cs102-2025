def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char.upper()) - ord("A")
            start = ord("A") if char.isupper() else ord("a")
            new_char = chr(start + (ord(char) - start + shift) % 26)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = keyword[i % len(keyword)]
            shift = ord(key_char.upper()) - ord("A")
            start = ord("A") if char.isupper() else ord("a")
            new_char = chr(start + (ord(char) - start - shift) % 26)
            plaintext += new_char
        else:
            plaintext += char
    return plaintext
