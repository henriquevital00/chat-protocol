from Models.Message import Message

class MessageRepository():
        def saveMessage(self, message):
            return Message.create(**message)