class Left:
    @staticmethod
    def leftRoom(room):
        pass

    @staticmethod
    def leftServer(server):
        pass

    @staticmethod
    def run(command):
        var = command.split(' ')
        del var[0]
        if var[0] == '-r':
            Left.leftRoom(var[0])
        else:
            Left.leftServer(var[1])
