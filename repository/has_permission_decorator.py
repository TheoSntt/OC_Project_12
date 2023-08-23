import jwt
from functools import wraps
from auth.auth_handler import AuthHandler


auth = AuthHandler()


def has_permission(permission):
    def decorator(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            token = args[0]
            payload = auth.verify_token(token)
            if payload is jwt.ExpiredSignatureError:
                return jwt.ExpiredSignatureError
            elif payload is jwt.DecodeError:
                return jwt.DecodeError
            else:
                user_permissions = payload['user_permissions']

            if permission in user_permissions:
                result = function(self, *args, **kwargs)
                return result
            else:
                return None

        return wrapper
    return decorator
