from simple_substitution.simple_sub import SubstitutionCipher


def main() -> None:
    message = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'encrypt'  # set to 'encrypt' or 'decrypt'

    SubstitutionCipher.check_valid_key(key)

    if myMode == 'encrypt':
        translated = SubstitutionCipher.encrypt(message, key)
    elif myMode == 'decrypt':
        translated = SubstitutionCipher.decrypt(message, key)
    print('Using key %s' % (key))
    print('The %sed message is:' % (myMode))
    print(translated)


if __name__ == '__main__':
    main()
