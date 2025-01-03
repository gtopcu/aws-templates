# secrets generate cryptographic safe passwords

import secrets
import string


def generate_pw(length: int) -> str:
    """Generate a password of the given length"""
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    pw = ""
    for _ in range(length):
        pw += "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation))
    
    any(char in string.digits for char in pw)
    return pw


if __name__ == "__main__":
    print(generate_pw(10))
