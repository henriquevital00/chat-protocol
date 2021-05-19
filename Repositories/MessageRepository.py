from Models.Message import Message
from Models.User import User

class MessageRepository():

        def saveMessage(self, message):
            return Message.create(**message)

        def findPrivateMessages(self):

            from_user = User.alias()
            to_user = User.alias()

            return(
                Message.select(from_user.username, to_user.username, from_user.id, to_user.id, Message.content,
                              Message.file_name, Message.file)
                .join(from_user, on=(from_user.id == Message.from_user_id), attr="from_user")
                .switch(Message)
                .join(to_user, on=(to_user.id == Message.to_user_id), attr="to_user")
            )
