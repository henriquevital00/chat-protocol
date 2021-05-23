from Controllers.AccountController import AccountController
from Auth.Auth import Auth


class Login:
    @staticmethod
    def login(username, password):
        return AccountController().signIn(username, password)

    @staticmethod
    def run(command):
        var = command.split(' ')
        Login.login(var[1], var[2])
