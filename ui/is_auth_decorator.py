import functools
from ui.display.messages import messages


def is_authenticated(function):
    """Decorator checking weither there is a valid token."""
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        token = args[0].token
        if token:
            # function(token, *args, **kwargs)
            function(*args, **kwargs)
        else:
            args[0].display.error(messages.LOCAL_TOKEN_MISSING_OR_EXPIRED)
    return wrapper
