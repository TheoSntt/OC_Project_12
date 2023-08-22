import json
import click
import functools
# from UI.click_commands.login import login


def is_authenticated(function):
    """Decorator for printing functions."""
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        with open("UI/token/token.json", "r") as json_file:
            data = json.load(json_file)
        token = data["token"]
        if token:
            # function(token, *args, **kwargs)
            function(token, *args, **kwargs)
        else:
            click.echo("You need to login first to access this command")
    return wrapper
