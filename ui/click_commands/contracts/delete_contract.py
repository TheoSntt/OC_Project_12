import click
from appcontainer import app_container
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


contract_repo = app_container.get_contract_repo()


@click.command()
@click.pass_obj
@click.argument("id")
@click.option("--confirm", help='Confirmation for contract deletion', is_flag=True, prompt='Are you sure?')
@is_authenticated
def delete_contract(session, id, confirm):
    """
    Delete a contract in the app.

    ID: The id of the contract to delete.


    """
    if confirm:
        token = session.token
        answer = contract_repo.delete_contract(token, id)
        if print_response(answer, session):
            session.display.log_styled(messages.delete_sucess("contract", str(answer)), style="green")
