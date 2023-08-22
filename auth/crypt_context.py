from passlib.context import CryptContext
from passlib.utils import saslprep
import time


cryptcontext = CryptContext.from_path('auth/security.ini')


if __name__ == '__main__':
    start_time = time.time()
    top_secret = cryptcontext.hash(saslprep("password"))
    print(top_secret)
    print("Temps d'exécution : {:.2f}s".format(time.time() - start_time))
    print(cryptcontext.identify(top_secret))
    print(cryptcontext.verify("password", top_secret))
    cfg = cryptcontext.to_string()
    print(cfg)
