from auth.crypt_context import cryptcontext
from passlib.utils import saslprep
from auth.jwt.jwt_handler import JWTHandler


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
                payload = {'user_id': user.id,
                           'user_role': str(user.role)}
                print(payload)
                token = self.jwt_handler.generate_token(payload)
                return token
            else:
                return False
