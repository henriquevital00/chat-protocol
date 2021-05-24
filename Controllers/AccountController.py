from Services.AccountService import AccountService
from Server.Response.Status import *
from Controllers.BaseController import BaseController


class AccountController(BaseController):

    def __init__(self, client):
        super().__init__(client)
        self.accountService = AccountService(client)

    def signIn(self, username, password):
        responseBody = self.accountService.signIn(username, password)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok("Logged succesfully")

    def signOut(self):

        responseBody = self.accountService.signOut()

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok("Sign out succesfully! Bye")
