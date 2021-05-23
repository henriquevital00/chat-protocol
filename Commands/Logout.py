from Controllers.AccountController import AccountController


class Logout:
    @staticmethod
    def logout():
        return AccountController().signOut()

    @staticmethod
    def run(command):
        Logout.logout()
