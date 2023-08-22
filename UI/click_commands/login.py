import click
import os
from appcontainer import app_container
from UI.utilities import ui_utils


auth_handler = app_container.get_auth_handler()
collab_repo = app_container.get_collab_repo()


@click.command()
@click.option("--username", prompt="Your username", help="The username for your account")
@click.password_option()
def login(username, password):
    """
    Method to login a signed in user

    """
    answer = auth_handler.verify_login_attempt(collab_repo, username, password)
    token = answer["token"]
    if token:
        # Store token
        ui_utils.store_token(token)
        # os.environ["EPICEVENTS_TOKEN"] = token

        # Retrieve an environment variable
        token = os.environ.get("YOUR_TOKEN_ENV_VAR")
        click.echo(f"Your login is successful. You are logged in as {answer['user_to_greet']}.")
    else:
        click.echo("Account not recognized. Please try login again, or signin if you don't have an account.")
    # click.echo(f"{username} {password}")
