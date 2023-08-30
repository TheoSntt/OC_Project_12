import jwt
from functools import wraps
from auth.auth_handler import AuthHandler


auth = AuthHandler()


def has_permission(permission):
    def decorator(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            token = args[0]
            payload = auth.verify_token(token)
            if payload is jwt.ExpiredSignatureError:
                return jwt.ExpiredSignatureError
            elif payload is jwt.DecodeError:
                return jwt.DecodeError
            else:
                user_permissions = payload['user_permissions']

            if permission in user_permissions:
                result = function(self, *args, **kwargs)
                return result
            else:
                return None

        return wrapper
    return decorator


def is_clients_contact(function):
    @wraps(function)
    def wrapper(instance, *args, **kwargs):
        token = args[0]
        # Retrieve the role the request user from the token
        payload = auth.verify_token(token)
        user_role = payload['user_role']
        # If the user is Sales team, he must be the clients contact to update him
        if user_role == "Sales":
            # Retrieve the ID of the request user from the token
            user_id = payload['user_id']
            # Retrieve the client to be updated to get his contact id
            client_to_update_id = args[1]
            client_to_update = instance.get_by_id(client_to_update_id)
            # Check if the request user is the client's contact
            # If not, deny request.
            if user_id == client_to_update.contact_id:
                result = function(instance, *args, **kwargs)
                return result
            else:
                return None
        # If the user is not Sales (then he is admin), he has permission
        else:
            result = function(instance, *args, **kwargs)
            return result
    return wrapper


def is_contracts_clients_contact(function):
    @wraps(function)
    def wrapper(instance, *args, **kwargs):
        token = args[0]
        # Retrieve the role the request user from the token
        payload = auth.verify_token(token)
        user_role = payload['user_role']
        # If the user is Sales team, he must be the contract's client's contact to update it
        if user_role == "Sales":
            # Retrieve the ID of the request user from the token
            user_id = payload['user_id']
            # Retrieve the contract to be updated to get its client's contact id
            contract_to_update_id = args[1]
            contract_to_update = instance.get_by_id(contract_to_update_id)
            # Retrieve the ID of the request user from the token
            payload = auth.verify_token(token)
            user_id = payload['user_id']
            # Check if the request user is the client's contact
            # If not, deny request.
            if user_id == contract_to_update.client.contact_id:
                result = function(instance, *args, **kwargs)
                return result
            else:
                return None
        # If the user is not Sales (then he is admin), he has permission
        else:
            result = function(instance, *args, **kwargs)
            return result
    return wrapper


def is_events_support(function):
    @wraps(function)
    def wrapper(instance, *args, **kwargs):
        token = args[0]
        # Retrieve the role the request user from the token
        payload = auth.verify_token(token)
        user_role = payload['user_role']
        # If the user is Support team, he must be the event's support to update it
        if user_role == "Support":
            # Retrieve the ID of the request user from the token
            user_id = payload['user_id']
            # Retrieve the event to be updated to get his support id
            event_to_update_id = args[1]
            event_to_update = instance.get_by_id(event_to_update_id)

            # Check if the request user is the event's support
            # If not, deny request.
            if user_id == event_to_update.support_id:
                result = function(instance, *args, **kwargs)
                return result
            else:
                return None
        # If the user is not Support (then he is admin), he has permission
        else:
            result = function(instance, *args, **kwargs)
            return result
    return wrapper
