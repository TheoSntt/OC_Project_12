import click
from appcontainer import app_container
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


contract_repo = app_container.get_contract_repo()


@click.command()
@click.pass_obj
@click.argument("legal_id")
@click.argument("price")
@click.argument("remaining_to_pay")
@click.argument("status")
@click.argument("client")
@is_authenticated
def create_contract(session, legal_id, price, remaining_to_pay, status, client):
    """
    Creates a new collaborator in the app.

    LEGAL ID: The unique code of the contract to be created.
    PRICE: The price of the contract.
    REMAINING TO PAY: The price remaining to pay.
    STATUS: The status of the contract.
    CLIENT: The client (his id) for this contract.

    """
    token = session.token
    data = {
        "legal_id": legal_id,
        "price": price,
        "remaining_to_pay": remaining_to_pay,
        'status': status,
        'client_id': client
    }
    answer = contract_repo.create_contract(token, data)
    if print_response(answer, session):
        session.display.log_styled(messages.creation_sucess("contract"), style="green")
        session.display.contractsAsTable([answer])
