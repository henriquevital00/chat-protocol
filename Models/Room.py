from peewee import CharField, IntegerField, ForeignKeyField, BooleanField
from .BaseModel import BaseModel
from .Message import Message
from .User import User

class Room(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    admin = ForeignKeyField(User.id, null = True)

class RoomMessage(BaseModel):
    room_id = ForeignKeyField(Room)
    message_id = ForeignKeyField(Message)

class RoomUser(BaseModel):
    room_id = ForeignKeyField(Room)
    user_id = ForeignKeyField(User)
    isInRoom = BooleanField(default=False, null=False)
