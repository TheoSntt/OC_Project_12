import click
from ui.click_commands.login import login
from ui.click_commands.collabs.create_collab import create_collaborator
from ui.click_commands.clients.create_client import create_client
from ui.click_commands.contracts.create_contract import create_contract
from ui.click_commands.events.create_event import create_event
# from UI.click_commands.print_stuff import print_stuff
from ui.click_commands.clients.show_all_clients import show_all_clients
from ui.click_commands.collabs.show_all_collabs import show_all_collaborators
from ui.click_commands.contracts.show_all_contracts import show_all_contracts
from ui.click_commands.events.show_all_events import show_all_events
from ui.display.display import Display
from ui.utilities import ui_utils


class Session(object):
    def __init__(self, display, token, user_id):
        self.display = display
        self.token = token
        self.user_id = user_id


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Session(Display(), ui_utils.get_token(), ui_utils.get_user_id())


cli.add_command(login)
cli.add_command(create_collaborator)
cli.add_command(create_client)
cli.add_command(create_contract)
cli.add_command(create_event)
cli.add_command(show_all_clients)
cli.add_command(show_all_collaborators)
cli.add_command(show_all_contracts)
cli.add_command(show_all_events)


if __name__ == '__main__':
    cli()
