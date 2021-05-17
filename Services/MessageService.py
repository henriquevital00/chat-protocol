from Repositories.MessageRepository import MessageRepository


class messageService():
    MessageRepository = MessageRepository()

    def saveMessage(self, from_user_id, content, room_id=None, to_user_id=None, file=None, file_name=None):

        try:
            message = {"from_user_id": from_user_id, "to_user_id": to_user_id, "content": content,
                       "file": file, "file_name": file_name, "room_id": room_id}

            self.messageRepository.saveMessage(message)

            return f"Created room {message} succesfully!"

        except:
            return "Not corresponding data was inserted"
