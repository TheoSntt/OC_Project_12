class Messages:
    def __init__(self):
        self.RESPONSE_EXPIRED_TOKEN = "Your token is expired. Please login again."
        self.RESPONSE_INVALID_TOKEN = "Your token is invalid. Please login again."
        self.RESPONSE_UNAUTHORIZED = "You are not authorized to perform this operation."
        self.LOCAL_TOKEN_MISSING_OR_EXPIRED = ("You either are not logged in or your token has expired."
                                               "\nYou need to login first to access this command.")
        self.DATA_NEEDED_FOR_UPDATE = "You have to pass at least one optionnal argument to update."

    def creation_sucess(self, model):
        return f"The following {model} has successfully being created."

    def update_sucess(self, model):
        return f"The following {model} has successfully being updated."

    def delete_sucess(self, model, name):
        return f"The following {model} has successfully being deleted : {name}"


messages = Messages()
