from Commands.BaseCommand import BaseCommand

class Create(BaseCommand):

    def __init__(self, client):
        super().__init__(client)

    def createUser(self, username, password):
        return self.client.userController.saveUser(username, password)

    def createRoom(self, room):
        return self.client.roomController.saveRoom(room)

    def run(self, command):

        command = command.split()

        if command[1] == '-r':
            room_name = command[2]
            return self.createRoom(room_name)

        else:
            username, password = command.split()[1:]
            return self.createUser(username, password)
