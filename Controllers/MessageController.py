from Services.MessageService import MessageService
from Auth.Decorators import Authorization
from Server.Response.Status import *

@Authorization
class MessageController():

    messageService = MessageService()

    def saveMessage(self, from_user_id, content, room_id=None, to_user_id=None, file=None, file_name=None):
        responseBody = self.messageService.saveMessage(from_user_id, content, room_id, to_user_id, file, file_name)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f"Message sent successfully!")

    def findPrivateMessages(self, id_user_from, id_user_to):

        messages = self.messageService.findPrivateMessages(id_user_from, id_user_to)

        if not len(messages):
            return BadRequest("No private messages with this user")

        return Ok(messages)

