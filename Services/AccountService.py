from Repositories.UserRepository import UserRepository
from Auth.Auth import Auth

class AccountService():

    userRepository = UserRepository()

    def signIn(self, username, password):

        users = list(self.userRepository.findByUsername(username))

        if len(users) == 1:

            user = users[0]

            if password == user.password:
                Auth.logged_user(user)

                return users[0]

        return "Incorrect username or password"

    def signOut(self):

        if Auth.logged_user() is not None:
            Auth.logout()



