from Commands.BaseCommand import BaseCommand


class Login(BaseCommand):
    def __init__(self, client):
        super().__init__(client)

    def login(self, username, password):
        return self.client.accountController.signIn(username, password)

    def run(self, command):

        command = command.split()
        del command[0]  # delete "login"

        username, password = command

        return self.login(username, password)
