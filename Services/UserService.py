from Repositories.UserRepository import UserRepository

class UserService():

    userRepository = UserRepository()

    def findAll(self):

        users = list(self.userRepository.findAll())

        return users

    def findUserRooms(self, id: int):

        rooms = list(self.userRepository.findUserRooms(id))

        return rooms if len(rooms) > 0 else "No rooms for this user"


    def findById(self, id):

        user = self.userRepository.findById(id)

        return user if user != None else f"No user with id {id} registered!"

    def saveUser(self, username, password):

        try:

            if len(self.userRepository.findByUsername(username)) == 1:
                return "User already registered with this username!"

            user = {"username": username,"password": password}

            self.userRepository.saveUser(user)

            return None

        except:

            return "Not corresponding data was inserted"



