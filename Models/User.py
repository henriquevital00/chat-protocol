from peewee import Model, CharField, IntegerField, SQL

class User(Model):
    id = IntegerField(primary_key=True, constraints=[SQL('AUTO_INCREMENT')])
    username = CharField(unique = True, null = False)
    password = CharField(null = False)

