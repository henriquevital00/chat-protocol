class Accept:
    @staticmethod
    def accept(username):
        pass

    @staticmethod
    def run(command):
        var = command.split(' ')
        Accept.accept(var[1])
