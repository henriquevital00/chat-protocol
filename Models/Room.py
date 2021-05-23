from peewee import CharField, IntegerField, ForeignKeyField, BooleanField
from .BaseModel import BaseModel
from .User import User


class Room(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True, null=False)
    admin_id = ForeignKeyField(User.id, null=True)


class RoomUser(BaseModel):
    room_id = ForeignKeyField(Room)
    user_id = ForeignKeyField(User)
    isInRoom = BooleanField(default=False, null=False)
