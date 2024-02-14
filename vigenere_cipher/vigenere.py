# mypy: disable-error-code="import-untyped"
import pyperclip


class VigenereCipher():

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def encrypt(cls, message, key):
        return VigenereCipher.translate_message(message, key, 'encrypt')

    @classmethod
    def decrypt(cls, message, key):
        return VigenereCipher.translate_message(message, key, 'decrypt')

    @classmethod
    def translate_message(cls, message, key, mode):
        translated = []  # Stores the encrypted/decrypted message string.

        keyIndex = 0
        key = key.upper()

        for symbol in message:  # Loop through each symbol in message.
            num = VigenereCipher.LETTERS.find(symbol.upper())
            if num != -1:  # -1 means symbol.upper() was not found in LETTERS.
                if mode == 'encrypt':
                    # Add if encrypting.
                    num += VigenereCipher.LETTERS.find(key[keyIndex])
                elif mode == 'decrypt':
                    # Subtract if decrypting.
                    num -= VigenereCipher.LETTERS.find(key[keyIndex])

                num %= len(VigenereCipher.LETTERS)  # Handle any wraparound.

                # Add the encrypted/decrypted symbol to the end of translated:
                if symbol.isupper():
                    translated.append(VigenereCipher.LETTERS[num])
                elif symbol.islower():
                    translated.append(VigenereCipher.LETTERS[num].lower())

                keyIndex += 1  # Move to the next letter in the key.
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # Append the symbol without encrypting/decrypting.
                translated.append(symbol)

        return ''.join(translated)
