from Controllers.RoomController import RoomController

class Request:

    @staticmethod
    def request(room):

        roomController = RoomController()

        room_id = roomController.findByName(room)[0].id

        print(roomController.createRoomRequest())

    @staticmethod
    def run(command):
        var = command.split(' ')
        Request.request(var[1])
