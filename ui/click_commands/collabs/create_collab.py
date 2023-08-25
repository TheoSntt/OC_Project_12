import click
from appcontainer import app_container
from ui.click_commands.validators import validate_email
from ui.click_commands.validators import validate_telephone
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated


collab_repo = app_container.get_collab_repo()


@click.command()
@click.pass_obj
@click.argument("name")
@click.argument("surname")
@click.argument("email", callback=validate_email)
@click.argument("telephone", callback=validate_telephone)
@click.argument("role")
@click.argument("username")
@click.argument("password")
@is_authenticated
def create_collaborator(session, name, surname, email, telephone, role, username, password):
    """
    Creates a new collaborator in the app.

    NAME: The name of the user to be created.
    SURNAME: The surname of the user to be created.
    EMAIL: The email adress of the user to be created.
    TELEPHONE: The phone number of the user to be created.
    ROLE: The Role of the user to be created. (1 for Admin, 2 for Sales, 3 for Support)
    USERNAME: The username with which the user will log in.
    PASSWORD: The password with which the user will log in.

    """
    token = session.token
    data = {
        "name": name,
        "surname": surname,
        "email": email,
        'telephone': telephone,
        'role_id': role,
        'username': username,
        'password': password

    }
    answer = collab_repo.create_collaborator(token, data)
    print_response(answer)
