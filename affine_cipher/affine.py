import sys
import random
from .cryptomath import find_mod_inverse, gcd


class AffineCipher():

    SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""  # note the space at the front

    def get_key_parts(key):
        keyA = key // len(AffineCipher.SYMBOLS)
        keyB = key % len(AffineCipher.SYMBOLS)
        return (keyA, keyB)

    @staticmethod
    def check_keys(keyA, keyB, mode):
        if keyA == 1 and mode == 'encrypt':
            sys.exit(
                'The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
        if keyB == 0 and mode == 'encrypt':
            sys.exit(
                'The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
        if keyA < 0 or keyB < 0 or keyB > len(AffineCipher.SYMBOLS) - 1:
            sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (
                len(AffineCipher.SYMBOLS) - 1))
        if gcd(keyA, len(AffineCipher.SYMBOLS)) != 1:
            sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (
                keyA, len(AffineCipher.SYMBOLS)))

    @classmethod
    def encrypt(cls, message, key):
        keyA, keyB = AffineCipher.get_key_parts(key)
        AffineCipher.check_keys(keyA, keyB, 'encrypt')
        ciphertext = ''
        for symbol in message:
            if symbol in AffineCipher.SYMBOLS:
                # encrypt this symbol
                symIndex = AffineCipher.SYMBOLS.find(symbol)
                ciphertext += AffineCipher.SYMBOLS[(symIndex * keyA + keyB) %
                                                   len(AffineCipher.SYMBOLS)]
            else:
                ciphertext += symbol  # just append this symbol unencrypted
        return ciphertext

    @classmethod
    def decrypt(cls, message, key):
        keyA, keyB = AffineCipher.get_key_parts(key)
        AffineCipher.check_keys(keyA, keyB, 'decrypt')
        plaintext = ''
        modInverseOfKeyA = find_mod_inverse(keyA, len(AffineCipher.SYMBOLS))

        for symbol in message:
            if symbol in AffineCipher.SYMBOLS:
                # decrypt this symbol
                symIndex = AffineCipher.SYMBOLS.find(symbol)
                plaintext += AffineCipher.SYMBOLS[(symIndex - keyB) *
                                                  modInverseOfKeyA % len(AffineCipher.SYMBOLS)]
            else:
                plaintext += symbol  # just append this symbol undecrypted
        return plaintext

    @staticmethod
    def get_random_key():
        while True:
            keyA = random.randint(2, len(AffineCipher.SYMBOLS))
            keyB = random.randint(2, len(AffineCipher.SYMBOLS))
            if gcd(keyA, len(AffineCipher.SYMBOLS)) == 1:
                return keyA * len(AffineCipher.SYMBOLS) + keyB
