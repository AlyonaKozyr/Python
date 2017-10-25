def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    alph = 26
    move = 3
    ciphertext = ''
    text = str(plaintext)
    for i in range(len(text)):
     if (65 <= ord(text[i]) <= 90) or (97 <= ord(text[i]) <= 122):
            if 65 <= ord(text[i]) + move <= 90:
                ciphertext += chr(ord(text[i]) + move)
            elif 97 <= ord(text[i]) + move <= 122:
                ciphertext += chr(ord(text[i]) + move)
            else:
                ciphertext += chr(ord(text[i]) + move - alph)
     else:
         ciphertext += chr(ord(text[i]))
    return ciphertext

def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    alph = 26
    move = 3
    plaintext = ''
    text = str(ciphertext)
    for i in range(len(text)):
        if (65 <= ord(text[i]) <= 90) or (97 <= ord(text[i]) <= 122):
            if 65 <= ord(text[i]) - move <= 90:
                plaintext += chr(ord(text[i]) - move)
            elif 97 <= ord(text[i]) - move <= 122:
                plaintext += chr(ord(text[i]) - move)
            else:
                plaintext += chr(ord(text[i]) - move + alph)
        else:
            plaintext += chr(ord(text[i]))
    return plaintext
