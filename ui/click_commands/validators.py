import re
import click


EMAIL_REGEX = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"


# Validate email with basic pattern
def validate_email(ctx, param, value):
    try:
        if not re.match(EMAIL_REGEX, value):
            raise click.BadParameter("Invalid email format.")
        return value
    except TypeError:
        return value


# Validate telephone number with basic pattern
def validate_telephone(ctx, param, value):
    try:
        if not re.match(r"^\d{10}$", value):
            raise click.BadParameter("Invalid telephone number format. Use 10 digits.")
        return value
    except TypeError:
        return value
