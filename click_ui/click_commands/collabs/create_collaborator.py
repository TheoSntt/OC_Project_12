import click
from appcontainer import app_container
from click_ui.click_commands.validators import validate_email
from click_ui.click_commands.validators import validate_telephone
from click_ui.response_printer import print_response


collab_repo = app_container.get_collab_repo()


@click.command()
@click.option("--name", prompt="Your name", required=True, help="Name of the user to create")
@click.option("--surname", prompt="Your surname", required=True, help="Surname of the user to create")
@click.option("--email", prompt="Your email", required=True,
              callback=validate_email, help="Email of the user to create")
@click.option("--telephone", prompt="Your phone number", required=True,
              callback=validate_telephone, help="Phone number of the user to create")
@click.option("--role", prompt="Your role (1 for Admin, 2 for Sales, 3 for Support)",
              help="Role of the user to create (1 for Admin, 2 for Sales, 3 for Support)")
@click.option("--username", prompt="Your username", help="Surname of the user to create")
@click.password_option()
def create_collaborator(name, surname, email, telephone, role, username, password):
    """
    Method to login a signed in user

    """
    data = {
        "name": name,
        "surname": surname,
        "email": email,
        'telephone': telephone,
        'role_id': role,
        'username': username,
        'password': password

    }
    answer = collab_repo.create_collaborator(data)
    print_response(answer)
