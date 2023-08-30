import click
from appcontainer import app_container
from ui.click_commands.validators import validate_email
from ui.click_commands.validators import validate_telephone
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


collab_repo = app_container.get_collab_repo()


@click.command()
@click.pass_obj
@click.argument("id")
@click.option("--name", help='New name')
@click.option("--surname", help='New surname')
@click.option("--email", help='New email', callback=validate_email)
@click.option("--telephone", help='New phone number', callback=validate_telephone)
@click.option("--role_id", help='ID of the new role')
@click.option("--username", help='New username')
@click.option("--password", help='New password')
@is_authenticated
def update_collaborator(session, id, name, surname, email, telephone, role_id, username, password):
    """
    Updates a collaborator in the app.

    ID: The id of the collaborator to update.


    """
    token = session.token
    excluded_keys = ['id', 'update_client', 'session', 'token', 'excluded_keys']
    data = {key: value for key, value in locals().items() if key not in excluded_keys and value is not None}
    if data == {}:
        session.display.error(messages.DATA_NEEDED_FOR_UPDATE)
    else:
        answer = collab_repo.update_collaborator(token, id, data)
        if print_response(answer, session):
            session.display.log_styled(messages.update_sucess("collaborator"), style="green")
            session.display.collabsAsTable([answer])
