import json
import datetime


class Utilities:
    # def __init__(self):

    def store_token(self, token, user_id):
        # Store token
        current_time = datetime.datetime.utcnow()
        expires_at = current_time + datetime.timedelta(minutes=20)
        data = {
            "user_id": user_id,
            "token": token,
            "expires": expires_at.isoformat()
            }
        with open("ui/token/token.json", "w") as json_file:
            json.dump(data, json_file)

    def get_token(self):
        # Retrieve token
        with open("ui/token/token.json", "r") as json_file:
            data = json.load(json_file)
        expires = datetime.datetime.strptime(data["expires"], "%Y-%m-%dT%H:%M:%S.%f")

        if expires < datetime.datetime.utcnow():
            return None
        token = data["token"]
        return token

    def get_user_id(self):
        # Retrieve token
        with open("ui/token/token.json", "r") as json_file:
            data = json.load(json_file)
        id = data["user_id"]
        return id


ui_utils = Utilities()
