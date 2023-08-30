import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


contract_repo = app_container.get_contract_repo()


@click.command()
@click.pass_obj
@click.option("--id", help='ID to filter on')
@click.option("--legal_id", help='Name to filter on')
@click.option("--price", help='Surname to filter on')
@click.option("--remaining_to_pay", help='Email to filter on')
@click.option("--status", help='Phone number to filter on')
@click.option("--client_id", help='Company name to filter on')
@is_authenticated
def show_contracts(session, id, legal_id, price, remaining_to_pay, status, client_id):
    """
    Method to retrieve and display contracts

    """
    token = session.token
    excluded_keys = ['show_contracts', 'session', 'token', 'excluded_keys']
    filters = {key: value for key, value in locals().items() if key not in excluded_keys and value is not None}
    answer = contract_repo.get(token, filters)
    if print_response(answer, session):
        session.display.contractsAsTable(answer)
