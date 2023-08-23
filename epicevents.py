import click
from click_ui.click_commands.login import login
from click_ui.click_commands.collabs.create_collaborator import create_collaborator
# from UI.click_commands.print_stuff import print_stuff
from click_ui.click_commands.clients.show_all_clients import show_all_clients
from click_ui.click_commands.collabs.show_all_collabs import show_all_collaborators
from click_ui.click_commands.contracts.show_all_contracts import show_all_contracts
from click_ui.click_commands.events.show_all_events import show_all_events
# from rich.panel import Panel
# from rich.console import Console
# from rich.padding import Padding

# pnl1 = Panel("[bold yellow]an old falcon", expand=False, border_style="blue")
# pnl2 = Panel.fit("[bold yellow]an old falcon", border_style="blue")

# console = Console()
# console.print(pnl1)
# console.print(pnl2)


@click.group()
def cli():
    pass


cli.add_command(login)
cli.add_command(create_collaborator)
cli.add_command(show_all_clients)
cli.add_command(show_all_collaborators)
cli.add_command(show_all_contracts)
cli.add_command(show_all_events)

# @click.command()
# @click.password_option()
# def encrypt(password):
#     click.echo('Encrypting password to %s' % password)


if __name__ == '__main__':
    cli()
