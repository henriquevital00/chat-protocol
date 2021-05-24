from Models.Message import Message
from Models.User import User


class MessageRepository():
    def saveMessage(self, message):
        return Message.create(**message)
