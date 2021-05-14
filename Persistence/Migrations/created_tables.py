from .Migration import Migration
from Models import Message, Room, User

class CreatedTableMigration(Migration):

    def migrate(self):
        self._conn.create_tables([
            User.User,
            Room.Room,
            Message.Message
        ])