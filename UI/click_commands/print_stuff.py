import click
from appcontainer import app_container
from UI.is_auth_decorator import is_authenticated


collab_repo = app_container.get_collab_repo()


@click.command()
@is_authenticated
def print_stuff():
    """
    Method to try somethings

    """
    all_collab = collab_repo.get_all()
    for collab in all_collab:
        click.echo(collab)
    # click.echo("ta mere")


if __name__ == '__main__':
    print_stuff()
