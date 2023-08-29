import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


client_repo = app_container.get_client_repo()


@click.command()
@click.pass_obj
@click.option("--id", help='ID to filter on')
@click.option("--name", help='Name to filter on')
@click.option("--surname", help='Surname to filter on')
@click.option("--email", help='Email to filter on')
@click.option("--telephone", help='Phone number to filter on')
@click.option("--enterprise_name", help='Company name to filter on')
@click.option("--contact_id", help='commercial contact ID to filter on')
@is_authenticated
def show_clients(session, id, name, surname, email, telephone, enterprise_name, contact_id):
    """
    Method to retrieve and display clients

    """
    token = session.token
    excluded_keys = ['show_clients', 'session', 'token', 'excluded_keys']
    filters = {key: value for key, value in locals().items() if key not in excluded_keys and value is not None}
    answer = client_repo.get(token, filters)
    if print_response(answer, session):
        session.display.clientsAsTable(answer)
