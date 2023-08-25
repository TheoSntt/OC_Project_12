import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


client_repo = app_container.get_client_repo()


@click.command()
@click.pass_obj
@is_authenticated
def show_all_clients(session):
    """
    Method to retrieve and display all clients

    """
    token = session.token
    answer = client_repo.get_all(token)
    print_response(answer)
