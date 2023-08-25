import jwt


def print_response(answer, session):
    if answer is jwt.ExpiredSignatureError:
        session.display.error("Your token is expired. Please login again")
        return False
    elif answer is jwt.DecodeError:
        session.display.error("Your token is invalid. Please login again")
        return False
    if answer is None:
        session.display.error("You are not authorized to perform this operation.")
        return False
    else:
        return True
