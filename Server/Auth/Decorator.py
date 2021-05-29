from functools import wraps

def Authorizate(action):

    @wraps(action)
    def wrapper(*args, **kw):

        client = args[0]

        if client.isLoggedIn:
            return action(*args, **kw)
        else:
            raise Exception("Access denied. You're not authenticated!")

    return wrapper


def AllowAnnonymous(action):

    @wraps(action)
    def wrapper(*args, **kw):

        client = args[0]

        if not client.isLoggedIn:
            return action(*args, **kw)
        else:
            raise Exception("You can't execute this command while you're authenticated")

    return wrapper
