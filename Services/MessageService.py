from Repositories.MessageRepository import MessageRepository


class MessageService():
    def __init__(self, client):
        self.client = client
        self.messageRepository = MessageRepository()

    def saveMessage(self, content):

        try:
            message = {
                "from_user_id": self.client.accountData.id,
                "content": content,
                "room_id": self.client.activeRoom
            }

            self.messageRepository.saveMessage(message)

            return None

        except Exception as ex:
            return str(ex)
