def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    keyword = keyword.lower()
    alph = 26
    text = str(plaintext)
    key = str(keyword)
    while len(text) > len(key):
        key += key
    while len(text) < len(key):
        key = key[: - 1]
    for i in range (len(text)):
        if 97 <= ord(text[i]) <= 122:
            if 97 <= ord(text[i]) + ord(key[i]) - 97 <= 122:
                ciphertext += chr(ord(text[i]) + ord(key[i]) - 97)
            else:
                ciphertext += chr(ord(text[i]) + ord(key[i]) - 97 - alph)
        elif 65 <= ord(text[i]) <= 90:
            if 65 <= ord(text[i]) + ord(key[i]) - 97 <= 90:
                ciphertext += chr(ord(text[i]) + ord(key[i]) - 97)
            else:
                ciphertext += chr(ord(text[i]) + ord(key[i]) - 97 - alph)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.lower()
    alph = 26
    key = keyword
    text = ciphertext
    while len(text) > len(key):
        key += key
    while len(key) > len(text):
        key = key[: - 1]
    for i in range(len(text)):
        if ciphertext[i].islower():
            if ord(text[i]) < ord(key[i]):
                plaintext += chr(ord(text[i]) - ord(key[i]) + 97 + alph)
            else:
                plaintext += chr(ord(text[i]) - ord(key[i]) + 97)
        elif ciphertext[i].isupper():
            if ord(text[i]) < ord(key[i]) - 32:
                plaintext += chr(ord(text[i]) - ord(key[i]) + 97 + alph)
            else:
                plaintext += chr(ord(text[i]) - ord(key[i]) + 97)
    return plaintext


print(encrypt_vigenere("PYTHON", "A"))
print(encrypt_vigenere("python", "a"))
print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))

print(decrypt_vigenere("PYTHON", "A"))
print(decrypt_vigenere("python", "a"))
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))