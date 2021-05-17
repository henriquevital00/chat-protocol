from Controllers.AccountController import AccountController


class Login:
    @staticmethod
    def login(username, password):
        AccountController().signIn(username, password)

    @staticmethod
    def run(command):
        var = command.split(' ')
        Login.login(var[1], var[2])
