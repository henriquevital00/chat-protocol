from Controllers.RoomController import RoomController
from Controllers.UserController import UserController


class Create:
    @staticmethod
    def createUser(username, password, client):
        return client.userController.saveUser(username, password)

    @staticmethod
    def createRoom(room, client):
        return client.roomController.saveRoom(room)

    @staticmethod
    def run(command, client):
        var = command.split(' ')

        if var[1] == '-r':
            return Create.createRoom(var[2], client)
        else:
            return Create.createUser(var[1], var[2], client)
