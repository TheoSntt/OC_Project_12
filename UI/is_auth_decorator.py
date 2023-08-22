import os
import click
import functools
from UI.click_commands.login import login


def is_authenticated(function):
    """Decorator for printing functions."""
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        token = os.environ.get("EPICEVENTS_TOKEN")
        print("the token")
        print(token)
        print("the token")
        try:
            token = os.environ["EPICEVENTS_TOKEN"]
            print("the token")
            print(token)
            print("the token")
        except KeyError:
            pass
        if token:
            function(token, *args, **kwargs)
        else:
            click.echo("You need to login first to access this command")
    return wrapper
