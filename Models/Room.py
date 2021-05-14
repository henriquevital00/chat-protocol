from peewee import CharField, IntegerField, ForeignKeyField, BooleanField
from .BaseModel import BaseModel
from .Message import Message
from .User import User

class Room(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    is_public = BooleanField()

class RoomMessage(BaseModel):
    room_id = ForeignKeyField(Room)
    message_id = ForeignKeyField(Message)

class RoomUser(BaseModel):
    room_id = ForeignKeyField(Room)
    user_id = ForeignKeyField(User)
