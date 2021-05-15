class List:
    @staticmethod
    def listFiles():
        pass

    @staticmethod
    def listUsers():
        pass

    @staticmethod
    def listRooms():
        pass

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
