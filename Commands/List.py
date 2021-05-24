class List:
    @staticmethod
    def listUsers(client):
        if client.activeRoom != None:
            users_name = client.roomController.findUsersAtRoom(
                client.activeRoom)
            users_name = list(map(lambda room: room.user.username, users_name))

            return '\n'.join(users_name)
        else:
            return 'No users at currently room'

    @staticmethod
    def listRooms(client):
        rooms = client.userController.findUserRooms()
        if len(rooms) and isinstance(rooms, list):
            rooms = list(map(lambda room: room.user_room.name, rooms))
            return '\n'.join(rooms)
        return rooms

    @staticmethod
    def listPendingUsers(client):
        users = client.roomController.findPendingUsers()
        if len(users) and isinstance(users, list):
            users = list(map(lambda room: room.user.username, users))
            return '\n'.join(users)
        return users

    @staticmethod
    def run(command, client):
        var = command.split(' ')
        del var[0]
        if var[0] == 'users':
            return List.listUsers(client)
        elif var[0] == '-r':
            return List.listPendingUsers(client)
        else:
            return List.listRooms(client)
