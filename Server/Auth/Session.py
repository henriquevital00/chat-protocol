from Controllers.RoomController import RoomController
from Controllers.AccountController import AccountController
from Controllers.UserController import UserController
from Controllers.MessageController import MessageController


class Session():
    def __init__(self):

        self.accountData = None
        self.isLoggedIn = False
        self.activeRoom = None

        # Session controllers
        self.roomController = RoomController(self)
        self.messageController = MessageController(self)
        self.accountController = AccountController(self)
        self.userController = UserController(self)
