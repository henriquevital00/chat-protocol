from Services.MessageService import MessageService
from Server.Response.Status import *


class MessageController():
    def __init__(self, client):
        self.client = client
        self.messageService = MessageService(client)

    def saveMessage(self, content):
        responseBody = self.messageService.saveMessage(content)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f'{self.client.accountData.username}: {content}')
