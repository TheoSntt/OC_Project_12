import click
import functools


def is_authenticated(function):
    """Decorator checking weither there is a valid token."""
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        token = args[0].token
        if token:
            # function(token, *args, **kwargs)
            function(*args, **kwargs)
        else:
            args[0].display.error("You either are not logged in or your token has expired."
                                  "\nYou need to login first to access this command")
    return wrapper
