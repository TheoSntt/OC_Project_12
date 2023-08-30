import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


collab_repo = app_container.get_collab_repo()


@click.command()
@click.pass_obj
@click.option("--id", help='ID to filter on')
@click.option("--name", help='Name to filter on')
@click.option("--surname", help='Surname to filter on')
@click.option("--email", help='Email to filter on')
@click.option("--telephone", help='Phone number to filter on')
@click.option("--role_id", help='Company name to filter on')
@is_authenticated
def show_collaborators(session, id, name, surname, email, telephone, role_id):
    """
    Method to retrieve and display all collaborators

    """
    token = session.token
    excluded_keys = ['show_collaborators', 'session', 'token', 'excluded_keys']
    filters = {key: value for key, value in locals().items() if key not in excluded_keys and value is not None}
    answer = collab_repo.get(token, filters)
    if print_response(answer, session):
        session.display.collabsAsTable(answer)
