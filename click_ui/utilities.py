import json


class Utilities:
    # def __init__(self):

    def store_token(self, token):
        # Store token
        data = {
            "token": token
            }
        with open("click_ui/token/token.json", "w") as json_file:
            json.dump(data, json_file)

    def get_token(self):
        # Retrieve token
        with open("click_ui/token/token.json", "r") as json_file:
            data = json.load(json_file)
        token = data["token"]
        return token


ui_utils = Utilities()
