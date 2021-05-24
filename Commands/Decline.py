from Controllers.RoomController import RoomController
from Controllers.UserController import UserController


class Decline:
    @staticmethod
    def decline(username, client):
        user_id = client.userController.findByName(username)[0].id

        return client.roomController.rejectUser(user_id)

    @staticmethod
    def run(command, client):
        var = command.split(' ')
        return Decline.decline(var[1], client)
