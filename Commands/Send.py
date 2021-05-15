class Send:
    @staticmethod
    def send_message(message):
        pass

    def send_files(file):
        pass

    @staticmethod
    def run(command):
        var = command.split(' ')
        del var[0]
        if var[0] == '-f':
            Send.send(var[1])
        else:
