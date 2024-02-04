from transposition_cipher.transposition import TranspositionCipher


def main() -> None:
    print(TranspositionCipher.encrypt("Common sense is not so common.", 8))
    print(TranspositionCipher.decrypt(
        "Cenoonommstmme oo snnio. s s c", 8))


if __name__ == "__main__":
    main()
