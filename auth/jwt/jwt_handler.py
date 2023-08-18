import os
import jwt
import ctypes


class JWTHandler:
    def __init__(self):
        self.secret_key = None  # Initialize as None

    def _load_secret_key(self):
        self.secret_key = os.environ.get("MYSQL_PROJECT_JWT_KEY")
        if self.secret_key is None:
            raise ValueError("JWT_SECRET_KEY environment variable is not set")

    def _clear_secret_key(self):
        if self.secret_key:
            secret_key_ptr = ctypes.c_char_p(self.secret_key.encode("utf-8"))
            ctypes.memset(secret_key_ptr, 0, len(self.secret_key))
            self.secret_key = None

    def generate_token(self, payload):
        if self.secret_key is None:
            self._load_secret_key()

        token = jwt.encode(payload, self.secret_key, algorithm="HS256")

        # Securely clear the secret key from memory
        self._clear_secret_key()

        return token

    def verify_jwt_token(self, token):
        if self.secret_key is None:
            self._load_secret_key()
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            # Securely clear the secret key from memory
            self._clear_secret_key()
            return payload
        except jwt.ExpiredSignatureError:
            # Securely clear the secret key from memory
            self._clear_secret_key()
            # Handle token expiration
            return None
        except jwt.DecodeError:
            # Securely clear the secret key from memory
            self._clear_secret_key()
            # Handle token verification failure
            return None
