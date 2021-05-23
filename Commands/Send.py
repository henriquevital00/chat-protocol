from Controllers.MessageController import MessageController
from Controllers.UserController import UserController
from Auth.Auth import Auth
from Auth.Session import Session


class Send:
    @staticmethod
    def sendPrivateMsg(message, to_user):
        return MessageController().saveMessage(
            Auth.logged_user(),
            message,
            to_user_id=UserController().findByName(to_user)[0].id)

    @staticmethod
    def sendGroupMsg(message):
        return MessageController().saveMessage(Auth.logged_user(),
                                               message,
                                               room_id=Session.getRoomId())

    @staticmethod
    def run(command):
        string = command.partition(' -m ')
        split_command = string[0].split()
        text = string[2].strip('"')

        if len(split_command) == 2:
            to_user = split_command[1]
            Send.sendPrivateMsg(text, to_user)
        else:
            Send.sendGroupMsg(text)
