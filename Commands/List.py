from Controllers.RoomController import RoomController
from Controllers.UserController import UserController
from Auth.Session import Session


class List:
    @staticmethod
    def listUsers():
        if Session.getRoomId() != None:
            users_name = RoomController().findUsersAtRoom(Session.getRoomId())
            return list(map(lambda room: room.user.username, users_name))
        else:
            print('None users at currently room')

    @staticmethod
    def listRooms():
        print(
            list(map(lambda room: room.name,
                     UserController().findUserRooms())))
        return list(
            map(lambda room: room.name,
                UserController().findUserRooms()))

    @staticmethod
    def run(command):
        var = command.split(' ')
        del var[0]
        if var[0] == 'users':
            List.listUsers()
        else:
            List.listRooms()
