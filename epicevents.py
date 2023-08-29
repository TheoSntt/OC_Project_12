import click
from ui.click_commands.login import login
from ui.click_commands.collabs.create_collab import create_collaborator
from ui.click_commands.clients.create_client import create_client
from ui.click_commands.contracts.create_contract import create_contract
from ui.click_commands.events.create_event import create_event
from ui.click_commands.clients.update_client import update_client
from ui.click_commands.collabs.update_collab import update_collaborator
from ui.click_commands.contracts.update_contract import update_contract
from ui.click_commands.events.update_event import update_event
from ui.click_commands.clients.delete_client import delete_client
from ui.click_commands.collabs.delete_collab import delete_collaborator
from ui.click_commands.contracts.delete_contract import delete_contract
from ui.click_commands.events.delete_event import delete_event
from ui.click_commands.clients.show_clients import show_clients
from ui.click_commands.collabs.show_collabs import show_collaborators
from ui.click_commands.contracts.show_contracts import show_contracts
from ui.click_commands.events.show_events import show_events
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
cli.add_command(update_client)
cli.add_command(update_collaborator)
cli.add_command(update_contract)
cli.add_command(update_event)
cli.add_command(delete_client)
cli.add_command(delete_collaborator)
cli.add_command(delete_contract)
cli.add_command(delete_event)
cli.add_command(show_clients)
cli.add_command(show_collaborators)
cli.add_command(show_contracts)
cli.add_command(show_events)


if __name__ == '__main__':
    cli()
