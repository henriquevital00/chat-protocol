from Commands.BaseCommand import BaseCommand


class Accept(BaseCommand):
    def __init__(self, client):
        super().__init__(client)

    def accept(self, username):

        user_id = self.client.userController.findByName(username)[0].id

        return self.client.roomController.acceptUser(user_id)

    def run(self, command):
        username = command.split()[1]

        return self.accept(username)
