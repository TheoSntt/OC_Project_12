import os


class Utilities:
    # def __init__(self):

    def store_token(self, token):
        # Store token
        os.environ["EPICEVENTS_TOKEN"] = token
        print("So supposedly i stored the token")
        token = os.environ.get("EPICEVENTS_TOKEN")
        print(token)

    def get_token_or_prompt_for_login(self):
        # Retrieve token
        token = os.environ.get("EPICEVENTS_TOKEN")
        if token:
            pass


ui_utils = Utilities()
