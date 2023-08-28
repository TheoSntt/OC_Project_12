import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


contract_repo = app_container.get_contract_repo()


@click.command()
@click.pass_obj
@is_authenticated
def show_all_contracts(session):
    """
    Method to retrieve and display all contracts

    """
    token = session.token
    answer = contract_repo.get_all(token)
    if print_response(answer, session):
        session.display.contractsAsTable(answer)
