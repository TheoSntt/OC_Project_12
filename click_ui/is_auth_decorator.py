import click
import functools
from click_ui.utilities import ui_utils


def is_authenticated(function):
    """Decorator for printing functions."""
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        # with open("click_ui/token/token.json", "r") as json_file:
        #     data = json.load(json_file)
        # token = data["token"]
        token = ui_utils.get_token()
        if token:
            # function(token, *args, **kwargs)
            function(token, *args, **kwargs)
        else:
            click.echo("You need to login first to access this command")
    return wrapper
