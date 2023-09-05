import click
from appcontainer import app_container
from ui.is_auth_decorator import is_authenticated
from ui.response_printer import print_response


event_repo = app_container.get_event_repo()


@click.command()
@click.pass_obj
@click.option("--id", help='ID to filter on')
@click.option("--title", help='Name to filter on')
@click.option("--start_date", help='Surname to filter on')
@click.option("--end_date", help='Email to filter on')
@click.option("--location", help='Phone number to filter on')
@click.option("--attendees", help='Company name to filter on')
@click.option("--comments", help='Company name to filter on')
@click.option("--support_id", help='Company name to filter on')
@click.option("--contract_id", help='Company name to filter on')
@is_authenticated
def show_events(session, id, title, start_date, end_date, location, attendees, comments, support_id, contract_id):
    """
    Method to retrieve and display contracts

    """
    token = session.token
    excluded_keys = ['show_events', 'session', 'token', 'excluded_keys']
    filters = {key: value for key, value in locals().items() if key not in excluded_keys and value is not None}
    answer = event_repo.get(token, filters)
    if print_response(answer, session):
        session.display.eventsAsTable(answer)
