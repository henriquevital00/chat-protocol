import peewee
from Repositories.UserRepository import UserRepository
from Models.User import User

class UserService():

    userRepository = UserRepository()

    def findAll(self):

        users = list(self.userRepository.findAll())

        return users if len(users)> 0 else "No users registered!"


    def findById(self, id):

        user = self.userRepository.findById(id)

        return user if user != None else f"No user with id {id} registered!"

    def saveUser(self, username, password):

        try:
            user = {
                "username": username,
                "password": password
            }

            self.userRepository.saveUser(user)

            return f"Inserted user {username} succesfulyy!"

        except:

            return "Not corresponding data was inserted"



