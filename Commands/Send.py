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
        string = ""
        for i in range(1, len(var)-1):
            string += var[i] + " "
        string += var[len(var)-1]
        if var[0] == "-m":
            Send.send_message(string)
        else:
            Send.send_file(string)


