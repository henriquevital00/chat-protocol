import peewee
from Repositories.UserRepository import UserRepository

class UserService():

    userRepository = UserRepository()

    def findAll(self):

        users = self.userRepository.findAll();

        return users if len(users > 0) else "No users registered!"


    def findById(self, id):

        user = self.userRepository.findById(id)

        return user if user != None else f"No user with id {id} registered!"