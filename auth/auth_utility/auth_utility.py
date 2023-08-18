from auth.auth_utility.crypt_context import cryptcontext
from passlib.utils import saslprep


class AuthUtility:
    def __init__(self, collab_repo):
        self.collab_repo = collab_repo
        self.cryptcontext = cryptcontext

    def hash_password(self, password):
        hashed_password = self.cryptcontext.hash(saslprep(password))
        return hashed_password

    def verify_password(self, input_password, stored_password):
        return self.cryptcontext.verify(saslprep(input_password), stored_password)

    def verify_login_attempt(self, input_username, input_pw):
        username_check = self.collab_repo.get_by_username(input_username)
        if len(username_check) == 1:
            user = username_check[0]
            return self.verify_password(input_pw, user.password)
        return False
