import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


event_repo = app_container.get_event_repo()


@click.command()
@click.pass_obj
@is_authenticated
def show_events(session):
    """
    Method to retrieve and display all clients

    """
    token = session.token
    answer = event_repo.get_all(token)
    if print_response(answer, session):
        session.display.eventsAsTable(answer)
