from Commands.BaseCommand import BaseCommand


class List(BaseCommand):
    def __init__(self, client):
        super().__init__(client)

    def listUsers(self):

        users_names = self.client.roomController.findUsersAtRoom(
            self.client.activeRoom)

        users_names = list(map(lambda room: room.user.username, users_names))

        return '\n'.join(users_names)

    def listRooms(self):

        rooms = self.client.userController.findUserRooms()

        if len(rooms) and isinstance(rooms, list):
            rooms = list(map(lambda room: room.user_room.name, rooms))

            return '\n'.join(rooms)

        return rooms

    def listPendingUsers(self):

        users = self.client.roomController.findPendingUsers()

        if len(users) and isinstance(users, list):
            users = list(map(lambda room: room.user.username, users))
            return '\n'.join(users)

        return users

    def listAllRooms(self):
        rooms = self.client.roomController.findAll()

        if len(rooms) and isinstance(rooms, list):
            rooms = list(map(lambda r: r.name, rooms))
            return '\n'.join(rooms)
        return rooms

    def run(self, command):
        command = command.split()

        del command[0]  # delete "list"

        if command[0] == 'users':
            return self.listUsers()
        elif command[0] == '-r':
            return self.listPendingUsers()
        elif command[0] == '-a':
            return self.listAllRooms()
        else:
            return self.listRooms()
