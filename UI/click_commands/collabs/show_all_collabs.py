import click
from appcontainer import app_container
from UI.is_auth_decorator import is_authenticated
from UI.response_printer import print_response


collab_repo = app_container.get_collab_repo()


@click.command()
@is_authenticated
def show_all_collaborators(token):
    """
    Method to retrieve and display all collaborators

    """
    answer = collab_repo.get_all(token)
    print_response(answer)
