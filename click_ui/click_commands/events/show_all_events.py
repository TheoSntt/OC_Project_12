import click
from appcontainer import app_container
from click_ui.is_auth_decorator import is_authenticated
from click_ui.response_printer import print_response


event_repo = app_container.get_event_repo()


@click.command()
@is_authenticated
def show_all_events(token):
    """
    Method to retrieve and display all clients

    """
    answer = event_repo.get_all(token)
    print_response(answer)
