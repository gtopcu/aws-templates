
# import jwt

# try:
#     # Extract the refresh token from cookies
#     access_token = request.COOKIES.get("access_token", "")
#     if not access_token:
#         access_token = request.headers.get("Authorization", "").split(' ').pop()
#         if not access_token:
#             raise MissingAccessToken

#     # Decode the JWT to find the user ID
#     decoded_user = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
#     user_id = decoded_user.get("user_id")
#     if not user_id:
#         raise InvalidTokenError
#
# except jwt.PyJWKError as e
#     print(e)

# ----------------------------------------------------------------------------------------------------

import jwt
from datetime import datetime, timedelta

JWT_SECRET = "your-secret-key"

active_tokens = set()

def generate_jwt_token(username):
    """Generate a JWT token for a user"""
    expiration = datetime.now(datetime.timezone.utc) + timedelta(hours=1)
    token = jwt.encode(
        {"username": username, "exp": expiration}, JWT_SECRET, algorithm="HS256"
    )
    active_tokens.add(token)
    return token

def verify_token(token):
    """Verify the JWT token"""
    try:
        if token not in active_tokens:
            return False
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        active_tokens.discard(token)
        return False
    except jwt.InvalidTokenError:
        return False