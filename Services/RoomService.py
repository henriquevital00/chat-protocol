import peewee
from Repositories.RoomRepository import RoomRepository
from Models.User import User
from Models.Room import *

class RoomService():

    roomRepository = RoomRepository()

    def findAll(self):
        return Room.select()

    def findUsersAtRoom(self, id):
        return RoomUser.select(User.id, User.username)\
               .join(User, on=(User.id == RoomUser.user_id))\
               .join(Room, on=(Room.id == RoomUser.room_id))\
               .where(Room.id == id)