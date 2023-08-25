import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated


collab_repo = app_container.get_collab_repo()


@click.command()
@click.pass_obj
@is_authenticated
def show_all_collaborators(session):
    """
    Method to retrieve and display all collaborators

    """
    token = session.token
    answer = collab_repo.get_all(token)
    # print_response(answer)
    for a in answer:
        session.display.log_styled(a, style="yellow")
