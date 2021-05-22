from Auth.Session import Session
from Controllers.RoomController import RoomController
from Controllers.UserController import UserController

class Mv:
    @staticmethod
    def move(room):
        for r in UserController().findUserRooms():
            if r.name == room:
                Session.get_instance(RoomController().findByName(room)[0])
                return
        print("User not in room!")

    @staticmethod
    def run(command):
        Mv.move(command.split(' ')[1])
