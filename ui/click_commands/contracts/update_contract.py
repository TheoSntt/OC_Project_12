import click
from appcontainer import app_container
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


contract_repo = app_container.get_contract_repo()


@click.command()
@click.pass_obj
@click.argument("id")
@click.option("--legal_id", help='New legal id')
@click.option("--price", help='New price')
@click.option("--remaining_to_pay", help='New value for price remaining to pay')
@click.option("--status", help='New status')
@click.option("--client_id", help='New client ID')
@is_authenticated
def update_contract(session, id, legal_id, price, remaining_to_pay, status, client_id):
    """
    Updates a contract in the app.

    ID: The id of the contract to update.


    """
    token = session.token
    excluded_keys = ['id', 'update_client', 'session', 'token', 'excluded_keys']
    data = {key: value for key, value in locals().items() if key not in excluded_keys and value is not None}
    if data == {}:
        session.display.error(messages.DATA_NEEDED_FOR_UPDATE)
    else:
        answer = contract_repo.update_contract(token, id, data)
        if print_response(answer, session):
            session.display.log_styled(messages.update_sucess("contract"), style="green")
            session.display.contractsAsTable([answer])
