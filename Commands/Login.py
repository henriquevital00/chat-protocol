
class Login:
    @staticmethod
    def login(username, password, client):
        return client.accountController.signIn(username, password)

    @staticmethod
    def run(command, client):
        var = command.split(' ')
        return Login.login(var[1], var[2], client)
