from Commands.BaseCommand import BaseCommand


class Mv(BaseCommand):
    def __init__(self, client):
        super().__init__(client)

    def move(self, room):

        rooms = self.client.userController.findUserRooms()

        if not isinstance(rooms, list):
            return rooms

        for r in rooms:

            if r.user_room.name == room:

                self.client.activeRoom = self.client.roomController.findByName(
                    room)[0].id

                messages = self.client.roomController.findRoomMessages()
                if not isinstance(messages, str):

                    messages = list(
                        map(
                            lambda message:
                            f'{message.user.username}: {message.content}',
                            messages))

                    return '\n'.join(messages)

                return messages
        roomExists = list(self.client.roomController.findByName(room))
        if not roomExists:
            return f"The room {room} doesn't exists"
        else:
            return ("\033[91m'User not in room!\033[0m")

    def run(self, command):
        room_name = command.split()[1]

        return self.move(room_name)
