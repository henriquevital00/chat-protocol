from Commands.BaseCommand import BaseCommand

class Request(BaseCommand):

    def __init__(self, client):
        super().__init__(client)

    def request(self, room):

        room_id = self.client.roomController.findByName(room)[0].id

        return self.client.roomController.createRoomRequest(room_id)

    def run(self, command):
        room_name = command.split()[1]

        return self.request(room_name)
