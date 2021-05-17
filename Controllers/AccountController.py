from Services.AccountService import AccountService
from Auth.Auth import Auth
from Server.Response.Status import *

class AccountController():

    accountService = AccountService()

    def signIn(self, username, password):
        responseBody = self.accountService.signIn(username, password)

        if responseBody is not None:
            return BadRequest(responseBody)

        return Ok(Auth.logged_user())

    def signOut(self):
        self.accountService.signOut()




