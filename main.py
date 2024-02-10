from affine_cipher.affine import AffineCipher


def main() -> None:
    message = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    key = 2023
    mode = 'encrypt'  # set to 'encrypt' or 'decrypt'

    if mode == 'encrypt':
        translated = AffineCipher.encrypt(message, key)
    elif mode == 'decrypt':
        translated = AffineCipher.decrypt(message, key)
    print('Key: %s' % (key))
    print('%sed text:' % (mode.title()))
    print(translated)


if __name__ == '__main__':
    main()
