from Services.BaseService import BaseService
from Repositories.UserRepository import UserRepository


class AccountService(BaseService):
    def __init__(self, client):
        super().__init__(client)
        self.userRepository = UserRepository()

    def signIn(self, username, password):

        users = list(self.userRepository.findByUsername(username))

        if len(users) == 1:

            user = users[0]

            if password == user.password:
                self.client.isLoggedIn = True
                self.client.accountData = user

                return None

        return "Incorrect username or password"

    def signOut(self):

        if self.client.isLoggedIn:
            self.client.isLoggedIn = False
            self.client.accountData = None

            return None

        return "No user logged in"
