import click
from appcontainer import app_container
from ui.click_commands.validators import validate_email
from ui.click_commands.validators import validate_telephone
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated


client_repo = app_container.get_client_repo()


@click.command()
@click.pass_obj
@click.argument("name")
@click.argument("surname")
@click.argument("email", callback=validate_email)
@click.argument("telephone", callback=validate_telephone)
@click.argument("enterprise_name")
@is_authenticated
def create_client(session, name, surname, email, telephone, enterprise_name):
    """
    Creates a new collaborator in the app.

    NAME: The name of the client to be created.
    SURNAME: The surname of the client to be created.
    EMAIL: The email adress of the client to be created.
    TELEPHONE: The phone number of the client to be created.
    CONTACT: The commercial contact for the client to be created.

    """
    token = session.token
    data = {
        "name": name,
        "surname": surname,
        "email": email,
        'telephone': telephone,
        'enterprise_name': enterprise_name,
        'contact_id': session.user_id
    }
    answer = client_repo.create_client(token, data)
    print_response(answer)
