import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


collab_repo = app_container.get_collab_repo()


@click.command()
@click.pass_obj
@is_authenticated
def show_collaborators(session):
    """
    Method to retrieve and display all collaborators

    """
    token = session.token
    answer = collab_repo.get_all(token)
    if print_response(answer, session):
        session.display.collabsAsTable(answer)
