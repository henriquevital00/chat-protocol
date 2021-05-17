from Controllers.RoomController import RoomController


class Create:
    @staticmethod
    def create(room):
        print(RoomController().saveRoom(room))

    @staticmethod
    def run(command):
        var = command.split(' ')
        Create.create(var[1])
