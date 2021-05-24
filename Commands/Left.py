class Left:
    @staticmethod
    def leftRoom(client):
        client.activeRoom = None
        return 'Left room'

    @staticmethod
    def run(command, client):
        return Left.leftRoom(client)
