from peewee import IntegerField, ForeignKeyField, TextField, BlobField
from .BaseModel import BaseModel
from .User import User
from .Room import Room

class Message(BaseModel):
    id = IntegerField(primary_key = True)
    from_user_id = ForeignKeyField(User)
    content = TextField(null = True)
    room_id = ForeignKeyField(Room, null=True)
