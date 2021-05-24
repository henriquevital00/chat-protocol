from Controllers.RoomController import RoomController


class Request:
    @staticmethod
    def request(room, client):

        room_id = client.roomController.findByName(room)[0].id

        return client.roomController.createRoomRequest(room_id)

    @staticmethod
    def run(command, client):
        var = command.split(' ')
        return Request.request(var[1], client)
