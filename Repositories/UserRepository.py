from Models.User import User

class UserRepository():

    def findAll(self):
        return User.select()

    def findById(self, id: int):
        return User.select().where(User.id == id)

    def saveUser(self, user):
        return User.create(**user)
