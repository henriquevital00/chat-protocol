from functools import wraps
from .Auth import Auth


def Authorization(action):

    def wrapper(*args, **kw):

        if Auth.logged_user() is not None:
            return action(*args, **kw)
        else:
            return "Access denied"

    return wrapper


