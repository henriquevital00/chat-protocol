from Models.Message import Message
from Models.User import User

class MessageRepository():

        def saveMessage(self, message):
            return Message.create(**message)

        def findPrivateMessages(self, id_user_from, id_user_to):
            from_user = User.alias("from_user")
            to_user = User.alias("to_user")
            return(

                #Message.select()

               # Message.select(from_user.username, to_user.username, Message.content,
               #                Message.file_name, Message.file)
               #     .join(from_user, on=(from_user.id == Message.from_user_id), attr="from_user")
               #     .join(to_user, on=(to_user.id == Message.to_user_id), attr="to_user")
               #     .where(from_user.id == id_user_from & to_user.id == id_user_to)
            )
