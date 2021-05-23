from Controllers.RoomController import RoomController
from Controllers.UserController import UserController


class Create:
    @staticmethod
    def createUser(username, password):
        return UserController().saveUser(username, password)

    @staticmethod
    def createRoom(room):
        return RoomController().saveRoom(room)

    @staticmethod
    def run(command):
        var = command.split(' ')
        if var[1] == '-r':
            Create.createRoom(var[2])
        else:
            Create.createUser(var[1], var[2])
