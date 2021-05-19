from Controllers.MessageController import MessageController
from Auth.Auth import Auth

from_user = Auth()
mc = MessageController()

class Send:

    @staticmethod
    def sendPrivateMsg(message, to_user):
        mc.saveMessage(from_user.logged_user(), message, to_user=to_user)

    @staticmethod
    def sendGroupMsg(message, to_user):
        mc.saveMessage(from_user.logged_user(), message)

    def sendPrivateFile(file):
        
        #falta implementar para enviar imagens
        pass

    def sendGroupFile(file):
        
        #falta implementar para enviar imagens
        pass

    @staticmethod
    def run(command):
        var = command.split(' ')
        del var[0]
        string = ""
        for i in range(1, len(var)-1):
            string += var[i] + " "
        string += var[len(var)-1]

        if var[0] != "-f" or var[0] != "-m": 
            to_user = var[0]
            if var[1] == "-m":
                Send.sendPrivateMsg(string, to_user)
            if var[1] == "-f":
                Send.sendPrivateFile(file, to_user)
        else:
            if var[0] == "-m":
                Send.sendGroupMsg(string, to_user)
            if var[0] == "-f":
                Send.sendGroupFile(file, to_user)