from Services.AccountService import AccountService
from Server.Response.Status import *


class AccountController():
    def __init__(self, client):
        self.client = client
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
