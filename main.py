# mypy: disable-error-code="import-untyped"
import pyperclip
from vigenere_cipher.vigenere import VigenereCipher


def main() -> None:
    # This text can be copy/pasted from https://invpy.com/vigenereCipher.py:
    message = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    key = 'ASIMOV'
    mode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.

    if mode == 'encrypt':
        translated = VigenereCipher.encrypt(message, key)
    elif mode == 'decrypt':
        translated = VigenereCipher.decrypt(message, key)

    print('%sed message:' % (mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')


if __name__ == '__main__':
    main()
