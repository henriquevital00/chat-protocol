from Controllers.RoomController import RoomController
from Controllers.UserController import UserController

class Accept:

    @staticmethod
    def accept(username, client):

        user_id = client.userController.findByName(username)[0].id

        return client.roomController.acceptUser(user_id)

    @staticmethod
    def run(command, client):
        var = command.split(' ')
        return Accept.accept(var[1], client)
