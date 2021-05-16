from peewee import CharField, IntegerField
from .BaseModel import BaseModel

class User(BaseModel):
    id = IntegerField(primary_key = True)
    username = CharField(unique = True, null = False)
    password = CharField(null = False)