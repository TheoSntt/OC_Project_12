from auth.security.crypt_context import cryptcontext
from passlib.utils import saslprep


def hash_password(password):
    hashed_password = cryptcontext.hash(saslprep(password))
    return hashed_password
