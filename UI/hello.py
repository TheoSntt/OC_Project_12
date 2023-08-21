import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
@click.option("--japon", default=False, help="Nani ???.")
def hello(count, name, japon):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        if japon:
            click.echo(f"Conichiwa, {name}san !")
        else:
            click.echo(f"Hello, {name}!")


if __name__ == '__main__':
    hello()
