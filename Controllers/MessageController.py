from Services.MessageService import MessageService
from Server.Response.Status import *
from Controllers.BaseController import BaseController
from Server.Auth.Decorator import Authorizate

class MessageController(BaseController):

    def __init__(self, client):
        super().__init__(client)
        self.messageService = MessageService(client)

    @Authorizate
    def saveMessage(self, content):
        responseBody = self.messageService.saveMessage(content)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(f'{self.client.accountData.username}: {content}')
