import click
import os
from appcontainer import app_container
from ui.utilities import ui_utils


auth_handler = app_container.get_auth_handler()
collab_repo = app_container.get_collab_repo()


@click.command()
@click.pass_obj
@click.option("--username", prompt="Your username", help="The username for your account")
@click.password_option()
def login(session, username, password):
    """
    Method to login a signed in user

    """
    answer = auth_handler.verify_login_attempt(collab_repo, username, password)
    token = answer["token"]
    if token:
        # Store token
        ui_utils.store_token(token, answer["user_id"])

        click.echo(f"Your login is successful. You are logged in as {answer['user_to_greet']}.")
    else:
        click.echo("Account not recognized. Please try login again.")
    # click.echo(f"{username} {password}")
