import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


client_repo = app_container.get_client_repo()


@click.command()
@is_authenticated
def print_stuff(token):
    """
    Method to try somethings

    """
    answer = client_repo.get_all(token)
    print_response(answer)


if __name__ == '__main__':
    print_stuff()
