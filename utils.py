import jwt
from hashlib import sha256
import secrets
import datetime
import os

SECRET_KEY = os.getenv("SECRET_KEY")
# Utility function to generate a JWT token
def generate_jwt_token(user_id, SECRET_KEY, expires_in=3600):
    """
    Generates a JWT token for authentication.

    Args:
        user_id (str): The user's ID to include in the token.
        SECRET_KEY (str): The secret key for token signing.
        expires_in (int, optional): The expiration time for the token in seconds (default is 3600 seconds).

    Returns:
        str: The JWT token.
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Utility function to extract user_id from an Authorization token
def get_user_id_from_token(authorization_header):
    """
    Extracts the user ID from an Authorization token.

    Args:
        authorization_header (str): The Authorization header containing the token.

    Returns:
        str: The user ID extracted from the token or None if the token is invalid.
    """
    if not authorization_header or not authorization_header.startswith("Bearer "):
        return None

    token = authorization_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        return user_id
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Other utility functions can be added here as needed.
