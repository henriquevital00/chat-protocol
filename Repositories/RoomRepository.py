from Models.Room import *
from Models.Message import Message


class RoomRepository():

    def findByName(self, room_name):
        
        return (Room.select().where(Room.name == room_name))

    def findAll(self):
        return Room.select()

    def findUsersAtRoom(self, id):

        return (RoomUser.select(
            RoomUser.user_id, User.username,
            Room.admin_id)
            .join(User, attr='user')
            .switch(RoomUser).join(Room, attr='room')
            .switch(RoomUser).where((Room.id == id) & (RoomUser.isInRoom == 1)))

    def findPendingUsers(self, id):

        return (RoomUser.select(RoomUser.user_id.coerce(), User.username)
            .join(User, attr="user")
            .switch(RoomUser)
            .where((RoomUser.isInRoom == 0) & (RoomUser.room_id == id)))

    def isRoomAdmin(self, room_id, user_id):
        return (Room.select(Room)
            .where((Room.id == room_id) & (Room.admin_id == user_id)))

    def findRoomMessages(self, id):
        return (Message.select(User.username, Message.content)
                .join(User, on=(Message.from_user_id == User.id), attr='user')
                .where(Message.room_id == id))

    def rejectUser(self, user_id, room_id):
        (RoomUser.delete()
        .where((RoomUser.user_id == user_id) & (RoomUser.room_id == room_id))
        .execute())

    def acceptUser(self, user_id, room_id):
        (RoomUser.update(isInRoom=True)
        .where((RoomUser.user_id == user_id) & (RoomUser.room_id == room_id))
        .execute())

    def saveRoom(self, room):
        return Room.create(**room)

    def createRequestToRoom(self, request):
        RoomUser.create(**request)

    def insertUserInRoom(self, user_room):
        return RoomUser.create(**user_room)
