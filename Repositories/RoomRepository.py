import peewee
from Models.User import User
from Models.Room import *
from Models.Message import Message

class RoomRepository():

    def findAll(self):
        return Room.select()

    def findUsersAtRoom(self, id):
        return RoomUser.select(User.id, User.username) \
            .join(User, on=(User.id == RoomUser.user_id)) \
            .join(Room, on=(Room.id == RoomUser.room_id)) \
            .where(Room.id == id)

    def findRoomMessages(self, id):
        return RoomMessage.select(User.username.alias("from_user"), User.username("to_user"),
                                  Message.content, Message.file) \
                .join(User, on=(Message.to_user == User.id and Message.from_user == User.id))\
                .join(Room, on=(Room.id == RoomMessage.room_id)) \
                .where(Room.id == id )

    def saveRoom(self, room):
        return Room.create(**room)

    def insertUserInRoom(self, user_room):
        return RoomUser.create(**user_room)
