import click
from appcontainer import app_container
from click_ui.is_auth_decorator import is_authenticated
from click_ui.response_printer import print_response


client_repo = app_container.get_client_repo()


@click.command()
@is_authenticated
def show_all_clients(token):
    """
    Method to retrieve and display all clients

    """
    answer = client_repo.get_all(token)
    print_response(answer)
