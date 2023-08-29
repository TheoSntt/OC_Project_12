import click
from appcontainer import app_container
from ui.response_printer import print_response
from ui.is_auth_decorator import is_authenticated
from ui.display.messages import messages


event_repo = app_container.get_event_repo()


@click.command()
@click.pass_obj
@click.argument("title")
@click.argument("start_date")
@click.argument("end_date")
@click.argument("location")
@click.argument("attendees")
@click.argument("comments")
@click.argument("support")
@click.argument("contract")
@is_authenticated
def create_event(session, title, start_date, end_date, location, attendees, comments, support, contract):
    """
    Creates a new collaborator in the app.

    TITLE: The title of the event to be create.
    START DATE: The starting date of the event.
    END DATE: The ending date of the event.
    LOCATION: The location of the event.
    ATTENDEES: The number of expected attendees.
    COMMENTS: Any comments for this event.
    SUPPORT: The support (his id) for the event.
    CONTRACT: The contract (its id) for the event.

    """
    token = session.token
    data = {
        "title": title,
        "start_date": start_date,
        "end_date": end_date,
        'location': location,
        'attendees': attendees,
        "comments": comments,
        'support_id': support,
        'contract_id': contract,
    }
    answer = event_repo.create_event(token, data)
    if print_response(answer, session):
        session.display.log_styled(messages.creation_sucess("event"), style="green")
        session.display.eventsAsTable(answer)
