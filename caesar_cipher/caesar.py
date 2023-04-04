from string import ascii_uppercase


class CaesarCipher():

    alphabet = list(ascii_uppercase)

    @classmethod
    def encrypt(cls, message: str, key: int) -> str:
        encrypted_message = ""
        alphabet_length = len(cls.alphabet)
        for letter in message.upper():
            if letter == " ":
                encrypted_message += " "
            elif letter.isnumeric():
                raise ValueError("Caesar Cipher only applies to letters")
            else:
                letter_index = cls.alphabet.index(letter)
                encrypted_message += f"{cls.alphabet[(letter_index + key) % alphabet_length]}"

        return encrypted_message.title()
