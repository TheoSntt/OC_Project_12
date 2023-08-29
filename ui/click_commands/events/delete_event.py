import click
from appcontainer import app_container
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


event_repo = app_container.get_event_repo()


@click.command()
@click.pass_obj
@click.argument("id")
@click.option("--confirm", help='Confirmation for event deletion', is_flag=True, prompt='Are you sure?')
@is_authenticated
def delete_event(session, id, confirm):
    """
    Delete an event in the app.

    ID: The id of the event to delete.


    """
    if confirm:
        token = session.token
        answer = event_repo.delete_event(token, id)
        if print_response(answer, session):
            deleted_event = answer[0]
            session.display.log_styled(messages.delete_sucess("event", str(deleted_event)), style="green")
