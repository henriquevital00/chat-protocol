from Controllers.RoomController import RoomController

rc = RoomController()


class List:
    @staticmethod
    def listFiles():        
        print(rc.findRoomFiles())
        return rc.findRoomFiles()


    @staticmethod
    def listUsers():
        print(rc.findUsersAtRoom())
        return rc.findUsersAtRoom()

    @staticmethod
    def listRooms():
        print(rc.findAll())
        return rc.findAll()

    @staticmethod
    def run(command):
        var = command.split(' ')
        del var[0]
        if var[0] == 'files':
            List.listFiles()
        elif var[0] == 'users':
            List.listUsers()
        else:
            List.listRooms()
