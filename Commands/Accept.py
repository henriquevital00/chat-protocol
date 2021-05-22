from Controllers.RoomController import RoomController

class Accept:
    @staticmethod
    def accept(username):
        RoomController().acceptUser(Session.getRoomId())

    @staticmethod
    def run(command):
        var = command.split(' ')
        Accept.accept(var[1])
