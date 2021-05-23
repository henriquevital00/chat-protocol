from Controllers.RoomController import RoomController
from Controllers.UserController import UserController

class Accept:

    @staticmethod
    def accept(username):

        userController, roomController = (UserController(), RoomController())

        user_id = userController.findByName(username)[0].id

        print(roomController.acceptUser(user_id))

    @staticmethod
    def run(command):
        var = command.split(' ')
        Accept.accept(var[1])
