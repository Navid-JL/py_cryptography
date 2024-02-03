class ReverseCipher():
    """A very basic encryption cipher that reverses a plain text

    Methods:
    - encrypt(cls, message: str) -> str:
      Encrypts (ironically) the plain text.
      Returns a reversed version of the message.  

    - decrypt(cls, rev_message: str) -> str:
      Decrypts the reversed_message by reversing it again to get the original message.
      Returns the original message.
    """
    @classmethod
    def encrypt(cls, message: str,):
        return message[::-1]

    @classmethod
    def decrypt(cls, rev_message: str):
        return rev_message[::-1]
