from Controllers.RoomController import RoomController
from Controllers.UserController import UserController


class Mv:
    @staticmethod
    def move(room, client):

        rooms = client.userController.findUserRooms()

        for r in rooms:
            if r.user_room.name == room:
                client.activeRoom = client.roomController.findByName(
                    room)[0].id
                messages = client.roomController.findRoomMessages()
                messages = list(
                    map(lambda msg: f'{msg.user.username}: {msg.content}',
                        messages))
                return '\n'.join(messages)

        return ("\033[91m'User not in room!\033[0m")

    @staticmethod
    def run(command, client):
        return Mv.move(command.split(' ')[1], client)
