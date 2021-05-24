from Repositories.UserRepository import UserRepository


class AccountService():
    def __init__(self, client):
        self.client = client
        self.userRepository = UserRepository()

    def signIn(self, username, password):

        users = list(self.userRepository.findByUsername(username))

        if len(users) == 1:

            user = users[0]

            if password == user.password:
                self.client.isLoggedIn = True
                self.client.accountData = user
                print(self.client.accountData)

                return None

        return "Incorrect username or password"

    def signOut(self):

        if self.client.isLoggedIn:
            self.client.isLoggedIn = False
            self.client.accountData = None

            return None

        return "No user logged in"
