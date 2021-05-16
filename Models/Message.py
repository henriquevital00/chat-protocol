from peewee import IntegerField, ForeignKeyField, TextField, BlobField
from .BaseModel import BaseModel
from .User import User
from .Room import Room

class Message(BaseModel):
    id = IntegerField(primary_key = True)
    from_user = ForeignKeyField(User)
    to_user = ForeignKeyField(User, null=True)
    content = TextField(null = True)
    file_name = TextField(null = True)
    file = BlobField(null = True)
    room_id = ForeignKeyField(Room, null=True)