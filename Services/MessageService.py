from Repositories.MessageRepository import MessageRepository


class MessageService():
    messageRepository = MessageRepository()

    def saveMessage(self, from_user_id, content, room_id=None, to_user_id=None, file=None, file_name=None):

        try:
            message = {"from_user_id": from_user_id, "to_user_id": to_user_id, "content": content,
                       "file": file, "file_name": file_name, "room_id": room_id}

            self.messageRepository.saveMessage(message)

            return None

        except Exception as ex:
            return str(ex)

    def findPrivateMessages(self, id_user_from, id_user_to):

        messages = list(self.messageRepository.findPrivateMessages())

        messages = list(filter(lambda message : message.from_user.id == id_user_from
                                                and message.to_user.id == id_user_to ,
                               messages))

        return messages

