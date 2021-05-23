from Controllers.RoomController import RoomController
from Controllers.UserController import UserController


class Decline:
    @staticmethod
    def decline(username):
        userController, roomController = (UserController(), RoomController())

        user_id = userController.findByName(username)[0].id

        return roomController.acceptUser(user_id)

    @staticmethod
    def run(command):
        var = command.split(' ')
        Decline.decline(var[1])
