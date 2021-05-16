from Services.AccountService import AccountService

# Account Controller
class AccountResources():

    accountService = AccountService()

    def signIn(self, username, password):
        return self.accountService.signIn(username, password)

    def signOut(self):
        return self.accountService.signOut()




