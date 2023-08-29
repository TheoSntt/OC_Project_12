import datetime
from auth.crypt_context import cryptcontext
from passlib.utils import saslprep
from auth.jwt.jwt_handler import JWTHandler
from models.permissions import permissions


class AuthHandler:
    def __init__(self):
        self.cryptcontext = cryptcontext
        self.jwt_handler = JWTHandler()

    def hash_password(self, password):
        hashed_password = self.cryptcontext.hash(saslprep(password))
        return hashed_password

    def verify_password(self, input_password, stored_password):
        return self.cryptcontext.verify(saslprep(input_password), stored_password)

    def verify_login_attempt(self, collab_repo, input_username, input_pw):
        username_check = collab_repo.get_by_username(input_username)
        if len(username_check) == 1:
            user = username_check[0]
            if self.verify_password(input_pw, user.password):
                current_time = datetime.datetime.utcnow()
                issued_at = current_time
                expires_at = current_time + datetime.timedelta(minutes=20)
                payload = {'user_id': user.id,
                           'user_role': str(user.role),
                           'user_permissions': permissions[str(user.role)],
                           "iat": issued_at,
                           "exp": expires_at}
                token = self.jwt_handler.generate_token(payload)
                return {"token": token,
                        "user_id": user.id,
                        "user_to_greet": str(user)}
            else:
                return False
        else:
            return False

    def verify_token(self, token):
        payload = self.jwt_handler.verify_jwt_token(token)
        return payload
