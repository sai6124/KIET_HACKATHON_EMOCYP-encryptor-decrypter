1
import hashlib
# Emoji mapping (characters to emojis and vice versa)
emoji_mapping = {
    'a': '😀', 'b': '😁', 'c': '😂', 'd': '🤣', 'e': '😃',
    'f': '😄', 'g': '😅', 'h': '😉', 'i': '😊', 'j': '😋',
    'k': '😎', 'l': '😍', 'm': '😘', 'n': '🥰', 'o': '😗',
    'p': '😙', 'q': '🥲', 'r': '😚', 's': '☺️', 't': '🙂',
    'u': '🤗', 'v': '🤩', 'w': '🤔', 'x': '🫡', 'y': '🤨',
    'z': '😐', 'A': '😑', 'B': '😶', 'C': '🫥', 'D': '😶‍🌫️',
    'E': '🙄', 'F': '😏', 'G': '😣', 'H': '😥', 'I': '😮', 'J': '🤐',
    'K': '😯', 'L': '😪', 'N': '😫', 'M': '🥱', 'O': '😴', 'P': '😌',
    'Q': '😛', 'R': '😜', 'S': '😝', 'T': '🤤', 'U': '😒', 'V': '😓',
    'W': '😔', 'X': '😕', 'Y': '🙃', 'Z': '😭', ' ': '👻',
    '0': '🤑', '1': '😲', '2': '😖', '3': '😤', '4': '😨',
    '5': '🤯', '6': '😰', '7': '🥵', '8': '😡', '9': '🤡',
    '⬛': ' ',  # Black square for spaces
}

# Create a reverse emoji mapping
reverse_emoji_mapping = {value: key for key, value in emoji_mapping.items()}
# Caesar cipher encryption
def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

# Caesar cipher decryption
def caesar_decipher(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted_text += char
    return decrypted_text

def atbash_cipher(text):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_text += chr(25 - (ord(char) - ascii_offset) + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

# Atbash cipher decryption
def atbash_decipher(encrypted_text):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_text += chr(25 - (ord(char) - ascii_offset) + ascii_offset)
        else:
            decrypted_text += char
    return decrypted_text

def rot13(text):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - ascii_offset + 13) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

# ROT13 decryption
def rot13_decipher(encrypted_text):
    return rot13(encrypted_text)

# Reverse cipher encryption
def reverse_cipher(text):
    return text[::-1]

# Reverse cipher decryption
def reverse_decipher(encrypted_text):
    return encrypted_text[::-1]

# Mixed case cipher encryption
def mixed_case_cipher(text):
    # Toggle the case of each character
    return ''.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text))

# Mixed case cipher decryption
def mixed_case_decipher(text):
    # Toggle the case of each character
    return ''.join(char.lower() if i % 2 == 0 else char.upper() for i, char in enumerate(text))


# Updated encryption phases to consider case
def encrypt_to_emojis(plain_text):
    encrypted_text = plain_text
    # Phase 1: Caesar Cipher
    encrypted_text = caesar_cipher(plain_text, 3)

    # Phase 2: Atbash Cipher
    encrypted_text = atbash_cipher(encrypted_text)

    # Phase 3: ROT13
    encrypted_text = rot13(encrypted_text)

    # Phase 4: Reverse
    encrypted_text = reverse_cipher(encrypted_text)

    # # Phase 5: Mixed Case
    # # Preserve original case of the characters
    # encrypted_text = ''.join(
    #     char.upper() if orig_char.isupper() else char.lower()
    #     for char, orig_char in zip(encrypted_text, plain_text)
    # )

    # Phase 6: Additional Encryption (Caesar Cipher with shift 5)
    encrypted_text = caesar_cipher(encrypted_text, 5)

    # Phase 7: Additional Encryption (Atbash Cipher)
    encrypted_text = atbash_cipher(encrypted_text)

    # Convert to emojis using the emoji mapping
    emojis = [emoji_mapping.get(char, char) for char in encrypted_text]
    return ' '.join(emojis)

def decrypt_to_text(emojis_text):
    # Split emojis text into a list of emojis
    emojis_list = emojis_text.split()

    # Phase 7: Reversing the Emoji Mapping
    reverse_emoji_mapping = {value: key for key, value in emoji_mapping.items()}

    # Reverse Phase 7: Convert emojis to characters using reverse mapping
    decrypted_text = ''.join(reverse_emoji_mapping.get(emoji, emoji) for emoji in emojis_list)

    # Reverse Phase 6: Additional Decryption (Atbash Cipher)
    decrypted_text = atbash_decipher(decrypted_text)

    # Reverse Phase 5: Additional Decryption (Caesar Cipher with shift -5)
    decrypted_text = caesar_decipher(decrypted_text, -5)

    # Reverse Phase 4: Reverse
    decrypted_text = reverse_decipher(decrypted_text)

    # Reverse Phase 3: ROT13
    decrypted_text = rot13_decipher(decrypted_text)

    # Reverse Phase 2: Additional Decryption (Atbash Cipher)
    decrypted_text = atbash_decipher(decrypted_text)

    # Reverse Phase 1: Additional Decryption (Caesar Cipher with shift -3)
    decrypted_text = caesar_decipher(decrypted_text, -3)
    decrypted_text = caesar_decipher(decrypted_text, -4)

    return decrypted_text

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Encrypt text to emojis")
        print("2. Decrypt emojis to text")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            plain_text = input("Enter the text to be encrypted: ")
            encrypted_text = encrypt_to_emojis(plain_text)
            print("Encrypted text in emojis:", encrypted_text)
        elif choice == 2:
            emojis_text = input("Enter the emojis to be decrypted: ")
            decrypted_text = decrypt_to_text(emojis_text)
            print("Decrypted text:", decrypted_text)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")
