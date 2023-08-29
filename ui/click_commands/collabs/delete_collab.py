import click
from appcontainer import app_container
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


collab_repo = app_container.get_collab_repo()


@click.command()
@click.pass_obj
@click.argument("id")
@click.option("--confirm", help='Confirmation for collaborator deletion', is_flag=True, prompt='Are you sure?')
@is_authenticated
def delete_collaborator(session, id, confirm):
    """
    Delete a collaborator in the app.

    ID: The id of the collaborator to delete.


    """
    if confirm:
        token = session.token
        answer = collab_repo.delete_collaborator(token, id)
        if print_response(answer, session):
            deleted_collab = answer[0]
            session.display.log_styled(messages.delete_sucess("collaborator", str(deleted_collab)), style="green")
