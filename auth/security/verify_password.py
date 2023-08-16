from auth.security.crypt_context import cryptcontext
from passlib.utils import saslprep


def hash_password(input_password, stored_password):
    return cryptcontext.verify(saslprep(input_password), stored_password)
