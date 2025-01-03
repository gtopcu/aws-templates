# pip install "passlib[bcrypt]"
# pip install "python-jose[cryptography]"
# pip install python-multipart

from datetime import datetime

from passlib.context import CryptContext

bcrpyt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed = bcrpyt_context.hash("123456")
print(hashed)
print(bcrpyt_context.verify("123456", hashed))

print(datetime.utcnow())


# from jose import jwt, JWTError
# from typing import Any

# secret_key: str = "secret"
# encoded: str = jwt.encode({"foo": "bar"}, secret_key, algorithm="HS256")

# try:
#     token_payload: dict[str, Any] = jwt.decode("XXXXXXXXXXXX")
#     user = token_payload.get("user")
# except JWTError:
#     raise JWTError("Invalid token")
