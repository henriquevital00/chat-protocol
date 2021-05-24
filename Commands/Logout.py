from Controllers.AccountController import AccountController


class Logout:
    @staticmethod
    def logout(client):
        return client.accountController.signOut()

    @staticmethod
    def run(command, client):
        return Logout.logout(client)
