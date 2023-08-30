import click
from appcontainer import app_container
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


client_repo = app_container.get_client_repo()


@click.command()
@click.pass_obj
@click.argument("id")
@click.option("--confirm", help='Confirmation for client deletion', is_flag=True, prompt='Are you sure?')
@is_authenticated
def delete_client(session, id, confirm):
    """
    Delete a client in the app.

    ID: The id of the client to delete.


    """
    if confirm:
        token = session.token
        answer = client_repo.delete_client(token, id)
        print(answer)
        if print_response(answer, session):
            session.display.log_styled(messages.delete_sucess("client", str(answer)), style="green")
            # session.display.clientsAsTable(answer)
