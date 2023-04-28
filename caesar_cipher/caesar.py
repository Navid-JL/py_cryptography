from string import ascii_uppercase


class CaesarCipher():
    """A class implementing the Caesar Cipher encryption and decryption methods.

    Attributes:
    - alphabet (list): A list containing the uppercase letters of the English alphabet.

    Methods:
    - encrypt(cls, message: str, key: int) -> str:
      Encrypts the input message using the Caesar Cipher with the specified key.
      Returns the encrypted message.

    - decrypt(cls, encrypted_message: str, key: int) -> str:
      Decrypts the input encrypted message using the Caesar Cipher with the specified key.
      Returns the decrypted message.

    Note:
    - The class methods do not support numeric characters, and attempting to encrypt or decrypt a message containing numeric characters will raise a ValueError.
    """
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

    def decrypt(cls, encrypted_message: str, key: int):
        decrypted_message = ""
        alphabet_length = len(cls.alphabet)
        for letter in encrypted_message.upper():
            if letter == " ":
                encrypted_message += " "
            elif letter.isnumeric():
                raise ValueError("Caesar Cipher only applies to letters")
            else:
                letter_index = cls.alphabet.index(letter)
                decrypted_message += f"{cls.alphabet[(letter_index - key) % alphabet_length]}"

        return decrypted_message.title()
