from Auth.Session import Session


class Left:
    @staticmethod
    def leftRoom():
        Session.get_instance(None)
        return 'Left room'

    @staticmethod
    def run(command):
        Left.leftRoom()
