from .Migration import Migration
from Models.Room import RoomMessage, RoomUser

class AssociativeEntitiesMigration(Migration):

    def migrate(self):
        self._conn.create_tables([
            RoomMessage,
            RoomUser
        ])