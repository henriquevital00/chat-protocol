from Controllers.MessageController import MessageController
from Controllers.UserController import UserController


class Send:
    @staticmethod
    def sendGroupMsg(message, client):
        return client.messageController.saveMessage(message)

    @staticmethod
    def run(command, client):
        string = command.partition(' -m ')
        split_command = string[0].split()
        text = string[2].strip('"')
        return Send.sendGroupMsg(text, client)
