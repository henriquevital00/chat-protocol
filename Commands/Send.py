from Controllers.MessageController import MessageController
from Auth.Auth import Auth
from Auth.Session import Session 

from_user = Auth()


class Send:

    @staticmethod
    def sendPrivateMsg(message, to_user):
        print(MessageController().saveMessage(from_user.logged_user(), message, to_user=to_user))

    @staticmethod
    def sendGroupMsg(message):
        print(MessageController().saveMessage(from_user.logged_user(), message, room_id=Session.getRoomId()))


    @staticmethod
    def run(command):
        var = command.split(' ')
        del var[0]
        string = ""
        for i in range(1, len(var)-1):
            string += var[i] + " "
        string += var[len(var)-1]

        if var[0] != "-m": 
            to_user = var[0]
            if var[1] == "-m":
                Send.sendPrivateMsg(string, to_user)
           
        else:
            if var[0] == "-m":
                Send.sendGroupMsg(string)
           