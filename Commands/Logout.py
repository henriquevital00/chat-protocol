from Commands.BaseCommand import BaseCommand

class Logout(BaseCommand):

    def __init__(self, client):
        super().__init__(client)

    def logout(self):
        return self.client.accountController.signOut()

    def run(self, command):
        return self.logout()
