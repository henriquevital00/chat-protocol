import peewee
from Services.UserServices import UserService

# User Controller
class UserResources():

    userService = UserService()

    def findAll(self):
        return self.userService.findAll()

    def findById(self, id):
        return self.userService.findById(id)

    def saveUser(self, username, password):
        return self.userService.saveUser(username, password)


