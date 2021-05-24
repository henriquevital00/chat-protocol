from Models.User import User
from Models.Room import RoomUser, Room

class UserRepository():

    def findAll(self):
        return User.select()

    def findByName(self, username):
        return User.select().where(User.username == username)

    def findByUsername(self, username):
        return User.select().where(User.username == username)

    def findById(self, id):
        return User.select().where(User.id == id)

    def saveUser(self, user):
        return User.create(**user)

    def findUserRooms(self, id):

        r = Room.alias()

        return (
            RoomUser.select(r.id, r.name, RoomUser.isInRoom)
            .join(r, on=(r.id == RoomUser.room_id),attr="user_room")
            .switch(RoomUser)
            .where(RoomUser.user_id == id)
        )
