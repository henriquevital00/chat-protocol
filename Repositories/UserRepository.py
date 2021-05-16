from Models.User import User
from Models.Room import RoomUser, Room

class UserRepository():

    def findAll(self):
        return User.select()

    def findByUsername(self, username):
        return User.select().where(User.username == username)

    def findById(self, id: int):
        return User.select().where(User.id == id)

    def saveUser(self, user):
        return User.create(**user)

    def findUserRooms(self, id: int):
        return (Room.select(Room.id, Room.name)
            .join(RoomUser, on=(Room.id == RoomUser.room_id))
            .where(RoomUser.user_id == id & RoomUser.isInRoom))


