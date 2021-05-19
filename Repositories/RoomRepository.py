import peewee
from Models.User import User
from Models.Room import *
from Models.Message import Message


class RoomRepository():
    def findByName(self, room_name):
        return (Room.select().where(Room.name == room_name))

    def findAll(self):
        return Room.select()

    def findUsersAtRoom(self, id):
        return (RoomUser.select(User.id, User.username).join(
            User, on=(User.id == RoomUser.user_id), attr='user').join(
                Room, on=(Room.id == RoomUser.room_id)).where(Room.id == id))

    def findRoomMessages(self, id):
        return (Message.select(User.username, Message.content,
                               Message.file_name, Message.file).join(
                                   User,
                                   on=(Message.from_user_id == User.id),
                                   attr='user').where(Message.room_id == id))

    def rejectUser(self, id):
        RoomUser.delete().where(RoomUser.user_id == id)


    def saveRoom(self, room):
        return Room.create(**room)

    def insertUserInRoom(self, user_room):
        return RoomUser.create(**user_room)
