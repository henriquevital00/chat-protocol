from Services.UserService import UserService
from Auth.Decorators import Authorization

class UserController():

    userService = UserService()

    def saveUser(self, username, password):
        return self.userService.saveUser(username, password)

    @Authorization
    def findAll(self):
        return self.userService.findAll()
    
    @Authorization
    def findById(self, id):
        return self.userService.findById(id)

    @Authorization
    def findUserRooms(self, id: int):
        return self.userService.findUserRooms(id)
