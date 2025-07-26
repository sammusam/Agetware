def caesar_cipher(text, shift, encode=True):
    if not encode:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

# Example:
print(caesar_cipher("Hello, World!", 3, encode=True))  # Khoor, Zruog!
print(caesar_cipher("Khoor, Zruog!", 3, encode=False)) # Hello, World!
