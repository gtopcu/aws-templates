# secrets generate cryptographic safe passwords

import secrets
import string


# secrets.randbelow(100)
# secrets.randbits(16)
# secrets.choice(range(1,10))
# secrets.token_bytes(32)
# secrets.token_urlsafe(16)
# secrets.compare_digest(user_input, pwd)
# secrets.SystemRandom().randint() # uses OS capabilities for best randomness


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
