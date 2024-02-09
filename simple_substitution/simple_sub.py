import sys
import random


class SubstitutionCipher():

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def check_valid_key(cls, key):
        keyList = list(key)
        lettersList = list(SubstitutionCipher.LETTERS)
        keyList.sort()
        lettersList.sort()
        if keyList != lettersList:
            sys.exit('There is an error in the key or symbol set.')

    @classmethod
    def encrypt(cls, message, key):
        return SubstitutionCipher.translate_message(message, key, 'encrypt')

    @classmethod
    def decrypt(cls, message, key):
        return SubstitutionCipher.translate_message(message, key, 'decrypt')

    @staticmethod
    def translate_message(message, key, mode):
        translated = ''
        charsA = SubstitutionCipher.LETTERS
        charsB = key
        if mode == 'decrypt':
            # For decrypting, we can use the same code as encrypting. We
            # just need to swap where the key and LETTERS strings are used.
            charsA, charsB = charsB, charsA

        # loop through each symbol in the message
        for symbol in message:
            if symbol.upper() in charsA:
                # encrypt/decrypt the symbol
                symIndex = charsA.find(symbol.upper())
                if symbol.isupper():
                    translated += charsB[symIndex].upper()
                else:
                    translated += charsB[symIndex].lower()
            else:
                # symbol is not in LETTERS, just add it
                translated += symbol

        return translated

    @staticmethod
    def get_random_key():
        key = list(SubstitutionCipher.LETTERS)
        random.shuffle(key)
        return ''.join(key)
