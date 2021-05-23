from Auth.Session import Session
from Controllers.RoomController import RoomController
from Controllers.UserController import UserController


class Mv:
    @staticmethod
    def move(room):

        userController, roomController = (UserController(), RoomController())

        rooms = userController.findUserRooms()

        for r in rooms:
            if r.user_room.name == room:
                Session.get_instance(roomController.findByName(room)[0])
                return

        return ("\033[91m'User not in room!\033[0m")

    @staticmethod
    def run(command):
        Mv.move(command.split(' ')[1])
