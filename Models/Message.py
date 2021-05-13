from peewee import Model, IntegerField, ForeignKeyField, TextField, BlobField, SQL
from Models.User import User

class Message(Model):
    id = IntegerField(primary_key = True, constraints=[SQL('AUTO_INCREMENT')])
    from_user = ForeignKeyField(User)
    to_user = ForeignKeyField(User)
    content = TextField(null = True)
    file = BlobField(null = True)
