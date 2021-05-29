from Commands.BaseCommand import BaseCommand


class Left(BaseCommand):
    def __init__(self, client):
        super().__init__(client)

    def leftRoom(self):
        return self.client.userController.leftRoom()

    def run(self, command):
        return self.leftRoom()
