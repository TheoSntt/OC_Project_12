import click
import jwt


def print_response(answer):
    if answer is jwt.ExpiredSignatureError:
        click.echo("Your token is expired. Please login again")
    elif answer is jwt.DecodeError:
        click.echo("Your token is invalid. Please login again")
    if answer is None:
        click.echo("You are not authorized to perform this operation.")
    else:
        click.echo(answer)
