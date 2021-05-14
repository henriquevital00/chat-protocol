from peewee import IntegerField, ForeignKeyField, TextField, BlobField
from .BaseModel import BaseModel
from .User import User

class Message(BaseModel):
    id = IntegerField(primary_key = True)
    from_user = ForeignKeyField(User)
    to_user = ForeignKeyField(User)
    content = TextField(null = True)
    file = BlobField(null = True)
