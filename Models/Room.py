from peewee import Model, CharField, IntegerField, ForeignKeyField, BooleanField, SQL
from Models.Message import Message
from Models.User import User

class Room(Model):
    id = IntegerField(primary_key=True, constraints=[SQL('AUTO_INCREMENT')])
    name = CharField()
    is_public = BooleanField()

class RoomMessage(Model):
    room_id = ForeignKeyField(Room)
    message_id = ForeignKeyField(Message)

class RoomUser(Model):
    room_id = ForeignKeyField(Room)
    user_id = ForeignKeyField(User)
