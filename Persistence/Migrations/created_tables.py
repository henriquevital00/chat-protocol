from .Migration import Migration
from Models.User import User
from Models.Message import Message
from Models.Room import *

class CreatedTableMigration(Migration):

    def migrate(self):
        self._conn.create_tables([
            User,
            Room,
            RoomUser,
            Message,
        ])