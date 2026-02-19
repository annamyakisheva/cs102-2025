def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            new_char = chr(start + (ord(char) - start + shift) % 26)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            new_char = chr(start + (ord(char) - start - shift) % 26)
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

