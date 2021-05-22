from Auth.Session import Session
from Controllers.RoomController import RoomController


class Mv:
    @staticmethod
    def move(room):
        print(Session.get_instance(RoomController().findByName(room)[0]))

    @staticmethod
    def run(command):
        Mv.move(command.split(' ')[1])
