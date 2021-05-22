from Auth.Session import Session


class Left:
    @staticmethod
    def leftRoom(room):
        Session.get_instance(None)

    @staticmethod
    def run(command):
        var = command.split(' ')
        del var[0]
        if var[0] == '-r':
            Left.leftRoom(var[0])
