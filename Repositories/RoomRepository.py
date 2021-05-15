import peewee
from Models.User import User
from Models.Room import Room

class RoomRepository():

    def findAll(self):
        return Room
