from .caesar import CaesarCipher


def decipher(encrypted_message: str) -> list[str]:
    """Break Caesar cipher message using brute force

    Args:
        encrypted_message (str): encrypted message

    Returns:
        list(str): a list of decrypted messages 
    """
    decrypted_messages = []
    for i in range(25, -1, -1):
        decrypted_messages.append(CaesarCipher.encrypt(encrypted_message, i))
    return decrypted_messages
