import click
from UI.click_commands.login import login
from UI.click_commands.print_stuff import print_stuff
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


@click.command()
@click.argument('name', type=str)
@click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name", help="The person to greet.")
@click.option("--japon", default=False, help="Nani ???.")
def hello(count, name, japon):
    """
    Simple program that greets NAME for a total of COUNT times..

    NAME: The person to greet.
    """
    for _ in range(count):
        if japon:
            click.echo(f"Conichiwa, {name}san !")
        else:
            click.echo(f"Hello, {name}!")


cli.add_command(hello)
cli.add_command(login)
cli.add_command(print_stuff)
# @click.command()
# @click.password_option()
# def encrypt(password):
#     click.echo('Encrypting password to %s' % password)


if __name__ == '__main__':
    cli()
