import jwt
from ui.display.messages import messages


def print_response(answer, session):
    if answer is jwt.ExpiredSignatureError:
        session.display.error(messages.RESPONSE_EXPIRED_TOKEN)
        return False
    elif answer is jwt.DecodeError:
        session.display.error(messages.RESPONSE_INVALID_TOKEN)
        return False
    if answer is None:
        session.display.error(messages.RESPONSE_UNAUTHORIZED)
        return False
    else:
        return True
