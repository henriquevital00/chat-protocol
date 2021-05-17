from Controllers.AccountController import AccountController


class Logout:
    @staticmethod
    def logout():
        print(AccountController().signOut())

    @staticmethod
    def run(command):
        Logout.logout()
