class Messages:
    def __init__(self):
        self.RESPONSE_EXPIRED_TOKEN = "Your token is expired. Please login again."
        self.RESPONSE_INVALID_TOKEN = "Your token is invalid. Please login again."
        self.RESPONSE_UNAUTHORIZED = "You are not authorized to perform this operation."
        self.LOCAL_TOKEN_MISSING_OR_EXPIRED = ("You either are not logged in or your token has expired."
                                               "\nYou need to login first to access this command.")

    def log(self, msg_obj=None) -> None:
        self._console.print(msg_obj, style="bold green")


messages = Messages()
