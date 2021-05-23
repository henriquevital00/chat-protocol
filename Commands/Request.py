class Request:
    @staticmethod
    def request(room):
        pass

    @staticmethod
    def run(command):
        var = command.split(' ')
        request(var[1])
