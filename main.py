# mypy: disable-error-code="import-untyped"
import pyperclip

from vigenere_cipher.vinegere_dict_breaker import vigenere_dict_break


def main() -> None:
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = vigenere_dict_break(ciphertext)

    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


if __name__ == '__main__':
    main()
