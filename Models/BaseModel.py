from peewee import Model
from Persistence.DbContext import DbContext

class BaseModel(Model):
    class Meta:
        database = DbContext.get_conn()