import json


class Utilities:
    # def __init__(self):

    def store_token(self, token):
        # Store token
        data = {
            "token": token
            }
        with open("UI/token/token.json", "w") as json_file:
            json.dump(data, json_file)

    def get_token_or_prompt_for_login(self):
        # Retrieve token
        with open("UI/token/token.json", "r") as json_file:
            data = json.load(json_file)

        token = data["token"]


ui_utils = Utilities()
