class Send:
    @staticmethod
    def send_message(message):
        pass

    def send_file(file):
        pass

    @staticmethod
    def run(command):
        var = command.split(' ')
        del var[0]
        if var[0] == "-f":
            Send.send_message(var[1])
        elif var[0] == "-m":
            Send.send_file(var[1])
        else:
            pass
