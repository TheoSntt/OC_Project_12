def sanitize_input(input_string):
    # Define a list of characters to remove or escape
    dangerous_characters = ["'", "\"", ";", "--", "/*", "*/"]

    # Remove or escape dangerous characters
    sanitized_input = input_string
    for char in dangerous_characters:
        sanitized_input = sanitized_input.replace(char, "")

    return sanitized_input
