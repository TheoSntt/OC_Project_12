import click
from appcontainer import app_container
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


event_repo = app_container.get_event_repo()


@click.command()
@click.pass_obj
@click.argument("id")
@click.option("--title", help='New title')
@click.option("--start_date", help='New start date')
@click.option("--end_date", help='New end date')
@click.option("--location", help='New location')
@click.option("--attendees", help='New number of attendees')
@click.option("--comments", help='New value for comments')
@click.option("--support_id", help='ID for new support')
@click.option("--contract_id", help='ID of new contract')
@is_authenticated
def update_event(session, id, title, start_date, end_date, location, attendees, comments, support_id, contract_id):
    """
    Updates an event in the app.

    ID: The id of the event to update.


    """
    token = session.token
    excluded_keys = ['id', 'update_client', 'session', 'token', 'excluded_keys']
    data = {key: value for key, value in locals().items() if key not in excluded_keys and value is not None}
    if data == {}:
        session.display.error(messages.DATA_NEEDED_FOR_UPDATE)
    else:
        answer = event_repo.update_event(token, id, data)
        if print_response(answer, session):
            session.display.log_styled(messages.update_sucess("event"), style="green")
            session.display.eventsAsTable(answer)
