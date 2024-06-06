

import jwt

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